select name as Customers from Customers 
where id not in (select distinct customerid from Orders)
