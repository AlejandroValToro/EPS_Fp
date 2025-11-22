from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.repositories.base import RepositorioBase
from app.models.models import HistoriasClinicas

class HistoriasClinicasRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, HistoriasClinicas)

    def crear(self, e: HistoriasClinicas):
        try:
            params = {
                '_id_paciente': e.id_paciente, 
                '_antecedentes': e.antecedentes
            }
            self.session.execute(text("CALL proc_insert_HistoriasClinicas(:_id_paciente, :_antecedentes, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo crear la historia clínica: {err}")
            return False

    def actualizar(self, e: HistoriasClinicas):
        try:
            params = {
                '_id_historia': e.id_historia, 
                '_id_paciente': e.id_paciente, 
                '_antecedentes': e.antecedentes
            }
            self.session.execute(text("CALL proc_update_HistoriasClinicas(:_id_historia, :_id_paciente, :_antecedentes)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo actualizar la historia clínica: {err}")
            return False
