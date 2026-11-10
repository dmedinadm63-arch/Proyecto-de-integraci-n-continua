CREATE TABLE IF NOT EXISTS estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

INSERT INTO estudiantes (nombre) VALUES
('Daniel'),
('Estudiante de prueba');
