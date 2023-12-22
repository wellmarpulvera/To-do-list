CREATE SCHEMA 'todolist_im' ;

-- Create Categories Table
CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Create Tasks Table
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    done BOOLEAN DEFAULT 0,
    category_id INT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

-- VIEWS
CREATE VIEW task_view AS
SELECT t.id, t.title, t.done, c.`name` AS category_name
FROM tasks t
JOIN categories c ON t.category_id = c.id;




