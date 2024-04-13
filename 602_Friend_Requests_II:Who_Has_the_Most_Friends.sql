select id,num from (
    select requester_id as id, count(accepter_id) as num from (
        select requester_id, accepter_id from RequestAccepted
        union All
        select accepter_id, requester_id from RequestAccepted) as a
    group by requester_id) as b
order by num desc
LIMIT 1
