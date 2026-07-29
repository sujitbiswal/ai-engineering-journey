# Phase 1 Cheat-Sheet — Days 1–25

*One line per pattern. This is a lookup, not a lesson. When you forget the syntax (everyone does), glance here instead of feeling like you lost the skill. The concept is yours — this just hands back the shape.*

**How to use it:** Ctrl+F for what you need. Every pattern below, you have already written and run in your own repo — the day file is noted so you can see it in full context.

---

## Python core (Days 1–11)

```python
# --- Variables & f-strings ---
name = "Hess"; amount = 8500
print(f"{name} owes ₹{amount}")            # f-string: embed values with {}
print(f"₹{amount:>8}")                     # right-align in 8 spaces
print(f"{name:<18}")                       # left-align in 18 spaces

# --- Lists (Day 3) ---
prices = [83.5, 84.2, 83.8]
prices.append(85.0)                        # add to end
prices[0]      prices[-1]      prices[1:3]  # first, last, slice
sum(prices)    max(prices)     min(prices)  # built-in aggregates
for p in prices: ...                        # loop

# --- Dictionaries (Day 4) ---
inv = {"vendor": "Acme", "amount": 8500}
inv["vendor"]                              # read a value
inv["status"] = "Approved"                 # add / update
counts[key] = counts.get(key, 0) + 1       # tally pattern (get returns 0 if absent)

# --- List of dicts + filter (Day 4) ---
for row in data:
    if row["amount"] > 10000: ...

# --- Functions (Day 5-6) ---
def total_payable(invoices):
    total = 0
    for inv in invoices:
        total += inv["amount"]
    return total                           # mutating methods change state, return nothing;
                                           # calculating functions return a value

# --- Classes / OOP (Day 8) ---
class BankAccount:
    def __init__(self, account_id, balance):   # runs on creation
        self.account_id = account_id           # self = this specific object
        self.balance = balance
    def deposit(self, amount):                 # method that CHANGES state
        self.balance += amount
    def summary(self):                         # method that RETURNS a value
        return f"{self.account_id} | ₹{self.balance}"

acc = BankAccount("ACC-001", 50000)        # create an instance
acc.deposit(15000)                          # call a method (no self passed)

# --- Modules (Day 9) ---
from bank import BankAccount                # import a class from bank.py (class-only file)

# --- Files + error handling (Day 7, 11) ---
with open("invoices.csv") as f:            # with = auto-closes the file
    for line in f:
        parts = line.strip().split(",")    # strip whitespace, split on comma
        try:
            amount = int(parts[2])
        except ValueError:                  # catch the specific error
            print(f"Skipping bad row: {line.strip()}")
            continue                        # skip to next loop iteration

# --- JSON (Day 10) ---
import json
data = json.loads(text_string)             # JSON text  -> Python dict
text = json.dumps(python_dict)             # Python dict -> JSON text
data["payments"][0]["vendor"]              # navigate nested: into list [0], into dict [key]
```

---

## Environment & Git (Day 9)

```bash
python -m venv venv                        # create the virtual environment (once)
venv\Scripts\activate                      # activate it (every new terminal) -> (venv) appears
pip install pandas                         # installs into THIS venv only
pip freeze > requirements.txt              # record installed packages
deactivate                                 # leave the venv
```
- **No `(venv)` in the prompt = global Python = ModuleNotFoundError.** Glance at the prompt before running.
- **`.gitignore`** should contain: `venv/`, `__pycache__/`, `*.pyc`, `*.db`
- **Commit then Push:** commit = save locally; push = upload to GitHub.

---

## Web requests (Day 9-10)

```python
import requests
r = requests.get("https://api.github.com", timeout=10)   # always set a timeout
r.status_code                              # 200 = success
data = r.json()                            # response JSON -> Python dict
```
Debug trick: bracket a risky call with prints —
```python
print("Starting...")
try: ...
except Exception as e: print("FAILED:", type(e).__name__, "-", e)
print("Finished.")
```

---

## NumPy (Days 12-13)

```python
import numpy as np
a = np.array([45, 52, 38, 61])            # 1D array
a + 5      a * 2      a > 50               # vectorized: applies to every element
a.sum()  a.mean()  a.max()  a.min()  a.std()   # aggregations
a[a > 50]                                  # boolean mask: elements where condition true

# 2D array (Day 13)
grid = np.array([[1,2,3],[4,5,6]])
grid.shape                                 # (rows, cols)
grid[1, 2]                                 # row 1, col 2 (0-indexed)
grid[0, :]     grid[:, 0]                  # whole row 0 / whole col 0
grid.sum(axis=0)                           # DOWN columns  -> per-column totals
grid.sum(axis=1)                           # ACROSS rows   -> per-row totals
```
**Memory hook:** axis=0 ↓ down (per column), axis=1 → across (per row). Axis picks direction, method picks calculation.

---

## Pandas — the daily driver (Days 15-20)

