import pandas as pd
from pathlib import Path

# project folder
project = Path(__file__).resolve().parent.parent
data = project / "data"

# read files
customers = pd.read_csv(data / "customers.csv")
orders = pd.read_csv(data / "orders.csv")
tickets = pd.read_csv(data / "support_tickets.csv")

print("Customer Analysis")
print("-" * 40)

# customers by segment
segment = customers["segment"].value_counts()

print("\nCustomers by segment:")
print(segment)

# sales made by each customer
sales = (
    orders.groupby("customer_id")["sales"]
    .sum()
    .reset_index()
)

# number of orders for each customer
order_count = (
    orders.groupby("customer_id")["order_id"]
    .nunique()
    .reset_index(name="orders")
)

# combine customer data with sales and order information
customer_data = customers.merge(
    sales,
    on="customer_id",
    how="left"
)

customer_data = customer_data.merge(
    order_count,
    on="customer_id",
    how="left"
)

customer_data["sales"] = customer_data["sales"].fillna(0)
customer_data["orders"] = customer_data["orders"].fillna(0)

# top customers
top_customers = customer_data.sort_values(
    "sales",
    ascending=False
).head(10)

print("\nTop 10 customers:")
print(
    top_customers[
        ["customer_id", "customer_name", "city",
         "segment", "orders", "sales"]
    ].to_string(index=False)
)

# city wise sales
city_sales = (
    customer_data.groupby("city")["sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by city:")
print(city_sales)

# support tickets per customer
ticket_count = (
    tickets.groupby("customer_id")["ticket_id"]
    .count()
    .reset_index(name="support_tickets")
)

customer_data = customer_data.merge(
    ticket_count,
    on="customer_id",
    how="left"
)

customer_data["support_tickets"] = (
    customer_data["support_tickets"].fillna(0)
)

# customers who have both high sales and support issues
high_value = customer_data["sales"].quantile(0.75)

customers_to_check = customer_data[
    (customer_data["sales"] >= high_value) &
    (customer_data["support_tickets"] > 0)
].sort_values("sales", ascending=False)

print("\nHigh-value customers with support tickets:")
print(
    customers_to_check[
        ["customer_id", "customer_name", "sales", "support_tickets"]
    ].head(10).to_string(index=False)
)

# save the result
output = project / "data" / "customer_analysis.csv"
customer_data.to_csv(output, index=False)

print("\nCustomer analysis completed.")
print(f"Saved to: {output}")