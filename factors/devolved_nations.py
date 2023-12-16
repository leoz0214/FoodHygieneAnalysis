"""
Investigate differences in metrics between
businesses in England, Wales and Northern Ireland.
"""
from collections import Counter

import __init__
from constants import Field
from utils import DATA, LOCAL_AUTHORITIES


NI_LOCAL_AUTHORITIES = {
    "Antrim and Newtownabbey", "Ards and North Down",
    "Armagh City, Banbridge and Craigavon", "Belfast City",
    "Causeway Coast and Glens", "Derry City and Strabane",
    "Fermanagh and Omagh", "Lisburn and Castlereagh City",
    "Mid and East Antrim", "Mid Ulster", "Newry, Mourne and Down"
}
WALES_LOCAL_AUTHORITIES = {
    "Anglesey", "Blaenau Gwent", "Bridgend", "Caerphilly",
    "Cardiff", "Carmarthenshire", "Ceredigion", "Conwy",
    "Denbighshire", "Flintshire", "Gwynedd", "Merthyr Tydfil",
    "Monmouthshire", "Neath Port Talbot", "Newport", "Pembrokeshire",
    "Powys", "Rhondda Cynon Taf", "Swansea", "Torfaen",
    "Vale of Glamorgan", "Wrexham"
}


def get_devolved_nation(local_authority_id: int) -> str:
    """Returns a string based on the devolved nation."""
    local_authority = LOCAL_AUTHORITIES[local_authority_id]
    return (
        "Northern Ireland" if local_authority in NI_LOCAL_AUTHORITIES
        else "Wales" if local_authority in WALES_LOCAL_AUTHORITIES
        else "England")


# Temporary column for grouping by devolved nation.
DATA[Field.TEMP.value] = DATA[
    Field.LOCAL_AUTHORITY_ID.value].apply(get_devolved_nation)
ORDER = ("England", "Wales", "Northern Ireland")
ESTABLISHMENTS_BY_DEVOLVED_NATION = dict(
    sorted(map(tuple, DATA.groupby(Field.TEMP.value, axis=0)),
        key=lambda pair: ORDER.index(pair[0])))
DATA.drop(Field.TEMP.value, axis=1)


def display_mean(field: Field) -> None:
    """Displays the mean for each devolved nation for a given field."""
    for devolved_nation, records in ESTABLISHMENTS_BY_DEVOLVED_NATION.items():
        mean = records[field.value].mean()
        print(f"Mean {field.value} in {devolved_nation}: {round(mean, 4)}")


def display_count(field: Field) -> None:
    """
    Displays the count and % breakdown of values
    for each devolved nation for a given field.
    """
    for devolved_nation, records in ESTABLISHMENTS_BY_DEVOLVED_NATION.items():
        print(f"{field.value} Counts for {devolved_nation}")
        counter = Counter(records[field.value])
        for value, count in sorted(counter.items()):
            print(
                f"{value}: {count} ({round(count / len(records) * 100, 2)}%)")


display_mean_rating = lambda: display_mean(Field.RATING)
display_mean_hygiene = lambda: display_mean(Field.HYGIENE)
display_mean_cleanliness = lambda: display_mean(Field.CLEANLINESS)
display_mean_management = lambda: display_mean(Field.MANAGEMENT)
display_rating_count = lambda: display_count(Field.RATING)
display_hygiene_count = lambda: display_count(Field.HYGIENE)
display_cleanliness_count = lambda: display_count(Field.CLEANLINESS)
display_management_count = lambda: display_count(Field.MANAGEMENT)

RUN_FUNCTIONS = {
    display_mean_rating: True,
    display_mean_hygiene: True,
    display_mean_cleanliness: True,
    display_mean_management: True,
    display_rating_count: True,
    display_hygiene_count: True,
    display_cleanliness_count: True,
    display_management_count: True
}


if __name__  == "__main__":
    for function, to_run in RUN_FUNCTIONS.items():
        if to_run:
            function()
