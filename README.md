# Market Anomaly Detector

A backend data engineering project that builds a real-time ETL pipeline to track cryptocurrency prices and detect sudden market volatility.

## Overview
This system runs continuously to fetch live market data, store it in a structured database, and perform immediate analysis to flag anomalies (price spikes). It demonstrates the core principles of Backend Engineering: **Extraction, Storage, and Analysis**.

**Key Features:**
- **Live Data Ingestion:** Fetches real-time pricing from the CoinGecko API.
- **Persistent Storage:** Saves historical data into a SQL database (SQLite).
- **Automated Analysis:** Compares current vs. historical data to calculate volatility.
- **Alert System:** Flags any price movement exceeding a defined threshold.

## Tech Stack
- **Language:** Python 3.10+
- **Database:** SQLite (Relational DB)
- **API:** CoinGecko Public API
- **Libraries:** `requests` (HTTP calls), `sqlite3` (Database interaction), `datetime` (Time-series management)

## Project Structure
The architecture is modular, separating concerns into distinct components:

```bash
market-analyzer/
├── tracker.py         # The Orchestrator (Main Entry Point)
├── fetch_price.py     # The "Extractor" (API Connection)
├── add_data.py        # The "Loader" (Database Insertions)
├── analyze.py         # The "Transformer" (Business Logic/Analysis)
├── database.py        # Database Setup (Schema Creation)
└── market_data.db     # The Storage (SQLite File)


