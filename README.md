# DEPI Learning Exercises

This repository collects Python exercises and notebooks from the DEPI learning track. It includes practice with Python basics, an exploratory analysis of the Wine dataset, and a small command-line employee manager. The notebooks retain their exercise prompts where they help explain the work.

## Contents

| File | What it covers |
|---|---|
| `Data_Visualization_session_2_Tasks.ipynb` | Exploring and plotting the built-in Wine dataset with pandas, Matplotlib and Seaborn |
| `Exercises datatypes.ipynb` | Lists, tuples, sets and dictionaries |
| `Tasks lec2_python.ipynb` | Conditions, loops and dictionaries |
| `Employees.py` | A CSV-backed employee manager with add, view, update, search and delete options |

The country-loop exercise in `Tasks lec2_python.ipynb` refers to separate course files named `countries.py` and `countries_details_data.py`; those files are not part of this repository.

## Run locally

Python 3.10 or newer is recommended. Install the notebook dependencies and launch Jupyter from the repository folder:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

The Wine notebook uses the dataset built into scikit-learn; no CSV download is needed. The employee manager can be run separately with `python Employees.py`. It creates `Employees_details.csv` in the current folder when first used.

## References

The data-types and Python fundamentals exercises are based on [Asabeneh Yetayeh's 30 Days of Python](https://github.com/Asabeneh/30-Days-Of-Python). The Wine dataset comes from [scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html).
