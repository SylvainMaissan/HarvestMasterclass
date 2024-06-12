SELECT
    first_name,
    last_name,
    age
FROM customers
WHERE last_name IN ("Smith", "Baker", "Fisher");
