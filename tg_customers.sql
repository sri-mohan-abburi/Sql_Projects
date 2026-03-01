WITH source AS (
    SELECT * FROM {{ source('raw_telecom', 'raw_customers') }}
),

renamed AS (
    SELECT
        customer_id,
        CAST(join_date AS DATE) AS joined_on,
        plan_type,
        CAST(monthly_fee AS DECIMAL(10,2)) AS monthly_fee_usd,
        LOWER(status) AS account_status -- Standardizing to lowercase
    FROM source
)

SELECT * FROM renamed
