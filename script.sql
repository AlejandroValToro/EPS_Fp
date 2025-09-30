-- Creación de tablas para sistema EPS

CREATE TABLE IF NOT EXISTS Pacientes (
    id_paciente INT PRIMARY KEY AUTO_INCREMENT,
    documento VARCHAR(20) NOT NULL,
    tipo_documento ENUM('CC', 'CE', 'TI', 'RC') NOT NULL,
    nombres VARCHAR(50) NOT NULL,
    apellidos VARCHAR(50) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    genero ENUM('M', 'F', 'O') NOT NULL,
    direccion VARCHAR(100),
    telefono VARCHAR(15),
    email VARCHAR(50),
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Especialidades (
    id_especialidad INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT
);

CREATE TABLE IF NOT EXISTS Medicos (
    id_medico INT PRIMARY KEY AUTO_INCREMENT,
    documento VARCHAR(20) NOT NULL,
    nombres VARCHAR(50) NOT NULL,
    apellidos VARCHAR(50) NOT NULL,
    id_especialidad INT,
    telefono VARCHAR(15),
    email VARCHAR(50),
    tarjeta_profesional VARCHAR(20) NOT NULL,
    FOREIGN KEY (id_especialidad) REFERENCES Especialidades(id_especialidad)
);

CREATE TABLE IF NOT EXISTS Citas (
    id_cita INT PRIMARY KEY AUTO_INCREMENT,
    id_paciente INT,
    id_medico INT,
    fecha_hora DATETIME NOT NULL,
    estado ENUM('Programada', 'Completada', 'Cancelada') NOT NULL,
    motivo TEXT,
    FOREIGN KEY (id_paciente) REFERENCES Pacientes(id_paciente),
    FOREIGN KEY (id_medico) REFERENCES Medicos(id_medico)
);

CREATE TABLE IF NOT EXISTS HistoriasClinicas (
    id_historia INT PRIMARY KEY AUTO_INCREMENT,
    id_paciente INT,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    antecedentes TEXT,
    FOREIGN KEY (id_paciente) REFERENCES Pacientes(id_paciente)
);

CREATE TABLE IF NOT EXISTS Consultas (
    id_consulta INT PRIMARY KEY AUTO_INCREMENT,
    id_cita INT,
    id_historia INT,
    diagnostico TEXT,
    tratamiento TEXT,
    observaciones TEXT,
    fecha_consulta DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_cita) REFERENCES Citas(id_cita),
    FOREIGN KEY (id_historia) REFERENCES HistoriasClinicas(id_historia)
);

CREATE TABLE IF NOT EXISTS Medicamentos (
    id_medicamento INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fabricante VARCHAR(50),
    stock INT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS Recetas (
    id_receta INT PRIMARY KEY AUTO_INCREMENT,
    id_consulta INT,
    id_medicamento INT,
    dosis VARCHAR(50),
    frecuencia VARCHAR(50),
    duracion VARCHAR(50),
    fecha_receta DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_consulta) REFERENCES Consultas(id_consulta),
    FOREIGN KEY (id_medicamento) REFERENCES Medicamentos(id_medicamento)
);

CREATE TABLE IF NOT EXISTS Departamentos (
    id_departamento INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT
);

CREATE TABLE IF NOT EXISTS Empleados (
    id_empleado INT PRIMARY KEY AUTO_INCREMENT,
    documento VARCHAR(20) NOT NULL,
    nombres VARCHAR(50) NOT NULL,
    apellidos VARCHAR(50) NOT NULL,
    id_departamento INT,
    cargo VARCHAR(50),
    fecha_contratacion DATE,
    FOREIGN KEY (id_departamento) REFERENCES Departamentos(id_departamento)
);

CREATE TABLE IF NOT EXISTS Laboratorios (
    id_laboratorio INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(100),
    telefono VARCHAR(15)
);

CREATE TABLE IF NOT EXISTS ExamenesLaboratorio (
    id_examen INT PRIMARY KEY AUTO_INCREMENT,
    id_consulta INT,
    id_laboratorio INT,
    tipo_examen VARCHAR(100),
    fecha_solicitud DATETIME DEFAULT CURRENT_TIMESTAMP,
    fecha_resultado DATETIME,
    resultado TEXT,
    FOREIGN KEY (id_consulta) REFERENCES Consultas(id_consulta),
    FOREIGN KEY (id_laboratorio) REFERENCES Laboratorios(id_laboratorio)
);

