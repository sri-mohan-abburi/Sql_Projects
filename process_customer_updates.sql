-- Assume we loaded today's fresh customer data into a temporary table called 'temp_customer_updates'

BEGIN;

-- 1. Expire the old records for customers whose plans have changed
UPDATE dim_customers_history dim
SET 
    valid_to = CURRENT_TIMESTAMP,
    is_current = FALSE
FROM temp_customer_updates temp
WHERE dim.customer_id = temp.customer_id
  AND dim.is_current = TRUE
  AND (dim.plan_type != temp.plan_type OR dim.status != temp.status); -- Check if anything actually changed

-- 2. Insert the new active records for those changed customers
INSERT INTO dim_customers_history (customer_id, plan_type, monthly_fee, status, valid_from, valid_to, is_current)
SELECT 
    temp.customer_id,
    temp.plan_type,
    temp.monthly_fee,
    temp.status,
    CURRENT_TIMESTAMP,
    '9999-12-31',
    TRUE
FROM temp_customer_updates temp
JOIN dim_customers_history dim ON temp.customer_id = dim.customer_id
WHERE dim.is_current = FALSE 
  AND dim.valid_to = CURRENT_TIMESTAMP; -- Only insert for the ones we just expired in Step 1

COMMIT;
