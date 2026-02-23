import psycopg2
import os

# Database connection settings
DB_PARAMS = {
    "dbname": "telecom_dw",
    "user": "admin",
    "password": "secretpassword",
    "host": "localhost",
    "port": "5433"
}

def setup_database():
    print("Connecting to PostgreSQL...")
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    # 1. Create Staging Tables
    print("Creating tables...")
    cur.execute("""
        DROP TABLE IF EXISTS raw_usage_logs;
        DROP TABLE IF EXISTS raw_customers;

        CREATE TABLE raw_customers (
            customer_id VARCHAR(50) PRIMARY KEY,
            join_date DATE,
            plan_type VARCHAR(50),
            monthly_fee DECIMAL(10, 2),
            status VARCHAR(20)
        );

        CREATE TABLE raw_usage_logs (
            log_id SERIAL PRIMARY KEY,
            customer_id VARCHAR(50) REFERENCES raw_customers(customer_id),
            timestamp TIMESTAMP,
            usage_type VARCHAR(20),
            data_mb_used DECIMAL(10, 2),
            call_duration_mins INTEGER
        );
    """)
    conn.commit()

    # 2. Bulk Load Customers
    print("Loading customers.csv...")
    with open('customers.csv', 'r') as f:
        next(f)  # Skip the header row
        cur.copy_expert("COPY raw_customers FROM STDIN WITH CSV", f)
    conn.commit()

    # 3. Bulk Load Usage Logs
    print("Loading usage_logs.csv...")
    with open('usage_logs.csv', 'r') as f:
        next(f)  # Skip the header row
        cur.copy_expert("COPY raw_usage_logs (log_id, customer_id, timestamp, usage_type, data_mb_used, call_duration_mins) FROM STDIN WITH CSV", f)
    conn.commit()

    # 4. Verify Data
    cur.execute("SELECT COUNT(*) FROM raw_customers;")
    cust_count = cur.fetchone()[0]
    
    cur.execute("SELECT COUNT(*) FROM raw_usage_logs;")
    log_count = cur.fetchone()[0]

    print(f"Success! Loaded {cust_count} customers and {log_count} usage logs.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    setup_database()
