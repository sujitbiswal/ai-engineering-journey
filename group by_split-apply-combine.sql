CREATE TABLE payments (
    payment_id TEXT,
    entity TEXT,
    amount INTEGER,
    status TEXT
);

INSERT INTO payments VALUES
('PAY-001','Hess',8500,'Approved'),
('PAY-002','Globex',3200,'Pending'),
('PAY-003','Hess',15000,'Approved'),
('PAY-004','Initech',42000,'Approved'),
('PAY-005','Globex',920,'Rejected'),
('PAY-006','Hess',11200,'Pending'),
('PAY-007','Initech',7800,'Approved'),
('PAY-008','Globex',4100,'Pending');

Part 1 — Basic GROUP BY

SELECT entity, SUM(amount)  AS total
from payments
GROUP By entity

SELECT status, COUNT(*) AS num_payments
from payments
GROUP BY status

SELECT entity, AVG(amount)  AS Average
from payments
GROUP BY entity

Part 2 — Multiple aggregates

SELECT entity,

	SUM(amount)  AS total,
        AVG(amount)  AS average,
        COUNT(*)     AS num_payments,
        MAX(amount)  AS biggest
FROM payments
GROUP By entity;

Part 3 — WHERE vs HAVING (the important part)

SELECT entity, SUM(amount)  As total
from payments
WHERE status = 'Approved'
GROUP BY entity
HAVING SUM(amount) > 20000