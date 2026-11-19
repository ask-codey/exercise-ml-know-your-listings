# Shared set-up for the tests. You don't need to change this file.
# Each test that asks for listings gets its own fresh copy of the 300 listings in listings.csv, read from this
# exercise's folder, so one test can't change the table another test reads.
from pathlib import Path

import pandas as pd
import pytest

LISTINGS = Path(__file__).parent.parent / "listings.csv"


@pytest.fixture
def listings():
    """The 300 apartment listings in listings.csv, freshly read for one test."""
    return pd.read_csv(LISTINGS)
