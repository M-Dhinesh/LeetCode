select round(sum(Distinct i1.tiv_2016),2) as tiv_2016 
from Insurance i1 join Insurance i2 on i1.tiv_2015 = i2.tiv_2015 
where (i1.lat !=i2.lat and i1.lon != i2.lon) and (i1.lat,i1.lon) in (
  select lat,lon from Insurance 
  group by (lat,lon) 
  having count(*) = 1
)
