SELECT *
FROM Orders 
JOIN Products ON Orders.ProductID = Products.ProductID 
ORDER BY CreatedDate;
