"""
Script to fetch data from the website: https://ratings.food.gov.uk/
API: https://api.ratings.food.gov.uk/
"""
import csv
import datetime as dt
import json
import operator
import time
from collections import namedtuple

import requests as rq

from constants import *


API = "https://api.ratings.food.gov.uk"
HEADERS = {"x-api-version": "2"}
PAGE_SIZE = 5000
FIELDS = tuple(map(lambda field: field.value, (
        Field.NAME,
        Field.TYPE_ID,
        Field.RATING,
        Field.HYGIENE,
        Field.CLEANLINESS,
        Field.MANAGEMENT,
        Field.DATE,
        Field.LOCAL_AUTHORITY_ID
    ))
)
# England, Northern Ireland and Wales. Omit Scotland (no scores).
COUNTRY_IDS = (1, 2, 4)
MAX_RETRIES = 3
RETRY_WAIT = 30

Data = namedtuple("Data", ("records", "business_types", "local_authorities"))


def get_record(establishment: dict) -> tuple | None:
    """Converts an establishment dictionary to a record."""
    if establishment["scores"]["Hygiene"] is None:
        # Incomplete food hygiene data.
        return None
    return (
        establishment["BusinessName"],
        establishment["BusinessTypeID"],
        establishment["RatingValue"],
        establishment["scores"]["Hygiene"],
        establishment["scores"]["Structural"],
        establishment["scores"]["ConfidenceInManagement"],
        establishment["RatingDate"].split("T")[0],
        establishment["LocalAuthorityCode"]
    )


def get_data() -> Data:
    """
    Sends requests to the website and obtains all establishment data.
    Returns records sorted by establishment type.
    Also returns maps for business type and local authority IDs to the values.
    """
    seen_ids = set()
    records = set()
    business_types = {}
    local_authorities = {}
    for country in COUNTRY_IDS:
        page = 1
        while True:
            params = {
                "pageSize": PAGE_SIZE,
                "countryId": country,
                "pageNumber": page
            }
            for _ in range(MAX_RETRIES + 1):
                try:
                    data = rq.get(
                        f"{API}/Establishments", headers=HEADERS, params=params
                    ).json()
                    for establishment in data["establishments"]:
                        id_ = establishment["FHRSID"]
                        if id_ in seen_ids:
                            continue
                        seen_ids.add(id_)
                        record = get_record(establishment)
                        if record is not None and record not in records:
                            records.add(record)
                            if record[1] not in business_types:
                                business_types[record[1]] = (
                                    establishment["BusinessType"])
                            if record[7] not in local_authorities:
                                local_authorities[record[7]] = (
                                    establishment["LocalAuthorityName"])
                    print(f"{len(records)} records added.")
                    break
                except Exception as e:
                    print(f"Error: {e} [retrying soon]")
                    time.sleep(RETRY_WAIT)
            else:
                raise Exception(f"Request failed despite {MAX_RETRIES} retries.")
            if data["meta"]["pageNumber"] >= data["meta"]["totalPages"]:
                break
            page += 1
    return Data(
        sorted(records, key=operator.itemgetter(1)),
        business_types,
        local_authorities)


def save(data: Data) -> None:
    """Saves the data."""
    DATA_FOLDER.mkdir(exist_ok=True)
    file = DATA_FOLDER / f"{dt.datetime.utcnow()}.csv".replace(":", "")
    with file.open("w", encoding="utf8") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(FIELDS)
        writer.writerows(data.records)
    for json_data, file in (
        (data.business_types, BUSINESS_TYPES_FILE),
        (data.local_authorities, LOCAL_AUTHORITIES_FILE)
    ):
        with file.open("w", encoding="utf8") as f:
            json.dump(json_data, f)


def main() -> None:
    """Main procedure of the script."""
    data = get_data()
    save(data)


if __name__ == "__main__":
    main()
