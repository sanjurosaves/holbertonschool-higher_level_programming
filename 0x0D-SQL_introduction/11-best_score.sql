-- lists all records of the table second_table with a score >=10 by score, top first
-- use SELECT ... FROM ... ORDER BY
SELECT score, name FROM second_table WHERE score >= '10' ORDER BY score DESC;
