# Vendor Sales Analysis

## 📌 Overview

Vendor Sales Analysis is an end-to-end data analytics project designed to evaluate vendor performance by integrating inventory, purchase, sales, pricing, and invoice data. The project uses Python for data ingestion and exploratory data analysis (EDA), and SQL with Common Table Expressions (CTEs) to generate business insights that help organizations identify high-performing vendors, optimize pricing strategies, and improve operational efficiency.

This project demonstrates a complete analytics workflow—from raw data ingestion to business intelligence reporting.

---

## 🎯 Problem Statement

Businesses often manage procurement, inventory, sales, and vendor invoices in separate systems, making it difficult to evaluate vendor performance effectively. Without consolidated analysis, organizations struggle to answer critical business questions such as:

- Which vendors generate the highest revenue?
- Which vendors provide the best profit margins?
- Are vendor invoices consistent with purchase records?
- Are products being sold below their purchase cost?
- Which vendors contribute the most to overall sales?

This project addresses these challenges by integrating multiple datasets into a unified analytical pipeline and generating actionable vendor performance metrics.

---

## 🚀 Objectives

- Build an automated data ingestion pipeline.
- Perform exploratory data analysis (EDA) to assess data quality.
- Analyze vendor performance using SQL.
- Calculate key business metrics such as revenue, cost, and profit margins.
- Identify pricing inefficiencies and invoice inconsistencies.
- Generate insights to support better procurement and business decisions.

---

## 📂 Dataset

The project utilizes multiple datasets representing different business operations:

- Begin Inventory
- End Inventory
- Purchases
- Purchase Prices
- Sales
- Vendor Invoices

These datasets are integrated to create a complete vendor performance analysis pipeline.

---

## 🛠️ Tech Stack

### Programming Language
- Python
- SQL (MySQL)

### Python Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn

### Database
- MySQL Server

### Development Environment
- Jupyter Notebook

---

## ⚙️ Project Workflow

### 1. Data Ingestion

- Imported multiple CSV datasets into MySQL.
- Implemented logging to monitor ingestion progress.
- Loaded datasets sequentially to maintain data integrity.

---

### 2. Exploratory Data Analysis (EDA)

Performed data quality assessment including:

- Missing value analysis
- Duplicate detection
- Summary statistics
- Sales trend analysis
- Pricing distribution
- Vendor contribution analysis
- Inventory consistency checks

---

### 3. Data Modeling

Integrated multiple datasets using SQL joins to create a unified analytical dataset for vendor evaluation.

---

### 4. Vendor Performance Analysis

Developed SQL queries using Common Table Expressions (CTEs) to calculate:

- Vendor Revenue
- Purchase Cost
- Gross Profit
- Profit Margin
- Vendor Contribution
- Sales Distribution
- Invoice Reconciliation Metrics

---

### 5. Business Insights

Generated insights to help businesses:

- Identify top-performing vendors.
- Detect pricing inconsistencies.
- Improve procurement decisions.
- Monitor vendor profitability.
- Optimize inventory planning.

---

## 📊 Key Features

- Automated data ingestion pipeline
- SQL-based analytical reporting
- Vendor performance evaluation
- Profitability analysis
- Pricing analysis
- Invoice reconciliation
- Exploratory Data Analysis (EDA)
- Business intelligence reporting
- Modular SQL queries using CTEs

---

## 📈 Business Impact

The project enables businesses to:

- Improve vendor selection.
- Increase procurement efficiency.
- Identify low-margin vendors.
- Detect invoice discrepancies.
- Support data-driven purchasing decisions.
- Reduce operational inefficiencies.

---

## 📁 Project Structure

```
Vendor-Sales-Analysis/
│
├── data/
│   ├── begin_inventory.csv
│   ├── end_inventory.csv
│   ├── purchases.csv
│   ├── purchase_prices.csv
│   ├── sales.csv
│   └── vendor_invoice.csv
│
├── notebooks/
│   ├── Exploratory Data Analysis.ipynb
│   └── Vendor Performance Analysis.ipynb
│
├── logs/
│   └── ingestion_db.log
│
├── sql/
│   └── vendor_analysis_queries.sql
│
├── README.md
└── requirements.txt
```

---

## 📊 Key SQL Concepts Used

- Common Table Expressions (CTEs)
- Joins
- Aggregate Functions
- GROUP BY
- ORDER BY
- CASE Statements
- Window Functions (where applicable)
- Data Aggregation

---

## 📚 Skills Demonstrated

- Data Analysis
- Business Analytics
- SQL Query Optimization
- Exploratory Data Analysis
- Data Cleaning
- Database Management
- Data Integration
- Business Intelligence
- Data Visualization
- Problem Solving

---

## 🔮 Future Enhancements

- Interactive Power BI Dashboard
- Streamlit Web Application
- Automated ETL Pipeline using Airflow
- Predictive Vendor Performance Modeling
- Inventory Forecasting
- Real-time Analytics Dashboard

---

## 👨‍💻 Author

**Devendra Kumar**

B.Tech | Indian Institute of Technology Guwahati

Data Analytics | SQL | Python | Power BI | Business Intelligence

---

## ⭐ If you found this project useful, consider giving it a Star!
