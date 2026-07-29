import pandas as pd


# Step 1 — Load Data

df = pd.read_csv("data/accounts_receivable.csv")

# Step 2 — The inspection reflex

# print(df.shape)                     # how big?
# print(df.head())                    # what does it look like?   
# print(df.info())                    # column types + non-null counts — THE key diagnostic
# print(df.columns.to_list())         # full list of column names

# Step 3 — Hunt for the mess

# print(df.isnull().sum())            # missing values per column
# print(df.duplicated().sum())          # how many duplicate rows

# Step 4 — Understand the key columns
# print(df["invoice_currency"].unique())      # which currencies?
# print(df["isOpen"].unique())                # what does isOpen look like?
# print(df["total_open_amount"].describe())     # the amount column — range, mean
print(df[["invoice_id","name_customer","total_open_amount","due_in_date","clear_date","isOpen"]].head(10))