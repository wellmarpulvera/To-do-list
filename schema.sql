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

CREATE PROCEDURE add_task(
  IN title_val VARCHAR(255),
  IN category_id_val INT
)
BEGIN
  INSERT INTO tasks (title, category_id)
  VALUES (title_val, category_id_val);
END //


CREATE PROCEDURE edit_task(
    IN task_id INT,
    IN new_title VARCHAR(255)
)
BEGIN
    UPDATE tasks
    SET title = new_title
    WHERE id = task_id;
END //

CREATE PROCEDURE get_task(
    IN task_id INT
)
BEGIN
    SELECT *
    FROM task_view
    WHERE id = task_id;
END //


CREATE PROCEDURE delete_task(
    IN task_id INT
)
BEGIN
    DELETE FROM tasks
    WHERE id = task_id;
END //


CREATE PROCEDURE change_task_status(
    IN task_id INT
)
BEGIN
    DECLARE current_done INT;
    
    SELECT done INTO current_done FROM tasks WHERE id = task_id;

    IF current_done = 0 THEN
        UPDATE tasks SET done = 1 WHERE id = task_id;
    ELSE
        UPDATE tasks SET done = 0 WHERE id = task_id;
    END IF;
END //

-- TRIGGERS
CREATE TRIGGER change_upper
BEFORE INSERT ON tasks
FOR EACH ROW
BEGIN
    SET NEW.title = upper(NEW.title);
END //

DELIMITER ;


