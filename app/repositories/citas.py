from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.repositories.base import RepositorioBase
from app.models.models import Citas

class CitasRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Citas)

    def crear(self, e: Citas):
        try:
            params = {
                '_id_paciente': e.id_paciente, 
                '_id_medico': e.id_medico, 
                '_fecha_hora': e.fecha_hora, 
                '_estado': e.estado, 
                '_motivo': e.motivo
            }
            self.session.execute(text("CALL proc_insert_Citas(:_id_paciente, :_id_medico, :_fecha_hora, :_estado, :_motivo, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo crear la cita: {err}")
            return False

    def actualizar(self, e: Citas):
        try:
            params = {
                '_id_cita': e.id_cita, 
                '_id_paciente': e.id_paciente, 
                '_id_medico': e.id_medico, 
                '_fecha_hora': e.fecha_hora, 
                '_estado': e.estado, 
                '_motivo': e.motivo
            }
            self.session.execute(text("CALL proc_update_Citas(:_id_cita, :_id_paciente, :_id_medico, :_fecha_hora, :_estado, :_motivo)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo actualizar la cita: {err}")
            return False