```python
import pandas as pd

# --- Create / load (Day 15-16) ---
df = pd.DataFrame({"vendor": [...], "amount": [...]})   # from a dict
df = pd.read_csv("file.csv")                            # load a CSV
df = pd.read_csv("f.csv", header=None, names=["a","b"]) # headerless file
df = pd.read_excel("f.xlsx", sheet_name="Q1")           # load Excel (needs openpyxl)

# --- Inspect FIRST, every time (Day 15) ---
df.head()      df.shape      df.columns
df.info()      # types + non-null counts (spots missing data & wrong types)
df.describe()  # stats for numeric columns

# --- Select (Day 15, 17) ---
df["amount"]                               # one column (Series)
df[["vendor", "amount"]]                   # multiple columns (DataFrame)
df[df["amount"] > 10000]                   # filter rows (boolean mask)
df[(df["amount"] > 5000) & (df["status"] == "Approved")]   # combined: () around each, & / |
df.loc[0, "vendor"]                        # by LABEL (name)
df.iloc[0, 1]                              # by POSITION (integer)
df = df.set_index("payment_id")            # make a column the index -> df.loc["PAY-004"]

# --- Sort (Day 17) ---
df.sort_values("amount", ascending=False)              # biggest first
df.sort_values("amount", ascending=False).head(3)      # top 3
df.sort_values(["entity", "amount"], ascending=[True, False])   # mixed directions

# --- Group / summarize (Day 18) ---
df.groupby("entity")["amount"].sum()       # total per entity
df.groupby("entity")["amount"].mean()      # average per entity
df.groupby("entity")["payment_id"].count() # count per entity
df.groupby(["entity","status"])["amount"].sum()        # two-level
df.groupby("entity")["amount"].agg(["sum","mean","count","max"])   # many stats at once
df.groupby("entity")["amount"].sum().idxmax()          # NAME of the top group (sum FIRST)

# --- Clean (Day 19) ---
df.isnull().sum()                          # count missing per column (THE diagnostic)
df.duplicated().sum()                      # count duplicate rows
df = df.drop_duplicates().copy()           # remove dupes; .copy() avoids the warning
df["col"] = df["col"].fillna("Unknown")    # fill missing (reassign to keep it)
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")   # text->number, bad->NaN
df["status"] = df["status"].str.strip().str.title()          # fix stray spaces + case
#   Finance judgment: a missing AMOUNT is unknown, not 0. Flag it, don't fill with 0.

# --- Merge / join (Day 20) ---
pd.merge(payments, vendors, on="vendor_id", how="inner")   # only matched rows
pd.merge(payments, vendors, on="vendor_id", how="left")    # ALL left rows, NaN if no match
#   Use LEFT when you must not lose rows from the primary table (a dropped payment breaks recon).
merged.isnull().sum()                      # after a left join: finds the orphans
```

---

## Visualization (Day 21)

```python
import matplotlib.pyplot as plt

totals = df.groupby("entity")["amount"].sum()
totals.plot(kind="bar", title="Total by Entity")   # kind: bar / barh / line / pie / hist
plt.ylabel("Amount (₹)")
plt.tight_layout()                         # stops labels being cut off
plt.savefig("chart.png", dpi=150)          # SAVE *before* show(), or the image is blank
plt.show()
```
**Month/category order trap:** groupby sorts alphabetically. For calendar order:
```python
df["month"] = pd.Categorical(df["month"], categories=["Jan","Feb","Mar",...], ordered=True)
```

---

## SQL (Days 22-24)

```sql
-- Core query. Fixed clause order: SELECT -> FROM -> WHERE -> GROUP BY -> HAVING -> ORDER BY -> LIMIT
SELECT vendor, amount FROM payments
WHERE amount > 5000 AND status = 'Approved'    -- text in 'single quotes', = not ==
ORDER BY amount DESC                            -- DESC = biggest first
LIMIT 3;                                        -- top N

SELECT DISTINCT status FROM payments;           -- unique values

-- Joins (Day 23) -- same logic as pandas merge
SELECT p.payment_id, v.vendor_name             -- table aliases: payments p, vendors v
FROM payments p
LEFT JOIN vendors v ON p.vendor_id = v.vendor_id;   -- INNER (matched) / LEFT (keep all left)
-- find orphans:
WHERE v.vendor_id IS NULL;                      -- IS NULL, not = NULL

-- Group + aggregate (Day 24)
SELECT entity, SUM(amount) AS total            -- always alias aggregates with AS
FROM payments
WHERE status = 'Approved'                       -- WHERE filters ROWS (before grouping)
GROUP BY entity
HAVING SUM(amount) > 20000;                     -- HAVING filters GROUPS (after grouping)
-- Rule: every SELECT column must be in GROUP BY or inside an aggregate.
```
**WHERE vs HAVING:** WHERE filters rows before grouping; HAVING filters groups on their aggregate after. A row fact (status) → WHERE. A group fact (SUM) → HAVING.

---

## SQL + Python (Day 25)

```python
import sqlite3, pandas as pd

conn = sqlite3.connect("treasury.db")          # opens/creates the .db file
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS payments (...)")
cursor.execute("DELETE FROM payments")         # makes the script re-runnable (avoids doubled rows)
cursor.executemany("INSERT INTO payments VALUES (?,?,?,?)", rows)   # ? = safe placeholders
conn.commit()                                  # SAVE changes (inserts lost without this)

df = pd.read_sql_query("SELECT ... FROM payments", conn)   # SQL result -> DataFrame
conn.close()
```
**Pattern:** SQL filters/aggregates at the database (fast on huge data) → Pandas analyzes the small result → matplotlib shows it. That's a data pipeline.
**Safety:** never put variable data directly in a SQL string — always `?` placeholders (prevents SQL injection).

---

## The instincts (worth more than the syntax)

- **Inspect before you trust.** `.head()`, `.shape`, `.info()` on any new data, always.
- **"Runs" ≠ "correct."** Code can execute cleanly and answer the wrong question (idxmax without sum; SELECT entity grouped by status; a chart with months out of order). Check the answer against what you can see.
- **Verify types after converting.** `df["col"].dtype` after a to_numeric — float64 means it worked.
- **Know what happens to rows that don't fit.** Rejected invoices, missing amounts, orphaned keys — in finance those are the rows that break reconciliations. Don't let them vanish silently.
- **Recall vs recognition.** You won't write this from memory — nobody does. You recognize the pattern and look up the shape. That's the actual skill. This sheet exists so "I forgot the syntax" is never a blocker.
```
```
