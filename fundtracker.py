import requests
import pandas as pd
from datetime import datetime
from typing import List, Dict

API_URL = "https://api.mfapi.in/mf/{}"

class NAVData:
    def __init__(self, scheme_code: str):
        self.scheme_code = scheme_code
        self.nav_df = None

    def fetch(self) -> pd.DataFrame:
        url = API_URL.format(self.scheme_code)
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()
        history = data.get('data', [])
        df = pd.DataFrame(history)
        df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
        df['nav'] = pd.to_numeric(df['nav'])
        df.sort_values('date', inplace=True)
        self.nav_df = df
        return df

    def get_returns(self) -> pd.Series:
        if self.nav_df is None:
            raise ValueError('NAV data not loaded')
        return self.nav_df['nav'].pct_change()

    def cagr(self) -> float:
        if self.nav_df is None:
            raise ValueError('NAV data not loaded')
        start_val = self.nav_df.iloc[0]['nav']
        end_val = self.nav_df.iloc[-1]['nav']
        days = (self.nav_df.iloc[-1]['date'] - self.nav_df.iloc[0]['date']).days
        years = days/365.0
        return (end_val/start_val)**(1/years) - 1

    def max_drawdown(self) -> float:
        if self.nav_df is None:
            raise ValueError('NAV data not loaded')
        cummax = self.nav_df['nav'].cummax()
        drawdown = self.nav_df['nav']/cummax - 1
        return drawdown.min()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Mutual fund NAV tracker')
    parser.add_argument('scheme_code', help='MF scheme code')
    args = parser.parse_args()

    nav = NAVData(args.scheme_code)
    df = nav.fetch()
    print(df.tail())
    print('CAGR: {:.2%}'.format(nav.cagr()))
    print('Max Drawdown: {:.2%}'.format(nav.max_drawdown()))
