import pandas as pd
import numpy as np

# CONCEPT 1 — Finding missing values

# df = pd.DataFrame({
#     "vendor": ["Acme", "Globex", None, "Umbrella", "Acme"],
#     "amount": [8500, np.nan, 15000, 920, 8500],
#     "status": ["Approved", "Pending", "Approved", None, "Approved"]
# })

# print(df.isnull())          # True/False for every cell — where are the holes?
# print(df.isnull().sum())    # count of missing per column — THE key diagnostic

# CONCEPT 2 — Handling missing values: drop or fill


# Option A — Drop rows with missing data:
# print(df.dropna())                            # drop any row with ANY missing value
# print(df.dropna(subset=["amount"]))             # drop only rows missing 'amount' specifically

# Option B — Fill missing data with something sensible:
# df["amount"].fillna(0)                          # fill missing amounts with 0
# df["amount"].fillna(df["amount"].mean())        # fill with the column average
# df["status"].fillna("Unknown")                  # fill missing text with a label

# # CONCEPT 3 — Duplicates
# print(df.duplicated())                          # True/False — is this row a duplicate of an earlier one?
# print(df.duplicated().sum())                    # how many duplicate rows total

df = pd.DataFrame({
    "payment_id": ["PAY-001","PAY-002","PAY-003","PAY-004","PAY-005","PAY-006","PAY-006"],
    "entity":     ["Hess","Globex","Hess",None,"Globex","Initech","Initech"],
    "amount":     [8500, np.nan, 15000, 42000, 920, 11200, 11200],
    "status":     ["Approved"," pending","APPROVED","Approved","Rejected ","Approved","Approved"]
})

# Part 1 — Diagnose
print(df.isnull().sum())                            # how many missing per column?
print(df.duplicated().sum())                        # how many duplicate rows?
print(df["status"].unique())                        # print the unique values

# Part 2 — Clean it
df_clean = df.drop_duplicates().copy()
df_clean["entity"] = df_clean["entity"].fillna("Unknown")
# df_clean["amount"] = df_clean["amount"].fillna(0)
df_clean["status"] = df_clean["status"].str.strip()
df_clean["status"] = df_clean["status"].str.title()

# Part 3 — Verify the clean worked
print(df_clean["status"].unique())
print(df_clean.isnull().sum())
print(df_clean.groupby("status")["amount"].sum())

missing_amount = df_clean[df_clean["amount"].isnull()]
print(f"{len(missing_amount)} payments need follow-up - missing amount:")
print(missing_amount)