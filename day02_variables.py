# f-strings - how you build messages in python

vendor = "Vendor A"
amount = 12500
currency = "INR"
print(f"Invoice from {vendor} for {amount} {currency}")

# String methods - built-in tools for cleaning text
status = " PENDING  "
print(status.strip())  # Remove spaces
print(status.lower())  # lowercase
print(status.upper())  # Uppercase

vendor = "vendor a"
print(vendor.title())  # Title case

# String checking
invoice_id = "INV-1001"
print(invoice_id.startswith("INV"))
print(invoice_id.endswith("001"))
print("1001" in invoice_id)

# Basic Arithmatic
gross_amount = 118000
tax_rate = 0.18
tax_amount = gross_amount * tax_rate
net_amount = gross_amount - tax_amount
print(f"Gross: {gross_amount}")
print(f"Tax (18%): {tax_amount}")
print(f"Net: {net_amount}")

# Rounding - critical for financial calculations
print(f"Net (rounded): {round(net_amount,2)}")

#Integer division and modulo
total_invoices = 157
batch_size = 10
full_batches = total_invoices // batch_size
remaining = total_invoices % batch_size
print(f"Full batches: {full_batches}, Remaining: {remaining}")

# Check what type something is
amount = 12500
print(type(amount))   # <class 'int'>

rate = 83.75
print(type(rate))  # <class 'float'>

# Convert between types
amount_str = '12500'
amount_int = int(amount_str)
print(amount_int + 500)

#Float to int - drop decimal ,does not round
print(int(83.75))

# Exercise
#You are processing a single invoice. Write Python code that:
#1. Creates variables for: vendor name, invoice ID, gross amount (pick any realistic number), tax rate (18%), and currency ("INR")
#2. Calculates the tax amount and net payable amount
#3. Creates an invoice status — set it to "pending"
#4. Prints a clean invoice summary using f-strings in this format:

vendor_name = 'wkc'
invoice_id = 'INV-102'
gross_amount = 10000
tax_rate = 0.12
tax_amount = gross_amount * tax_rate
net_pay = gross_amount  - tax_amount
invoice_status = 'pending'

print("-------Invoice Summary--------")
print(f"Invoice ID: {invoice_id}")
print(f"\nVendor: {vendor_name}")
print(f"\nGross Amount: {gross_amount}")
print(f"\nTax (12%): {round(tax_amount)}")
print(f"\nNet Payable: {round(net_pay)}")
print(f"\nStatus: {invoice_status.upper()}")

