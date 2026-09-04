import pandas as pd
from pathlib import Path

project = Path(__file__).resolve().parent.parent
data = project / "data"

tickets = pd.read_csv(data / "support_tickets.csv")


print("Support Ticket Analysis")
print("-" * 40)


# Basic ticket numbers
total_tickets = tickets["ticket_id"].nunique()

print("\nTotal support tickets:", total_tickets)


# Tickets by issue
issue_count = (
    tickets["issue_type"]
    .value_counts()
)

print("\nTickets by Issue")
print("-" * 40)
print(issue_count)


# Tickets by priority
priority_count = (
    tickets["priority"]
    .value_counts()
)

print("\nTickets by Priority")
print("-" * 40)
print(priority_count)


# Ticket status
status_count = (
    tickets["status"]
    .value_counts()
)

print("\nTickets by Status")
print("-" * 40)
print(status_count)


# Average resolution time for each issue
resolution_by_issue = (
    tickets.groupby("issue_type")["resolution_hours"]
    .agg(["count", "mean"])
    .sort_values("mean", ascending=False)
)

print("\nResolution Time by Issue")
print("-" * 40)
print(resolution_by_issue)


# Average resolution time by priority
resolution_by_priority = (
    tickets.groupby("priority")["resolution_hours"]
    .mean()
    .sort_values(ascending=False)
)

print("\nResolution Time by Priority")
print("-" * 40)
print(resolution_by_priority)


# Find issues that take the longest to resolve
slow_issues = resolution_by_issue.head(3)

print("\nIssues Taking the Longest to Resolve")
print("-" * 40)
print(slow_issues)


# Save useful results
issue_count.to_csv(
    data / "support_issues.csv",
    header=["ticket_count"]
)

resolution_by_issue.to_csv(
    data / "issue_resolution_analysis.csv"
)

print("\nSupport analysis completed.")