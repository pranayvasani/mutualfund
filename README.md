# Mutual Fund Tracker

This repository provides a small command line tool to fetch NAV data from [mfapi.in](https://mfapi.in) and compute simple performance metrics such as CAGR and max drawdown.

## Usage

Install dependencies:

```bash
pip install -r requirements.txt
```

Fetch data and view metrics for a scheme code:

```bash
python fundtracker.py 119598
```

This will print the latest NAV data along with CAGR and max drawdown statistics.

