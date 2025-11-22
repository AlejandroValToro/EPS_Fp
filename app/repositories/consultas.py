from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.repositories.base import RepositorioBase
from app.models.models import Consultas

class ConsultasRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Consultas)

    def crear(self, e: Consultas):
        try:
            params = {
                '_id_cita': e.id_cita, 
                '_id_historia': e.id_historia, 
                '_diagnostico': e.diagnostico, 
                '_tratamiento': e.tratamiento, 
                '_observaciones': e.observaciones
            }
            self.session.execute(text("CALL proc_insert_Consultas(:_id_cita, :_id_historia, :_diagnostico, :_tratamiento, :_observaciones, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo crear la consulta: {err}")
            return False

    def actualizar(self, e: Consultas):
        try:
            params = {
                '_id_consulta': e.id_consulta, 
                '_id_cita': e.id_cita, 
                '_id_historia': e.id_historia, 
                '_diagnostico': e.diagnostico, 
                '_tratamiento': e.tratamiento, 
                '_observaciones': e.observaciones
            }
            self.session.execute(text("CALL proc_update_Consultas(:_id_consulta, :_id_cita, :_id_historia, :_diagnostico, :_tratamiento, :_observaciones)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo actualizar la consulta: {err}")
            return False
