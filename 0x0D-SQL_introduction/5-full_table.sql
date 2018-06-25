-- prints the full description of the table first_table from the database hbtn_0c_0
-- cannot use DESCRIBE or explain command
SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH FROM information_schema.columns where table_name = 'first_table';

