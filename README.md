# Telecom Data Analytics Engine
**End-to-End ELT Pipeline:** PostgreSQL • Docker • dbt • Python



This project simulates a modern Data Engineering and Quality Assurance workflow for a telecommunications provider. It handles the generation, ingestion, staging, and transformation of 50,000+ Call Detail Records (CDRs) to identify revenue leakage, track historical plan changes, and serve analytics-ready data to BI tools.

## Overview
The engine transforms messy, raw CSV logs into an optimized Star Schema using industry-standard ELT practices.
* **High-Speed Ingestion:** Python/`psycopg2` utilizing the PostgreSQL `COPY` command for bulk loading, bypassing standard insert bottlenecks.
* **Modular Transformation:** SQL modeling using **dbt (Data Build Tool)** to isolate staging, core facts, and presentation marts.
* **Historical Tracking (SCD Type 2):** Automated dbt snapshots to track mutating state (e.g., customer plan upgrades) without destroying historical financial records.
* **Automated Data Quality (QA):** Built-in dbt testing suite to guarantee data integrity (uniqueness, referential integrity, and custom business logic like preventing negative data usage).
* **Containerized Infrastructure:** Fully isolated PostgreSQL environment using Docker.

## Architecture Design
* **Raw Layer:** 50,000+ simulated records of customer metadata and usage logs.
* **Staging Layer (`stg_`):** Data cleaning, type casting (`DECIMAL` for financial accuracy), and field standardization.
* **Snapshots Layer:** SCD Type 2 tracking of the `customers` table to maintain billing history.
* **Core Layer (`fct_`):** Production-ready Fact tables aggregating usage by customer and billing cycle.
* **Marts Layer (`mart_`):** Denormalized, wide tables specifically designed for seamless ingestion by BI tools (Tableau, Power BI).

## Tech Stack
* **Database:** PostgreSQL 15
* **Transformation & Testing:** dbt-core, dbt-postgres
* **Language:** Python 3.12, Advanced SQL
* **Libraries:** Pandas, Psycopg2-binary

## How to Run Locally

**1. Start the Infrastructure**
Spin up the isolated PostgreSQL database on port 5433.
```bash
docker-compose up -d
