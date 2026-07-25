CREATE TABLE payments (
    payment_id TEXT,
    vendor_id TEXT,
    amount INTEGER
);

CREATE TABLE vendors (
    vendor_id TEXT,
    vendor_name TEXT,
    category TEXT
);

INSERT INTO payments VALUES
('PAY-001','V01',8500),
('PAY-002','V02',3200),
('PAY-003','V01',15000),
('PAY-004','V03',42000),
('PAY-005','V02',920),
('PAY-006','V09',5000);      -- V09 is not in vendors

INSERT INTO vendors VALUES
('V01','Acme','IT'),
('V02','Globex','Logistics'),
('V03','Initech','IT'),
('V04','Umbrella','Facilities');   -- V04 has no payments

Part 1 — Inner join
Inner join payments and vendors on vendor_id, selecting payment_id, amount, vendor_name, category.

SELECT p.payment_id,p.amount,v.vendor_name,v.category
FROM payments p
INNER JOIN vendors v ON p.vendor_id = v.vendor_id;

Part 2 — Left join
2. Same query but LEFT JOIN — PAY-006 should now survive with NULL vendor_name/category

SELECT p.payment_id,p.amount,v.vendor_name,v.category
FROM payments p
LEFT JOIN vendors v ON p.vendor_id = v.vendor_id;

3.Find the orphan: LEFT JOIN, then WHERE v.vendor_id IS NULL — this isolates the payment with no matching vendor

SELECT p.payment_id,p.amount,v.vendor_name,v.category
FROM payments p
LEFT JOIN vendors v ON p.vendor_id = v.vendor_id
WHERE v.vendor_id IS NULL;

Part 3 — Join + the rest of SQL

4. Inner join, but only show payments over 5000, sorted by amount descending (combine JOIN with WHERE and ORDER BY)

SELECT p.payment_id,p.amount,v.vendor_name,v.category
FROM payments p
INNER JOIN vendors v ON p.vendor_id = v.vendor_id
WHERE p.amount > 5000
ORDER BY p.amount DESC