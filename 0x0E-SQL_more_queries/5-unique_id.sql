-- creates a table called unique_id
-- will not fail if table already exists, has id and name values
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT '1' UNIQUE, name VARCHAR(256));

