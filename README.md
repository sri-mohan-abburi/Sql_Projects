# Telecom Data Analytics Engine
End-to-End ELT Pipeline: PostgreSQL • Docker • dbt • Python

This project simulates a modern Data Engineering workflow for a telecommunications company. It handles the ingestion, staging, and transformation of 50,000+ Call Detail Records (CDRs) to identify revenue leakage and customer usage patterns.

# Overview
The engine transforms messy, raw CSV logs into an analytics-ready Star Schema.

Ingestion: Python/Psycopg2 utilizing PostgreSQL COPY command for high-speed bulk loading.

Infrastructure: Fully containerized PostgreSQL environment using Docker.

Transformation: Modular SQL modeling using dbt (Data Build Tool).

Analytics: Revenue leakage detection and monthly usage aggregation.
