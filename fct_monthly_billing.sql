WITH usage AS (
    SELECT * FROM {{ ref('stg_usage_logs') }}
),

customers AS (
    SELECT * FROM {{ ref('stg_customers') }}
),

monthly_aggregation AS (
    SELECT
        u.customer_id,
        u.billing_month,
        SUM(u.data_mb_used) AS total_data_mb,
        SUM(u.call_duration_mins) AS total_call_mins,
        COUNT(u.log_id) AS total_transactions
    FROM usage u
    GROUP BY 1, 2
)

SELECT
    m.customer_id,
    c.plan_type,
    c.account_status,
    m.billing_month,
    m.total_data_mb,
    m.total_call_mins,
    c.monthly_fee_usd AS base_fee
FROM monthly_aggregation m
LEFT JOIN customers c ON m.customer_id = c.customer_id
