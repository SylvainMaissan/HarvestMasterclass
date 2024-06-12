SELECT
    name,
    (SELECT COUNT(*) FROM orders WHERE user_id = user_id) AS order_count
FROM users;
