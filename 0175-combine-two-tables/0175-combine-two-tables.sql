# Write your MySQL query statement below
SELECT
    p.firstname,
    p.lastname,
    a.city,
    a.state

FROM Person as p
LEFT JOIN Address AS a
   on p.personId = a.personId
