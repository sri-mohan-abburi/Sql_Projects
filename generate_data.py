import csv
import random
from datetime import datetime, timedelta
import uuid

# Configuration
NUM_CUSTOMERS = 1000
NUM_RECORDS = 50000 

# 1. Generate Customers
print("Generating Customers...")
customers = []
plans = ['Basic_5GB', 'Pro_50GB', 'Unlimited_Max']

with open('customers.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['customer_id', 'join_date', 'plan_type', 'monthly_fee', 'status'])
    
    for _ in range(NUM_CUSTOMERS):
        cust_id = str(uuid.uuid4())[:8]
        plan = random.choice(plans)
        fee = 30 if plan == 'Basic_5GB' else (60 if plan == 'Pro_50GB' else 90)
        status = random.choices(['Active', 'Suspended', 'Churned'], weights=[80, 10, 10])[0]
        
        # Random join date in the last year
        join_date = datetime.now() - timedelta(days=random.randint(10, 365))
        
        customers.append(cust_id)
        writer.writerow([cust_id, join_date.strftime('%Y-%m-%d'), plan, fee, status])

# 2. Generate Call Detail Records (CDRs)
print(f"Generating {NUM_RECORDS} Usage Records...")
with open('usage_logs.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['log_id', 'customer_id', 'timestamp', 'usage_type', 'data_mb_used', 'call_duration_mins'])
    
    for i in range(NUM_RECORDS):
        log_id = i + 1
        cust_id = random.choice(customers)
        timestamp = datetime.now() - timedelta(days=random.randint(0, 30), minutes=random.randint(0, 1440))
        usage_type = random.choice(['Data', 'Call', 'Text'])
        
        data_mb = round(random.uniform(1.0, 500.0), 2) if usage_type == 'Data' else 0
        call_mins = random.randint(1, 45) if usage_type == 'Call' else 0
        
        writer.writerow([log_id, cust_id, timestamp.strftime('%Y-%m-%d %H:%M:%S'), usage_type, data_mb, call_mins])

print("Data generation complete! You now have customers.csv and usage_logs.csv")
