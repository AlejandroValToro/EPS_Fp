from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.repositories.base import RepositorioBase
from app.models.models import Pacientes
from app.utils.security import Security

class PacientesRepositorioModified(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Pacientes, encrypted_fields=['documento', 'nombres', 'apellidos', 'direccion', 'telefono', 'email'])

    def crear(self, e: Pacientes):
        try:
            doc_enc = Security.encrypt_value(e.documento)
            nom_enc = Security.encrypt_value(e.nombres)
            ape_enc = Security.encrypt_value(e.apellidos)
            dir_enc = Security.encrypt_value(e.direccion)
            tel_enc = Security.encrypt_value(e.telefono)
            ema_enc = Security.encrypt_value(e.email)

            params = {
                'p_documento': doc_enc, 
                'p_tipo_documento': e.tipo_documento, 
                'p_nombres': nom_enc, 
                'p_apellidos': ape_enc, 
                'p_fecha_nacimiento': e.fecha_nacimiento, 
                'p_genero': e.genero, 
                'p_direccion': dir_enc, 
                'p_telefono': tel_enc, 
                'p_email': ema_enc,
                'Respuesta': 0
            }
            
            self.session.execute(text("CALL proc_insert_Pacientes(:p_documento, :p_tipo_documento, :p_nombres, :p_apellidos, :p_fecha_nacimiento, :p_genero, :p_direccion, :p_telefono, :p_email, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo crear el paciente: {err}")
            return False 

    def actualizar(self, e: Pacientes):
        try:
            doc_enc = Security.encrypt_value(e.documento)
            nom_enc = Security.encrypt_value(e.nombres)
            ape_enc = Security.encrypt_value(e.apellidos)
            dir_enc = Security.encrypt_value(e.direccion)
            tel_enc = Security.encrypt_value(e.telefono)
            ema_enc = Security.encrypt_value(e.email)

            params = {
                '_id_paciente': e.id_paciente, 
                '_documento': doc_enc, 
                '_tipo_documento': e.tipo_documento, 
                '_nombres': nom_enc, 
                '_apellidos': ape_enc, 
                '_fecha_nacimiento': e.fecha_nacimiento, 
                '_genero': e.genero, 
                '_direccion': dir_enc, 
                '_telefono': tel_enc, 
                '_email': ema_enc
            }
            self.session.execute(text("CALL proc_update_Pacientes(:_id_paciente, :_documento, :_tipo_documento, :_nombres, :_apellidos, :_fecha_nacimiento, :_genero, :_direccion, :_telefono, :_email)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo actualizar el paciente: {err}")
            return False
