# Retail Analytics End-to-End Project

An end-to-end data analytics project demonstrating synthetic data generation, data quality validation, relational database management, SQL business analysis, and interactive dashboard development using Power BI.

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

- **Python:** Data generation, loading, and validation.
- **Pandas and NumPy:** Data manipulation and synthetic data generation.
- **PostgreSQL:** Relational database storage.
- **SQL:** Business analysis and aggregation queries.
- **Power BI:** Interactive dashboard and KPI visualization.
- **DAX:** Business metrics and calculations.
- **Git and GitHub:** Version control and project documentation.

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
8. Document analytical findings and version the project using Git.

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

```sql
quantity * unit_price * (1 - discount_pct)
```

In this dataset, `discount_pct` is stored as a fraction. For example, `0.10` represents a 10% discount.

Only completed orders are included in sales revenue calculations.

## Power BI Dashboard

The `Sales Overview` report provides an interactive view of retail sales performance.

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

### Dashboard Preview

![Retail Sales Dashboard](images/sales_overview.png)

*If the screenshot is not available in the repository yet, add it to `images/sales_overview.png` or update this path to match the actual filename.*

## Key Findings

The following findings were obtained from the synthetic dataset by comparing August 2025 with August 2026.

### 1. Overall Revenue Performance

Net revenue decreased by approximately **4.85% year over year**, from 263,229.54 in August 2025 to 250,454.42 in August 2026.

### 2. Category Performance

Category performance varied considerably over the same period:

| Category | August 2025 Net Revenue | August 2026 Net Revenue | Year-over-Year Change |
|---|---:|---:|---:|
| Home | 41,825.78 | 61,395.58 | +46.78% |
| Sports | 74,317.19 | 58,503.27 | -21.28% |
| Stationery | 57,921.33 | 64,942.72 | +12.12% |
| Technology | 89,165.24 | 65,612.85 | -26.42% |

Home and Stationery recorded revenue growth, while Sports and Technology experienced declines. Technology had the largest percentage decrease among the four categories.

### 3. Sales Volume Versus Revenue

Completed-order units sold increased from 1,028 in August 2025 to 1,060 in August 2026, an increase of approximately **3.11%**.

Despite this increase in volume, net revenue declined. Net revenue per unit decreased from approximately 256.06 to 236.28, a decline of around **7.73%**.

This indicates that sales volume alone does not explain revenue performance. Further analysis of product mix, prices, and discounts could help investigate the difference.

### 4. Product Performance

The SQL analysis ranks the top 10 products by net revenue, helping identify the products that contributed the most revenue in the synthetic dataset.

The ranking can be explored in the Power BI dashboard and used to demonstrate product-level analysis.

### Interpretation and Limitations

These findings are descriptive and refer exclusively to the generated dataset. They do not establish the causes of revenue changes and should not be interpreted as the performance of a real company.

The analysis demonstrates how SQL and Power BI can be used to compare periods, identify category-level changes, and highlight questions for further business investigation.

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

The Power BI `.pbix` report may also be included in the repository if its file size is within GitHub's limits. If included, add its actual filename to this structure.

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

Activate it on Windows PowerShell:

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

### 5. Generate, Validate, and Load the Data

Run the scripts from the project root:

```bash
python src/generate_data.py
python src/validate_data.py
```

Execute `sql/01_create_schema.sql` against the `retail_analytics` database, then load the datasets:

```bash
python src/load_data.py
```

**Note:** The loading script expects the target tables to be empty. If the tables already contain data, follow the project's loading safeguards rather than loading the same records again.

### 6. Run the SQL Analysis

Execute the queries in `sql/02_business_analysis.sql` using pgAdmin or another PostgreSQL client.

### 7. Open the Power BI Report

If the `.pbix` file is included in the repository, open it using Power BI Desktop.

Otherwise, connect Power BI Desktop to the PostgreSQL database and recreate the report using the project data model, measures, and visualizations.

## Skills Demonstrated

- Data preparation and validation with Python.
- Relational data modeling with PostgreSQL.
- SQL aggregation and business analysis.
- KPI design and DAX measures.
- Interactive reporting with Power BI.
- Comparative sales and category performance analysis.
- Version control and technical documentation.

## Project Status

The core data pipeline, relational database schema, SQL business analysis, and interactive Power BI dashboard have been developed.

The project includes documented findings based on synthetic data. The dashboard screenshot and Power BI report file should be included in the repository when available.

## Author

**Andrés Díaz Arias**  
Data and Software Engineer

GitHub: [andresdiaz0217-bot](https://github.com/andresdiaz0217-bot)  
Repository: [Retail Analytics End-to-End](https://github.com/andresdiaz0217-bot/retail-analytics-end-to-end)
