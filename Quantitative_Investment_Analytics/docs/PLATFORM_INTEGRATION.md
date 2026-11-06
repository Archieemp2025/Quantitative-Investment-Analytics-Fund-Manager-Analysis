# Production integration blueprint (not deployed)

1. Ingest licensed FactSet / Morningstar Direct exports or approved platform extracts via secure APIs and scheduled Fabric Data Factory pipelines. No vendor connection is included or claimed.
2. Land raw files in OneLake bronze, validate identifiers, dates, currency, fees and return conventions, quarantine exceptions.
3. Create silver canonical fund, benchmark, calendar, manager and holdings dimensions with daily fact returns and AUM snapshots.
4. Build gold performance marts with daily, monthly and rolling risk measures; reconcile to approved external analytics.
5. Publish semantic model in Power BI, add RLS for investment governance users, implement refresh monitoring and approval workflows. Direct Lake is a proposed deployment option, not a deliverable in this demo.
6. Record methodology versions, source lineage, benchmark mappings and Investment Committee sign-off.

Suggested metrics: rolling 1/3/5-year returns, manager quartile ranks, tracking error, active share (requires holdings), attribution (requires holdings and sector weights), exposure drift, stale NAV, missing benchmark, exceptions SLA.
