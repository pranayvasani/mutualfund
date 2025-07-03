"""SIP calculation utilities."""

from __future__ import annotations

import pandas as pd


def sip_value(df: pd.DataFrame, amount: float, date_col: str = "date") -> float:
    """Compute value of SIP investing ``amount`` every month.

    Parameters
    ----------
    df : DataFrame
        NAV history with columns ``date`` and ``nav``.
    amount : float
        Monthly investment amount in rupees.
    """
    df = df.sort_values(date_col)
    units = 0.0
    for _, row in df.iterrows():
        nav = row["nav"]
        units += amount / nav
    return units * df.iloc[-1]["nav"]
