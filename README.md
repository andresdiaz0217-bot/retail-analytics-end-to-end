# Retail Analytics End-to-End Project

An end-to-end data analytics project demonstrating data generation, data quality validation, relational database management, SQL business analysis, and interactive dashboard development using Power BI.

## Project Overview

The goal of this project is to build a complete retail analytics workflow, from preparing structured datasets to analyzing sales performance and presenting business metrics in an interactive dashboard.

The project uses **synthetic retail data** to demonstrate practical data analytics and business intelligence skills.

## Business Objectives

- Analyze sales performance over time.
- Measure completed orders and order cancellation rates.
- Identify the best-performing product categories and products.
- Compare revenue across customer regions.
- Build an interactive dashboard to explore sales performance.
- Implement data quality checks and a structured relational database.

## Tech Stack

- **Python:** data generation, loading, and validation.
- **Pandas and NumPy:** data manipulation and synthetic data generation.
- **PostgreSQL:** relational database storage.
- **SQL:** business analysis and aggregation queries.
- **Power BI:** interactive dashboard and KPI visualization.
- **Git and GitHub:** version control and project documentation.

## Data Model

The project contains four related tables:

| Table | Description |
|---|---|
| `customers` | Customer identifiers, regions, and signup dates |
| `products` | Product identifiers, names, categories, and prices |
| `orders` | Order dates, customer references, and order statuses |
| `order_items` | Products purchased, quantities, unit prices, and discounts |

### Dataset Size

| Table | Records |
|---|---:|
| Customers | 500 |
| Products | 80 |
| Orders | 2,500 |
| Order Items | 7,394 |

The dataset covers a synthetic retail period from January 2025 to September 2026.

## Project Workflow

1. Generate synthetic retail datasets using Python.
2. Validate the data before loading it into the database.
3. Create a relational schema in PostgreSQL.
4. Load the CSV files into PostgreSQL.
5. Execute SQL queries to analyze business performance.
6. Connect Power BI to PostgreSQL and define relationships between tables.
7. Create DAX measures and an interactive sales dashboard.
8. Document the results and version the project using Git.

## Data Quality

The Python validation script performs checks on the generated datasets before database loading. The checks cover data consistency and structural requirements.

The PostgreSQL schema also defines primary keys, foreign keys, and data constraints to support relational integrity.

## SQL Business Analysis

The SQL analysis includes:

- Overall order performance.
- Monthly net revenue for completed orders.
- Revenue by product category.
- Revenue by customer region.
- Top 10 products ranked by net revenue.

Net revenue is calculated after discounts:

`quantity × unit_price × (1 - discount_pct)`

In this dataset, `discount_pct` is stored as a fraction. For example, `0.10` represents a 10% discount.

Only completed orders are included in sales revenue calculations.

## Power BI Dashboard

The `Sales Overview` report includes KPI cards and visualizations for exploring retail performance.

### Key Performance Indicators

- Net Revenue
- Completed Orders
- Units Sold
- Cancellation Rate

### Visualizations

- Monthly net revenue trend.
- Revenue by product category.
- Revenue by customer region.
- Top 10 products by net revenue.

### Interactive Filters

- Year
- Month
- Product category

The dashboard allows users to explore performance across different periods and product categories.

<!-- Add a dashboard screenshot at images/sales_overview.png when available. -->

## Repository Structure

```text
retail-analytics-end-to-end/
├── data/
│   └── synthetic/
│       ├── customers.csv
│       ├── products.csv
│       ├── orders.csv
│       └── order_items.csv
├── images/
│   └── sales_overview.png
├── sql/
│   ├── 01_create_schema.sql
│   └── 02_business_analysis.sql
├── src/
│   ├── generate_data.py
│   ├── load_data.py
│   └── validate_data.py
├── .gitignore
├── README.md
└── requirements.txt
```

The `images/` folder should contain the dashboard screenshot once it has been added to the repository. The Power BI `.pbix` report may also be included as a project deliverable.

## Getting Started

### Prerequisites

- Python 3.12 or a compatible Python version.
- PostgreSQL.
- Power BI Desktop.
- Git.

### 1. Clone the Repository

```bash
git clone https://github.com/andresdiaz0217-bot/retail-analytics-end-to-end.git
cd retail-analytics-end-to-end
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Database

Create a PostgreSQL database named `retail_analytics`.

Create a `.env` file in the project root with the following variable:

```env
DATABASE_URL=postgresql+psycopg://USERNAME:PASSWORD@localhost:5432/retail_analytics
```

Replace `USERNAME` and `PASSWORD` with your local PostgreSQL credentials. Do not commit this file to GitHub.

### 5. Prepare and Load the Data

Run the scripts from the project root:

```bash
python src/generate_data.py
python src/validate_data.py
```

Execute `sql/01_create_schema.sql` against the `retail_analytics` database, then load the datasets:

```bash
python src/load_data.py
```

### 6. Run the SQL Analysis

Execute the queries in `sql/02_business_analysis.sql` using pgAdmin or another PostgreSQL client.

### 7. Open the Power BI Report

Connect Power BI Desktop to the PostgreSQL database and recreate or open the report using the project data model and measures.

## Key Findings

The analysis supports comparisons of monthly revenue, category performance, regional sales, and product rankings.

Because the dataset is synthetic, these results are intended to demonstrate analytical methods rather than represent actual retail business performance.

## Skills Demonstrated

- Data preparation and validation with Python.
- Relational data modeling with PostgreSQL.
- SQL aggregation and business analysis.
- KPI design and DAX measures.
- Interactive reporting with Power BI.
- Version control and technical documentation.

## Project Status

The core data pipeline, SQL analysis, and Power BI dashboard have been developed. Documentation and portfolio presentation can be improved further with dashboard screenshots and the Power BI report file.

## Author

**Andrés Díaz Arias**  
Data and Software Engineer

GitHub: [andresdiaz0217-bot](https://github.com/andresdiaz0217-bot)
