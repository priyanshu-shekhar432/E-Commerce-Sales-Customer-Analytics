# E-Commerce Sales & Customer Analytics

A data analysis project to understand e-commerce sales, customers, products, payments and support activities.

## Project Overview

This project analyzes e-commerce data to find useful business insights related to sales performance, customer behavior, product performance, payment failures and customer support.

The analysis was done using SQL, Python and Power BI.

## Tools Used

- SQL / MySQL
- Python
- Pandas
- NumPy
- Matplotlib
- Power BI
- Power Query
- DAX

## Dataset

The project contains the following tables:

- Customers - Customer details and segments
- Orders - Order and sales information
- Products - Product and category details
- Payments - Payment transactions and payment status
- Support Tickets - Customer support issues and resolution time

The dataset contains around 4,000 orders and 500 customers.

## What I Did

### Data Analysis
- Cleaned and checked the data using Python
- Performed exploratory data analysis
- Analyzed sales and customer data using SQL
- Checked order, payment and support data
- Identified top customers, products and cities

### Power BI Dashboard
Created a 3-page interactive dashboard covering:

**Page 1 - Executive Overview**
- Total Sales
- Total Orders
- Total Customers
- Cancelled %
- Monthly Sales Trend
- Sales by City
- Sales by Category
- Orders by Status

**Page 2 - Sales & Product Performance**
- Sales and order performance
- Product performance
- Category analysis
- Payment analysis
- Customer segment analysis

**Page 3 - Customer, Payment & Support Insights**
- Failed Payments
- Support Tickets
- Average Resolution Hours
- High Value Customers
- Failed Payments by Payment Method
- Support Issues by Type

## Key Insights

- Total sales were around ₹21.71M.
- The dataset contains around 4,000 orders from 500 customers.
- 24 customers were identified as high-value customers based on sales above ₹90,000.
- Payment analysis was used to identify failed transactions and payment methods with higher failures.
- Support ticket analysis was used to compare issue types and resolution time.
- Sales trends were analyzed month by month to understand business performance.

## Project Structure

```text
E-Commerce-Sales-Customer-Analytics
│
├── data
│   ├── customers.csv
│   ├── orders.csv
│   ├── products.csv
│   ├── payments.csv
│   ├── support_tickets.csv
│   └── analysis
│
├── Python
│   ├── customer_analysis.py
│   ├── data_analysis.py
│   ├── payment_analysis.py
│   ├── sales_analysis.py
│   └── support_analysis.py
│
├── powerbi
│   └── Ecommerce_Dashboard.pbix
│
├── screenshot
│
├── sql
│   └── ecommerce_analysis.sql
│
└── README.md