CREATE TABLE IF NOT EXISTS Facturas (
    id_factura INT PRIMARY KEY AUTO_INCREMENT,
    id_paciente INT,
    fecha_emision DATETIME DEFAULT CURRENT_TIMESTAMP,
    monto_total DECIMAL(10,2),
    estado ENUM('Pendiente', 'Pagada', 'Anulada') DEFAULT 'Pendiente',
    FOREIGN KEY (id_paciente) REFERENCES Pacientes(id_paciente)
);

CREATE TABLE IF NOT EXISTS DetallesFactura (
    id_detalle INT PRIMARY KEY AUTO_INCREMENT,
    id_factura INT,
    concepto VARCHAR(100),
    cantidad INT,
    precio_unitario DECIMAL(10,2),
    subtotal DECIMAL(10,2),
    FOREIGN KEY (id_factura) REFERENCES Facturas(id_factura)
);

CREATE TABLE IF NOT EXISTS Horarios (
    id_horario INT PRIMARY KEY AUTO_INCREMENT,
    id_medico INT,
    dia_semana ENUM('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'),
    hora_inicio TIME,
    hora_fin TIME,
    FOREIGN KEY (id_medico) REFERENCES Medicos(id_medico)
);

-- -----------------------------------------------------
-- Stored Procedures
-- -----------------------------------------------------

-- Pacientes
DELIMITER $$
DROP PROCEDURE IF EXISTS proc_select_all_Pacientes$$
CREATE PROCEDURE proc_select_all_Pacientes()
BEGIN
    SELECT * FROM Pacientes;
END$$

DROP PROCEDURE IF EXISTS proc_select_by_id_Pacientes$$
CREATE PROCEDURE proc_select_by_id_Pacientes(IN _id_paciente INT)
BEGIN
    SELECT * FROM Pacientes WHERE id_paciente = _id_paciente;
END$$

DROP PROCEDURE IF EXISTS proc_insert_Pacientes$$
CREATE PROCEDURE proc_insert_Pacientes(
    IN _documento VARCHAR(20),
    IN _tipo_documento ENUM('CC', 'CE', 'TI', 'RC'),
    IN _nombres VARCHAR(50),
    IN _apellidos VARCHAR(50),
    IN _fecha_nacimiento DATE,
    IN _genero ENUM('M', 'F', 'O'),
    IN _direccion VARCHAR(100),
    IN _telefono VARCHAR(15),
    IN _email VARCHAR(50),
    INOUT _Respuesta INT
)
BEGIN
    INSERT INTO Pacientes (documento, tipo_documento, nombres, apellidos, fecha_nacimiento, genero, direccion, telefono, email)
    VALUES (_documento, _tipo_documento, _nombres, _apellidos, _fecha_nacimiento, _genero, _direccion, _telefono, _email);
    SET _Respuesta = 1;
END$$

DROP PROCEDURE IF EXISTS proc_update_Pacientes$$
CREATE PROCEDURE proc_update_Pacientes(
    IN _id_paciente INT,
    IN _documento VARCHAR(20),
    IN _tipo_documento ENUM('CC', 'CE', 'TI', 'RC'),
    IN _nombres VARCHAR(50),
    IN _apellidos VARCHAR(50),
    IN _fecha_nacimiento DATE,
    IN _genero ENUM('M', 'F', 'O'),
    IN _direccion VARCHAR(100),
    IN _telefono VARCHAR(15),
    IN _email VARCHAR(50)
)
BEGIN
    UPDATE Pacientes
    SET documento = _documento,
        tipo_documento = _tipo_documento,
        nombres = _nombres,
        apellidos = _apellidos,
        fecha_nacimiento = _fecha_nacimiento,
        genero = _genero,
        direccion = _direccion,
        telefono = _telefono,
        email = _email
    WHERE id_paciente = _id_paciente;
END$$

DROP PROCEDURE IF EXISTS proc_delete_Pacientes$$
CREATE PROCEDURE proc_delete_Pacientes(IN _id_paciente INT)
BEGIN
    DELETE FROM Pacientes WHERE id_paciente = _id_paciente;
END$$

-- Especialidades
DROP PROCEDURE IF EXISTS proc_select_all_Especialidades$$
CREATE PROCEDURE proc_select_all_Especialidades()
BEGIN
    SELECT * FROM Especialidades;
END$$

DROP PROCEDURE IF EXISTS proc_select_by_id_Especialidades$$
CREATE PROCEDURE proc_select_by_id_Especialidades(IN _id_especialidad INT)
BEGIN
    SELECT * FROM Especialidades WHERE id_especialidad = _id_especialidad;
