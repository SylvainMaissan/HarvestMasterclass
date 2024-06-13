SELECT 
    Orders.OrderID,
    Orders.ProductID,
    Orders.CreatedDate AS OrderCreatedDate,
    Products.Name,
    Products.CreatedDate AS ProductCreatedDate
FROM 
    Orders
JOIN 
    Products ON Orders.ProductID = Products.ProductID
ORDER BY 
    Orders.CreatedDate;