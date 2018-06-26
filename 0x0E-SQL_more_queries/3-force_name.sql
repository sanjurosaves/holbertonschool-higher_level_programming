-- creates a table called force_name in the current database
-- will not fail if table already exists, has id and name values
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);