END$$

DROP PROCEDURE IF EXISTS proc_insert_Especialidades$$
CREATE PROCEDURE proc_insert_Especialidades(
    IN _nombre VARCHAR(50),
    IN _descripcion TEXT,
    INOUT _Respuesta INT
)
BEGIN
    INSERT INTO Especialidades (nombre, descripcion)
    VALUES (_nombre, _descripcion);
    SET _Respuesta = 1;
END$$

DROP PROCEDURE IF EXISTS proc_update_Especialidades$$
CREATE PROCEDURE proc_update_Especialidades(
    IN _id_especialidad INT,
    IN _nombre VARCHAR(50),
    IN _descripcion TEXT
)
BEGIN
    UPDATE Especialidades
    SET nombre = _nombre,
        descripcion = _descripcion
    WHERE id_especialidad = _id_especialidad;
END$$

DROP PROCEDURE IF EXISTS proc_delete_Especialidades$$
CREATE PROCEDURE proc_delete_Especialidades(IN _id_especialidad INT)
BEGIN
    DELETE FROM Especialidades WHERE id_especialidad = _id_especialidad;
END$$

-- Medicos
DROP PROCEDURE IF EXISTS proc_select_all_Medicos$$
CREATE PROCEDURE proc_select_all_Medicos()
BEGIN
    SELECT * FROM Medicos;
END$$

DROP PROCEDURE IF EXISTS proc_select_by_id_Medicos$$
CREATE PROCEDURE proc_select_by_id_Medicos(IN _id_medico INT)
BEGIN
    SELECT * FROM Medicos WHERE id_medico = _id_medico;
END$$

DROP PROCEDURE IF EXISTS proc_insert_Medicos$$
CREATE PROCEDURE proc_insert_Medicos(
    IN _documento VARCHAR(20),
    IN _nombres VARCHAR(50),
    IN _apellidos VARCHAR(50),
    IN _id_especialidad INT,
    IN _telefono VARCHAR(15),
    IN _email VARCHAR(50),
    IN _tarjeta_profesional VARCHAR(20),
    INOUT _Respuesta INT
)
BEGIN
    INSERT INTO Medicos (documento, nombres, apellidos, id_especialidad, telefono, email, tarjeta_profesional)
    VALUES (_documento, _nombres, _apellidos, _id_especialidad, _telefono, _email, _tarjeta_profesional);
    SET _Respuesta = 1;
END$$

DROP PROCEDURE IF EXISTS proc_update_Medicos$$
CREATE PROCEDURE proc_update_Medicos(
    IN _id_medico INT,
    IN _documento VARCHAR(20),
    IN _nombres VARCHAR(50),
    IN _apellidos VARCHAR(50),
    IN _id_especialidad INT,
    IN _telefono VARCHAR(15),
    IN _email VARCHAR(50),
    IN _tarjeta_profesional VARCHAR(20)
)
BEGIN
    UPDATE Medicos
    SET documento = _documento,
        nombres = _nombres,
        apellidos = _apellidos,
        id_especialidad = _id_especialidad,
        telefono = _telefono,
        email = _email,
        tarjeta_profesional = _tarjeta_profesional
    WHERE id_medico = _id_medico;
END$$

DROP PROCEDURE IF EXISTS proc_delete_Medicos$$
CREATE PROCEDURE proc_delete_Medicos(IN _id_medico INT)
BEGIN
    DELETE FROM Medicos WHERE id_medico = _id_medico;
END$$

-- Citas
DROP PROCEDURE IF EXISTS proc_select_all_Citas$$
CREATE PROCEDURE proc_select_all_Citas()
BEGIN
    SELECT * FROM Citas;
END$$

DROP PROCEDURE IF EXISTS proc_select_by_id_Citas$$
CREATE PROCEDURE proc_select_by_id_Citas(IN _id_cita INT)
BEGIN
    SELECT * FROM Citas WHERE id_cita = _id_cita;
END$$

DROP PROCEDURE IF EXISTS proc_insert_Citas$$
CREATE PROCEDURE proc_insert_Citas(
    IN _id_paciente INT,
    IN _id_medico INT,
    IN _fecha_hora DATETIME,
    IN _estado ENUM('Programada', 'Completada', 'Cancelada'),
    IN _motivo TEXT,
    INOUT _Respuesta INT
)
BEGIN
    INSERT INTO Citas (id_paciente, id_medico, fecha_hora, estado, motivo)
    VALUES (_id_paciente, _id_medico, _fecha_hora, _estado, _motivo);
    SET _Respuesta = 1;
