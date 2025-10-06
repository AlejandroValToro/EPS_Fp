from sqlalchemy import create_engine, Column, Integer, String, DATE, DATETIME, Enum, TEXT, DECIMAL, TIME, ForeignKey, text
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

# --- Datos de conexion de la base de datos ---
DB_USER = "user_ptyhon"
DB_PASSWORD = "Clas3s1Nt2024_!"
DB_HOST = "localhost"
DB_PORT = "3307"
DB_NAME = "EPS"

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- Modelo de la base de datos---
class Pacientes(Base):
    __tablename__ = 'Pacientes'
    id_paciente = Column(Integer, primary_key=True)
    documento = Column(String(20))
    tipo_documento = Column(Enum('CC', 'CE', 'TI', 'RC'))
    nombres = Column(String(50))
    apellidos = Column(String(50))
    fecha_nacimiento = Column(DATE)
    genero = Column(Enum('M', 'F', 'O'))
    direccion = Column(String(100))
    telefono = Column(String(15))
    email = Column(String(50))
    fecha_registro = Column(DATETIME)

class Especialidades(Base):
    __tablename__ = 'Especialidades'
    id_especialidad = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    descripcion = Column(TEXT)

class Medicos(Base):
    __tablename__ = 'Medicos'
    id_medico = Column(Integer, primary_key=True)
    documento = Column(String(20))
    nombres = Column(String(50))
    apellidos = Column(String(50))
    id_especialidad = Column(Integer)
    telefono = Column(String(15))
    email = Column(String(50))
    tarjeta_profesional = Column(String(20))

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
    documento = Column(String(20))
    nombres = Column(String(50))
    apellidos = Column(String(50))
    id_departamento = Column(Integer)
    cargo = Column(String(50))
    fecha_contratacion = Column(DATE)

class Laboratorios(Base):
    __tablename__ = 'Laboratorios'
    id_laboratorio = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    direccion = Column(String(100))
    telefono = Column(String(15))

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


class RepositorioBase:
    def __init__(self, session, model):
        self.session = session
        self.model = model

    def _map_result(self, result):
        column_names = result.keys()
        return [self.model(**{col: getattr(row, col) for col in column_names}) for row in result]

    def leer_todos(self):
        try:
            sp_name = f"proc_select_all_{self.model.__tablename__}"
            result = self.session.execute(text(f"CALL {sp_name}()"))
            return self._map_result(result)
        except SQLAlchemyError as e:
            print(f"Error en {sp_name}: {e}")
            return []

    def leer_por_id(self, id_):
        try:
            pk_name = self.model.__table__.primary_key.columns.values()[0].name
            sp_name = f"proc_select_by_id_{self.model.__tablename__}"
            result = self.session.execute(text(f"CALL {sp_name}(:id)"), {"id": id_})
            mapped_result = self._map_result(result)
            return mapped_result[0] if mapped_result else None
        except SQLAlchemyError as e:
            print(f"Error en {sp_name}: {e}")
            return None

    def eliminar(self, id_):
        try:
            pk_name = self.model.__table__.primary_key.columns.values()[0].name
            sp_name = f"proc_delete_{self.model.__tablename__}"
            self.session.execute(text(f"CALL {sp_name}(:id)"), {"id": id_})
            self.session.commit()
            return True
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error en {sp_name}: {e}")
            return False

# --- Repositorio ---

class PacientesRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Pacientes)

    def crear(self, e: Pacientes):
        try:
            params = {'_documento': e.documento, '_tipo_documento': e.tipo_documento, '_nombres': e.nombres, '_apellidos': e.apellidos, '_fecha_nacimiento': e.fecha_nacimiento, '_genero': e.genero, '_direccion': e.direccion, '_telefono': e.telefono, '_email': e.email}
            self.session.execute(text("CALL proc_insert_Pacientes(:_documento, :_tipo_documento, :_nombres, :_apellidos, :_fecha_nacimiento, :_genero, :_direccion, :_telefono, :_email, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al crear Paciente: {err}")
            return False

    def actualizar(self, e: Pacientes):
        try:
            params = {'_id_paciente': e.id_paciente, '_documento': e.documento, '_tipo_documento': e.tipo_documento, '_nombres': e.nombres, '_apellidos': e.apellidos, '_fecha_nacimiento': e.fecha_nacimiento, '_genero': e.genero, '_direccion': e.direccion, '_telefono': e.telefono, '_email': e.email}
            self.session.execute(text("CALL proc_update_Pacientes(:_id_paciente, :_documento, :_tipo_documento, :_nombres, :_apellidos, :_fecha_nacimiento, :_genero, :_direccion, :_telefono, :_email)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al actualizar Paciente: {err}")
            return False

class EspecialidadesRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Especialidades)

    def crear(self, e: Especialidades):
        try:
            params = {'_nombre': e.nombre, '_descripcion': e.descripcion}
            self.session.execute(text("CALL proc_insert_Especialidades(:_nombre, :_descripcion, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al crear Especialidad: {err}")
            return False

    def actualizar(self, e: Especialidades):
        try:
            params = {'_id_especialidad': e.id_especialidad, '_nombre': e.nombre, '_descripcion': e.descripcion}
            self.session.execute(text("CALL proc_update_Especialidades(:_id_especialidad, :_nombre, :_descripcion)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al actualizar Especialidad: {err}")
            return False

class MedicosRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Medicos)

    def crear(self, e: Medicos):
        try:
            params = {'_documento': e.documento, '_nombres': e.nombres, '_apellidos': e.apellidos, '_id_especialidad': e.id_especialidad, '_telefono': e.telefono, '_email': e.email, '_tarjeta_profesional': e.tarjeta_profesional}
            self.session.execute(text("CALL proc_insert_Medicos(:_documento, :_nombres, :_apellidos, :_id_especialidad, :_telefono, :_email, :_tarjeta_profesional, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al crear Medico: {err}")
            return False

    def actualizar(self, e: Medicos):
        try:
            params = {'_id_medico': e.id_medico, '_documento': e.documento, '_nombres': e.nombres, '_apellidos': e.apellidos, '_id_especialidad': e.id_especialidad, '_telefono': e.telefono, '_email': e.email, '_tarjeta_profesional': e.tarjeta_profesional}
            self.session.execute(text("CALL proc_update_Medicos(:_id_medico, :_documento, :_nombres, :_apellidos, :_id_especialidad, :_telefono, :_email, :_tarjeta_profesional)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al actualizar Medico: {err}")
            return False

class CitasRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Citas)

    def crear(self, e: Citas):
        try:
            params = {'_id_paciente': e.id_paciente, '_id_medico': e.id_medico, '_fecha_hora': e.fecha_hora, '_estado': e.estado, '_motivo': e.motivo}
            self.session.execute(text("CALL proc_insert_Citas(:_id_paciente, :_id_medico, :_fecha_hora, :_estado, :_motivo, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al crear Cita: {err}")
            return False

    def actualizar(self, e: Citas):
        try:
            params = {'_id_cita': e.id_cita, '_id_paciente': e.id_paciente, '_id_medico': e.id_medico, '_fecha_hora': e.fecha_hora, '_estado': e.estado, '_motivo': e.motivo}
            self.session.execute(text("CALL proc_update_Citas(:_id_cita, :_id_paciente, :_id_medico, :_fecha_hora, :_estado, :_motivo)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al actualizar Cita: {err}")
            return False

class HistoriasClinicasRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, HistoriasClinicas)

    def crear(self, e: HistoriasClinicas):
        try:
            params = {'_id_paciente': e.id_paciente, '_antecedentes': e.antecedentes}
            self.session.execute(text("CALL proc_insert_HistoriasClinicas(:_id_paciente, :_antecedentes, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al crear Historia Clinica: {err}")
            return False

    def actualizar(self, e: HistoriasClinicas):
        try:
            params = {'_id_historia': e.id_historia, '_id_paciente': e.id_paciente, '_antecedentes': e.antecedentes}
            self.session.execute(text("CALL proc_update_HistoriasClinicas(:_id_historia, :_id_paciente, :_antecedentes)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al actualizar Historia Clinica: {err}")
            return False

class ConsultasRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Consultas)

    def crear(self, e: Consultas):
        try:
            params = {'_id_cita': e.id_cita, '_id_historia': e.id_historia, '_diagnostico': e.diagnostico, '_tratamiento': e.tratamiento, '_observaciones': e.observaciones}
            self.session.execute(text("CALL proc_insert_Consultas(:_id_cita, :_id_historia, :_diagnostico, :_tratamiento, :_observaciones, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al crear Consulta: {err}")
            return False

    def actualizar(self, e: Consultas):
        try:
            params = {'_id_consulta': e.id_consulta, '_id_cita': e.id_cita, '_id_historia': e.id_historia, '_diagnostico': e.diagnostico, '_tratamiento': e.tratamiento, '_observaciones': e.observaciones}
            self.session.execute(text("CALL proc_update_Consultas(:_id_consulta, :_id_cita, :_id_historia, :_diagnostico, :_tratamiento, :_observaciones)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al actualizar Consulta: {err}")
            return False

class MedicamentosRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Medicamentos)

    def crear(self, e: Medicamentos):
        try:
            params = {'_nombre': e.nombre, '_descripcion': e.descripcion, '_fabricante': e.fabricante, '_stock': e.stock}
            self.session.execute(text("CALL proc_insert_Medicamentos(:_nombre, :_descripcion, :_fabricante, :_stock, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al crear Medicamento: {err}")
            return False

    def actualizar(self, e: Medicamentos):
        try:
            params = {'_id_medicamento': e.id_medicamento, '_nombre': e.nombre, '_descripcion': e.descripcion, '_fabricante': e.fabricante, '_stock': e.stock}
            self.session.execute(text("CALL proc_update_Medicamentos(:_id_medicamento, :_nombre, :_descripcion, :_fabricante, :_stock)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al actualizar Medicamento: {err}")
            return False

class RecetasRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Recetas)

    def crear(self, e: Recetas):
        try:
            params = {'_id_consulta': e.id_consulta, '_id_medicamento': e.id_medicamento, '_dosis': e.dosis, '_frecuencia': e.frecuencia, '_duracion': e.duracion}
            self.session.execute(text("CALL proc_insert_Recetas(:_id_consulta, :_id_medicamento, :_dosis, :_frecuencia, :_duracion, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al crear Receta: {err}")
            return False

    def actualizar(self, e: Recetas):
        try:
            params = {'_id_receta': e.id_receta, '_id_consulta': e.id_consulta, '_id_medicamento': e.id_medicamento, '_dosis': e.dosis, '_frecuencia': e.frecuencia, '_duracion': e.duracion}
            self.session.execute(text("CALL proc_update_Recetas(:_id_receta, :_id_consulta, :_id_medicamento, :_dosis, :_frecuencia, :_duracion)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al actualizar Receta: {err}")
            return False

class DepartamentosRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Departamentos)

    def crear(self, e: Departamentos):
        try:
            params = {'_nombre': e.nombre, '_descripcion': e.descripcion}
            self.session.execute(text("CALL proc_insert_Departamentos(:_nombre, :_descripcion, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al crear Departamento: {err}")
            return False

    def actualizar(self, e: Departamentos):
        try:
            params = {'_id_departamento': e.id_departamento, '_nombre': e.nombre, '_descripcion': e.descripcion}
            self.session.execute(text("CALL proc_update_Departamentos(:_id_departamento, :_nombre, :_descripcion)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al actualizar Departamento: {err}")
            return False

class EmpleadosRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Empleados)

    def crear(self, e: Empleados):
        try:
            params = {'_documento': e.documento, '_nombres': e.nombres, '_apellidos': e.apellidos, '_id_departamento': e.id_departamento, '_cargo': e.cargo, '_fecha_contratacion': e.fecha_contratacion}
            self.session.execute(text("CALL proc_insert_Empleados(:_documento, :_nombres, :_apellidos, :_id_departamento, :_cargo, :_fecha_contratacion, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al crear Empleado: {err}")
            return False

    def actualizar(self, e: Empleados):
        try:
            params = {'_id_empleado': e.id_empleado, '_documento': e.documento, '_nombres': e.nombres, '_apellidos': e.apellidos, '_id_departamento': e.id_departamento, '_cargo': e.cargo, '_fecha_contratacion': e.fecha_contratacion}
            self.session.execute(text("CALL proc_update_Empleados(:_id_empleado, :_documento, :_nombres, :_apellidos, :_id_departamento, :_cargo, :_fecha_contratacion)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al actualizar Empleado: {err}")
            return False

class LaboratoriosRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Laboratorios)

    def crear(self, e: Laboratorios):
        try:
            params = {'_nombre': e.nombre, '_direccion': e.direccion, '_telefono': e.telefono}
            self.session.execute(text("CALL proc_insert_Laboratorios(:_nombre, :_direccion, :_telefono, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al crear Laboratorio: {err}")
            return False

    def actualizar(self, e: Laboratorios):
        try:
            params = {'_id_laboratorio': e.id_laboratorio, '_nombre': e.nombre, '_direccion': e.direccion, '_telefono': e.telefono}
            self.session.execute(text("CALL proc_update_Laboratorios(:_id_laboratorio, :_nombre, :_direccion, :_telefono)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al actualizar Laboratorio: {err}")
            return False

class ExamenesLaboratorioRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, ExamenesLaboratorio)

    def crear(self, e: ExamenesLaboratorio):
        try:
            params = {'_id_consulta': e.id_consulta, '_id_laboratorio': e.id_laboratorio, '_tipo_examen': e.tipo_examen, '_resultado': e.resultado}
            self.session.execute(text("CALL proc_insert_ExamenesLaboratorio(:_id_consulta, :_id_laboratorio, :_tipo_examen, :_resultado, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al crear Examen de Laboratorio: {err}")
            return False

    def actualizar(self, e: ExamenesLaboratorio):
        try:
            params = {'_id_examen': e.id_examen, '_id_consulta': e.id_consulta, '_id_laboratorio': e.id_laboratorio, '_tipo_examen': e.tipo_examen, '_resultado': e.resultado}
            self.session.execute(text("CALL proc_update_ExamenesLaboratorio(:_id_examen, :_id_consulta, :_id_laboratorio, :_tipo_examen, :_resultado)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al actualizar Examen de Laboratorio: {err}")
            return False

class FacturasRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Facturas)

    def crear(self, e: Facturas):
        try:
            params = {'_id_paciente': e.id_paciente, '_monto_total': e.monto_total, '_estado': e.estado}
            self.session.execute(text("CALL proc_insert_Facturas(:_id_paciente, :_monto_total, :_estado, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al crear Factura: {err}")
            return False

    def actualizar(self, e: Facturas):
        try:
            params = {'_id_factura': e.id_factura, '_id_paciente': e.id_paciente, '_monto_total': e.monto_total, '_estado': e.estado}
            self.session.execute(text("CALL proc_update_Facturas(:_id_factura, :_id_paciente, :_monto_total, :_estado)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al actualizar Factura: {err}")
            return False

class DetallesFacturaRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, DetallesFactura)

    def crear(self, e: DetallesFactura):
        try:
            params = {'_id_factura': e.id_factura, '_concepto': e.concepto, '_cantidad': e.cantidad, '_precio_unitario': e.precio_unitario, '_subtotal': e.subtotal}
            self.session.execute(text("CALL proc_insert_DetallesFactura(:_id_factura, :_concepto, :_cantidad, :_precio_unitario, :_subtotal, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al crear Detalle de Factura: {err}")
            return False

    def actualizar(self, e: DetallesFactura):
        try:
            params = {'_id_detalle': e.id_detalle, '_id_factura': e.id_factura, '_concepto': e.concepto, '_cantidad': e.cantidad, '_precio_unitario': e.precio_unitario, '_subtotal': e.subtotal}
            self.session.execute(text("CALL proc_update_DetallesFactura(:_id_detalle, :_id_factura, :_concepto, :_cantidad, :_precio_unitario, :_subtotal)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al actualizar Detalle de Factura: {err}")
            return False

class HorariosRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Horarios)

    def crear(self, e: Horarios):
        try:
            params = {'_id_medico': e.id_medico, '_dia_semana': e.dia_semana, '_hora_inicio': e.hora_inicio, '_hora_fin': e.hora_fin}
            self.session.execute(text("CALL proc_insert_Horarios(:_id_medico, :_dia_semana, :_hora_inicio, :_hora_fin, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al crear Horario: {err}")
            return False

    def actualizar(self, e: Horarios):
        try:
            params = {'_id_horario': e.id_horario, '_id_medico': e.id_medico, '_dia_semana': e.dia_semana, '_hora_inicio': e.hora_inicio, '_hora_fin': e.hora_fin}
            self.session.execute(text("CALL proc_update_Horarios(:_id_horario, :_id_medico, :_dia_semana, :_hora_inicio, :_hora_fin)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"Error al actualizar Horario: {err}")
            return False

# ---  inicio de la conexion base de datos ---
def inicializar_db():
    try:
        connection = engine.connect()
        connection.close()
        print("Conexión a la base de datos verificada exitosamente.")
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")