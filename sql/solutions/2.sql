SELECT
    users.name,
    COUNT(orders.*) AS order_count
FROM users
INNER JOIN orders ON users.id = orders.user_id
GROUP BY users.id;
