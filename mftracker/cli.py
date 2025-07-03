"""Command line interface for mutual fund tracker."""

from __future__ import annotations

import argparse
import sys

import pandas as pd

from .data import fetch_nav_data
from .performance import calculate_returns, calculate_cagr, volatility, max_drawdown
from .sip import sip_value
from .plotting import plot_nav


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Mutual fund tracker")
    parser.add_argument("scheme_code", help="Mutual fund scheme code")
    parser.add_argument("--sip", type=float, help="Monthly SIP amount")
    parser.add_argument("--plot", action="store_true", help="Show NAV plot")
    args = parser.parse_args(argv)

    df = fetch_nav_data(args.scheme_code)
    print("Data points:", len(df))

    cagr = calculate_cagr(df)
    vol = volatility(df)
    mdd = max_drawdown(df)
    print(f"CAGR: {cagr:.2%}")
    print(f"Volatility (daily std): {vol:.2%}")
    print(f"Max Drawdown: {mdd:.2%}")

    if args.sip:
        value = sip_value(df, args.sip)
        invested = args.sip * len(df)
        gain = value - invested
        print(f"SIP value: ₹{value:,.2f} (invested ₹{invested:,.2f}, gain ₹{gain:,.2f})")

    if args.plot:
        fig = plot_nav(df)
        fig.show()

    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
