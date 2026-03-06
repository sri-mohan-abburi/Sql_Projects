{% snapshot customers_snapshot %}

{{
    config(
      target_schema='snapshots',
      unique_key='customer_id',
      
      -- We use the 'check' strategy because our raw CSV doesn't have an 'updated_at' timestamp.
      -- dbt will compare these specific columns. If they change, it creates a new historical record.
      strategy='check',
      check_cols=['plan_type', 'monthly_fee', 'status']
    )
}}

-- This points directly to your raw staging data
SELECT * FROM {{ source('raw_telecom', 'raw_customers') }}

{% endsnapshot %}
