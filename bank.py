class BankAccount:
    def __init__(self,account_id,entity_name,balance):
        self.account_id = account_id
        self.entity_name = entity_name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if amount > self.balance:
            print(f"Insufficient fund for {self.account_id}")
        else:
            self.balance -= amount

    def summary(self):
        return f"{self.account_id} | {self.entity_name} | Balance: ₹{self.balance}"