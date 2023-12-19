"""
Investigate the variations in food hygiene scores by race,
by considering majority White, Black and Asian local authorities
and comparing scores.
Best to control the analysis by sticking to London boroughs only,
since London is the main place in the UK with signficiant enough
Black/Asian populations.
"""
from collections import Counter

import __init__
from constants import Field
from utils import DATA, LOCAL_AUTHORITIES


WHITE = {"Havering", "Bromley", "Bexley", "Richmond-Upon-Thames"}
BLACK = {"Lewisham", "Southwark", "Lambeth", "Hackney"}
ASIAN = {"Redbridge", "Tower Hamlets", "Newham", "Harrow"}


def get_race(local_authority_id: int) -> str | None:
    """Returns the associated race, else None if irrelevant."""
    local_authority = LOCAL_AUTHORITIES[local_authority_id]
    for race, local_authorities in (
        ("White", WHITE), ("Black", BLACK), ("Asian", ASIAN)
    ):
        if local_authority in local_authorities:
            return race
    return None


DATA[Field.TEMP.value] = DATA[Field.LOCAL_AUTHORITY_ID.value].apply(get_race)
ORDER = ("White", "Black", "Asian")
ESTABLISHMENTS_BY_RACE = dict(
    sorted(map(tuple, DATA.groupby(Field.TEMP.value, axis=0)),
        key=lambda pair: ORDER.index(pair[0])))
DATA.drop(Field.TEMP.value, axis=1)


def display_mean(field: Field) -> None:
    """Displays the mean score for a given field for each race."""
    for race, records in ESTABLISHMENTS_BY_RACE.items():
        mean = records[field.value].mean()
        print(f"Mean {field.value} ({race}): {round(mean, 4)}")


def display_count(field: Field) -> None:
    """Displays the score frequencies for a given field by race."""
    for race, records in ESTABLISHMENTS_BY_RACE.items():
        counter = Counter(records[field.value])
        print(f"{field.value} Counts ({race})")
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

if __name__ == "__main__":
    for function, to_run in RUN_FUNCTIONS.items():
        if to_run:
            function()
