# Describes Riverside's 300 listings with your three functions from listings_stats.py, and prints what each one
# gave, so you can see them at work. Ready to use.
# Run it with: python report.py
import pandas as pd

from listings_stats import LABEL, center_and_spread, features_and_label, ranked_by_correlation

listings = pd.read_csv("listings.csv")
X, y = features_and_label(listings, LABEL)
print("1) listings:", len(listings))
print("2) features:", list(X.columns))
print("3) label:", y.name)

rent = center_and_spread(listings, LABEL)
print("4) rent, mean:", rent["mean"])
print("5) rent, median:", rent["median"])
print("6) rent, standard deviation:", rent["std"])

size = center_and_spread(listings, "size_sqft")
print("7) size, mean and standard deviation:", size["mean"], size["std"])

print("8) features, strongest correlation with the rent first:", ranked_by_correlation(listings, LABEL))
