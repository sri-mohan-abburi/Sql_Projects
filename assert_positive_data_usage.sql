-- This test checks if any usage logs have negative data consumption.
-- If this returns ANY rows, the dbt test will fail and alert us.

SELECT
    log_id,
    customer_id,
    data_mb_used
FROM {{ ref('stg_usage_logs') }}
WHERE data_mb_used < 0
