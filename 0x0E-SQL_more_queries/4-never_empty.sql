-- creates a table called id_not_null
-- will not fail if table already exists, has id and name values
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT '1', name VARCHAR(256));

