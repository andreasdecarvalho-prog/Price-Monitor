# Price Monitor — Automated Web Data Collection Pipeline

## Overview

This project is a Python-based automation pipeline for collecting, cleaning, and delivering structured data from websites.

It demonstrates how to:

- scrape data from paginated websites
- process and normalize raw data using pandas
- export clean datasets to CSV
- run the entire pipeline automatically with a single command

The project is structured to reflect real-world freelance automation and data collection tasks.

---

## Features

- Web scraping with `requests` and `BeautifulSoup`
- Pagination handling
- Data cleaning and transformation with `pandas`
- Duplicate removal and type normalization
- CSV report generation
- Modular, production-style project structure
- Config-driven setup (no hardcoded URLs)

---

## Project Structure

price_monitor/
│
├── app/
│   ├── core/
│   │   └── config.py          
│   │
│   └── services/
│       ├── scraper.py         
│       ├── processor.py      
│       ├── reporter.py        
│       └── delivery.py        
│
├── scripts/
│   └── run_pipeline.py        
│
├── data/
│   └── books.csv              
│
├── requirements.txt
├── .env.example
└── README.md

---

## How It Works

### 1. Scraper

- Fetches data from a paginated website
- Extracts structured fields (e.g. title, price, URL)
- Returns raw data as Python dictionaries

### 2. Processor

- Converts raw data into a pandas DataFrame
- Cleans and normalizes values
- Removes duplicates
- Ensures correct data types

### 3. Reporter

- Exports the processed dataset to CSV
- Stores reports in an organized directory

### 4. Pipeline

- Orchestrates all steps from scraping to delivery
- Designed to run unattended

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/andreasdecarvalho-prog/price_monitor.git
cd price_monitor
pip install -r requirements.txt


---

Configuration

All configurable values live in one place.

Create a .env file based on the example:

cp .env.example .env

Edit values in app/core/config.py or .env as needed.


---

Running the Pipeline

Run the full automation pipeline with:

python scripts/run_pipeline.py

After execution:

Cleaned data will be saved as a CSV file in data/books.csv

Logs and prints will indicate processing status



---

Use Cases

This project reflects common freelance tasks such as:

price monitoring

product catalog extraction

market research data collection

replacing manual Excel workflows

scheduled or recurring data delivery



---

Notes

The target website used during development is a public demo site for scraping practice.

The architecture is intentionally simple and extensible.

The project can be adapted to other websites, schemas, or delivery formats.



---

Author

Developed by Andreas de Carvalho
Python Automation • Web Scraping • Data Processing

