-- ANSI-style SQL; adapt date parsing / functions to your warehouse.
CREATE TABLE fund_daily_returns (date DATE, fund_id VARCHAR(32), fund_name VARCHAR(100), asset_class VARCHAR(60), daily_return DECIMAL(18,10), aum_m DECIMAL(18,2), fee_pct DECIMAL(8,4));
CREATE TABLE benchmark_daily_returns (date DATE, benchmark_return DECIMAL(18,10), cash_daily_rate DECIMAL(18,10));
-- Uniqueness / missing values / outlier investigations
SELECT fund_id, date, COUNT(*) AS duplicate_count FROM fund_daily_returns GROUP BY fund_id,date HAVING COUNT(*)>1;
SELECT COUNT(*) AS null_critical_fields FROM fund_daily_returns WHERE date IS NULL OR fund_id IS NULL OR daily_return IS NULL;
SELECT * FROM fund_daily_returns WHERE daily_return <= -1 OR ABS(daily_return)>0.20;
-- Coverage reconciliation against benchmark
SELECT f.fund_id, COUNT(*) AS fund_observations, COUNT(b.date) AS matched_benchmark_observations
FROM fund_daily_returns f LEFT JOIN benchmark_daily_returns b ON f.date=b.date GROUP BY f.fund_id;
