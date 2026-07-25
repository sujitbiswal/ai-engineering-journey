1.Select all columns, all rows

SELECT *
from payments

2.Select only entity and amount for every row

SELECT entity,amount
from payments

3.Select the distinct entities (should return Hess, Globex, Initech)

SELECT DISTINCT entity
from payments

4.All payments where amount is over 10000

SELECT *
FROM payments
WHERE amount > 10000

5.All Approved payments (mind the single quotes)

SELECT *
FROM payments
where status = 'Approved'

6. All payments that are Approved AND over 10000

SELECT *
FROM payments
WHERE status = 'Approved' AND amount > 10000

7.All payments sorted by amount, largest first

SELECT *
FROM payments
ORDER BY amount DESC

8.The top 3 payments by amount (sort + limit)

SELECT *
FROM payments
ORDER BY amount DESC
LIMIT 3

9.All Pending payments, sorted by amount ascending

SELECT *
from payments
WHERE status = 'Pending'
ORDER BY amount ASC