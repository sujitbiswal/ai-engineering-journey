import pandas as pd

df = pd.read_csv("invoices.csv",header= None,
                 names = ["invoice_id","vendor","amount","status"])
# print(df.head())

# print(df.info())

# print(df.shape)

# print(df[df['status'] == 'Approved'])

# print(df.describe())

# print(df[df["amount"] > 10000])

df["amount"] = pd.to_numeric(df["amount"],errors= "coerce")

# print(df.info())

# print(df[df["amount"] > 10000])

# df_1 = df[df["amount"] > 10000]

# df_1.to_csv("high_value.csv",index=False)

print(df["amount"].dtype)