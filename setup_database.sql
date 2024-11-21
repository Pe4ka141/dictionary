-- Create the database
CREATE DATABASE IF NOT EXISTS dictionary;

-- Use the database
USE dictionary;

-- Create the `words` table
CREATE TABLE IF NOT EXISTS words (
    id INT AUTO_INCREMENT PRIMARY KEY,
    word VARCHAR(100) NOT NULL,
    translation VARCHAR(255) NOT NULL,
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a user
CREATE USER 'pe4ka11'@'localhost' IDENTIFIED BY '1P2P3P4p!';

-- Grant permissions
GRANT ALL PRIVILEGES ON dictionary.* TO 'pe4ka11'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;