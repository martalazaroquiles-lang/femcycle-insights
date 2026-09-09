-- Outlier detection based on percentiles (P5-P95) for this dataset,
-- rather than the fixed clinical range (21-35 days), since the simulated 
-- population has a mean cycle length of 37.4 days.

WITH percentiles AS (
    SELECT 
        (SELECT "Cycle Length" FROM ciclos ORDER BY "Cycle Length" LIMIT 1 OFFSET CAST(0.05 * (SELECT COUNT(*) FROM ciclos) AS INT)) AS p5,
        (SELECT "Cycle Length" FROM ciclos ORDER BY "Cycle Length" LIMIT 1 OFFSET CAST(0.95 * (SELECT COUNT(*) FROM ciclos) AS INT)) AS p95
)
SELECT 
    c."User ID",
    c."Cycle Start Date",
    c."Cycle Length",
    c."Period Length"
FROM ciclos c, percentiles p
WHERE c."Cycle Length" < p.p5 OR c."Cycle Length" > p.p95;