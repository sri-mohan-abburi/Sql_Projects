{{ config(materialized='table') }}

WITH monthly_facts AS (
    SELECT * FROM {{ ref('fct_monthly_billing') }}
),

customer_history AS (
    SELECT * FROM {{ ref('customers_snapshot') }}
),

joined_data AS (
    SELECT
        f.billing_month,
        f.customer_id,
        -- Use the snapshot data to see what plan they were actually on DURING that billing month
        c.plan_type AS historical_plan_type,
        c.monthly_fee AS historical_monthly_fee,
        c.status AS historical_account_status,
        f.total_data_mb,
        f.total_call_mins,
        
        -- Business Logic: Did they churn this month?
        CASE WHEN c.status = 'Churned' THEN 1 ELSE 0 END AS is_churned,
        
        -- Revenue Calculation Base
        c.monthly_fee AS base_revenue
        
    FROM monthly_facts f
    -- The critical join: Match the customer ID, and ensure the billing month falls within the snapshot's valid timeframe
    LEFT JOIN customer_history c 
        ON f.customer_id = c.customer_id
        AND f.billing_month >= c.dbt_valid_from 
        AND (f.billing_month < c.dbt_valid_to OR c.dbt_valid_to IS NULL)
)

SELECT * FROM joined_data
