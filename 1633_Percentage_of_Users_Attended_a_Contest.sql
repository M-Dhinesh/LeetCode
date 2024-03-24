select contest_id, round(count(u.user_id) / (select count(*) from Users) * 100,2) as percentage 
from Users u join Register r on u.user_id = r.user_id
group by contest_id
order by percentage desc,contest_id 
