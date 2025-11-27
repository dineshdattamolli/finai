from typing import Dict


def calc_emi(principal: float, annual_rate: float, years: float) -> float:
    """
    Calculate monthly EMI for a loan.

    :param principal: Total loan amount
    :param annual_rate: Annual interest rate in % (e.g. 10 for 10%)
    :param years: Tenure in years
    :return: Monthly EMI rounded to 2 decimals
    """
    if principal <= 0 or years <= 0:
        return 0.0

    monthly_rate = annual_rate / 12 / 100
    n_months = int(years * 12)

    if monthly_rate == 0:
        return round(principal / n_months, 2)

    emi = principal * monthly_rate * (1 + monthly_rate) ** n_months / (
        (1 + monthly_rate) ** n_months - 1
    )
    return round(emi, 2)


def build_budget(
    income: float,
    rent: float,
    transport: float,
    food: float,
    other: float,
    emi: float,
) -> Dict[str, float]:
    """
    Build a simple budget summary dictionary.
    """
    fixed = rent + transport + food + other + emi
    remaining = income - fixed
    savings = max(0.0, remaining)

    return {
        "income": round(income, 2),
        "rent": round(rent, 2),
        "transport": round(transport, 2),
        "food": round(food, 2),
        "other": round(other, 2),
        "emi": round(emi, 2),
        "savings": round(savings, 2),
        "fixed_total": round(fixed, 2),
        "remaining_after_fixed": round(remaining, 2),
        "savings_rate_pct": round((savings / income) * 100, 2) if income > 0 else 0.0,
    }
