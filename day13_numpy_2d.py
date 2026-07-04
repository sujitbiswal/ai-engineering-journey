
# ----- CONCEPT 1 — The 2D array: a grid of numbers ----
import numpy as np
balances = np.array([
    [45,52,48],
    [30,28,35],
    [60,65,70],
])
print(balances)
print(balances.shape)

# ----- CONCEPT 2 — Indexing a grid: [row, column] -----
print(balances[0,0])
print(balances[1,2])
print(balances[2,1])

# To grab a whole row or a whole column, use a colon : meaning "all of this dimension":
# Get all of row 0
print(balances[0,:])

# Get all of column 0
print(balances[:,0])

# ---- CONCEPT 3 — Aggregating with axis: down vs across ----
print(balances.sum())
print(balances.sum(axis = 0)) # Goes down - sum down each column
print(balances.sum(axis = 1)) # Goes across - sum across each row

data = np.array([
    [120,135,128,142], # Hess
    [80,75,90,85], # Globex
    [200,210,195,220] # Initech
])
# ----- EXERCISE - Part 1 — Shape & indexing -----

print(f"Shape: {data.shape}")
print(f"Initech Q3: {data[2,2]}")
print(f"Globex all quarters: {data[1,:]}")
print(f"Q1 for all entities: {data[:,0]}")

# ----- EXERCISE - Part 2 — Aggregation by axis -----
print(f" Total per quarter: {data.sum(axis = 0)}")
print(f"Total per entity: {data.sum(axis = 1)}")
print(f"Grand total: {data.sum()}")

# ----- EXERCISE - Part 3 — Combine with what you know -----
print(f"Average per entity: {data.mean(axis = 1)}")
print(f"Highest quarter total: {data.sum(axis = 0).max()}")


