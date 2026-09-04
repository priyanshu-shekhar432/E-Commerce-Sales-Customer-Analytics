import pandas as pd
from pathlib import Path

project = Path(__file__).resolve().parent.parent
data = project / "data"

orders = pd.read_csv(data / "orders.csv")
products = pd.read_csv(data / "products.csv")


print("Sales Analysis")
print("-" * 40)


# Convert order date into datetime
orders["order_date"] = pd.to_datetime(orders["order_date"])


# Basic sales numbers
total_sales = orders["sales"].sum()
total_orders = orders["order_id"].nunique()
total_units = orders["quantity"].sum()

print("\nOverall Sales")
print(f"Total sales  : ₹{total_sales:,.2f}")
print(f"Total orders : {total_orders:,}")
print(f"Units sold   : {total_units:,}")


# Average order value
average_order_value = total_sales / total_orders

print(f"Average order value: ₹{average_order_value:,.2f}")


# Monthly sales
orders["month"] = orders["order_date"].dt.to_period("M").astype(str)

monthly_sales = (
    orders.groupby("month")["sales"]
    .sum()
    .sort_index()
)

print("\nMonthly Sales")
print("-" * 40)
print(monthly_sales)


# Sales by product
product_sales = (
    orders.groupby("product_id")["sales"]
    .sum()
    .reset_index()
    .merge(
        products[["product_id", "product_name", "category"]],
        on="product_id",
        how="left"
    )
    .sort_values("sales", ascending=False)
)

print("\nTop Products")
print("-" * 40)
print(
    product_sales[
        ["product_id", "product_name", "category", "sales"]
    ].head(10).to_string(index=False)
)


# Sales by category
category_sales = (
    product_sales
    .groupby("category")["sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Category")
print("-" * 40)
print(category_sales)


# Discount analysis
discount_sales = (
    orders.groupby("discount_pct")
    .agg(
        orders=("order_id", "nunique"),
        sales=("sales", "sum")
    )
    .sort_index()
)

print("\nDiscount Analysis")
print("-" * 40)
print(discount_sales)


# Order status performance
status_sales = (
    orders.groupby("status")
    .agg(
        orders=("order_id", "nunique"),
        sales=("sales", "sum")
    )
    .sort_values("sales", ascending=False)
)

print("\nSales by Order Status")
print("-" * 40)
print(status_sales)


# Save the results
monthly_sales.to_csv(data / "monthly_sales.csv", header=["sales"])

product_sales.to_csv(
    data / "product_sales.csv",
    index=False
)

category_sales.to_csv(
    data / "category_sales.csv",
    header=["sales"]
)

print("\nSales analysis completed.")