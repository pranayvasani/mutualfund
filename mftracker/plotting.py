"""Plotting utilities using Plotly."""

from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go


def plot_nav(df: pd.DataFrame, title: str = "NAV History") -> go.Figure:
    """Return a Plotly figure for NAV history."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["date"], y=df["nav"], mode="lines", name="NAV"))
    fig.update_layout(title=title, xaxis_title="Date", yaxis_title="NAV")
    return fig