END$$

DROP PROCEDURE IF EXISTS proc_update_Citas$$
CREATE PROCEDURE proc_update_Citas(
    IN _id_cita INT,
    IN _id_paciente INT,
    IN _id_medico INT,
    IN _fecha_hora DATETIME,
    IN _estado ENUM('Programada', 'Completada', 'Cancelada'),
    IN _motivo TEXT
)
BEGIN
    UPDATE Citas
    SET id_paciente = _id_paciente,
        id_medico = _id_medico,
        fecha_hora = _fecha_hora,
        estado = _estado,
        motivo = _motivo
    WHERE id_cita = _id_cita;
END$$

DROP PROCEDURE IF EXISTS proc_delete_Citas$$
CREATE PROCEDURE proc_delete_Citas(IN _id_cita INT)
BEGIN
    DELETE FROM Citas WHERE id_cita = _id_cita;
END$$

-- HistoriasClinicas
DROP PROCEDURE IF EXISTS proc_select_all_HistoriasClinicas$$
CREATE PROCEDURE proc_select_all_HistoriasClinicas()
BEGIN
    SELECT * FROM HistoriasClinicas;
END$$

DROP PROCEDURE IF EXISTS proc_select_by_id_HistoriasClinicas$$
CREATE PROCEDURE proc_select_by_id_HistoriasClinicas(IN _id_historia INT)
BEGIN
    SELECT * FROM HistoriasClinicas WHERE id_historia = _id_historia;
END$$

DROP PROCEDURE IF EXISTS proc_insert_HistoriasClinicas$$
CREATE PROCEDURE proc_insert_HistoriasClinicas(
    IN _id_paciente INT,
    IN _antecedentes TEXT,
    INOUT _Respuesta INT
)
BEGIN
    INSERT INTO HistoriasClinicas (id_paciente, antecedentes)
    VALUES (_id_paciente, _antecedentes);
    SET _Respuesta = 1;
END$$

DROP PROCEDURE IF EXISTS proc_update_HistoriasClinicas$$
CREATE PROCEDURE proc_update_HistoriasClinicas(
    IN _id_historia INT,
    IN _id_paciente INT,
    IN _antecedentes TEXT
)
BEGIN
    UPDATE HistoriasClinicas
    SET id_paciente = _id_paciente,
        antecedentes = _antecedentes
    WHERE id_historia = _id_historia;
END$$

DROP PROCEDURE IF EXISTS proc_delete_HistoriasClinicas$$
CREATE PROCEDURE proc_delete_HistoriasClinicas(IN _id_historia INT)
BEGIN
    DELETE FROM HistoriasClinicas WHERE id_historia = _id_historia;
END$$

-- Consultas
DROP PROCEDURE IF EXISTS proc_select_all_Consultas$$
CREATE PROCEDURE proc_select_all_Consultas()
BEGIN
    SELECT * FROM Consultas;
END$$

DROP PROCEDURE IF EXISTS proc_select_by_id_Consultas$$
CREATE PROCEDURE proc_select_by_id_Consultas(IN _id_consulta INT)
BEGIN
    SELECT * FROM Consultas WHERE id_consulta = _id_consulta;
END$$

DROP PROCEDURE IF EXISTS proc_insert_Consultas$$
CREATE PROCEDURE proc_insert_Consultas(
    IN _id_cita INT,
    IN _id_historia INT,
    IN _diagnostico TEXT,
    IN _tratamiento TEXT,
    IN _observaciones TEXT,
    INOUT _Respuesta INT
)
BEGIN
    INSERT INTO Consultas (id_cita, id_historia, diagnostico, tratamiento, observaciones)
    VALUES (_id_cita, _id_historia, _diagnostico, _tratamiento, _observaciones);
    SET _Respuesta = 1;
END$$

DROP PROCEDURE IF EXISTS proc_update_Consultas$$
CREATE PROCEDURE proc_update_Consultas(
    IN _id_consulta INT,
    IN _id_cita INT,
    IN _id_historia INT,
    IN _diagnostico TEXT,
    IN _tratamiento TEXT,
    IN _observaciones TEXT
)
BEGIN
    UPDATE Consultas
    SET id_cita = _id_cita,
        id_historia = _id_historia,
        diagnostico = _diagnostico,
        tratamiento = _tratamiento,
        observaciones = _observaciones
    WHERE id_consulta = _id_consulta;
