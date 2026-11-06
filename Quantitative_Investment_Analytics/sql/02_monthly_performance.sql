-- Microsoft Fabric Warehouse / T-SQL: monthly compounded returns via log aggregation.
-- Validate daily_return > -1 before applying LOG.
WITH monthly AS (
 SELECT fund_id, DATEFROMPARTS(YEAR([date]),MONTH([date]),1) AS month_start,
        EXP(SUM(LOG(1.0+CAST(daily_return AS FLOAT))))-1.0 AS monthly_return
 FROM dbo.fund_daily_returns
 GROUP BY fund_id,DATEFROMPARTS(YEAR([date]),MONTH([date]),1)
)
SELECT * FROM monthly ORDER BY fund_id,month_start;
