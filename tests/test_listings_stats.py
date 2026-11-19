# Tests for listings_stats.py. Run them with: python -m pytest (in the exercise folder, with the virtual environment
# active). Each test calls one of your functions, on the 300 listings in listings.csv or on a small table written in
# the test, and checks what comes back. A failing test says what it called, what it expected and what came back.
# You don't need to change this file.
import pandas as pd

from listings_stats import ID_COLUMN, LABEL, center_and_spread, features_and_label, ranked_by_correlation

FEATURES_FOR_RENT = ["size_sqft", "bedrooms", "bathrooms", "minutes_to_downtown", "has_parking", "floor"]


def check(call, got, expected):
    """Fails with a message that says what the call returned and what it should return."""
    assert got == expected, f"{call} should return {expected!r}, but it returned {got!r}."


# features_and_label

def test_1_features_and_label_x_is_the_six_feature_columns_for_monthly_rent(listings):
    X, y = features_and_label(listings, "monthly_rent")
    check("the columns of X from features_and_label(listings, 'monthly_rent')", list(X.columns), FEATURES_FOR_RENT)
    check("the number of rows in X", len(X), 300)


def test_2_features_and_label_y_is_the_300_monthly_rents(listings):
    X, y = features_and_label(listings, "monthly_rent")
    check("the name of y from features_and_label(listings, 'monthly_rent')", y.name, "monthly_rent")
    check("the number of values in y", len(y), 300)
    check("the first three values of y", y.iloc[:3].tolist(), [1870, 960, 1605])


def test_3_features_and_label_with_bedrooms_as_the_label_keeps_the_rent_as_a_feature(listings):
    X, y = features_and_label(listings, "bedrooms")
    check("the name of y from features_and_label(listings, 'bedrooms')", y.name, "bedrooms")
    check("the columns of X from features_and_label(listings, 'bedrooms')", list(X.columns),
          ["size_sqft", "bathrooms", "minutes_to_downtown", "has_parking", "floor", "monthly_rent"])


def test_4_features_and_label_leaves_the_table_it_was_given_unchanged(listings):
    features_and_label(listings, "monthly_rent")
    check("the table's columns after features_and_label(listings, 'monthly_rent')", list(listings.columns),
          [ID_COLUMN] + FEATURES_FOR_RENT + ["monthly_rent"])


# center_and_spread

def test_5_center_and_spread_of_monthly_rent_is_1373_97_1345_and_356_87(listings):
    check("center_and_spread(listings, 'monthly_rent')", center_and_spread(listings, "monthly_rent"),
          {"mean": 1373.97, "median": 1345.0, "std": 356.87})


def test_6_center_and_spread_of_size_sqft_is_855_8_845_and_225_53(listings):
    check("center_and_spread(listings, 'size_sqft')", center_and_spread(listings, "size_sqft"),
          {"mean": 855.8, "median": 845.0, "std": 225.53})


def test_7_center_and_spread_of_five_rents_is_1200_1100_and_400():
    building = pd.DataFrame({"monthly_rent": [1100, 900, 1900, 1000, 1100]})
    check("center_and_spread(a table of 1100, 900, 1900, 1000 and 1100, 'monthly_rent')",
          center_and_spread(building, "monthly_rent"), {"mean": 1200.0, "median": 1100.0, "std": 400.0})


def test_8_center_and_spread_of_1250_and_1350_divides_by_one_less_than_the_count_for_70_71():
    building = pd.DataFrame({"monthly_rent": [1250, 1350]})
    check("center_and_spread(a table of 1250 and 1350, 'monthly_rent')",
          center_and_spread(building, "monthly_rent"), {"mean": 1300.0, "median": 1300.0, "std": 70.71})


def test_9_center_and_spread_gives_plain_python_numbers(listings):
    result = center_and_spread(listings, "monthly_rent")
    check("the types of the values center_and_spread returns", [type(value).__name__ for value in result.values()],
          ["float", "float", "float"])


# ranked_by_correlation

def test_10_ranked_by_correlation_for_monthly_rent_starts_with_size_and_ends_with_floor(listings):
    check("ranked_by_correlation(listings, 'monthly_rent')", ranked_by_correlation(listings, "monthly_rent"),
          ["size_sqft", "bedrooms", "bathrooms", "minutes_to_downtown", "has_parking", "floor"])


def test_11_ranked_by_correlation_for_size_sqft_starts_with_monthly_rent(listings):
    check("ranked_by_correlation(listings, 'size_sqft')", ranked_by_correlation(listings, "size_sqft"),
          ["monthly_rent", "bedrooms", "bathrooms", "minutes_to_downtown", "has_parking", "floor"])


def test_12_ranked_by_correlation_puts_a_strong_negative_before_a_weak_positive():
    table = pd.DataFrame({
        "listing_id": ["RA-9001", "RA-9002", "RA-9003", "RA-9004"],
        "size_sqft": [700, 900, 800, 600],
        "minutes_to_downtown": [10, 20, 30, 40],
        "monthly_rent": [1600, 1500, 1400, 1300],
    })
    check("ranked_by_correlation(four listings: minutes and rent r = -1, size and rent r = 0.4, 'monthly_rent')",
          ranked_by_correlation(table, "monthly_rent"), ["minutes_to_downtown", "size_sqft"])


def test_13_ranked_by_correlation_leaves_out_the_id_and_the_label(listings):
    ranked = ranked_by_correlation(listings, LABEL)
    check("whether listing_id or monthly_rent is in ranked_by_correlation(listings, 'monthly_rent')",
          [name for name in ranked if name in (ID_COLUMN, LABEL)], [])