END$$

DROP PROCEDURE IF EXISTS proc_delete_Consultas$$
CREATE PROCEDURE proc_delete_Consultas(IN _id_consulta INT)
BEGIN
    DELETE FROM Consultas WHERE id_consulta = _id_consulta;
END$$

-- Medicamentos
DROP PROCEDURE IF EXISTS proc_select_all_Medicamentos$$
CREATE PROCEDURE proc_select_all_Medicamentos()
BEGIN
    SELECT * FROM Medicamentos;
END$$

DROP PROCEDURE IF EXISTS proc_select_by_id_Medicamentos$$
CREATE PROCEDURE proc_select_by_id_Medicamentos(IN _id_medicamento INT)
BEGIN
    SELECT * FROM Medicamentos WHERE id_medicamento = _id_medicamento;
END$$

DROP PROCEDURE IF EXISTS proc_insert_Medicamentos$$
CREATE PROCEDURE proc_insert_Medicamentos(
    IN _nombre VARCHAR(100),
    IN _descripcion TEXT,
    IN _fabricante VARCHAR(50),
    IN _stock INT,
    INOUT _Respuesta INT
)
BEGIN
    INSERT INTO Medicamentos (nombre, descripcion, fabricante, stock)
    VALUES (_nombre, _descripcion, _fabricante, _stock);
    SET _Respuesta = 1;
END$$

DROP PROCEDURE IF EXISTS proc_update_Medicamentos$$
CREATE PROCEDURE proc_update_Medicamentos(
    IN _id_medicamento INT,
    IN _nombre VARCHAR(100),
    IN _descripcion TEXT,
    IN _fabricante VARCHAR(50),
    IN _stock INT
)
BEGIN
    UPDATE Medicamentos
    SET nombre = _nombre,
        descripcion = _descripcion,
        fabricante = _fabricante,
        stock = _stock
    WHERE id_medicamento = _id_medicamento;
END$$

DROP PROCEDURE IF EXISTS proc_delete_Medicamentos$$
CREATE PROCEDURE proc_delete_Medicamentos(IN _id_medicamento INT)
BEGIN
    DELETE FROM Medicamentos WHERE id_medicamento = _id_medicamento;
END$$

-- Recetas
DROP PROCEDURE IF EXISTS proc_select_all_Recetas$$
CREATE PROCEDURE proc_select_all_Recetas()
BEGIN
    SELECT * FROM Recetas;
END$$

DROP PROCEDURE IF EXISTS proc_select_by_id_Recetas$$
CREATE PROCEDURE proc_select_by_id_Recetas(IN _id_receta INT)
BEGIN
    SELECT * FROM Recetas WHERE id_receta = _id_receta;
END$$

DROP PROCEDURE IF EXISTS proc_insert_Recetas$$
CREATE PROCEDURE proc_insert_Recetas(
    IN _id_consulta INT,
    IN _id_medicamento INT,
    IN _dosis VARCHAR(50),
    IN _frecuencia VARCHAR(50),
    IN _duracion VARCHAR(50),
    INOUT _Respuesta INT
)
BEGIN
    INSERT INTO Recetas (id_consulta, id_medicamento, dosis, frecuencia, duracion)
    VALUES (_id_consulta, _id_medicamento, _dosis, _frecuencia, _duracion);
    SET _Respuesta = 1;
END$$

DROP PROCEDURE IF EXISTS proc_update_Recetas$$
CREATE PROCEDURE proc_update_Recetas(
    IN _id_receta INT,
    IN _id_consulta INT,
    IN _id_medicamento INT,
    IN _dosis VARCHAR(50),
    IN _frecuencia VARCHAR(50),
    IN _duracion VARCHAR(50)
)
BEGIN
    UPDATE Recetas
    SET id_consulta = _id_consulta,
        id_medicamento = _id_medicamento,
        dosis = _dosis,
        frecuencia = _frecuencia,
        duracion = _duracion
    WHERE id_receta = _id_receta;
END$$

DROP PROCEDURE IF EXISTS proc_delete_Recetas$$
CREATE PROCEDURE proc_delete_Recetas(IN _id_receta INT)
BEGIN
    DELETE FROM Recetas WHERE id_receta = _id_receta;
END$$

-- Departamentos
DROP PROCEDURE IF EXISTS proc_select_all_Departamentos$$
CREATE PROCEDURE proc_select_all_Departamentos()
BEGIN
    SELECT * FROM Departamentos;
