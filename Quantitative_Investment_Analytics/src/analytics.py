"""Reproducible investment analytics for synthetic daily fund returns.
Requires pandas and numpy: pip install -r requirements.txt
"""
from pathlib import Path
import numpy as np
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]

def metrics(fund, benchmark, rf_annual=0.038):
    x = pd.Series(fund, dtype=float).dropna()
    b = pd.Series(benchmark, dtype=float).reindex(x.index)
    paired = pd.concat([x.rename('r'), b.rename('b')], axis=1).dropna()
    x, b = paired.r, paired.b
    if len(x) < 2: raise ValueError('At least two aligned observations required')
    excess = x - b
    curve = (1+x).cumprod()
    drawdown = curve / curve.cummax() - 1
    annual_return = curve.iloc[-1]**(252/len(x))-1
    vol = x.std(ddof=1)*np.sqrt(252)
    downside = np.minimum(x-rf_annual/252,0)
    downside_dev = np.sqrt(np.mean(downside**2))*np.sqrt(252)
    te = excess.std(ddof=1)*np.sqrt(252)
    beta = x.cov(b)/b.var(ddof=1) if b.var(ddof=1)>0 else np.nan
    return {'annualised_return':annual_return,'annualised_volatility':vol,
            'sharpe':(annual_return-rf_annual)/vol if vol else np.nan,
            'sortino':(annual_return-rf_annual)/downside_dev if downside_dev else np.nan,
            'max_drawdown':drawdown.min(), 'tracking_error':te,
            'information_ratio':excess.mean()*252/te if te else np.nan, 'beta':beta}

def main():
    fund = pd.read_csv(ROOT/'data/fund_daily_returns.csv',parse_dates=['date'])
    bench = pd.read_csv(ROOT/'data/benchmark_daily_returns.csv',parse_dates=['date'])
    bench = bench.set_index('date').benchmark_return
    output=[]
    for fund_id,g in fund.groupby('fund_id'):
        s=g.set_index('date').daily_return.sort_index()
        output.append({'fund_id':fund_id,**metrics(s,bench)})
    out=pd.DataFrame(output).sort_values('sharpe',ascending=False)
    out.to_csv(ROOT/'data/fund_risk_summary.csv',index=False)
    print(out.to_string(index=False))
if __name__=='__main__':main()
