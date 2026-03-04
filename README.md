# Telecom Data Analytics Engine
**End-to-End ELT Pipeline:** PostgreSQL • Docker • dbt • Python

[Image of ELT Data Pipeline Architecture with dbt and PostgreSQL]

This project simulates a modern Data Engineering and Quality Assurance workflow for a telecommunications provider. It handles the generation, ingestion, staging, and transformation of 50,000+ Call Detail Records (CDRs) to identify revenue leakage and analyze customer usage patterns.

## Overview
The engine transforms messy, raw CSV logs into an analytics-ready Star Schema using industry-standard ELT practices.
* **Ingestion:** Python/`psycopg2` utilizing the PostgreSQL `COPY` command for high-speed bulk loading.
* **Infrastructure:** Fully containerized PostgreSQL environment using Docker.
* **Transformation:** Modular SQL modeling using dbt (Data Build Tool).
* **Automated QA:** Built-in dbt testing suite to guarantee data integrity (uniqueness, referential integrity, and custom business logic).
* **Analytics:** Revenue leakage detection and monthly usage aggregation.

## Architecture
* **Raw Layer:** 50,000+ simulated records of customer metadata and usage logs (Data/Calls/Texts).
* **Staging Layer (`stg_`):** Data cleaning, type casting (handling `DECIMAL` for financial accuracy), and field standardization.
* **Core Layer (`fct_`):** Production-ready Fact tables aggregating usage by customer and billing cycle.

## Tech Stack
* **Database:** PostgreSQL 15 (Dockerized)
* **Transformation & Testing:** dbt-core, dbt-postgres
* **Language:** Python 3.12, Advanced SQL (CTEs, Window Functions)
* **Libraries:** Pandas, Psycopg2-binary

## How to Run Locally

**1. Start the Infrastructure**
Spin up the isolated PostgreSQL database on port 5433.
```bash
docker-compose up -d

## Results

Will post them tomorrow
