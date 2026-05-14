# Without list comprehension — 4 lines
# amounts = [12500,8000,45000,3200,17800]
# tax_amounts = []

# for amount in amounts:
#     tax_amounts.append(round(amount * 0.8,2))

# print(tax_amounts)

# With list comprehension — 1 line
amounts = [12500,8000,45000,3200,17800]

tax_amounts = [round(amount * 0.18, 2) for amount in amounts]

print(tax_amounts)

# List comprehension with a condition:
amounts = [12500, 8000, 45000, 3200, 17800]

# Only keep amounts above 10000
high_value = [amount for amount in amounts if amount > 10000]
print(high_value)

# Real finance use case — filter pending invoices:
invoices = [
    {"id": "INV-001", "amount": 12500, "status": "pending"},
    {"id": "INV-002", "amount": 8000,  "status": "approved"},
    {"id": "INV-003", "amount": 45000, "status": "pending"},
    {"id": "INV-004", "amount": 3200,  "status": "rejected"},
]
# Get all pending invoice IDs in one line
pending_ids = [inv["id"] for inv in invoices if inv["status"] == "pending"]

print(pending_ids)

# Get total of pending amounts in one line
pending_total = sum([inv["amount"] for inv in invoices if inv["status"] == "pending"])

print(f"Total Pending: ₹{pending_total}")

# CONCEPT 2 — String Methods for Data Cleaning
# The essential string methods:
raw_vendor = "  VENDOR A  "
# strip() — removes leading and trailing spaces
clean = raw_vendor.strip()
print(f"'{clean}'")

# lower() — converts to lowercase
print(clean.lower())

# upper() — converts to uppercase
print(clean.upper())

# title() — capitalises first letter of each word
print(clean.title())

# replace() — replaces one string with another
invoice_id = "INV-001-2024"
clean_id = invoice_id.replace("-","")
print(clean_id)

# split() — splits a string into a list
#            by a separator you specify
currencies = "USD,EUR,GBP,INR"
currency_list = currencies.split(",")
print(currency_list)

# join() — opposite of split
#          joins a list into a string
rejoined = "|".join(currency_list)
print(rejoined)

# Checking string content:
invoice_id = "INV-1001"
status = "pending"
vendor = "  Vendor A  "

# startswith() — does it start with this?
print(invoice_id.startswith("INV"))
print(invoice_id.startswith("PAY"))

# endswith() — does it end with this?
print(invoice_id.endswith("1001"))

# in — does it contain this?
print("1001" in invoice_id)

# isdigit() — is it all numbers?
print("12500".isdigit())
print("125.50".isdigit())

# strip() with specific character
messy = "***INV-001***"
clean = messy.strip("*")
print(clean)

# Combining string methods — real data cleaning pipeline:
# Raw data coming from ABBYY OCR — messy vendor names
raw_vendors = ["  ACME CORP  ", "buildright ltd.", "CORE SUPPLY", "  dataflow inc  "]

# Clean all vendor names in one list comprehension
clean_vendors = [vendor.strip().title() for vendor in raw_vendors]
print(clean_vendors)

# Part 1 — List Comprehension: Exercise

amounts = [15000, 8500, 42000, 6200, 28000, 3500, 11000]

# Create a new list tax_amounts with 18% tax for each amount
tax_amounts = [round (amount * 0.18,2) for amount in amounts]
print(tax_amounts)

# Create a new list high_value with only amounts above ₹10000
high_value = [amount for amount in amounts if amount >10000 ]
print(high_value)

# Create a new list net_payable with gross + 18% tax for each amount
net_payable = [round(amount + (amount *0.18),2) for amount in amounts]
print(net_payable)

# Part 2 — String Cleaning:Exercise
raw_vendors = ["  ACME CORP  ", "buildright ltd.", "  CORE SUPPLY  ", "dataflow INC"]
raw_statuses = ["PENDING", "approved", "  Pending  ", "APPROVED"]
raw_ids = ["INV-001-2024", "INV-002-2024", "INV-003-2024"]

# Clean raw_vendors — strip spaces and convert to title case
clean_vendors = [vendor.strip().title() for vendor in raw_vendors]
print(clean_vendors)

# Clean raw_statuses — strip spaces and convert to lowercase
clean_statuses = [status.strip().lower() for status in raw_statuses]
print(clean_statuses)

# Clean raw_ids — remove the -2024 suffix from each ID
clean_ids = [id.replace("-2024","") for id in raw_ids]
print(clean_ids)

# Part 3 — Combine both: Exercise
""" Write a function called clean_invoice(invoice) that:

Strips and title-cases the vendor name
Lowercases the status
Returns the cleaned invoice dictionary

Then use a list comprehension to apply clean_invoice to all invoices and print the results.
 """

invoices = [
    {"id": "INV-001", "vendor": "  ACME CORP  ", "amount": 15000, "status": "PENDING"},
    {"id": "INV-002", "vendor": "buildright ltd.", "amount": 8500,  "status": "approved"},
    {"id": "INV-003", "vendor": "  CORE SUPPLY  ", "amount": 42000, "status": "PENDING"},
    {"id": "INV-004", "vendor": "dataflow INC",    "amount": 3500,  "status": "approved"},
]

def cleaned_invoice(invoice):
    invoice["vendor"] = invoice["vendor"].strip().title()
    invoice["status"] = invoice["status"].strip().lower()
    return invoice

cleaned_invoices = [cleaned_invoice(invoice) for invoice in invoices]

for inv in cleaned_invoices:
    print(inv)