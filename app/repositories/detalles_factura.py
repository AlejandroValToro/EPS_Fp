from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.repositories.base import RepositorioBase
from app.models.models import DetallesFactura

class DetallesFacturaRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, DetallesFactura)

    def crear(self, e: DetallesFactura):
        try:
            params = {
                '_id_factura': e.id_factura, 
                '_concepto': e.concepto, 
                '_cantidad': e.cantidad, 
                '_precio_unitario': e.precio_unitario, 
                '_subtotal': e.subtotal
            }
            self.session.execute(text("CALL proc_insert_DetallesFactura(:_id_factura, :_concepto, :_cantidad, :_precio_unitario, :_subtotal, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo crear el detalle de factura: {err}")
            return False

    def actualizar(self, e: DetallesFactura):
        try:
            params = {
                '_id_detalle': e.id_detalle, 
                '_id_factura': e.id_factura, 
                '_concepto': e.concepto, 
                '_cantidad': e.cantidad, 
                '_precio_unitario': e.precio_unitario, 
                '_subtotal': e.subtotal
            }
            self.session.execute(text("CALL proc_update_DetallesFactura(:_id_detalle, :_id_factura, :_concepto, :_cantidad, :_precio_unitario, :_subtotal)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo actualizar el detalle de factura: {err}")
            return False
