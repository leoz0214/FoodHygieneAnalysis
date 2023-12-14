"""
Checks for correlation strengths between the 3 sub-metrics.
Obviously, there will be a general positive correlation,
but to varying degrees for different combinations.
"""
import itertools

import __init__
from constants import SUB_METRICS, Field
from utils import *


def display_pearson_correlation(data = DATA) -> None:
    """Displays Pearson correlations between each pair of metrics."""
    for first, second in itertools.combinations(SUB_METRICS, 2):
        correlation = data[first.value].corr(data[second.value], "pearson")
        print(
            f"Pearson Correlation between {first.value} "
            f"and {second.value}: {round(correlation, 4)}")


def display_spearman_correlation(data = DATA) -> None:
    """Displays Spearman correlations between each pair of metrics."""
    for first, second in itertools.combinations(SUB_METRICS, 2):
        correlation = data[first.value].corr(data[second.value], "spearman")
        print(
            f"Spearman Correlation between {first.value} "
            f"and {second.value}: {round(correlation, 4)}")
        

def display_low_rating_correlation() -> None:
    """
    Displays Pearson correlations between each pair of metrics,
    but only for establishments with an overall rating of 2 or less.
    """
    print("Low (<= 2) Rating Correlations")
    records = DATA.loc[DATA[Field.RATING.value] <= 2]
    display_pearson_correlation(records)
    display_spearman_correlation(records)


RUN_FUNCTIONS = {
    display_pearson_correlation: True,
    display_spearman_correlation: True,
    display_low_rating_correlation: True,
}


if __name__ == "__main__":
    for function, to_run in RUN_FUNCTIONS.items():
        if to_run:
            function()
