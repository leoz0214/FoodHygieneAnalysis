"""
Determines the highest/lowest scoring sub-metric,
from the perspective of various statistical averages.
"""
from collections import Counter

import __init__
from constants import Field
from utils import *


def display_mean() -> None:
    """Display the raw mean values of Hygiene, Cleanliness and Management."""
    for field in (Field.HYGIENE, Field.CLEANLINESS, Field.MANAGEMENT):
        mean = DATA[field.value].mean()
        print(f"Mean {field.value}: {round(mean, 4)}")


def display_weighted_mean() -> None:
    """
    Makes differences clearer using the following rule:
    Adjusts values using the following formula and then determines
    the weighted mean for each metric:
    score = 1.5 ** score
    Make larger scores weight more, since they get exponentially rarer.
    Furthermore, reduce a Management score of 30 to 25 for consistency.
    """
    for field in (Field.HYGIENE, Field.CLEANLINESS, Field.MANAGEMENT):
        weighted_mean = DATA[field.value].map(
            lambda score: 1.5 ** min(score, 25)).mean()
        print(f"Weighted Mean {field.value}: {round(weighted_mean, 4)}")


def display_counts() -> None:
    """Simply displays the number of instances of each score per metric."""
    for field in (Field.HYGIENE, Field.CLEANLINESS, Field.MANAGEMENT):
        print(f"Score Counts for {field.value}")
        counter = Counter(DATA[field.value])
        for score, count in sorted(counter.items()):
            print(f"{score}: {count} ({round(count / len(DATA) * 100, 2)}%)")


RUN_FUNCTIONS = {
    display_mean: True,
    display_weighted_mean: True,
    display_counts: True
}


if __name__  == "__main__":
    for function, to_run in RUN_FUNCTIONS.items():
        if to_run:
            function()