END$$

DROP PROCEDURE IF EXISTS proc_select_by_id_Departamentos$$
CREATE PROCEDURE proc_select_by_id_Departamentos(IN _id_departamento INT)
BEGIN
    SELECT * FROM Departamentos WHERE id_departamento = _id_departamento;
END$$

DROP PROCEDURE IF EXISTS proc_insert_Departamentos$$
CREATE PROCEDURE proc_insert_Departamentos(
    IN _nombre VARCHAR(50),
    IN _descripcion TEXT,
    INOUT _Respuesta INT
)
BEGIN
    INSERT INTO Departamentos (nombre, descripcion)
    VALUES (_nombre, _descripcion);
    SET _Respuesta = 1;
END$$

DROP PROCEDURE IF EXISTS proc_update_Departamentos$$
CREATE PROCEDURE proc_update_Departamentos(
    IN _id_departamento INT,
    IN _nombre VARCHAR(50),
    IN _descripcion TEXT
)
BEGIN
    UPDATE Departamentos
    SET nombre = _nombre,
        descripcion = _descripcion
    WHERE id_departamento = _id_departamento;
END$$

DROP PROCEDURE IF EXISTS proc_delete_Departamentos$$
CREATE PROCEDURE proc_delete_Departamentos(IN _id_departamento INT)
BEGIN
    DELETE FROM Departamentos WHERE id_departamento = _id_departamento;
END$$

-- Empleados
DROP PROCEDURE IF EXISTS proc_select_all_Empleados$$
CREATE PROCEDURE proc_select_all_Empleados()
BEGIN
    SELECT * FROM Empleados;
END$$

DROP PROCEDURE IF EXISTS proc_select_by_id_Empleados$$
CREATE PROCEDURE proc_select_by_id_Empleados(IN _id_empleado INT)
BEGIN
    SELECT * FROM Empleados WHERE id_empleado = _id_empleado;
END$$

DROP PROCEDURE IF EXISTS proc_insert_Empleados$$
CREATE PROCEDURE proc_insert_Empleados(
    IN _documento VARCHAR(20),
    IN _nombres VARCHAR(50),
    IN _apellidos VARCHAR(50),
    IN _id_departamento INT,
    IN _cargo VARCHAR(50),
    IN _fecha_contratacion DATE,
    INOUT _Respuesta INT
)
BEGIN
    INSERT INTO Empleados (documento, nombres, apellidos, id_departamento, cargo, fecha_contratacion)
    VALUES (_documento, _nombres, _apellidos, _id_departamento, _cargo, _fecha_contratacion);
    SET _Respuesta = 1;
END$$

DROP PROCEDURE IF EXISTS proc_update_Empleados$$
CREATE PROCEDURE proc_update_Empleados(
    IN _id_empleado INT,
    IN _documento VARCHAR(20),
    IN _nombres VARCHAR(50),
    IN _apellidos VARCHAR(50),
    IN _id_departamento INT,
    IN _cargo VARCHAR(50),
    IN _fecha_contratacion DATE
)
BEGIN
    UPDATE Empleados
    SET documento = _documento,
        nombres = _nombres,
        apellidos = _apellidos,
        id_departamento = _id_departamento,
        cargo = _cargo,
        fecha_contratacion = _fecha_contratacion
    WHERE id_empleado = _id_empleado;
END$$

DROP PROCEDURE IF EXISTS proc_delete_Empleados$$
CREATE PROCEDURE proc_delete_Empleados(IN _id_empleado INT)
BEGIN
    DELETE FROM Empleados WHERE id_empleado = _id_empleado;
END$$

-- Laboratorios
DROP PROCEDURE IF EXISTS proc_select_all_Laboratorios$$
CREATE PROCEDURE proc_select_all_Laboratorios()
BEGIN
    SELECT * FROM Laboratorios;
END$$

DROP PROCEDURE IF EXISTS proc_select_by_id_Laboratorios$$
CREATE PROCEDURE proc_select_by_id_Laboratorios(IN _id_laboratorio INT)
BEGIN
    SELECT * FROM Laboratorios WHERE id_laboratorio = _id_laboratorio;
END$$

DROP PROCEDURE IF EXISTS proc_insert_Laboratorios$$
CREATE PROCEDURE proc_insert_Laboratorios(
    IN _nombre VARCHAR(100),
    IN _direccion VARCHAR(100),
    IN _telefono VARCHAR(15),
    INOUT _Respuesta INT
)
BEGIN
    INSERT INTO Laboratorios (nombre, direccion, telefono)
    VALUES (_nombre, _direccion, _telefono);
    SET _Respuesta = 1;
