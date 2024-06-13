SELECT
    a.product AS _name,
    COUNT(*) AS num_orders
FROM product AS a
LEFT
JOIN orders AS b
    ON a.product_id = b.product_id
GROUP BY
    a.product_name;
