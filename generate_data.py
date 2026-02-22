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
