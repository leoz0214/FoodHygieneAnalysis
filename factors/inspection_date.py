"""
Investigate differences in metrics based on inspection date.
Firstly, investigate metrics by Year/Month e.g. 2023-11
going back to a reasonable date.
Then, investigate metrics by just Month e.g. February.
"""
import matplotlib.pyplot as plt

import __init__
from constants import Field
from utils import DATA


EARLIEST_YEAR = 2010
MONTHS = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December")


def get_year_month(date: str) -> str | None:
    """
    Fetches the year-month of a date,
    returning None if year less than earliest year to analyse.
    """
    year, month, _ = date.split("-")
    return None if int(year) < EARLIEST_YEAR else f"{year}-{month}"


DATA[Field.TEMP.value] = DATA[Field.DATE.value].apply(get_year_month)
ESTABLISHMENTS_BY_YEAR_MONTH = dict(
    map(iter, DATA.groupby(Field.TEMP.value, axis=0, sort=True)))
DATA.drop(Field.TEMP.value, axis=1)


def get_month(date: str) -> str:
    """Fetches the month of a date."""
    return MONTHS[int(date.split("-")[1]) - 1]


DATA[Field.TEMP.value] = DATA[Field.DATE.value].apply(get_month)
ESTABLISHMENTS_BY_MONTH = dict(
    sorted(map(tuple, DATA.groupby(Field.TEMP.value, axis=0)),
        key=lambda pair: MONTHS.index(pair[0])))


def get_mean(dictionary: dict, field: Field) -> dict[str, float]:
    """
    Converts a dictionary of key, DataFrame pairs to means for a given field.
    """
    return {
        key: records[field.value].mean() for key, records in dictionary.items()}


def display_year_month_mean(field: Field) -> None:
    """Displays the year/month mean for a given metric."""
    for year_month, mean in get_mean(
        ESTABLISHMENTS_BY_YEAR_MONTH, field
    ).items():
        print(f"Mean {field.value} in {year_month}: {round(mean, 4)}")


def display_year_month_graph(field: Field) -> None:
    """Displays a bar chart of year/month for a given metric."""
    means = get_mean(ESTABLISHMENTS_BY_YEAR_MONTH, field)
    plt.rcParams.update({"font.size": 5})
    plt.bar(means.keys(), means.values())
    plt.title(f"{field.value} by Year/Month")
    plt.show()


def display_month_mean(field: Field) -> None:
    """Displays the monthly mean for a given metric (Jan - Dec)."""
    for month, mean in get_mean(ESTABLISHMENTS_BY_MONTH, field).items():
        print(f"Mean {field.value} in {month}: {round(mean, 4)}")


def display_month_graph(field: Field) -> None:
    """Displays a bar chart for given metrics by month."""
    means = get_mean(ESTABLISHMENTS_BY_MONTH, field)
    plt.rcParams.update({"font.size": 5})
    plt.bar(means.keys(), means.values())
    plt.title(f"{field.value} by Month")
    plt.show()   


display_year_month_rating = lambda: display_year_month_mean(Field.RATING)
display_year_month_hygiene = lambda: display_year_month_mean(Field.HYGIENE)
display_year_month_cleanliness = lambda: display_year_month_mean(Field.CLEANLINESS)
display_year_month_management = lambda: display_year_month_mean(Field.MANAGEMENT)
display_year_month_rating_graph = lambda: display_year_month_graph(Field.RATING)
display_year_month_hygiene_graph = lambda: display_year_month_graph(Field.HYGIENE)
display_year_month_cleanliness_graph = lambda: display_year_month_graph(Field.CLEANLINESS)
display_year_month_management_graph = lambda: display_year_month_graph(Field.MANAGEMENT)

display_month_rating = lambda: display_month_mean(Field.RATING)
display_month_hygiene = lambda: display_month_mean(Field.HYGIENE)
display_month_cleanliness = lambda: display_month_mean(Field.CLEANLINESS)
display_month_management = lambda: display_month_mean(Field.MANAGEMENT)
display_month_rating_graph = lambda: display_month_graph(Field.RATING)
display_month_hygiene_graph = lambda: display_month_graph(Field.HYGIENE)
display_month_cleanliness_graph = lambda: display_month_graph(Field.CLEANLINESS)
display_month_management_graph = lambda: display_month_graph(Field.MANAGEMENT)

RUN_FUNCTIONS = {
    display_year_month_rating: False,
    display_year_month_hygiene: False,
    display_year_month_cleanliness: False,
    display_year_month_management: False,
    display_year_month_rating_graph: False,
    display_year_month_hygiene_graph: False,
    display_year_month_cleanliness_graph: False,
    display_year_month_management_graph: False,

    display_month_rating: True,
    display_month_hygiene: True,
    display_month_cleanliness: True,
    display_month_management: True,
    display_month_rating_graph: True,
    display_month_hygiene_graph: True,
    display_month_cleanliness_graph: True,
    display_month_management_graph: True
}


if __name__  == "__main__":
    for function, to_run in RUN_FUNCTIONS.items():
        if to_run:
            function()
