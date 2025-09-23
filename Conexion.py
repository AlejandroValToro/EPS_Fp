from sqlalchemy import create_engine, text, Column, Integer, String, DECIMAL, Date, DateTime, Enum, Text, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from datetime import datetime

Base = declarative_base()

# Definición de modelos
class Paciente(Base):
    __tablename__ = "Pacientes"
    
    id_paciente = Column(Integer, primary_key=True, autoincrement=True)
    documento = Column(String(20), nullable=False)
    tipo_documento = Column(Enum('CC', 'CE', 'TI', 'RC'), nullable=False)
    nombres = Column(String(50), nullable=False)
    apellidos = Column(String(50), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    genero = Column(Enum('M', 'F', 'O'), nullable=False)
    direccion = Column(String(100))
    telefono = Column(String(15))
    email = Column(String(50))
    fecha_registro = Column(DateTime, default=datetime.now)

class Especialidad(Base):
    __tablename__ = "Especialidades"
    
    id_especialidad = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(Text)

class Medico(Base):
    __tablename__ = "Medicos"
    
    id_medico = Column(Integer, primary_key=True, autoincrement=True)
    documento = Column(String(20), nullable=False)
    nombres = Column(String(50), nullable=False)
    apellidos = Column(String(50), nullable=False)
    id_especialidad = Column(Integer, ForeignKey('Especialidades.id_especialidad'))
    telefono = Column(String(15))
    email = Column(String(50))
    tarjeta_profesional = Column(String(20), nullable=False)
    
    especialidad = relationship("Especialidad")

class Conexion:
    def __init__(self):
        self.host = "localhost";
        self.database = "EPS";
        self.port = 3307;
        self.user = "user_ptyhon";
        self.password = "Clas3s1Nt2024_!";
        
        # Create SQLAlchemy connection string
        self.connection_string = f"mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

        self.engine = create_engine(self.connection_string)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    
    def obtener_pacientes(self) -> list:
        try:
            pacientes = self.session.query(Paciente).all()
            return pacientes
        except Exception as error:
            print(f"Error al consultar pacientes: {error}")
            return []
        finally:
            self.session.close()
    
    def obtener_medicos(self) -> list:
        try:
            medicos = self.session.query(Medico).all()
            return medicos
        except Exception as error:
            print(f"Error al consultar médicos: {error}")
            return []
        finally:
            self.session.close()
    
    def obtener_especialidades(self) -> list:
        try:
            especialidades = self.session.query(Especialidad).all()
            return especialidades
        except Exception as error:
            print(f"Error al consultar especialidades: {error}")
            return []
        finally:
            self.session.close()

if __name__ == "__main__":
    conexion = Conexion()
    # Ejemplo de uso
    pacientes = conexion.obtener_pacientes()
    for paciente in pacientes:
        print(f"Paciente: {paciente.nombres} {paciente.apellidos}")