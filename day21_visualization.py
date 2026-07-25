# import matplotlib.pyplot as plt


# CONCEPT 1 — The basic plot, and how matplotlib thinks

# entities = ["Hess", "Globex", "Initech"]
# totals   = [34700, 8220, 49800]

# plt.bar(entities,totals)
# plt.title("Total Payments by Entity")
# plt.xlabel("Entity")
# plt.ylabel("Amount (₹)")
# plt.show()

# plt.bar(x, y)         # bar chart — comparing categories (most common in finance)
# plt.barh(x, y)        # horizontal bars — better when category names are long
# plt.plot(x, y)        # line chart — trends over time
# plt.pie(values, labels=names)   # pie — use sparingly, bars are usually clearer
# plt.hist(values, bins=10)       # histogram — distribution of one variable

# CONCEPT 2 — Plotting straight from Pandas
# import pandas as pd

# df = pd.DataFrame({
#     "entity": ["Hess","Globex","Hess","Initech","Globex","Hess"],
#     "amount": [8500, 3200, 15000, 42000, 920, 11200]
# })

# totals = df.groupby("entity")["amount"].sum()
# totals.plot(kind="bar",title="Total Payments by Entity")
# plt.ylabel("Amount (₹)")
# plt.tight_layout()
# plt.show()

# totals.plot(kind="bar",title="Total Payments by Entity")
# plt.ylabel("Amount (₹)")
# plt.tight_layout()
# plt.savefig("payments_by_entity.png",dpi=150)
# plt.close()

# EXERCISE - Part 1 — Bar chart from a groupby
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "payment_id": ["PAY-001","PAY-002","PAY-003","PAY-004","PAY-005","PAY-006","PAY-007","PAY-008"],
    "entity":     ["Hess","Globex","Hess","Initech","Globex","Hess","Initech","Globex"],
    "amount":     [8500, 3200, 15000, 42000, 920, 11200, 7800, 4100],
    "status":     ["Approved","Pending","Approved","Approved","Rejected","Pending","Approved","Pending"],
    "month":      ["Jan","Jan","Feb","Feb","Mar","Mar","Apr","Apr"]
})

# totals = df.groupby("entity")["amount"].sum()
# totals.plot(kind="bar",title="Total Payments by Entity")
# plt.ylabel("Amount (₹)")
# plt.tight_layout()
# plt.show()

# EXERCISE - Part 2 — A second chart, different question
# totals = df.groupby("status")["amount"].sum()
# totals.plot(kind="barh",title="Total Payments by Status")
# plt.ylabel("Amount (₹)")
# plt.tight_layout()
# plt.show()

# EXERCISE - Part 3 — A second chart, different question
# month_order = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
# df["month"] = pd.Categorical(df["month"],categories= month_order,ordered=True)
# totals = df.groupby("month")["amount"].sum()
# totals.plot(kind="line",marker="o",title = "Total Payments by month")
# plt.ylabel("Amount (₹)")
# plt.tight_layout()
# plt.show()

# EXERCISE - Part 4 — Save one to a file
totals = df.groupby("entity")["amount"].sum()
totals.plot(kind="bar",title="Total Payments by Entity")
plt.ylabel("Amount (₹)")
plt.tight_layout()
plt.savefig("payments_by_entity_1.png",dpi=150)
plt.close()