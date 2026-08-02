import pandas as pd

# # Load Data
df = pd.read_csv("data/accounts_receivable.csv")

# print(df.head())

# print(df.columns.to_list())

# # Drop the empty column
df = df.drop(columns=["area_business"])

# print(df.shape)

# Investigate, then drop the duplicate column
# print((df["document_create_date"] == df["document_create_date.1"]).all())

# # See where they differ and what the differences look like
# diff = df[df["document_create_date"] != df["document_create_date.1"]]
# print(f"Rows where they differ: {len(diff)}")
# print(diff[["document_create_date","document_create_date.1"]].head(15))

# Verified document_create_date.1 is a distinct date (~1-4 days after creation),
# but undocumented and out of scope for the payment analysis — dropping it.

df = df.drop(columns=["document_create_date.1"])

print(df.shape)

# Remove duplicates

before = df.shape[0]
df = df.drop_duplicates().copy()
after = df.shape[0]
print(f"Removed {before - after} duplicate rows")

# # Convert number-dates to real dates
# date_cols = ["due_in_date", "posting_date", "document_create_date",
#              "baseline_create_date", "clear_date"]
# for col in date_cols:
#     df[col] = pd.to_datetime(df[col],format="%Y%m%d",errors="coerce")

# print(df.info())

# The above code converted clear_date & posting_date into NaT, as these two columns were already in date format, 
# we wanted a perticular format and because of errors = "coerce".

# Number-format dates (YYYYMMDD as floats) — need explicit format

num_date_cols = ["due_in_date","document_create_date","baseline_create_date"]
for col in num_date_cols:
    df[col] = pd.to_datetime(df[col],errors="coerce")

# String-format dates (YYYY-MM-DD HH:MM:SS) — let Pandas auto-detect
str_date_cols = ["clear_date","posting_date"]
for col in str_date_cols:
    df[col] = pd.to_datetime(df[col],errors="coerce")

# print(df.info())

# # flag the 6 missing invoice_ids
# missing_id = df[df["invoice_id"].isnull()]
# print(f"⚠️  {len(missing_id)} invoices missing invoice_id — flagged for follow-up:")
# print(missing_id[["name_customer", "total_open_amount", "due_in_date"]])

# confirm the open-invoice logic holds:
print(df[df["clear_date"].isnull()]["isOpen"].unique())    # expect [1] - all open
print(df[df["clear_date"].notnull()]["isOpen"].unique())    # expect [0] - all paid