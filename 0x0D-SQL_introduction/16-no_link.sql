-- lists all records of the table second_table by score, top first, omits NULL names
-- use SELECT ... FROM ... ORDER BY
SELECT score, name FROM second_table where name is not NULL ORDER BY score DESC;
