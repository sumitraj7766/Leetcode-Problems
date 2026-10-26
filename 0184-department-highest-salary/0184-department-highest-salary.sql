# Write your MySQL query statement below
SELECT 
    d.name AS Department ,
    e.name AS Employee ,
    e.salary AS Salary 

FROM Employee e
JOIN Department d 
    ON e.departmentID = d.id 

WHERE (e.departmentID , e.salary) IN (SELECT departmentID ,
MAX(salary)
    FROM Employee
    GROUP BY departmentID
    );
