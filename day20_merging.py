import pandas as pd

# CONCEPT 1 — merge: combining two tables on a key

# payments = pd.DataFrame({
#     "payment_id": ["PAY-001", "PAY-002", "PAY-003", "PAY-004"],
#     "vendor_id":  ["V01", "V02", "V01", "V03"],
#     "amount":     [8500, 3200, 15000, 42000]
# })

# vendors = pd.DataFrame({
#     "vendor_id":   ["V01", "V02", "V03"],
#     "vendor_name": ["Acme", "Globex", "Initech"],
#     "category":    ["IT", "Logistics", "IT"]
# })

# merged = pd.merge(payments,vendors,on="vendor_id")
# print(merged)

payments = pd.DataFrame({
    "payment_id": ["PAY-001","PAY-002","PAY-003","PAY-004","PAY-005","PAY-006"],
    "vendor_id":  ["V01","V02","V01","V03","V02","V09"],   # note: V09 is not in the vendor master
    "amount":     [8500, 3200, 15000, 42000, 920, 5000]
})

vendors = pd.DataFrame({
    "vendor_id":   ["V01","V02","V03","V04"],              # note: V04 has no payments
    "vendor_name": ["Acme","Globex","Initech","Umbrella"],
    "category":    ["IT","Logistics","IT","Facilities"]
})

# EXERCISE - Part 1 — Inner join (the default)
# merged = pd.merge(payments, vendors, on= "vendor_id", how= "inner")
# print(merged)

# EXERCISE - Part 2 — Left join (keep all payments)
merged_left = pd.merge(payments,vendors,on="vendor_id",how="left")
# print(merged_left)
# print(merged_left.isnull().sum())

# EXERCISE - Part 3 — Analyze the joined data
merged_left["vendor_name"] = merged_left["vendor_name"].fillna("UNKNOWN")
merged_left["category"] = merged_left["category"].fillna("UNKNOWN")
print(merged_left.groupby("category")["amount"].sum())