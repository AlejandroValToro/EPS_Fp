from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.repositories.base import RepositorioBase
from app.models.models import Medicos
from app.utils.security import Security

class MedicosRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Medicos, encrypted_fields=['documento', 'nombres', 'apellidos', 'telefono', 'email', 'tarjeta_profesional'])

    def crear(self, e: Medicos):
        try:
            doc_enc = Security.encrypt_value(e.documento)
            nom_enc = Security.encrypt_value(e.nombres)
            ape_enc = Security.encrypt_value(e.apellidos)
            tel_enc = Security.encrypt_value(e.telefono)
            ema_enc = Security.encrypt_value(e.email)
            tar_enc = Security.encrypt_value(e.tarjeta_profesional)

            params = {
                '_documento': doc_enc, 
                '_nombres': nom_enc, 
                '_apellidos': ape_enc, 
                '_id_especialidad': e.id_especialidad, 
                '_telefono': tel_enc, 
                '_email': ema_enc, 
                '_tarjeta_profesional': tar_enc
            }
            self.session.execute(text("CALL proc_insert_Medicos(:_documento, :_nombres, :_apellidos, :_id_especialidad, :_telefono, :_email, :_tarjeta_profesional, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo crear el médico: {err}")
            return False

    def actualizar(self, e: Medicos):
        try:
            doc_enc = Security.encrypt_value(e.documento)
            nom_enc = Security.encrypt_value(e.nombres)
            ape_enc = Security.encrypt_value(e.apellidos)
            tel_enc = Security.encrypt_value(e.telefono)
            ema_enc = Security.encrypt_value(e.email)
            tar_enc = Security.encrypt_value(e.tarjeta_profesional)

            params = {
                '_id_medico': e.id_medico, 
                '_documento': doc_enc, 
                '_nombres': nom_enc, 
                '_apellidos': ape_enc, 
                '_id_especialidad': e.id_especialidad, 
                '_telefono': tel_enc, 
                '_email': ema_enc, 
                '_tarjeta_profesional': tar_enc
            }
            self.session.execute(text("CALL proc_update_Medicos(:_id_medico, :_documento, :_nombres, :_apellidos, :_id_especialidad, :_telefono, :_email, :_tarjeta_profesional)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo actualizar el médico: {err}")
            return False
