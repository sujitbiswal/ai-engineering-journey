import pandas as pd
# df = pd.DataFrame({
#     "vendor": ["Acme", "Globex", "Initech", "Umbrella"],
#     "amount": [8500, 3200, 15000, 920],
#     "status": ["Approved", "Pending", "Approved", "Rejected"]
# })

# CONCEPT 1 — .loc and .iloc: label vs position
# .loc — by label (the names: index labels and column names)
# .iloc — by position (the integer position: 0th, 1st, 2nd... regardless of labels)

# print(df.loc[0])                      # the row with index LABEL 0 (the whole row)
# print(df.loc[0,"vendor"])              # row label 0, column named "vendor" → "Acme"
# print(df.loc[0:2,"vendor"])            # rows 0 to 2, the vendor column
# print(df.loc[:,"amount"])              # all rows, the amount column
# print(df.loc[0:2,["vendor","amount"]]) # specific rows AND columns by name

# CONCEPT 2 — Sorting: sort_values
# df.sort_values("amount")                             # ascending (smallest first) — default
# df.sort_values("amount",ascending= False)            # descending (biggest first)

# Sort by multiple columns — pass a list. It sorts by the first, then breaks ties with the second:
# df.sort_values(["status","amount"],ascending= False)
# df_sorted = df.sort_values(["status","amount"],ascending= False)
# print(df_sorted)

# top3 = df.sort_values("amount",ascending= False).head(3)
# print(top3)

df = pd.DataFrame({
    "payment_id": ["PAY-001", "PAY-002", "PAY-003", "PAY-004", "PAY-005", "PAY-006"],
    "entity":     ["Hess", "Globex", "Hess", "Initech", "Globex", "Hess"],
    "amount":     [8500, 3200, 15000, 42000, 920, 11200],
    "status":     ["Approved", "Pending", "Approved", "Approved", "Rejected", "Pending"]
})

# Exercise: Part 1 — .iloc (by position)
print(df.iloc[0])
print(df.iloc[3,2])
print(df.iloc[0:3,:])

# Exercise: Part 2 — .loc (by label)
print(df.loc[0,['entity','amount']])
print(df.loc[:,'amount'])
df_indexed = df.set_index("payment_id")
print(df_indexed)

print(df_indexed.loc["PAY-004"])

# Exercise: Part 3 — Sorting
print(df.sort_values("amount",ascending= False))

top3 = df.sort_values("amount",ascending= False).head(3)
print(top3)

df_sorted = df.sort_values(["entity","amount"],ascending= False)
print(df_sorted)