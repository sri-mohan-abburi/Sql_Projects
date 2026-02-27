import psycopg2
import pandas as pd

DB_PARAMS = {
    "dbname": "telecom_dw",
    "user": "admin",
    "password": "secretpassword",
    "host": "localhost",
    "port": "5433"
}

def run_analytical_query():
    print("Connecting to Data Warehouse...")
    conn = psycopg2.connect(**DB_PARAMS)
    
    # This is Advanced Analytical SQL. 
    sql_query = """
    WITH monthly_usage AS (
        -- Step 1: Aggregate total data used per customer for the current month
        SELECT 
            customer_id,
            DATE_TRUNC('month', timestamp) AS billing_month,
            SUM(data_mb_used) AS total_mb_used
        FROM raw_usage_logs
        WHERE usage_type = 'Data'
        GROUP BY 1, 2
    ),
    plan_limits AS (
        -- Step 2: Map the string plan names to actual MB limits
        SELECT 
            customer_id,
            plan_type,
            monthly_fee,
            status,
            CASE 
                WHEN plan_type = 'Basic_5GB' THEN 5000
                WHEN plan_type = 'Pro_50GB' THEN 50000
                WHEN plan_type = 'Unlimited_Max' THEN 9999999
            END AS plan_limit_mb
        FROM raw_customers
        WHERE status = 'Active'
    ),
    overage_calculation AS (
        -- Step 3: Join them together and calculate who went over their limit
        SELECT 
            p.customer_id,
            p.plan_type,
            p.plan_limit_mb,
            m.total_mb_used,
            (m.total_mb_used - p.plan_limit_mb) AS overage_mb
        FROM plan_limits p
        JOIN monthly_usage m ON p.customer_id = m.customer_id
        WHERE (m.total_mb_used - p.plan_limit_mb) > 0 -- Only keep the violators
    )
    -- Step 4: Use a Window Function to Rank the worst offenders
    SELECT 
        customer_id,
        plan_type,
        ROUND(plan_limit_mb, 2) AS limit_mb,
        ROUND(total_mb_used, 2) AS used_mb,
        ROUND(overage_mb, 2) AS overage_mb,
        RANK() OVER (ORDER BY overage_mb DESC) as violation_rank
    FROM overage_calculation
    LIMIT 10;
    """

    print("\n--- TOP 10 DATA OVERAGE OFFENDERS ---")
    df = pd.read_sql_query(sql_query, conn)
    print(df.to_string(index=False))
    
    conn.close()

if __name__ == "__main__":
    run_analytical_query()
