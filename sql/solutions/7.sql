-- Improved SQL query with best practices
SELECT
    u.id AS user_id,
    u.name AS username,
    SUM(t.amount) AS total_amount
FROM
    users AS u
LEFT JOIN
    transactions AS t
    ON u.id = t.user_id
WHERE
    t.transaction_date >= '2022-07-01'
    AND u.status IN ('active', 'inactive')
    AND u.email LIKE '%@gmail.com'
GROUP BY
    u.id, u.name
HAVING
    SUM(t.amount) > 1000
ORDER BY
    MAX(t.transaction_date) DESC;
