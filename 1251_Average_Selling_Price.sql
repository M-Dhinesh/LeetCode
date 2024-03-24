select p.product_id , IFNULL(round(sum(p.price * u.units)/sum(units),2),0) as average_price from Prices p 
left join UnitsSold u on p.product_id = u.product_id 
where purchase_date between start_date and end_date or u.product_id is null
group by p.product_id 
