# Investment analytics methodology

All returns and AUM values are synthetic and not sourced from Netwealth, FactSet, or Morningstar Direct. No live market data is used.

- Daily returns are net of a simulated annual management fee; returns are compounded, never summed.
- Annualised return = (product(1 + daily return))^(252 / observations) - 1.
- Annualised volatility = sample standard deviation(daily return) × sqrt(252).
- Sharpe = (annualised return − assumed annual cash rate 3.8%) / annualised volatility.
- Sortino = (annualised return − cash rate) / annualised downside deviation against daily cash hurdle.
- Maximum drawdown = minimum(wealth index / historical peak − 1).
- Tracking error = std(daily fund return − daily benchmark return) × sqrt(252).
- Information ratio = mean(daily active return) × 252 / tracking error.
- Beta = covariance(fund, benchmark) / variance(benchmark).
- Browser dashboard calculates the same concepts using **monthly** aggregated returns (12 periods per year); values may differ from daily Python outputs. The browser assumes a constant 3.8% annual cash rate.
- Benchmark is a synthetic broad-market reference applied uniformly across funds for demonstration only. In production use asset-class-specific benchmarks and review mandate appropriateness.
- Manager ratings, governance flags and allocations are illustrative; no investment advice or actual fund due diligence is implied.
