from flask import Blueprint, request, jsonify
from app import get_db
from app.repositories.recetas import RecetasRepositorio
from app.models.models import Recetas
from app.utils.decorators import token_required

recetas_bp = Blueprint('recetas', __name__)

@recetas_bp.route('/', methods=['GET'])
@token_required
def get_recetas():
    try:
        db = next(get_db())
        repo = RecetasRepositorio(db)
        entidades = repo.leer_todos()
        return jsonify({"Entidades": entidades, "Respuesta": "OK"})
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@recetas_bp.route('/<int:id>', methods=['GET'])
@token_required
def get_receta(id):
    try:
        db = next(get_db())
        repo = RecetasRepositorio(db)
        receta = repo.leer_por_id(id)
        
        if receta:
            receta_dict = {
                'id_receta': receta.id_receta,
                'id_consulta': receta.id_consulta,
                'id_medicamento': receta.id_medicamento,
                'dosis': receta.dosis,
                'frecuencia': receta.frecuencia,
                'duracion': receta.duracion,
            }
            return jsonify({"Entidad": receta_dict, "Respuesta": "OK"})
        else:
            return jsonify({"Error": "Recetas no encontrado", "Respuesta": "Error"}), 404
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@recetas_bp.route('/', methods=['POST'])
@token_required
def create_receta():
    try:
        data = request.get_json()
        db = next(get_db())
        repo = RecetasRepositorio(db)
        
        nuevo_receta = Recetas(
            id_consulta=data.get('id_consulta'),
            id_medicamento=data.get('id_medicamento'),
            dosis=data.get('dosis'),
            frecuencia=data.get('frecuencia'),
            duracion=data.get('duracion')
        )
        
        if repo.crear(nuevo_receta):
            return jsonify({'message': 'Recetas creado exitosamente', 'Respuesta': 'OK'}), 201
        else:
            return jsonify({'error': 'Error al crear receta', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@recetas_bp.route('/<int:id>', methods=['PUT'])
@token_required
def update_receta(id):
    try:
        data = request.get_json()
        db = next(get_db())
        repo = RecetasRepositorio(db)
        
        receta_actualizado = Recetas(
            id_receta=id,
            id_consulta=data.get('id_consulta'),
            id_medicamento=data.get('id_medicamento'),
            dosis=data.get('dosis'),
            frecuencia=data.get('frecuencia'),
            duracion=data.get('duracion')
        )
        
        if repo.actualizar(receta_actualizado):
            return jsonify({'message': 'Recetas actualizado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al actualizar receta', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@recetas_bp.route('/<int:id>', methods=['DELETE'])
@token_required
def delete_receta(id):
    try:
        db = next(get_db())
        repo = RecetasRepositorio(db)
        
        if repo.eliminar(id):
            return jsonify({'message': 'Recetas eliminado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al eliminar receta', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500
