# Write your MySQL query statement below
SELECT 
    id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN EXISTS (
            SELECT * 
            FROM Tree t2
            WHERE t2.p_id = t1.id
        )THEN 'Inner'

        ELSE 'Leaf'

    END AS type

FROM Tree t1;
