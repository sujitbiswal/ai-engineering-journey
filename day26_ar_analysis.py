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

# Rows and columns: 50,000 rows × 19 columns.
### ------ Missing values ----------
# clear_date — 10,000 missing
# area_business — 50,000 missing (the entire column is empty)
# invoice_id — 6 missing
# Duplicates — 1,161
# The odd column names : document_create_date and document_create_date.1
# The dates-as-numbers : due_in_date
# isOpen = 0 ; clear_date present (a real date) → the invoice was paid
# isOpen = 1 ; clear_date missing (NaN) → never paid
""" 
Drop area_business (100% empty)
Investigate and drop the redundant document_create_date.1
Remove 1,161 duplicate rows
Convert the number-dates (due_in_date, and check the others) to real dates with pd.to_datetime
Decide what to do about the 6 missing invoice_ids
Understand that clear_date missing = still open (not dirty data — meaningful)

"""
print(df[df["invoice_id"].isnull()])