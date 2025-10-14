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

def get_revenue_vs_budget(month: str, year: int, data):
    """Return actual vs budget revenue for a given month/year."""
    actual = data["actuals"]
    budget = data["budget"]

    actual_val = actual.query("Month == @month and Year == @year and Account == 'Revenue'")["Value"].sum()
    budget_val = budget.query("Month == @month and Year == @year and Account == 'Revenue'")["Value"].sum()

    return {"actual": actual_val, "budget": budget_val}


def get_gross_margin(data, month_filter=None):
    """
    Return gross margin % by month.
    Expects data['actuals'] to have columns:
    month | entity | account_category | amount | currency
    """
    df = data["actuals"].copy()

    # Optional month filter
    if month_filter:
        df = df[df["month"] == month_filter]

    # Pivot so each account_category becomes a column
    pivot = df.pivot_table(
        index="month",
        columns="account_category",
        values="amount",
        aggfunc="sum"
    )

    # Compute gross margin %
    if "Revenue" in pivot.columns and "COGS" in pivot.columns:
        pivot["GrossMargin%"] = (pivot["Revenue"] - pivot["COGS"]) / pivot["Revenue"] * 100
    else:
        pivot["GrossMargin%"] = None

    return pivot.reset_index()[["month", "GrossMargin%"]]




def get_opex_breakdown(month: str, year: int, data):
    """Return Opex breakdown by category."""
    df = data["actuals"]
    opex = df.query("Month == @month and Year == @year and Account.str.startswith('Opex')", engine="python")
    return opex[["Account", "Value"]]


def get_cash_runway(data):
    """Estimate cash runway in months."""
    cash = data["cash"]
    last_cash = cash.sort_values(["Year", "Month"]).iloc[-1]["Balance"]
    # Assume net burn = avg of last 3 months of negative cash change
    cash["Delta"] = cash["Balance"].diff()
    avg_burn = abs(cash["Delta"].tail(3).mean())
    if avg_burn == 0:
        return float("inf")
    return last_cash / avg_burn
