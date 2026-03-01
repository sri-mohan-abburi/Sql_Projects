WITH source AS (
    SELECT * FROM {{ source('raw_telecom', 'raw_usage_logs') }}
),

renamed AS (
    SELECT
        log_id,
        customer_id,
        CAST(timestamp AS TIMESTAMP) AS usage_timestamp,
        DATE_TRUNC('month', timestamp) AS billing_month,
        LOWER(usage_type) AS usage_type,
        COALESCE(data_mb_used, 0.0) AS data_mb_used, -- Handle potential nulls
        COALESCE(call_duration_mins, 0) AS call_duration_mins
    FROM source
)

SELECT * FROM renamed
