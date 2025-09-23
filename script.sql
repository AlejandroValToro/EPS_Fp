-- Creación de tablas para sistema EPS

CREATE TABLE Pacientes (
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

CREATE TABLE Especialidades (
    id_especialidad INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT
);

CREATE TABLE Medicos (
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

CREATE TABLE Citas (
    id_cita INT PRIMARY KEY AUTO_INCREMENT,
    id_paciente INT,
    id_medico INT,
    fecha_hora DATETIME NOT NULL,
    estado ENUM('Programada', 'Completada', 'Cancelada') NOT NULL,
    motivo TEXT,
    FOREIGN KEY (id_paciente) REFERENCES Pacientes(id_paciente),
    FOREIGN KEY (id_medico) REFERENCES Medicos(id_medico)
);

CREATE TABLE HistoriasClinicas (
    id_historia INT PRIMARY KEY AUTO_INCREMENT,
    id_paciente INT,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    antecedentes TEXT,
    FOREIGN KEY (id_paciente) REFERENCES Pacientes(id_paciente)
);

CREATE TABLE Consultas (
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

CREATE TABLE Medicamentos (
    id_medicamento INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fabricante VARCHAR(50),
    stock INT DEFAULT 0
);

CREATE TABLE Recetas (
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

CREATE TABLE Departamentos (
    id_departamento INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT
);

CREATE TABLE Empleados (
    id_empleado INT PRIMARY KEY AUTO_INCREMENT,
    documento VARCHAR(20) NOT NULL,
    nombres VARCHAR(50) NOT NULL,
    apellidos VARCHAR(50) NOT NULL,
    id_departamento INT,
    cargo VARCHAR(50),
    fecha_contratacion DATE,
    FOREIGN KEY (id_departamento) REFERENCES Departamentos(id_departamento)
);

CREATE TABLE Laboratorios (
    id_laboratorio INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(100),
    telefono VARCHAR(15)
);

CREATE TABLE ExamenesLaboratorio (
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

CREATE TABLE Facturas (
    id_factura INT PRIMARY KEY AUTO_INCREMENT,
    id_paciente INT,
    fecha_emision DATETIME DEFAULT CURRENT_TIMESTAMP,
    monto_total DECIMAL(10,2),
    estado ENUM('Pendiente', 'Pagada', 'Anulada') DEFAULT 'Pendiente',
    FOREIGN KEY (id_paciente) REFERENCES Pacientes(id_paciente)
);

CREATE TABLE DetallesFactura (
    id_detalle INT PRIMARY KEY AUTO_INCREMENT,
    id_factura INT,
    concepto VARCHAR(100),
    cantidad INT,
    precio_unitario DECIMAL(10,2),
    subtotal DECIMAL(10,2),
    FOREIGN KEY (id_factura) REFERENCES Facturas(id_factura)
);

CREATE TABLE Horarios (
    id_horario INT PRIMARY KEY AUTO_INCREMENT,
    id_medico INT,
    dia_semana ENUM('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'),
    hora_inicio TIME,
    hora_fin TIME,
    FOREIGN KEY (id_medico) REFERENCES Medicos(id_medico)
);