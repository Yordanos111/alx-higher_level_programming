-- script that creates the table force_name on your MySQL server.
-- id INT, name VARCHAR(256) can't be null
-- If table already exists, script should not fail
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
