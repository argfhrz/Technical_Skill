#nomer_1
SELECT Product.ID, Product.Category, Product.Name, Trans.quantity
From Trans, Product
Group BY Product.Category
ORDER BY Trans.quantity;

#nomer_2
SELECT Customers.Cust_ID, Customers.Name, SUM(Trans.Total)
FROM Customers.Trans 
WHERE Customers.Cust_ID = Trans.Customers_Cust_ID
ORDER BY sum(Trans.Total) DESC;

#nomer_3
SELECT HOUR(Trans.Time), COUNT(*)
From Trans 
GROUP BY HOUR(Trans.Time) DIV 2;