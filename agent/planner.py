from .data_tools import (
    load_data,
    get_revenue_vs_budget,
    get_gross_margin,
    get_opex_breakdown,
    get_cash_runway,
)

def process_query(user_input: str):
    """Very simple rule-based intent routing."""
    data = load_data()
    q = user_input.lower()

    if "revenue" in q and "budget" in q:
        result = get_revenue_vs_budget("June", 2025, data)
        return f"June 2025 revenue was ${result['actual']:,} vs budget ${result['budget']:,}."

    elif "gross margin" in q:
        gm = get_gross_margin(data)
        latest = gm.tail(3)
        return f"Recent gross margin trend:\n{latest.to_string(index=False)}"

    elif "opex" in q:
        opex = get_opex_breakdown("June", 2025, data)
        return f"Opex breakdown for June 2025:\n{opex.to_string(index=False)}"

    elif "cash" in q and "runway" in q:
        runway = get_cash_runway(data)
        return f"Current cash runway is approximately {runway:.1f} months."

    else:
        return "Sorry, I didn't understand the question yet."
