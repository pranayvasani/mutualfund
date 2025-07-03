"""Mutual fund tracker package."""

__all__ = ["fetch_nav_data", "calculate_returns", "calculate_cagr", "max_drawdown", "sip_value", "plot_nav"]

from .data import fetch_nav_data
from .performance import (
    calculate_returns,
    calculate_cagr,
    volatility,
    max_drawdown,
)
from .sip import sip_value
from .plotting import plot_nav
