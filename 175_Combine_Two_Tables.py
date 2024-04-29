select p.firstName, p.lastName, a.city, a.state 
from Person p left join Address a z
on p.personId = a.personId 
