SELECT U.id, U.name, T.transaction_date, T.amount
FROM users U, transactions T
WHERE U.id = T.user_id
AND year(T.transaction_date) = 2022
AND month(T.transaction_date) > 6
AND U.status IN ('active', 'inactive')
AND U.email LIKE '%@gmail.com'
GROUP BY U.id, U.name, T.transaction_date, T.amount
HAVING SUM(T.amount) > 1000
ORDER BY T.transaction_date DESC;

-- The tables have to be left joined on the user_id column.