END$$

DROP PROCEDURE IF EXISTS proc_update_Laboratorios$$
CREATE PROCEDURE proc_update_Laboratorios(
    IN _id_laboratorio INT,
    IN _nombre VARCHAR(100),
    IN _direccion VARCHAR(100),
    IN _telefono VARCHAR(15)
)
BEGIN
    UPDATE Laboratorios
    SET nombre = _nombre,
        direccion = _direccion,
        telefono = _telefono
    WHERE id_laboratorio = _id_laboratorio;
END$$

DROP PROCEDURE IF EXISTS proc_delete_Laboratorios$$
CREATE PROCEDURE proc_delete_Laboratorios(IN _id_laboratorio INT)
BEGIN
    DELETE FROM Laboratorios WHERE id_laboratorio = _id_laboratorio;
END$$

-- ExamenesLaboratorio
DROP PROCEDURE IF EXISTS proc_select_all_ExamenesLaboratorio$$
CREATE PROCEDURE proc_select_all_ExamenesLaboratorio()
BEGIN
    SELECT * FROM ExamenesLaboratorio;
END$$

DROP PROCEDURE IF EXISTS proc_select_by_id_ExamenesLaboratorio$$
CREATE PROCEDURE proc_select_by_id_ExamenesLaboratorio(IN _id_examen INT)
BEGIN
    SELECT * FROM ExamenesLaboratorio WHERE id_examen = _id_examen;
END$$

DROP PROCEDURE IF EXISTS proc_insert_ExamenesLaboratorio$$
CREATE PROCEDURE proc_insert_ExamenesLaboratorio(
    IN _id_consulta INT,
    IN _id_laboratorio INT,
    IN _tipo_examen VARCHAR(100),
    IN _resultado TEXT,
    INOUT _Respuesta INT
)
BEGIN
    INSERT INTO ExamenesLaboratorio (id_consulta, id_laboratorio, tipo_examen, resultado)
    VALUES (_id_consulta, _id_laboratorio, _tipo_examen, _resultado);
    SET _Respuesta = 1;
END$$

DROP PROCEDURE IF EXISTS proc_update_ExamenesLaboratorio$$
CREATE PROCEDURE proc_update_ExamenesLaboratorio(
    IN _id_examen INT,
    IN _id_consulta INT,
    IN _id_laboratorio INT,
    IN _tipo_examen VARCHAR(100),
    IN _resultado TEXT
)
BEGIN
    UPDATE ExamenesLaboratorio
    SET id_consulta = _id_consulta,
        id_laboratorio = _id_laboratorio,
        tipo_examen = _tipo_examen,
        resultado = _resultado
    WHERE id_examen = _id_examen;
END$$

DROP PROCEDURE IF EXISTS proc_delete_ExamenesLaboratorio$$
CREATE PROCEDURE proc_delete_ExamenesLaboratorio(IN _id_examen INT)
BEGIN
    DELETE FROM ExamenesLaboratorio WHERE id_examen = _id_examen;
END$$

-- Facturas
DROP PROCEDURE IF EXISTS proc_select_all_Facturas$$
CREATE PROCEDURE proc_select_all_Facturas()
BEGIN
    SELECT * FROM Facturas;
END$$

DROP PROCEDURE IF EXISTS proc_select_by_id_Facturas$$
CREATE PROCEDURE proc_select_by_id_Facturas(IN _id_factura INT)
BEGIN
    SELECT * FROM Facturas WHERE id_factura = _id_factura;
END$$

DROP PROCEDURE IF EXISTS proc_insert_Facturas$$
CREATE PROCEDURE proc_insert_Facturas(
    IN _id_paciente INT,
    IN _monto_total DECIMAL(10,2),
    IN _estado ENUM('Pendiente', 'Pagada', 'Anulada'),
    INOUT _Respuesta INT
)
BEGIN
    INSERT INTO Facturas (id_paciente, monto_total, estado)
    VALUES (_id_paciente, _monto_total, _estado);
    SET _Respuesta = 1;
END$$

DROP PROCEDURE IF EXISTS proc_update_Facturas$$
CREATE PROCEDURE proc_update_Facturas(
    IN _id_factura INT,
    IN _id_paciente INT,
    IN _monto_total DECIMAL(10,2),
    IN _estado ENUM('Pendiente', 'Pagada', 'Anulada')
)
BEGIN
    UPDATE Facturas
    SET id_paciente = _id_paciente,
        monto_total = _monto_total,
        estado = _estado
    WHERE id_factura = _id_factura;
