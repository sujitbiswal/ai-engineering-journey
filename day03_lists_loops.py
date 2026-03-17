# Looping through Lists
invoice_amounts = [12500,8000,45000,3200,17800]
for amount in invoice_amounts:
    print(f"Processing: {amount}")

# Accumulating a total inside a loop
invoice_amounts = [12500,8000,45000,3200,17800]

total = 0  # Start at 0 before the loop

for amount in invoice_amounts:
    total += amount
print(f"Total: ₹{total}")

#----------------------------------------#

# Built-in functions that work on entire lists
invoice_amounts = [12500, 8000, 45000, 3200, 17800]

print(sum(invoice_amounts)) # Add all items in the list together
print(max(invoice_amounts))  # Returns the largest value in the list
print(min(invoice_amounts)) # Returns the smallest value in the list
print(len(invoice_amounts)) # Returns the count of items

# Average  - Python has no built-in 
average = sum(invoice_amounts)/len(invoice_amounts)
print(f"Average: ₹{round(average,2)}")

# Checking if a value exists in a list
blocked_vendors = ['Vendor X','Vendor Y','Vendor Z']
vendor = 'Vendor X'

if vendor in blocked_vendors:
    print(f"{vendor} is blocked - escalate")

else:
    print(f"{vendor} is cleared for payment")

# Exercise
fx_rates = [83.5, 84.2, 83.8, 84.5, 83.1, 84.8, 83.6]

print("--- FX Rate Summary ---")

highest_rate = max(fx_rates)
print(f"Highest Rate : {highest_rate}")
lowest_rate = min(fx_rates)
print(f"Lowest Rate : {lowest_rate}")
total_entries = len(fx_rates)
average_rate = round(sum(fx_rates)/total_entries,2)
print(f"Average Rate : {average_rate}")
print(f"Total Entries : {total_entries}")

# Exercise - Loop with a flag
for rate in fx_rates:
    if rate > 84.3:
        print(f"{rate} - High Alert")
    else:
        print(f"{rate} - Normal")