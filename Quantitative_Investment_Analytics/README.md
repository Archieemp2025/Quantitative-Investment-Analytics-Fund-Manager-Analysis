# Quantitative Investment Analytics | Fund Manager Research Dashboard

**Independent portfolio demonstration aligned with investment governance, performance measurement and manager research workflows. Not affiliated with Netwealth.**

![Status](https://img.shields.io/badge/data-synthetic-orange) ![Python](https://img.shields.io/badge/Python-analytics-blue) ![SQL](https://img.shields.io/badge/SQL-validation-275DAD)

## Live dashboard
Open [`dashboard.html`](dashboard.html) locally in a modern browser. It is a **self-contained, offline HTML dashboard** with no external libraries or APIs. To publish on GitHub Pages, enable Pages on `main` / root and visit `https://YOUR_USERNAME.github.io/YOUR_REPO/dashboard.html`.

## Business questions answered
- Which funds outperform the benchmark, and is the excess return explained by risk?
- How do Sharpe, Sortino, drawdown, tracking error and beta vary across managers?
- How do growth, balanced and defensive model portfolios allocate capital?
- What data-quality controls should govern investment reporting?
- What should an Investment Committee monitor before further due diligence?

## Technology
Python, pandas, NumPy, pytest, SQL (Fabric Warehouse compatible example), JavaScript, HTML, CSS, SVG charts, CSV; Microsoft Fabric / Power BI integration blueprint. No FactSet or Morningstar access is represented.

## Repository layout
```
dashboard.html                    Interactive offline investment dashboard
data/fund_daily_returns.csv       Synthetic daily fund observations
data/benchmark_daily_returns.csv  Synthetic daily benchmark observations
data/model_allocations.csv        Synthetic model weights
data/dashboard_monthly.json       Browser-ready compounded returns
src/analytics.py                 Daily-return risk/performance engine
sql/                             Schema, QA and monthly performance SQL
tests/                           Automated analytics tests
docs/                            Methodology and deployment blueprint
```

## Run analytics
```bash
pip install -r requirements.txt
python src/analytics.py
pytest -q
```

## Dashboard interactions
Select a fund, comparison period and model portfolio; switch between Overview, Manager Research and Governance. Export the current manager table as CSV. Metrics recalculate for the selected window.

## Assumptions & limitations
All figures are **synthetic**, generated using a seeded stochastic process, not investment returns of real products. Benchmark and cash assumptions are illustrative. Browser metrics use monthly frequency, Python uses daily frequency. No holdings-level attribution, live NAV feed, external vendor API, production Fabric pipeline, Power BI report or investment recommendation is claimed. See `docs/METHODOLOGY.md`.

## Portfolio positioning
Demonstrates quantitative analytics, investment performance measurement, benchmark comparison, risk reporting, fund-manager screening, data-quality controls, SQL and Python engineering, and stakeholder-oriented reporting.
