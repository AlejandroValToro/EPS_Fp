from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.repositories.base import RepositorioBase
from app.models.models import Laboratorios
from app.utils.security import Security

class LaboratoriosRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Laboratorios, encrypted_fields=['telefono'])

    def crear(self, e: Laboratorios):
        try:
            tel_enc = Security.encrypt_value(e.telefono)

            params = {
                '_nombre': e.nombre, 
                '_direccion': e.direccion, 
                '_telefono': tel_enc
            }
            self.session.execute(text("CALL proc_insert_Laboratorios(:_nombre, :_direccion, :_telefono, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo crear el laboratorio: {err}")
            return False

    def actualizar(self, e: Laboratorios):
        try:
            tel_enc = Security.encrypt_value(e.telefono)

            params = {
                '_id_laboratorio': e.id_laboratorio, 
                '_nombre': e.nombre, 
                '_direccion': e.direccion, 
                '_telefono': tel_enc
            }
            self.session.execute(text("CALL proc_update_Laboratorios(:_id_laboratorio, :_nombre, :_direccion, :_telefono)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo actualizar el laboratorio: {err}")
            return False
