"""
Investigate differences in metrics based on the various business types
e.g. Takeaways, Schools, Pubs etc.
"""
import matplotlib.pyplot as plt

import __init__
from constants import Field
from utils import DATA, BUSINESS_TYPES


# Fixed categories based on available business types. 
CATEGORIES = {
    "Restaurants/Cafes/Canteens": {"Restaurant/Cafe/Canteen"},
    "Takeaways": {"Takeaway/sandwich shop"},
    "Pubs/Bars": {"Pub/bar/nightclub"},
    "Retailers": {
        "Retailers - supermarkets/hypermarkets", "Retailers - other"},
    "Schools/Universities": {"School/college/university"},
    "Hospitals/Childcare": {"Caring Premises"},
    "Hotels": {"Hotel/bed & breakfast/guest house"},
    "Mobile Caterers": {"Mobile caterer"},
    "Manufacturers": {"Manufacturers/packers"},
    "Farmers": {"Farmers/growers"},
    "Distributors/Transporters": {"Distributors/Transporters"},
    "Importers/Exporters": {"Importers/Exporters"}
}


def get_business_type(type_id: int) -> str | None:
    """Returns a string based on the business type."""
    business_type = BUSINESS_TYPES[type_id]
    for category, types in CATEGORIES.items():
        if business_type in types:
            return category
    # Not relevant to the program.
    return None


DATA[Field.TEMP.value] = DATA[Field.TYPE_ID.value].apply(get_business_type)
BUSINESS_TYPES_GROUPS = dict(map(iter, DATA.groupby(Field.TEMP.value, axis=0)))
ESTABLISHMENTS_BY_TYPE = {
    category: BUSINESS_TYPES_GROUPS[category] for category in CATEGORIES}


def get_mean(field: Field) -> dict[str, float]:
    """Returns the mean values for a given field for each business type."""
    return {
        business_type: records[field.value].mean()
        for business_type, records in ESTABLISHMENTS_BY_TYPE.items()
    }


def display_mean(field: Field) -> None:
    """Display the mean values for a given field for each business type."""
    for business_type, mean in get_mean(field).items():
        print(f"Mean {field.value} of {business_type}: {round(mean, 4)}")


def display_bar_chart(field: Field) -> None:
    """Displays a bar chart for a given field for each business type."""
    means = get_mean(field)
    plt.rcParams.update({"font.size": 5})
    plt.bar(means.keys(), means.values())
    plt.title(f"{field.value} by Business Type")
    plt.show()


display_mean_rating = lambda: display_mean(Field.RATING)
display_mean_hygiene = lambda: display_mean(Field.HYGIENE)
display_mean_cleanliness = lambda: display_mean(Field.CLEANLINESS)
display_mean_management = lambda: display_mean(Field.MANAGEMENT)
display_rating_graph = lambda: display_bar_chart(Field.RATING)
display_hygiene_graph = lambda: display_bar_chart(Field.HYGIENE)
display_cleanliness_graph = lambda: display_bar_chart(Field.CLEANLINESS)
display_management_graph = lambda: display_bar_chart(Field.MANAGEMENT)

RUN_FUNCTIONS = {
    display_mean_rating: True,
    display_mean_hygiene: True,
    display_mean_cleanliness: True,
    display_mean_management: True,
    display_rating_graph: True,
    display_hygiene_graph: True,
    display_cleanliness_graph: True,
    display_management_graph: True
}


if __name__  == "__main__":
    for function, to_run in RUN_FUNCTIONS.items():
        if to_run:
            function()
