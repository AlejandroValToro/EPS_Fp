from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.repositories.base import RepositorioBase
from app.models.models import Departamentos

class DepartamentosRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Departamentos)

    def crear(self, e: Departamentos):
        try:
            params = {
                '_nombre': e.nombre, 
                '_descripcion': e.descripcion
            }
            self.session.execute(text("CALL proc_insert_Departamentos(:_nombre, :_descripcion, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo crear el departamento: {err}")
            return False

    def actualizar(self, e: Departamentos):
        try:
            params = {
                '_id_departamento': e.id_departamento, 
                '_nombre': e.nombre, 
                '_descripcion': e.descripcion
            }
            self.session.execute(text("CALL proc_update_Departamentos(:_id_departamento, :_nombre, :_descripcion)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo actualizar el departamento: {err}")
            return False
