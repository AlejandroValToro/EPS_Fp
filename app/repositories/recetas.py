from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.repositories.base import RepositorioBase
from app.models.models import Recetas

class RecetasRepositorio(RepositorioBase):
    def __init__(self, session):
        super().__init__(session, Recetas)

    def crear(self, e: Recetas):
        try:
            params = {
                '_id_consulta': e.id_consulta, 
                '_id_medicamento': e.id_medicamento, 
                '_dosis': e.dosis, 
                '_frecuencia': e.frecuencia, 
                '_duracion': e.duracion
            }
            self.session.execute(text("CALL proc_insert_Recetas(:_id_consulta, :_id_medicamento, :_dosis, :_frecuencia, :_duracion, @Respuesta)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo crear la receta: {err}")
            return False

    def actualizar(self, e: Recetas):
        try:
            params = {
                '_id_receta': e.id_receta, 
                '_id_consulta': e.id_consulta, 
                '_id_medicamento': e.id_medicamento, 
                '_dosis': e.dosis, 
                '_frecuencia': e.frecuencia, 
                '_duracion': e.duracion
            }
            self.session.execute(text("CALL proc_update_Recetas(:_id_receta, :_id_consulta, :_id_medicamento, :_dosis, :_frecuencia, :_duracion)"), params)
            self.session.commit()
            return True
        except SQLAlchemyError as err:
            self.session.rollback()
            print(f"No se pudo actualizar la receta: {err}")
            return False
