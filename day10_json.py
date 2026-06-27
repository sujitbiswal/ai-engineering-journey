# ----- Day 10 examples (done, kept for reference) ----

# import requests

# response = requests.get("https://api.github.com")
# data = response.json()     # JSON text -> Python dict

# print(type(data))
# print(data["current_user_url"])

# import json

# text = '{"vendor": "Acme","amount": 8500}'  # This is a string

# data = json.loads(text)  # loads = "load string" -> dict
# print(data["vendor"])

# invoice = {"vendor": "Acme", "amount": 8500}

# text = json.dumps(invoice)  # dumps = "dump string" -> JSON text
# print(text)

# data = {
#     "batch_id": "BATCH-2026-06",
#     "status": "Released",
#     "payments": [
#         {"id": "PAY-001", "vendor": "Acme", "amount": 8500},
#         {"id": "PAY-002", "vendor": "Globex", "amount": 3200},
#         {"id": "PAY-003", "vendor": "Initech", "amount": 15000}
#     ]
# }

# total = 0
# for payment in data["payments"]:
#     print(f"{payment['id']} | {payment['vendor']} | ₹{payment['amount']}")
#     total += payment["amount"]

# print(f"Total: ₹{total}")

# ---- Part 1 — parse JSON string ----
# import json

# raw = '{"account_id": "ACC-001", "entity": "Hess Malaysia", "balance": 65000, "active": true}'
# data = json.loads(raw)    # loads = "load string" -> dict
# print(data["active"])

# ---- Part 2 — nested JSON ----
# batch = {
#     "batch_id": "BATCH-2026-06",
#     "currency": "INR",
#     "payments": [
#         {"id": "PAY-001", "vendor": "Acme",    "amount": 8500},
#         {"id": "PAY-002", "vendor": "Globex",  "amount": 3200},
#         {"id": "PAY-003", "vendor": "Initech", "amount": 15000},
#         {"id": "PAY-004", "vendor": "Umbrella", "amount": 920}
#     ]
# }

# total = 0
# single_largest = 0
# largest_payment = None
# for payment in batch["payments"]:
#     print(f"{payment['id']} | {payment['vendor']} | ₹{payment['amount']}")
#     total += payment['amount']
#     if payment['amount'] > single_largest:
#         single_largest = payment['amount']
#         largest_payment = payment['vendor']
        
# print(f"Total: ₹{total}")
# print(f"Largest payment: {largest_payment}")


#---- Part 3 — Real API, real JSON ----
# import requests

# response = requests.get("https://api.github.com", timeout=10)
# data = response.json()

# print(response.status_code)
# print(data["current_user_url"])

# ---- Part 3 — Real API, real JSON ----
import requests

print("Starting API call...")          # proves we reached Part 3
try:
    response = requests.get("https://api.github.com", timeout=10)
    print("Status code:", response.status_code)
    data = response.json()
    print("URL:", data["current_user_url"])
except Exception as e:
    print("REQUEST FAILED:", type(e).__name__, "-", e)
print("Part 3 finished.")              # proves we got to the end




