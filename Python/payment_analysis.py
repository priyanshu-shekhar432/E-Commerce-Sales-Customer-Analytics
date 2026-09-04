import pandas as pd
from pathlib import Path

project = Path(__file__).resolve().parent.parent
data = project / "data"

payments = pd.read_csv(data / "payments.csv")

print("Payment Analysis")
print("-" * 40)


# Basic payment information
total_payments = payments["order_id"].nunique()
total_amount = payments["amount"].sum()

print("\nPayment Summary")
print(f"Total payments : {total_payments:,}")
print(f"Total amount   : ₹{total_amount:,.2f}")


# Payment status
status_count = (
    payments["payment_status"]
    .value_counts()
)

print("\nPayment Status")
print("-" * 40)
print(status_count)


# Amount by payment status
status_amount = (
    payments.groupby("payment_status")["amount"]
    .agg(["count", "sum", "mean"])
    .sort_values("sum", ascending=False)
)

print("\nAmount by Payment Status")
print("-" * 40)
print(status_amount)


# Payment method analysis
method_analysis = (
    payments.groupby("payment_method")
    .agg(
        transactions=("order_id", "nunique"),
        amount=("amount", "sum")
    )
    .sort_values("amount", ascending=False)
)

print("\nPayment Method Analysis")
print("-" * 40)
print(method_analysis)


# Failed payments
failed_payments = payments[
    payments["payment_status"] == "Failed"
]

print("\nFailed Payments")
print("-" * 40)
print(f"Failed transactions: {len(failed_payments)}")

if len(failed_payments) > 0:
    print(
        failed_payments[
            ["order_id", "customer_id", "amount", "payment_method"]
        ].head(10).to_string(index=False)
    )


# Pending payments
pending_payments = payments[
    payments["payment_status"] == "Pending"
]

print("\nPending Payments")
print("-" * 40)
print(f"Pending transactions: {len(pending_payments)}")


# Save the analysis
status_amount.to_csv(
    data / "payment_status_analysis.csv"
)

method_analysis.to_csv(
    data / "payment_method_analysis.csv"
)

print("\nPayment analysis completed.")