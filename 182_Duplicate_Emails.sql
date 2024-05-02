select email as EMail from Person 
group by email
having count(id) != 1
