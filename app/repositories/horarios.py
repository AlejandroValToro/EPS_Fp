from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.repositories.base import RepositorioBase
from app.models.models import Horarios

class HorariosRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Horarios)

    def crear(self, e: Horarios):
        try:
            params = {
                '_id_medico': e.id_medico, 
                '_dia_semana': e.dia_semana, 
                '_hora_inicio': e.hora_inicio, 
                '_hora_fin': e.hora_fin
            }
            self.session.execute(text("CALL proc_insert_Horarios(:_id_medico, :_dia_semana, :_hora_inicio, :_hora_fin, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo crear el horario: {err}")
            return False

    def actualizar(self, e: Horarios):
        try:
            params = {
                '_id_horario': e.id_horario, 
                '_id_medico': e.id_medico, 
                '_dia_semana': e.dia_semana, 
                '_hora_inicio': e.hora_inicio, 
                '_hora_fin': e.hora_fin
            }
            self.session.execute(text("CALL proc_update_Horarios(:_id_horario, :_id_medico, :_dia_semana, :_hora_inicio, :_hora_fin)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo actualizar el horario: {err}")
            return False
