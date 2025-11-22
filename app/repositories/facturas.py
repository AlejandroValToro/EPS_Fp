from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.repositories.base import RepositorioBase
from app.models.models import Facturas

class FacturasRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Facturas)

    def crear(self, e: Facturas):
        try:
            params = {
                '_id_paciente': e.id_paciente, 
                '_monto_total': e.monto_total, 
                '_estado': e.estado
            }
            self.session.execute(text("CALL proc_insert_Facturas(:_id_paciente, :_monto_total, :_estado, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo crear la factura: {err}")
            return False

    def actualizar(self, e: Facturas):
        try:
            params = {
                '_id_factura': e.id_factura, 
                '_id_paciente': e.id_paciente, 
                '_monto_total': e.monto_total, 
                '_estado': e.estado
            }
            self.session.execute(text("CALL proc_update_Facturas(:_id_factura, :_id_paciente, :_monto_total, :_estado)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo actualizar la factura: {err}")
            return False
