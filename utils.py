"""
Utilities loaded first, before data analysis occurs.
This includes loading the CSV of data and the business types/authorities.
"""
import json

import pandas as pd

from constants import BUSINESS_TYPES_FILE, LOCAL_AUTHORITIES_FILE, DATA_FOLDER


# Select most recent file as the data file.
DATA_FILE = tuple(DATA_FOLDER.iterdir())[-1]
DATA = pd.read_csv(DATA_FILE)


with BUSINESS_TYPES_FILE.open("r", encoding="utf8") as f:
    BUSINESS_TYPES = dict(
        map(lambda pair: (int(pair[0]), pair[1]), json.load(f).items()))

with LOCAL_AUTHORITIES_FILE.open("r", encoding="utf8") as f:
    LOCAL_AUTHORITIES = dict(
        map(lambda pair: (int(pair[0]), pair[1]), json.load(f).items()))