END$$

DROP PROCEDURE IF EXISTS proc_delete_Facturas$$
CREATE PROCEDURE proc_delete_Facturas(IN _id_factura INT)
BEGIN
    DELETE FROM Facturas WHERE id_factura = _id_factura;
END$$

-- DetallesFactura
DROP PROCEDURE IF EXISTS proc_select_all_DetallesFactura$$
CREATE PROCEDURE proc_select_all_DetallesFactura()
BEGIN
    SELECT * FROM DetallesFactura;
END$$

DROP PROCEDURE IF EXISTS proc_select_by_id_DetallesFactura$$
CREATE PROCEDURE proc_select_by_id_DetallesFactura(IN _id_detalle INT)
BEGIN
    SELECT * FROM DetallesFactura WHERE id_detalle = _id_detalle;
END$$

DROP PROCEDURE IF EXISTS proc_insert_DetallesFactura$$
CREATE PROCEDURE proc_insert_DetallesFactura(
    IN _id_factura INT,
    IN _concepto VARCHAR(100),
    IN _cantidad INT,
    IN _precio_unitario DECIMAL(10,2),
    IN _subtotal DECIMAL(10,2),
    INOUT _Respuesta INT
)
BEGIN
    INSERT INTO DetallesFactura (id_factura, concepto, cantidad, precio_unitario, subtotal)
    VALUES (_id_factura, _concepto, _cantidad, _precio_unitario, _subtotal);
    SET _Respuesta = 1;
END$$

DROP PROCEDURE IF EXISTS proc_update_DetallesFactura$$
CREATE PROCEDURE proc_update_DetallesFactura(
    IN _id_detalle INT,
    IN _id_factura INT,
    IN _concepto VARCHAR(100),
    IN _cantidad INT,
    IN _precio_unitario DECIMAL(10,2),
    IN _subtotal DECIMAL(10,2)
)
BEGIN
    UPDATE DetallesFactura
    SET id_factura = _id_factura,
        concepto = _concepto,
        cantidad = _cantidad,
        precio_unitario = _precio_unitario,
        subtotal = _subtotal
    WHERE id_detalle = _id_detalle;
END$$

DROP PROCEDURE IF EXISTS proc_delete_DetallesFactura$$
CREATE PROCEDURE proc_delete_DetallesFactura(IN _id_detalle INT)
BEGIN
    DELETE FROM DetallesFactura WHERE id_detalle = _id_detalle;
END$$

-- Horarios
DROP PROCEDURE IF EXISTS proc_select_all_Horarios$$
CREATE PROCEDURE proc_select_all_Horarios()
BEGIN
    SELECT * FROM Horarios;
END$$

DROP PROCEDURE IF EXISTS proc_select_by_id_Horarios$$
CREATE PROCEDURE proc_select_by_id_Horarios(IN _id_horario INT)
BEGIN
    SELECT * FROM Horarios WHERE id_horario = _id_horario;
END$$

DROP PROCEDURE IF EXISTS proc_insert_Horarios$$
CREATE PROCEDURE proc_insert_Horarios(
    IN _id_medico INT,
    IN _dia_semana ENUM('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'),
    IN _hora_inicio TIME,
    IN _hora_fin TIME,
    INOUT _Respuesta INT
)
BEGIN
    INSERT INTO Horarios (id_medico, dia_semana, hora_inicio, hora_fin)
    VALUES (_id_medico, _dia_semana, _hora_inicio, _hora_fin);
    SET _Respuesta = 1;
END$$

DROP PROCEDURE IF EXISTS proc_update_Horarios$$
CREATE PROCEDURE proc_update_Horarios(
    IN _id_horario INT,
    IN _id_medico INT,
    IN _dia_semana ENUM('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'),
    IN _hora_inicio TIME,
    IN _hora_fin TIME
)
BEGIN
    UPDATE Horarios
    SET id_medico = _id_medico,
        dia_semana = _dia_semana,
        hora_inicio = _hora_inicio,
        hora_fin = _hora_fin
    WHERE id_horario = _id_horario;
END$$

DROP PROCEDURE IF EXISTS proc_delete_Horarios$$
CREATE PROCEDURE proc_delete_Horarios(IN _id_horario INT)
BEGIN
    DELETE FROM Horarios WHERE id_horario = _id_horario;
END$$;