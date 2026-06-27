from bank import BankAccount
acc = BankAccount("ACC-001", "Hess Malaysia", 50000)
acc.deposit(15000)
print(acc.summary())

# Part 3 - using an installed package
import requests

response = requests.get("https://api.github.com")
print(response.status_code)