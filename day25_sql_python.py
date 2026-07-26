import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. Connect to a database file (creates it if it doesn't exist)
conn = sqlite3.connect("treasury.db")

# 2. Get a cursor — the object that runs queries
cursor = conn.cursor()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            payment_id TEXT,
            entity TEXT,
            amount INTEGER,
            status TEXT
            )
""")
cursor.execute("DELETE FROM payments")    # clear existing rows first

# cursor.execute("INSERT INTO payments VALUES ('PAY-001', 'Hess', 8500, 'Approved')")
# cursor.execute("INSERT INTO payments VALUES ('PAY-002','Globex',3200,'Pending')")
# cursor.execute("INSERT INTO payments VALUES ('PAY-003','Hess',15000,'Approved')")
# cursor.execute("INSERT INTO payments VALUES ('PAY-004','Initech',42000,'Approved')")
# cursor.execute("INSERT INTO payments VALUES ('PAY-005','Globex',920,'Rejected')")
# cursor.execute("INSERT INTO payments VALUES ('PAY-006','Hess',11200,'Pending')")

payments = [
    ('PAY-001', 'Hess',    8500,  'Approved'),
    ('PAY-002', 'Globex',  3200,  'Pending'),
    ('PAY-003', 'Hess',    15000, 'Approved'),
    ('PAY-004', 'Initech', 42000, 'Approved'),
    ('PAY-005', 'Globex',  920,   'Rejected'),
    ('PAY-006', 'Hess',    11200, 'Pending'),
]

cursor.executemany("INSERT INTO payments VALUES (?,?,?,?)",payments)

conn.commit()

# df = pd.read_sql_query("SELECT * FROM payments",conn)

# print(df.shape)
# print(df.head())

# conn.close()

query = """
    SELECT entity, SUM(amount) AS total
    FROM payments
    WHERE status = 'Approved'
    GROUP BY entity
    ORDER BY total DESC
"""
df_summary = pd.read_sql_query(query,conn)
conn.close()

print(df_summary)
df_summary.plot(kind='bar',x = 'entity',y='total', title='Approved Payments by Entity')
plt.savefig("approved_by_entity.png",dpi=150)
