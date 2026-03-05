-- Create the SCD Type 2 Dimension Table
CREATE TABLE dim_customers_history (
    customer_sk SERIAL PRIMARY KEY,          -- The Surrogate Key (unique for this exact version)
    customer_id VARCHAR(50) NOT NULL,        -- The actual Business Key
    plan_type VARCHAR(50),
    monthly_fee DECIMAL(10,2),
    status VARCHAR(20),
    valid_from TIMESTAMP NOT NULL,           -- When did they start this plan?
    valid_to TIMESTAMP DEFAULT '9999-12-31', -- When did it end? (9999 means it's still active)
    is_current BOOLEAN DEFAULT TRUE          -- Quick flag to find the active row
);
