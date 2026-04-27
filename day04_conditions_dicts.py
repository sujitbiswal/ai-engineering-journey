# If Statements and Dictionaries
# AI Engineering Journey - Sujit

invoice_amount = 15000
if invoice_amount > 10000:
    print("Requires senior approval")

# if / elif / else — multiple conditions:

invoice_amount1 = 15000

if invoice_amount1 > 50000:
    print("Requires CFO approval")

elif invoice_amount1 > 10000:
    print("Requires senior approval")

elif invoice_amount1 > 5000:
    print("Requires manager approvel")

else:
    print("Auto-approved")

# Combining conditions — and / or / not:
vendor_verified = True
amount_within_limit = True
is_duplicate = False

# AND- both must be True
if vendor_verified and amount_within_limit:
    print("Invoice can be processed")
# OR - at least one must be True
if vendor_verified or amount_within_limit:
    print("At least one check passed")
# NOT - flips True to False, False to True
if not is_duplicate:
    print("Not a duplicate - safe to process")

# Checking membership with 'in':
blocked_vendors = ["Vendor X", "Vendor Y", "Vendor Z"]
current_vendor = "Vendor X"

if current_vendor in blocked_vendors:
    print(f"{current_vendor} is blocked")
else:
    print(f"{current_vendor} is cleared")

# CONCEPT 2 — Dictionaries

# Accessing values:
invoice = {
    "invoice id": "INV-1001",
    "vendor": "Vendor A",
    "amount": 12500,
    "status": "pending"
}

print(invoice["invoice id"])
print(invoice["amount"])
# use value in calculation
tax = invoice["amount"] * 0.18
print(f"Tax: {round(tax,2)}")

# Updating and adding values:
invoice = {
    "invoice_id": "INV-1001",
    "vendor":     "Vendor A",
    "amount":     12500,
    "status":     "pending"
}

invoice["status"] = "approved"

print(invoice["status"])

# Add a new key-value pair
invoice["approved_by"] = "Sujit"

print(invoice["approved_by"])

# Looping through a dictionary:
invoice = {
    "invoice_id": "INV-1001",
    "vendor":     "Vendor A",
    "amount":     12500,
    "status":     "pending"
}

for key,value in invoice.items():
    print(f"{key}: {value}")

# List of dictionaries — how real data looks:
invoices = [
    {"invoice_id": "INV-1001", "vendor": "Vendor A", "amount": 12500, "status": "pending"},
    {"invoice_id": "INV-1002", "vendor": "Vendor B", "amount": 4200,  "status": "approved"},
    {"invoice_id": "INV-1003", "vendor": "Vendor C", "amount": 18000, "status": "pending"},
    {"invoice_id": "INV-1004", "vendor": "Vendor D", "amount": 750,   "status": "rejected"},
    {"invoice_id": "INV-1005", "vendor": "Vendor E", "amount": 9300,  "status": "pending"},
]

# Loop and filter pending invoices
for invoice in invoices:
    if invoice["status"] == "pending":
        print(f"{invoice["invoice_id"]} | {invoice["vendor"]} | {invoice["amount"]}")


# EXERCISE

invoice_1 = 4500
invoice_2 = 12000
invoice_3 = 67000

# Check invoice_1
if invoice_1 > 50000:
    print("CFO Approval Required")
elif invoice_1 > 10000:
    print("Senior Manager Approval")
elif invoice_1 > 5000:
    print("Manager Approval")
else:
    print("Auto Approved")

# check invoice_2
if invoice_2 > 50000:
    print("CFO Approval Required")
elif invoice_2 > 10000:
    print("Senior Manager Approval")
elif invoice_2 > 5000:
    print("Manager Approval")
else:
    print("Auto Approved")

# check invoice_3
if invoice_3 > 50000:
    print("CFO Approval Required")
elif invoice_3 > 10000:
    print("Senior Manager Approval")
elif invoice_3 > 5000:
    print("Manager Approval")
else:
    print("Auto Approved")

# Exercise Part 2 — Dictionary:

transactions = {
    "transaction_id": "FX-001",
    "currency_pair": "USD/INR",
    "rate": 90.5,
    "amount_usd": 10000,
    "status": "pending"
}

for key,value in transactions.items():
    print(f"{key} : {value}")

# update status
transactions["status"] = "settled"

# add new key
transactions["processed_by"] = "Sujit"

# print final dictionary
print("\n---- Updated Transactions ----") 
for key,value in transactions.items():
    print(f"{key} : {value}")

# Exercise Part 3 — List of dictionaries:
transactions = [
    {"id": "FX-001", "currency": "USD/INR", "rate": 83.5, "amount": 10000, "status": "pending"},
    {"id": "FX-002", "currency": "USD/INR", "rate": 84.2, "amount": 25000, "status": "settled"},
    {"id": "FX-003", "currency": "GBP/INR", "rate": 105.3,"amount": 8000,  "status": "pending"},
    {"id": "FX-004", "currency": "USD/INR", "rate": 84.8, "amount": 15000, "status": "settled"},
    {"id": "FX-005", "currency": "EUR/INR", "rate": 89.1, "amount": 5000,  "status": "pending"},
]

# Prints all pending transactions
for transaction in transactions:
    if transaction["status"] == "pending":
        print(f"{transaction["id"]} | {transaction["currency"]} | {transaction["rate"]} | {transaction["amount"]}")

# Total amount of settled transactions
transactions = [
    {"id": "FX-001", "currency": "USD/INR", "rate": 83.5, "amount": 10000, "status": "pending"},
    {"id": "FX-002", "currency": "USD/INR", "rate": 84.2, "amount": 25000, "status": "settled"},
    {"id": "FX-003", "currency": "GBP/INR", "rate": 105.3,"amount": 8000,  "status": "pending"},
    {"id": "FX-004", "currency": "USD/INR", "rate": 84.8, "amount": 15000, "status": "settled"},
    {"id": "FX-005", "currency": "EUR/INR", "rate": 89.1, "amount": 5000,  "status": "pending"},
]

total_settled_amount = 0
for transaction in transactions:
    if transaction["status"] == "settled":
        total_settled_amount += transaction["amount"]

print(f"\nTotal Settled Amount: {total_settled_amount}")


# Find transaction with highest rate

highest_rate = 0
highest_transaction = None

for transaction in transactions:
    if transaction["rate"] > highest_rate:
        highest_rate = transaction["rate"]
        highest_transaction = transaction

print(f"\nHighest Rate Transaction")
print(f"{highest_transaction["id"]} | {highest_transaction["currency"]} | {highest_transaction["rate"]} | {highest_transaction["amount"]}")
