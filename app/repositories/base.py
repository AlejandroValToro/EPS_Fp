from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from app.utils.security import Security

class RepositorioBase:
    def __init__(self, session, model, encrypted_fields=None):
        self.session = session
        self.model = model
        self.encrypted_fields = encrypted_fields or []

    def _map_result(self, result):
        column_names = result.keys()
        mapped_results = []
        for row in result:
            data = {col: getattr(row, col) for col in column_names}
            
            for field in self.encrypted_fields:
                if field in data and data[field] is not None:
                    data[field] = Security.decrypt_value(data[field])
            
            mapped_results.append(self.model(**data))
        return mapped_results

    def _format_results(self, results):
        formatted_response = {}
        for i, obj in enumerate(results):
            obj_dict = {c.name: getattr(obj, c.name) for c in obj.__table__.columns}
            
            for field in self.encrypted_fields:
                if field in obj_dict and obj_dict[field] is not None:
                    decrypted = Security.decrypt_value(obj_dict[field])
                    obj_dict[field] = decrypted
            
            for key, value in obj_dict.items():
                if hasattr(value, 'isoformat'):
                    obj_dict[key] = value.isoformat()
                    
            formatted_response[str(i)] = obj_dict
        return formatted_response

    def leer_todos(self):
        try:
            sp_name = f"proc_select_all_{self.model.__tablename__}"
            result = self.session.execute(text(f"CALL {sp_name}()"))
            objects = self._map_result(result)
            return self._format_results(objects)
        except SQLAlchemyError as e:
            print(f"No se pudieron cargar los datos: {e}")
            return {}

    def leer_por_id(self, id_):
        try:
            sp_name = f"proc_select_by_id_{self.model.__tablename__}"
            result = self.session.execute(text(f"CALL {sp_name}(:id)"), {"id": id_})
            mapped_result = self._map_result(result)
            return mapped_result[0] if mapped_result else None
        except SQLAlchemyError as e:
            print(f"Error al buscar el registro: {e}")
            return None

    def eliminar(self, id_):
        try:
            sp_name = f"proc_delete_{self.model.__tablename__}"
            self.session.execute(text(f"CALL {sp_name}(:id)"), {"id": id_})
            self.session.commit()
            return True
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"No se pudo eliminar: {e}")
            return False
