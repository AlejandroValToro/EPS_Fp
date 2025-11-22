from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.repositories.base import RepositorioBase
from app.models.models import ExamenesLaboratorio

class ExamenesLaboratorioRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, ExamenesLaboratorio)

    def crear(self, e: ExamenesLaboratorio):
        try:
            params = {
                '_id_consulta': e.id_consulta, 
                '_id_laboratorio': e.id_laboratorio, 
                '_tipo_examen': e.tipo_examen, 
                '_resultado': e.resultado
            }
            self.session.execute(text("CALL proc_insert_ExamenesLaboratorio(:_id_consulta, :_id_laboratorio, :_tipo_examen, :_resultado, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo crear el examen de laboratorio: {err}")
            return False

    def actualizar(self, e: ExamenesLaboratorio):
        try:
            params = {
                '_id_examen': e.id_examen, 
                '_id_consulta': e.id_consulta, 
                '_id_laboratorio': e.id_laboratorio, 
                '_tipo_examen': e.tipo_examen, 
                '_resultado': e.resultado
            }
            self.session.execute(text("CALL proc_update_ExamenesLaboratorio(:_id_examen, :_id_consulta, :_id_laboratorio, :_tipo_examen, :_resultado)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo actualizar el examen de laboratorio: {err}")
            return False
