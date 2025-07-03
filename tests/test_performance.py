from pathlib import Path
import json

import pandas as pd

from mftracker.data import fetch_nav_data
from mftracker.performance import calculate_cagr, max_drawdown, volatility
from mftracker.sip import sip_value


def load_sample_df() -> pd.DataFrame:
    sample_path = Path(__file__).parent / "data" / "sample_response.json"
    with open(sample_path) as f:
        data = json.load(f)
    df = pd.DataFrame(data["data"])
    df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")
    df["nav"] = pd.to_numeric(df["nav"])
    return df


def test_performance_metrics():
    df = load_sample_df()
    cagr = calculate_cagr(df)
    assert round(cagr, 6) == round((df.iloc[-1]["nav"] / df.iloc[0]["nav"]) ** (1 / (3/365.25)) - 1, 6)
    assert max_drawdown(df) < 0
    assert volatility(df) > 0


def test_sip_value():
    df = load_sample_df()
    value = sip_value(df, 1000)
    assert value > 0
