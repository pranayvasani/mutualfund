"""Performance metrics for mutual funds."""

from __future__ import annotations

import pandas as pd


def calculate_returns(df: pd.DataFrame, period: str = "D") -> pd.Series:
    """Calculate periodic returns.

    Parameters
    ----------
    df : DataFrame
        NAV history with a ``nav`` column and ``date`` index or column.
    period : str
        Resample frequency (``D`` daily, ``W`` weekly, ``M`` monthly, ``A`` annual).
    """
    series = df.set_index("date")["nav"].astype(float)
    resampled = series.resample(period).last()
    returns = resampled.pct_change().dropna()
    return returns


def volatility(df: pd.DataFrame) -> float:
    """Return standard deviation of daily returns."""
    daily_returns = calculate_returns(df, "D")
    return daily_returns.std()


def calculate_cagr(df: pd.DataFrame) -> float:
    """Compute compounded annual growth rate."""
    if df.empty:
        return float("nan")
    start_nav = df.iloc[0]["nav"]
    end_nav = df.iloc[-1]["nav"]
    days = (df.iloc[-1]["date"] - df.iloc[0]["date"]).days
    years = days / 365.25
    if years == 0:
        return float("nan")
    return (end_nav / start_nav) ** (1 / years) - 1


def max_drawdown(df: pd.DataFrame) -> float:
    """Compute maximum drawdown."""
    nav_series = df.set_index("date")["nav"].astype(float)
    cummax = nav_series.cummax()
    drawdown = (nav_series - cummax) / cummax
    return drawdown.min()
