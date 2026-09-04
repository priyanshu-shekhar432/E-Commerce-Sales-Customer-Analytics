import pandas as pd
from pathlib import Path


# Locate the project and data folders
project_path = Path(__file__).resolve().parent.parent
data_path = project_path / "data"


# Load the datasets
customers = pd.read_csv(data_path / "customers.csv")
orders = pd.read_csv(data_path / "orders.csv")
products = pd.read_csv(data_path / "products.csv")
support_tickets = pd.read_csv(data_path / "support_tickets.csv")
payments = pd.read_csv(data_path / "payments.csv")


# Keep all datasets together for quick inspection
dataframes = {
    "Customers": customers,
    "Orders": orders,
    "Products": products,
    "Support Tickets": support_tickets,
    "Payments": payments
}


print("\nDataset Overview")
print("-" * 45)

for name, df in dataframes.items():
    print(f"{name}: {df.shape[0]:,} rows, {df.shape[1]} columns")


# Check the structure of each dataset
print("\nColumn Details")
print("-" * 45)

for name, df in dataframes.items():
    print(f"\n{name}")
    print(df.columns.tolist())


# Look for missing values
print("\nMissing Values")
print("-" * 45)

for name, df in dataframes.items():
    missing = df.isna().sum()
    missing = missing[missing > 0]

    print(f"\n{name}")

    if missing.empty:
        print("No missing values")
    else:
        print(missing)


# Check duplicate records
print("\nDuplicate Records")
print("-" * 45)

for name, df in dataframes.items():
    print(f"{name}: {df.duplicated().sum()} duplicates")


# Basic sales metrics
total_customers = customers["customer_id"].nunique()
total_orders = orders["order_id"].nunique()
total_sales = orders["sales"].sum()
total_quantity = orders["quantity"].sum()

print("\nBusiness Metrics")
print("-" * 45)
print(f"Unique customers : {total_customers:,}")
print(f"Total orders     : {total_orders:,}")
print(f"Total sales      : ₹{total_sales:,.2f}")
print(f"Units sold       : {total_quantity:,}")


# Understand the order distribution
print("\nOrder Status")
print("-" * 45)
print(orders["status"].value_counts())


# Combine orders with product information
order_products = orders.merge(
    products[["product_id", "category"]],
    on="product_id",
    how="left"
)

category_sales = (
    order_products
    .groupby("category")["sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Category")
print("-" * 45)
print(category_sales)


# Add customer city information to the orders
order_customers = orders.merge(
    customers[["customer_id", "customer_name", "city"]],
    on="customer_id",
    how="left"
)

city_sales = (
    order_customers
    .groupby("city")["sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by City")
print("-" * 45)
print(city_sales)


# Identify the highest-value customers
top_customers = (
    order_customers
    .groupby(["customer_id", "customer_name"])["sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Customers")
print("-" * 45)
print(top_customers)


# Review customer support activity
print("\nSupport Tickets")
print("-" * 45)
print(support_tickets["issue_type"].value_counts())

print(
    f"\nAverage resolution time: "
    f"{support_tickets['resolution_hours'].mean():.2f} hours"
)


# Check payment outcomes
print("\nPayment Status")
print("-" * 45)
print(payments["payment_status"].value_counts())


print("\nData exploration completed.")