"""Riverside Apartments: three functions for you to finish.

The docstring under each function says what it should do, with examples.
Replace each raise NotImplementedError("Not built yet.") line with your own code.
Return each answer: the tests read what comes back, not what's printed.

listings is a pandas table (a DataFrame) with one row per apartment and the
columns listing_id, size_sqft, bedrooms, bathrooms, minutes_to_downtown,
has_parking, floor and monthly_rent, like the one pd.read_csv("listings.csv")
gives you. pandas is everything the three functions need.
"""
import pandas as pd

# The column that only names each row. It's never a feature. Ready to use.
ID_COLUMN = "listing_id"

# The column this exercise's report guesses: the rent. Ready to use.
LABEL = "monthly_rent"


def features_and_label(listings, label):
    """Split the table into X, the features, and y, the label, and return both.

    X is every column except ID_COLUMN and label, in the table's order, as a
    table. y is the label column. The table you're given stays as it was.

    With listings.csv and label "monthly_rent": X has 300 rows and the six
    columns size_sqft, bedrooms, bathrooms, minutes_to_downtown, has_parking
    and floor, and y is the 300 rents, named monthly_rent.
    """
    raise NotImplementedError("Not built yet.")


def center_and_spread(listings, column):
    """Return a column's middle and spread as a dictionary, each value rounded to 2 decimal places.

    The keys are "mean", "median" and "std" (the standard deviation, dividing
    by one less than the count, as pandas' std() and statistics.stdev do).
    Give back plain Python numbers: float() turns pandas' answer into one.

    With listings.csv:
    center_and_spread(listings, "monthly_rent") -> {"mean": 1373.97, "median": 1345.0, "std": 356.87}
    For a column holding 1100, 900, 1900, 1000 and 1100:
    -> {"mean": 1200.0, "median": 1100.0, "std": 400.0}
    """
    raise NotImplementedError("Not built yet.")


def ranked_by_correlation(listings, label):
    """Return the feature names, from the strongest correlation with the label to the weakest.

    The features are the columns features_and_label gives (no ID, no label).
    Strength is the size of each feature's correlation with the label, its sign
    ignored: -0.9 is stronger than 0.5. Return a list of column names.

    With listings.csv and label "monthly_rent":
    -> ["size_sqft", "bedrooms", "bathrooms", "minutes_to_downtown", "has_parking", "floor"]
    """
    raise NotImplementedError("Not built yet.")
