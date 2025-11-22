from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.repositories.base import RepositorioBase
from app.models.models import Especialidades

class EspecialidadesRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Especialidades)

    def crear(self, e: Especialidades):
        try:
            params = {
                '_nombre': e.nombre, 
                '_descripcion': e.descripcion
            }
            self.session.execute(text("CALL proc_insert_Especialidades(:_nombre, :_descripcion, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo crear la especialidad: {err}")
            return False

    def actualizar(self, e: Especialidades):
        try:
            params = {
                '_id_especialidad': e.id_especialidad, 
                '_nombre': e.nombre, 
                '_descripcion': e.descripcion
            }
            self.session.execute(text("CALL proc_update_Especialidades(:_id_especialidad, :_nombre, :_descripcion)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo actualizar la especialidad: {err}")
            return False
