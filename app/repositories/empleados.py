from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.repositories.base import RepositorioBase
from app.models.models import Empleados
from app.utils.security import Security

class EmpleadosRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Empleados, encrypted_fields=['documento', 'nombres', 'apellidos'])

    def crear(self, e: Empleados):
        try:
            doc_enc = Security.encrypt_value(e.documento)
            nom_enc = Security.encrypt_value(e.nombres)
            ape_enc = Security.encrypt_value(e.apellidos)

            params = {
                '_documento': doc_enc, 
                '_nombres': nom_enc, 
                '_apellidos': ape_enc, 
                '_id_departamento': e.id_departamento, 
                '_cargo': e.cargo, 
                '_fecha_contratacion': e.fecha_contratacion
            }
            self.session.execute(text("CALL proc_insert_Empleados(:_documento, :_nombres, :_apellidos, :_id_departamento, :_cargo, :_fecha_contratacion, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo crear el empleado: {err}")
            return False

    def actualizar(self, e: Empleados):
        try:
            doc_enc = Security.encrypt_value(e.documento)
            nom_enc = Security.encrypt_value(e.nombres)
            ape_enc = Security.encrypt_value(e.apellidos)

            params = {
                '_id_empleado': e.id_empleado, 
                '_documento': doc_enc, 
                '_nombres': nom_enc, 
                '_apellidos': ape_enc, 
                '_id_departamento': e.id_departamento, 
                '_cargo': e.cargo, 
                '_fecha_contratacion': e.fecha_contratacion
            }
            self.session.execute(text("CALL proc_update_Empleados(:_id_empleado, :_documento, :_nombres, :_apellidos, :_id_departamento, :_cargo, :_fecha_contratacion)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo actualizar el empleado: {err}")
            return False
