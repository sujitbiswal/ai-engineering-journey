class Invoice:
    def __init__(self,invoice_id,vendor,amount,status):
        self.invoice_id = invoice_id
        self.vendor = vendor
        self.amount = amount
        self.status = status

    def is_high_value(self):
        return self.amount > 10000
    
    def summary(self):
        return f"{self.invoice_id} | {self.vendor:<18} | ₹{self.amount:>7} | {self.status}"
    

def load_invoices(filename):
    invoices = []
    with open(filename) as f:
        for line in f:
            parts = line.strip().split(",")
            invoice_id = parts[0]
            vendor = parts[1]
            status = parts[3]
            try:
                amount = int(parts[2])
            except ValueError:
                print(f"Skipping bad row: {line.strip()}")
                continue
            invoices.append(Invoice(invoice_id,vendor,amount,status))
    return invoices


# invoices = load_invoices("invoices.csv")
# for inv in invoices:
#     print(inv.summary())

def total_payable(invoices):
    total = 0
    for inv in invoices:
        if inv.status == "Rejected":
            continue
        total += inv.amount

    return total

def count_by_status(invoices):
    counts = {}
    for inv in invoices:
        counts[inv.status] = counts.get(inv.status,0) + 1
    return counts

def high_value_invoices(invoices):
    result = []
    for inv in invoices:
        if inv.is_high_value():
            result.append(inv)
    return result

invoices = load_invoices("invoices.csv")

print("=" * 50)
print("AP PAYABLE SUMMARY")
print("=" * 50)

for inv in invoices:
    print(inv.summary())

print("-" * 50)
print(f"Total Payable: ₹{total_payable(invoices)}")
print(f"Status Breakdown: {count_by_status(invoices)}")
print("\nHigh-value invoices (>₹10,000):")
for inv in high_value_invoices(invoices):
    print(f" {inv.vendor} - ₹{inv.amount}")