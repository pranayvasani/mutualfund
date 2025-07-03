"""Data retrieval utilities for mfapi.in."""

from __future__ import annotations

import json
import os
import time
from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd
import requests

CACHE_DIR = Path(os.environ.get("MF_CACHE_DIR", ".cache"))
CACHE_DIR.mkdir(parents=True, exist_ok=True)
CACHE_TTL = 24 * 3600  # one day


def _cache_path(scheme_code: str) -> Path:
    return CACHE_DIR / f"{scheme_code}.json"


def fetch_nav_data(scheme_code: str) -> pd.DataFrame:
    """Fetch NAV history for the given scheme code.

    Results are cached in ``CACHE_DIR`` for 24 hours.
    """
    cache_file = _cache_path(scheme_code)
    if cache_file.exists() and time.time() - cache_file.stat().st_mtime < CACHE_TTL:
        with open(cache_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        url = f"https://api.mfapi.in/mf/{scheme_code}"
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(data, f)

    # Convert to DataFrame
    records = data.get("data", [])
    df = pd.DataFrame(records)
    df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")
    df["nav"] = pd.to_numeric(df["nav"], errors="coerce")
    df = df.sort_values("date")
    df = df.reset_index(drop=True)
    return df
