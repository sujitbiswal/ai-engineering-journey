# CONCEPT 1 — The groupby pattern: split, apply, combine
import pandas as pd

# df = pd.DataFrame({
#     "entity": ["Hess", "Globex", "Hess", "Initech", "Globex", "Hess"],
#     "amount": [8500, 3200, 15000, 42000, 920, 11200],
#     "status": ["Approved", "Pending", "Approved", "Approved", "Rejected", "Pending"]
# })

# Total amount per entity
# print(df.groupby("entity")["amount"].sum())

# print(df.groupby("entity")["amount"].mean())   # Average per entity
# print(df.groupby("entity")["amount"].max())    # Biggest per entity
# print(df.groupby("entity")["amount"].count())  # How many payments per entity

""" 
CONCEPT 2 — Grouping by multiple columns, and .agg() for several stats at once
Group by more than one column — pass a list. "Total per entity and status":

"""
# print(df.groupby(["entity","status"])["amount"].sum())   # Total per entity and status

"""
Multiple stats at once with .agg() — when you want sum and mean and count together, 
don't call groupby three times. Use .agg() with a list:

"""
# print(df.groupby(["entity","status"])["amount"].agg(["sum","mean","count","max"]))

# EXERCISE-Part 1 — Single-column groupby 

df = pd.DataFrame({
    "payment_id": ["PAY-001","PAY-002","PAY-003","PAY-004","PAY-005","PAY-006","PAY-007","PAY-008"],
    "entity":     ["Hess","Globex","Hess","Initech","Globex","Hess","Initech","Globex"],
    "amount":     [8500, 3200, 15000, 42000, 920, 11200, 7800, 4100],
    "status":     ["Approved","Pending","Approved","Approved","Rejected","Pending","Approved","Pending"]
})

# Total amount per entity
print(df.groupby("entity")["amount"].sum())
# Average amount per entity
print(df.groupby("entity")["amount"].mean())
# Count of payments per entity (how many each)
print(df.groupby("entity")["payment_id"].count())

# EXERCISE-Part 2 — Group by status

# Total amount per status (how much is Approved vs Pending vs Rejected?)
print(df.groupby("status")["amount"].sum())
#Count of payments per status
print(df.groupby("status")["payment_id"].count())

# EXERCISE-Part 3 — Multi-column + .agg()
# Total amount grouped by entity and status (two-level)
print(df.groupby(["entity","status"])["amount"].sum())
# Using .agg(), produce a per-entity summary showing sum, mean, count, and max of amount in one table
print(df.groupby("entity")["amount"].agg(["sum","mean","count","max"]))

# EXERCISE-Part 4 - A real question
"""
Which entity has the highest total payments? 
(Hint: groupby-sum, then .sort_values(ascending=False), or .idxmax() for the name of the top one — try .idxmax())

"""
print(df.groupby("entity")["amount"].sum().idxmax())