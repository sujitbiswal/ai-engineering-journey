import numpy as np

# prices = np.array([85.2,84.2,83.8,84.5])
# print(prices)
# print(type(prices))

# ------ CONCEPT 2 — Vectorization: math on the whole array at once ------
# prices = np.array([85.2,84.2,83.8,84.5])
# print(prices + 1)
# print(prices * 2)
# print(prices > 84)

# usd = np.array([1000,5000,12000,500])
# rate = 83.9

# inr = usd * rate
# print(inr)

# -----CONCEPT 3 — Built-in aggregations-----
# prices = np.array([83.5, 84.2, 83.8, 84.5, 83.1, 84.8, 83.6])

# print(prices.sum())
# print(prices.mean())
# print(prices.max())
# print(prices.min())
# print(prices.std())

# ----- CONCEPT 4 — Indexing and filtering (boolean masks) ------
# prices = np.array([83.5, 84.2, 83.8, 84.5, 83.1])

# print(prices[0])
# print(prices[-1])
# print(prices[1:3])

# high = prices[prices > 84]

# print(high)

# ---- EXERCISE - Part 1 — Array basics & vectorization ----
# balances = np.array([45, 52, 38, 61, 49, 55, 42])
# print(f"Balances: {balances}")
# print(f"After 5L inflow: {balances + 5}")
# print(f"Above 50: {balances > 50}")

# -----EXERCISE - Part 2 - Aggregations -----
# balances = np.array([45, 52, 38, 61, 49, 55, 42])
# print(f"Total: {balances.sum()} lakhs")
# print(f"Average: {round(balances.mean(),2)} lakhs")
# print(f"Max: {balances.max()} | Min: {balances.min()}")
# print(f"Std dev: {round(balances.std(),2)}")

# -----EXERCISE - Part 3 - Boolean filtering -----
balances = np.array([45, 52, 38, 61, 49, 55, 42])
low = balances[balances < 45]
print(f"Low-liquidity days (<45): {low}")
print(f"Count of low days: {len(low)}")