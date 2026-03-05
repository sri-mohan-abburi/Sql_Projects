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

COMMIT;
