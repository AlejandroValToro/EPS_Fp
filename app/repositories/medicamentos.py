from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.repositories.base import RepositorioBase
from app.models.models import Medicamentos

class MedicamentosRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Medicamentos)

    def crear(self, e: Medicamentos):
        try:
            params = {
                '_nombre': e.nombre, 
                '_descripcion': e.descripcion, 
                '_fabricante': e.fabricante, 
                '_stock': e.stock
            }
            self.session.execute(text("CALL proc_insert_Medicamentos(:_nombre, :_descripcion, :_fabricante, :_stock, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo crear el medicamento: {err}")
            return False

    def actualizar(self, e: Medicamentos):
        try:
            params = {
                '_id_medicamento': e.id_medicamento, 
                '_nombre': e.nombre, 
                '_descripcion': e.descripcion, 
                '_fabricante': e.fabricante, 
                '_stock': e.stock
            }
            self.session.execute(text("CALL proc_update_Medicamentos(:_id_medicamento, :_nombre, :_descripcion, :_fabricante, :_stock)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo actualizar el medicamento: {err}")
            return False
