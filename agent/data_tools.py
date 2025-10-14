import pandas as pd

# Global cache for loaded data
_data_cache = {}

def load_data():
    """Load all CSVs from fixtures folder once and cache them."""
    global _data_cache
    if _data_cache:
        return _data_cache  # already loaded

    try:
        actuals = pd.read_csv("fixtures/actuals.csv")
        budget = pd.read_csv("fixtures/budget.csv")
        cash = pd.read_csv("fixtures/cash.csv")
        fx = pd.read_csv("fixtures/fx.csv")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Missing file: {e.filename}")

    _data_cache = {
        "actuals": actuals,
        "budget": budget,
        "cash": cash,
        "fx": fx,
    }
    return _data_cache
