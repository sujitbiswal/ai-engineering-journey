# CONCEPT 1 — The two Pandas structures: Series and DataFrame
import pandas as pd
# balances = pd.Series([45,52,38,61],index = ['Mon','Tue','Wed','Thu'])
# print(balances)

# data = {
#     "vendor" :["Acme","Globex","Initech","Umbrella"],
#     "amount" :[8500,3200,15000,920],
#     "status" : ["Approved","Pending","Approved","Rejected"]
# }
# df = pd.DataFrame(data)
# print(df)

# # CONCEPT 2 — Inspecting a DataFrame: the first thing you always do
# df.head()       # First 5 rows
# df.shape        # (rows,coulmns)
# df.columns      # the column names
# df.info()       # column names, data types, missing-value counts
# df.describe()   # summary stats

# CONCEPT 3 — Selecting columns and rows
# print(df['vendor'])
# print(df['amount'])
# print(df[['vendor','amount']])

# -----EXERCISE - Part 1 — Inspect
data = {
    "payment_id": ["PAY-001", "PAY-002", "PAY-003", "PAY-004", "PAY-005", "PAY-006"],
    "entity":     ["Hess", "Globex", "Hess", "Initech", "Globex", "Hess"],
    "amount":     [8500, 3200, 15000, 42000, 920, 11200],
    "status":     ["Approved", "Pending", "Approved", "Approved", "Rejected", "Pending"]
}
df = pd.DataFrame(data)

# print(df)

# print(df.head())
# print(df.shape)
# print(df.info())
# print(df.describe())

# -----EXERCISE - Part 2 — Select columns
print(df['entity'])
print(df[["payment_id","amount"]])

# -----EXERCISE - Part 3 — Filter rows (boolean masks)
print(df[df['amount'] > 10000])

print(df[df['status'] == 'Approved'])

print(df[(df["amount"] > 5000) & (df['status'] == "Approved")])
