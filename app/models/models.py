from sqlalchemy import Column, Integer, String, DATE, DATETIME, Enum, TEXT, DECIMAL, TIME
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Pacientes(Base):
    __tablename__ = 'Pacientes'
    id_paciente = Column(Integer, primary_key=True)
    documento = Column(String(255))
    tipo_documento = Column(Enum('CC', 'CE', 'TI', 'RC'))
    nombres = Column(String(255))
    apellidos = Column(String(255))
    fecha_nacimiento = Column(DATE)
    genero = Column(Enum('M', 'F', 'O'))
    direccion = Column(String(255))
    telefono = Column(String(255))
    email = Column(String(255))
    fecha_registro = Column(DATETIME)

class Especialidades(Base):
    __tablename__ = 'Especialidades'
    id_especialidad = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    descripcion = Column(TEXT)

class Medicos(Base):
    __tablename__ = 'Medicos'
    id_medico = Column(Integer, primary_key=True)
    documento = Column(String(255))
    nombres = Column(String(255))
    apellidos = Column(String(255))
    id_especialidad = Column(Integer)
    telefono = Column(String(255))
    email = Column(String(255))
    tarjeta_profesional = Column(String(255))

class Citas(Base):
    __tablename__ = 'Citas'
    id_cita = Column(Integer, primary_key=True)
    id_paciente = Column(Integer)
    id_medico = Column(Integer)
    fecha_hora = Column(DATETIME)
    estado = Column(Enum('Programada', 'Completada', 'Cancelada'))
    motivo = Column(TEXT)

class HistoriasClinicas(Base):
    __tablename__ = 'HistoriasClinicas'
    id_historia = Column(Integer, primary_key=True)
    id_paciente = Column(Integer)
    fecha_creacion = Column(DATETIME)
    antecedentes = Column(TEXT)

class Consultas(Base):
    __tablename__ = 'Consultas'
    id_consulta = Column(Integer, primary_key=True)
    id_cita = Column(Integer)
    id_historia = Column(Integer)
    diagnostico = Column(TEXT)
    tratamiento = Column(TEXT)
    observaciones = Column(TEXT)
    fecha_consulta = Column(DATETIME)

class Medicamentos(Base):
    __tablename__ = 'Medicamentos'
    id_medicamento = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    descripcion = Column(TEXT)
    fabricante = Column(String(50))
    stock = Column(Integer)

class Recetas(Base):
    __tablename__ = 'Recetas'
    id_receta = Column(Integer, primary_key=True)
    id_consulta = Column(Integer)
    id_medicamento = Column(Integer)
    dosis = Column(String(50))
    frecuencia = Column(String(50))
    duracion = Column(String(50))
    fecha_receta = Column(DATETIME)

class Departamentos(Base):
    __tablename__ = 'Departamentos'
    id_departamento = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    descripcion = Column(TEXT)

class Empleados(Base):
    __tablename__ = 'Empleados'
    id_empleado = Column(Integer, primary_key=True)
    documento = Column(String(255))
    nombres = Column(String(255))
    apellidos = Column(String(255))
    id_departamento = Column(Integer)
    cargo = Column(String(50))
    fecha_contratacion = Column(DATE)

class Laboratorios(Base):
    __tablename__ = 'Laboratorios'
    id_laboratorio = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    direccion = Column(String(100))
    telefono = Column(String(255))

class ExamenesLaboratorio(Base):
    __tablename__ = 'ExamenesLaboratorio'
    id_examen = Column(Integer, primary_key=True)
    id_consulta = Column(Integer)
    id_laboratorio = Column(Integer)
    tipo_examen = Column(String(100))
    fecha_solicitud = Column(DATETIME)
    fecha_resultado = Column(DATETIME)
    resultado = Column(TEXT)

class Facturas(Base):
    __tablename__ = 'Facturas'
    id_factura = Column(Integer, primary_key=True)
    id_paciente = Column(Integer)
    fecha_emision = Column(DATETIME)
    monto_total = Column(DECIMAL(10, 2))
    estado = Column(Enum('Pendiente', 'Pagada', 'Anulada'))

class DetallesFactura(Base):
    __tablename__ = 'DetallesFactura'
    id_detalle = Column(Integer, primary_key=True)
    id_factura = Column(Integer)
    concepto = Column(String(100))
    cantidad = Column(Integer)
    precio_unitario = Column(DECIMAL(10, 2))
    subtotal = Column(DECIMAL(10, 2))

class Horarios(Base):
    __tablename__ = 'Horarios'
    id_horario = Column(Integer, primary_key=True)
    id_medico = Column(Integer)
    dia_semana = Column(Enum('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'))
    hora_inicio = Column(TIME)
    hora_fin = Column(TIME)
