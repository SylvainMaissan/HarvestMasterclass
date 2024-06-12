SELECT
    first_name,
    last_name,
    age
FROM customers
WHERE lastname = "Smith" OR last_name = "Baker" OR last_name = "Fisher";
