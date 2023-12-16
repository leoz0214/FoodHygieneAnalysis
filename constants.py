"""Common constants for use throughout the project."""
import enum
import pathlib


class Field(enum.Enum):
    NAME = "Name"
    TYPE_ID = "Type ID"
    RATING = "Rating"
    HYGIENE = "Hygiene"
    CLEANLINESS = "Cleanliness"
    MANAGEMENT = "Management"
    DATE = "Inspection Date"
    LOCAL_AUTHORITY_ID = "Local Authority ID"
    # Temporary field used for batch grouping.
    TEMP = "temp"


SUB_METRICS = (Field.HYGIENE, Field.CLEANLINESS, Field.MANAGEMENT)


FOLDER = pathlib.Path(__file__).parent
DATA_FOLDER = FOLDER / "FoodHygieneData"
BUSINESS_TYPES_FILE = FOLDER / "business_types.json"
LOCAL_AUTHORITIES_FILE = FOLDER / "local_authorities.json"
