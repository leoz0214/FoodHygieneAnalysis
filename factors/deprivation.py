"""
Investigate the effects of deprivation on food hygiene standards
by considering a sample of least deprived, average and most deprived
local authorities.
"""
from collections import Counter

import __init__
from constants import Field
from utils import DATA, LOCAL_AUTHORITIES


# Samples mostly come from England, but one NI/Wales local authority each too.
# Local authorities selected based on research and basic judgement.
MOST_DEPRIVED = {
    "Blackpool", "Oldham", "Knowsley", "Tower Hamlets", "Newham",
    "Middlesbrough", "Derry City and Strabane", "Blaenau Gwent"}
MIDDLE = {
    "Shropshire", "Herefordshire", "Breckland", "Dorset", "Wandsworth",
    "Bedford", "Mid Ulster", "Ceredigion"}
LEAST_DEPRIVED = {
    "Surrey Heath", "Mid Sussex", "Kensington and Chelsea", "Buckinghamshire",
    "Windsor and Maidenhead", "Wokingham", "Antrim and Newtownabbey",
    "Monmouthshire"}


def get_deprivation_level(local_authority_id: int) -> str | None:
    """Returns the deprivation level, or None if irrelevant."""
    local_authority = LOCAL_AUTHORITIES[local_authority_id]
    for level, local_authorities in (
        ("highest", MOST_DEPRIVED),
        ("average", MIDDLE),
        ("lowest", LEAST_DEPRIVED)
    ):
        if local_authority in local_authorities:
            return level
    return None


DATA[Field.TEMP.value] = DATA[
    Field.LOCAL_AUTHORITY_ID.value].apply(get_deprivation_level)
ORDER = ("highest", "average", "lowest")
ESTABLISHMENTS_BY_DEPRIVATION = dict(
    sorted(map(tuple, DATA.groupby(Field.TEMP.value, axis=0)),
        key=lambda pair: ORDER.index(pair[0])))
DATA.drop(Field.TEMP.value, axis=1)


def display_mean(field: Field) -> None:
    """Displays the means for a given field based on deprivation."""
    for deprivation, records in ESTABLISHMENTS_BY_DEPRIVATION.items():
        mean = records[field.value].mean()
        print(
            f"Mean {field.value} ({deprivation} deprivation): "
            f"{round(mean, 4)}")


def display_count(field: Field) -> None:
    """
    Display the frequencies of each score for a given field, by deprivation.
    """
    for deprivation, records in ESTABLISHMENTS_BY_DEPRIVATION.items():
        counter = Counter(records[field.value])
        print(f"{field.value} counts ({deprivation} deprivation)")
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
