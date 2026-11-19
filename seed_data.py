"""Makes listings.csv: 300 made-up apartment listings in the town of Riverside.

Ready to use; you don't need to run it. The CSV it made is already in this folder,
and the lessons, the tests and report.py all read that file.

Every number in the file is made up, and the pattern is built in on purpose, so you
can check whether the statistics find it. A real dataset's pattern is what you're
trying to find; this one is planted:

    monthly_rent = 300
                   + 1.5 for each square foot (size_sqft)
                   - 10 for each minute from downtown (minutes_to_downtown)
                   + 120 with a parking space (has_parking is 1)
                   + a random wobble (a standard deviation of 100 dollars)
    then rounded to the nearest 5 dollars.

Bedrooms and bathrooms follow size (bigger apartments have more of them) but add
nothing of their own to the rent, and the floor has no effect at all.

The random numbers come from a fixed seed, 103, so this script makes the same file
every time on the same version of NumPy. NumPy doesn't promise the same random
numbers from a seed across its versions (NEP 19), so the CSV in this folder, not
this script, is what keeps every learner's numbers the same.
"""
import numpy as np
import pandas as pd

SEED = 103
LISTINGS = 300


def make_listings(seed=SEED, count=LISTINGS):
    """Return the made-up listings as a DataFrame, one row per apartment."""
    rng = np.random.default_rng(seed)
    size_sqft = (rng.normal(850, 230, size=count).clip(400, 1700) / 10).round() * 10
    bedrooms = (size_sqft / 420 + rng.normal(0, 0.35, size=count)).round().clip(1, 4)
    bathrooms = np.where(size_sqft + rng.normal(0, 150, size=count) > 1000, 2, 1)
    minutes_to_downtown = rng.integers(5, 46, size=count)
    has_parking = (rng.random(size=count) < 0.4).astype(int)
    floor = rng.integers(1, 13, size=count)
    wobble = rng.normal(0, 100, size=count)
    rent = 300 + 1.5 * size_sqft - 10 * minutes_to_downtown + 120 * has_parking + wobble
    monthly_rent = (rent / 5).round() * 5

    return pd.DataFrame({
        "listing_id": [f"RA-{1001 + i}" for i in range(count)],
        "size_sqft": size_sqft.astype(int),
        "bedrooms": bedrooms.astype(int),
        "bathrooms": bathrooms.astype(int),
        "minutes_to_downtown": minutes_to_downtown.astype(int),
        "has_parking": has_parking.astype(int),
        "floor": floor.astype(int),
        "monthly_rent": monthly_rent.astype(int),
    })


if __name__ == "__main__":
    listings = make_listings()
    listings.to_csv("listings.csv", index=False)
    print("Wrote listings.csv:", len(listings), "listings.")
