# Mutual Fund Tracker

This project provides utilities to fetch NAV data for Indian mutual funds using [mfapi.in](https://www.mfapi.in/), compute basic performance metrics and simulate SIP investments.

## Features

- Retrieve and cache NAV history for a scheme code.
- Calculate returns, volatility, CAGR and maximum drawdown.
- Run a simple SIP calculation.
- Plot NAV history using Plotly.
- Command line interface for quick analysis.

## Installation

Create a virtual environment and install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Fetch NAV data, compute metrics and show a plot:

```bash
python -m mftracker.cli 119598 --plot --sip 1000
```

This will download the NAV history for scheme code `119598`, output statistics and display an interactive chart. SIP calculations assume a monthly investment of ₹1,000 for each data point in the history.
