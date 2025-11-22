from flask import Blueprint, request, jsonify
from app import get_db
from app.repositories.especialidades import EspecialidadesRepositorio
from app.models.models import Especialidades
from app.utils.decorators import token_required

especialidades_bp = Blueprint('especialidades', __name__)

@especialidades_bp.route('/', methods=['GET'])
@token_required
def get_especialidades():
    try:
        db = next(get_db())
        repo = EspecialidadesRepositorio(db)
        entidades = repo.leer_todos()
        return jsonify({"Entidades": entidades, "Respuesta": "OK"})
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@especialidades_bp.route('/<int:id>', methods=['GET'])
@token_required
def get_especialidad(id):
    try:
        db = next(get_db())
        repo = EspecialidadesRepositorio(db)
        especialidad = repo.leer_por_id(id)
        
        if especialidad:
            esp_dict = {
                'id_especialidad': especialidad.id_especialidad,
                'nombre': especialidad.nombre,
                'descripcion': especialidad.descripcion
            }
            return jsonify({"Entidad": esp_dict, "Respuesta": "OK"})
        else:
            return jsonify({"Error": "Especialidad no encontrada", "Respuesta": "Error"}), 404
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@especialidades_bp.route('/', methods=['POST'])
@token_required
def create_especialidad():
    try:
        data = request.get_json()
        db = next(get_db())
        repo = EspecialidadesRepositorio(db)
        
        nueva_especialidad = Especialidades(
            nombre=data.get('nombre'),
            descripcion=data.get('descripcion')
        )
        
        if repo.crear(nueva_especialidad):
            return jsonify({'message': 'Especialidad creada exitosamente', 'Respuesta': 'OK'}), 201
        else:
            return jsonify({'error': 'Error al crear especialidad', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@especialidades_bp.route('/<int:id>', methods=['PUT'])
@token_required
def update_especialidad(id):
    try:
        data = request.get_json()
        db = next(get_db())
        repo = EspecialidadesRepositorio(db)
        
        especialidad_actualizada = Especialidades(
            id_especialidad=id,
            nombre=data.get('nombre'),
            descripcion=data.get('descripcion')
        )
        
        if repo.actualizar(especialidad_actualizada):
            return jsonify({'message': 'Especialidad actualizada exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al actualizar especialidad', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@especialidades_bp.route('/<int:id>', methods=['DELETE'])
@token_required
def delete_especialidad(id):
    try:
        db = next(get_db())
        repo = EspecialidadesRepositorio(db)
        
        if repo.eliminar(id):
            return jsonify({'message': 'Especialidad eliminada exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al eliminar especialidad', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500
