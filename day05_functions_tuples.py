# Functions
def check_approval(amount):
    if amount > 50000:
        return "CFO Approval Required"
    elif amount > 10000:
        return "Senior Manager Approval"
    elif amount > 5000:
        return "Manager Approval "
    else:
        return "Auto Approved"
    
# Calling the Function
result = check_approval(12000)
print(result)

# Functions with multiple parameters:
def calculate_tax(gross_amount,tax_rate):
    tax_amount = gross_amount * tax_rate
    net_payable = gross_amount + tax_amount
    return round(tax_amount,2), round(net_payable,2)

# Calling with two arguments
tax, net = calculate_tax(10000,0.18)

print(f"Tax: {tax}")
print(f"Net Payable: {net}")

# Default parameters — a parameter with a pre-set value:
def calculate_tax(gross_amount,tax_rate = 0.18):
    tax_amount = gross_amount * tax_rate
    net_payable = gross_amount + tax_amount
    return round(tax_amount,2), round(net_payable,2)

# Call WITHOUT tax_rate — uses default 0.18
tax,net = calculate_tax(10000)
print(f"Tax : {tax} | Net : {net}")

# Call WITH a different tax_rate — overrides the default

tax,net = calculate_tax(10000,0.12)
print(f"Tax : {tax} | Net : {net}")

# Functions + Lists — where it all connects:
invoices = [15000,8500,42000,6200,28000]

total_net = 0

for amount in invoices:
    tax,net = calculate_tax(amount) # loop through each invoice amount

    print(f"Gross: {amount} | Tax: {tax} | Net: {net}")

    total_net += net

print(f"Total Net Payable: {round(total_net,2)}")

# CONCEPT 2 — Tuples

# List — uses square brackets, can be changed
vendors = ["Vendor A","Vendor B","Vendor C"]
vendors.append("Vendor D")  # Allowed

# Tuple — uses round brackets, cannot be changed
currency_codes = ("USD","EUR","GBP","INR")

# Trying to change a tuple causes an error
#currency_codes.append("JPY") # TypeError: 'tuple' object has no attribute 'append'

# Accessing tuple items — same as lists:
currency_codes = ("USD", "EUR", "GBP", "INR")
print(currency_codes[1])
print(currency_codes[-1])
print(len(currency_codes))

# Looping through a tuple:
approval_levels = ("Auto Approved", "Manager Approval",
                   "Senior Manager Approval", "CFO Approval Required")
for level in approval_levels:
    print(level)


# Real use case — tuple unpacking:
def get_fx_range(currency_pair):
    if currency_pair == 'USD/INR':
        return 83.2, 84.5
    elif currency_pair == 'GBP/INR':
        return 104.1,106.3
    
# Unpacking the tuple into two variables
low,high = get_fx_range('USD/INR')

print(f"USD/INR today: Low {low} | High {high}")

# EXERCISE: Part 1 — Write and call a function:

def process_invoice(vendor, amount, tax_rate = 0.18):

    tax_amount = amount * tax_rate
    net_payable = amount + tax_amount
    return vendor ,round(tax_amount,2),round(net_payable,2)

vendor,tax,net = process_invoice("Vendor A", 12500)
print(f"{vendor} | Tax: {tax} | Net: {net}")

vendor,tax,net = process_invoice("Vendor B", 8000,0.12)
print(f"{vendor} | Tax: {tax} | Net: {net}")

vendor,tax,net = process_invoice("Vendor C", 45000)
print(f"{vendor} | Tax: {tax} | Net: {net}")

# EXERCISE: Part 2 — Function + List:
fx_transactions = [
    ("USD/INR", 83.5, 10000),
    ("GBP/INR", 105.3, 8000),
    ("EUR/INR", 89.1, 5000),
    ("USD/INR", 84.2, 15000),
]

def convert_to_inr(currency_pair,rate,amount_usd):
    amount_inr = amount_usd * rate
    return currency_pair, round(amount_inr,2)

for currency, rate, amount in fx_transactions:
    pair,inr = convert_to_inr(currency,rate,amount)

    print(f"{pair} -> {inr}")

# EXERCISE: Part 3 — Tuple:
approval_thresholds = (5000,10000,50000)

def get_approval_level(amount):
    if amount > approval_thresholds[2]:
        return "CFO Approval Required"
    elif amount > approval_thresholds[1]:
        return "Senior Manager Approval"
    elif amount > approval_thresholds[0]:
        return "Manager Approval"
    else:
        return "Auto Approved"

print(get_approval_level(4500))
print(get_approval_level(12000))
print(get_approval_level(67000))

    
