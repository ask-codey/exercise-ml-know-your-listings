# Exercise: Know Your Listings

Exercise code for the lesson **Exercise: Know Your Listings** in the Machine Learning with Python course on [ask-codey.com](https://www.ask-codey.com).

An owner in the town of Riverside wants to price apartments with a model one day, and the town has 300 past listings to learn from. Before any model, you'll get to know the data: you'll write three functions in `listings_stats.py` that split the table into features and a label, sum up a column's middle and spread, and rank the features by how closely each moves with the rent. Tests call each function and check what it returns.

## What's here

- `listings.csv`: the 300 listings, our own made-up data: each apartment's `listing_id`, `size_sqft`, `bedrooms`, `bathrooms`, `minutes_to_downtown`, `has_parking` (1 with a parking space, 0 without), `floor` and `monthly_rent`. The lessons, the tests and `report.py` all read this file. Ready to use.
- `seed_data.py`: the script that made `listings.csv`, so you can see how the data was built and the pattern planted in it. You don't need to run it: NumPy doesn't promise the same random numbers from a seed on every version, so the CSV, not the script, is what keeps everyone's numbers the same. Ready to use.
- `listings_stats.py`: the three functions, `features_and_label`, `center_and_spread` and `ranked_by_correlation`, with the `ID_COLUMN` and `LABEL` they use. Each function stops with `NotImplementedError: Not built yet.` for now. The docstring under each says what it should do, with examples. For you to finish.
- `explore.ipynb`: a notebook for looking at the listings, with a histogram and a scatter plot, and trying your functions as you write them. The tests don't read it. Ready to use, and yours to change.
- `report.py`: describes the listings with your three functions and prints what each one gave, so you can see them at work. Ready to use.
- `tests/test_listings_stats.py`: tests that call your functions and check what comes back. You don't need to change this file.
- `tests/conftest.py`: gives each test a fresh copy of the 300 listings from `listings.csv`. Ready to use.
- `requirements.txt`: the packages this exercise needs, each at an exact version: pandas, NumPy, matplotlib (for the notebook's charts), ipykernel (so VS Code can run the notebook) and pytest. Ready to use.
- `pytest.ini`: tells pytest where the tests are and where to find `listings_stats.py`. Ready to use.
- `.gitignore`: tells Git to leave out the virtual environment and the files Python, pytest and the notebook make as they run. Ready to use.

## Before you start

The packages go in a virtual environment: a private set of packages for this folder only. In VS Code's terminal, in this folder, run these three commands.

On Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

On a Mac (zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- The first command makes the virtual environment, in a folder named `.venv`.
- The second turns it on for this terminal: the prompt starts with `(.venv)` from then on.
- The third installs the packages `requirements.txt` lists into it.

*Virtual Environments and pip* explains all three. The `.venv` folder is in `.gitignore`, so Git leaves it out: these commands make it again on any computer.

If PowerShell answers that running scripts is disabled on this system, run this once, then run the second command again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Each new terminal starts with the virtual environment off. If the prompt doesn't start with `(.venv)`, run the second command again. (VS Code often turns it on for you.)

To look at the listings, open `explore.ipynb`, choose the `.venv` kernel with **Select Kernel** (top right), and run the cells.

## Check your work

```bash
python -m pytest
```

At first every test fails: that is expected, because each function stops with a `NotImplementedError` for now. Each function you finish turns its tests green. A failing test's message says what it called, what it expected and what came back, for example *center_and_spread(a table of 1250 and 1350, 'monthly_rent') should return {'mean': 1300.0, 'median': 1300.0, 'std': 70.71}, but it returned {'mean': 1300.0, 'median': 1300.0, 'std': 50.0}.*

To see your functions at work on the whole file, run:

```bash
python report.py
```

## The rules

- Keep each function's name and parameters as they are, and keep `ID_COLUMN` and `LABEL` as they are.
- Leave the table you're given as it was: make new tables, don't change the one passed in.
- Round each number `center_and_spread` returns to 2 decimal places, and return plain Python numbers.
- Return each answer; don't only print it.
- Don't change the tests, `conftest.py`, `listings.csv`, `seed_data.py` or `report.py`.

## Tips

- Try each step in `explore.ipynb` first, on the real listings, then move the lines that work into `listings_stats.py`.
- `drop(columns=[...])` gives back a new table without those columns, and leaves the old one alone.
- pandas' `mean()`, `median()` and `std()` work on one column; `std()` divides by one less than the count, as `statistics.stdev` does.
- `X.corrwith(y)` gives each column of `X` its correlation with `y`; `abs()` drops the signs, and `sort_values(ascending=False)` puts the biggest first.
- After you change `listings_stats.py`, restart the notebook's kernel before you try it there, so the notebook imports your newest code.

## Hand it in

When it works, push your solution to a public repo of your own on GitHub, then paste that repo's address into **Submit your exercise** on the lesson page at [ask-codey.com](https://www.ask-codey.com). That's what completes the lesson. The lesson page shows the Git commands, step by step.
