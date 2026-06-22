# Defining a class: __init__ and self
class Invoice:
    def __init__(self,invoice_id,vendor,amount,status):
        self.invoice_id = invoice_id
        self.vendor = vendor
        self.amount = amount
        self.status = status
    
inv1 = Invoice("INV-001", "Acme", 8500, "Pending")
inv2 = Invoice("INV-002", "Globex", 3200, "Approved")

print(inv1.vendor)
print(inv2.amount)

# Methods: behaviour that belongs to the object
class Invoice:
    def __init__(self,invoice_id,vendor,amount,status):
        self.invoice_id = invoice_id
        self.vendor = vendor
        self.amount = amount
        self.status = status
    
    def is_high_value(self):
        return self.amount > 10000
    
    def summary(self):
        return f"{self.invoice_id} | {self.vendor} | ₹{self.amount} | {self.status}"

inv = Invoice("INV-003", "Initech", 15000, "Approved")

print(inv.summary())
print(inv.is_high_value())

# Part 1 — Build the class

class BankAccount:
    def __init__(self,account_id,entity_name,balance):
        self.account_id = account_id
        self.entity_name = entity_name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        if amount > self.balance:
            print(f" Insufficient funds for {self.account_id}")
        else:
            self.balance -= amount
    def summary(self):
        return f" {self.account_id} | {self.entity_name} | {self.balance}" 
    


acc1 = BankAccount("ACC-001", "Hess Malaysia", 50000)
acc2 = BankAccount("ACC-002", "Globex Treasury", 12000)

acc1.deposit(15000)
acc2.withdraw(20000)

print(acc1.summary())
print(acc2.summary())