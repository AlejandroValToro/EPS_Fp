from flask import Blueprint, request, jsonify
from app import get_db
from app.repositories.historias_clinicas import HistoriasClinicasRepositorio
from app.models.models import HistoriasClinicas
from app.utils.decorators import token_required

historias_clinicas_bp = Blueprint('historias_clinicas', __name__)

@historias_clinicas_bp.route('/', methods=['GET'])
@token_required
def get_historias():
    try:
        db = next(get_db())
        repo = HistoriasClinicasRepositorio(db)
        entidades = repo.leer_todos()
        return jsonify({"Entidades": entidades, "Respuesta": "OK"})
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@historias_clinicas_bp.route('/<int:id>', methods=['GET'])
@token_required
def get_historia(id):
    try:
        db = next(get_db())
        repo = HistoriasClinicasRepositorio(db)
        historia = repo.leer_por_id(id)
        
        if historia:
            historia_dict = {
                'id_historia': historia.id_historia,
                'id_paciente': historia.id_paciente,
                'antecedentes': historia.antecedentes,
            }
            return jsonify({"Entidad": historia_dict, "Respuesta": "OK"})
        else:
            return jsonify({"Error": "HistoriasClinicas no encontrado", "Respuesta": "Error"}), 404
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@historias_clinicas_bp.route('/', methods=['POST'])
@token_required
def create_historia():
    try:
        data = request.get_json()
        db = next(get_db())
        repo = HistoriasClinicasRepositorio(db)
        
        nuevo_historia = HistoriasClinicas(
            id_paciente=data.get('id_paciente'),
            antecedentes=data.get('antecedentes')
        )
        
        if repo.crear(nuevo_historia):
            return jsonify({'message': 'HistoriasClinicas creado exitosamente', 'Respuesta': 'OK'}), 201
        else:
            return jsonify({'error': 'Error al crear historia', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@historias_clinicas_bp.route('/<int:id>', methods=['PUT'])
@token_required
def update_historia(id):
    try:
        data = request.get_json()
        db = next(get_db())
        repo = HistoriasClinicasRepositorio(db)
        
        historia_actualizado = HistoriasClinicas(
            id_historia=id,
            id_paciente=data.get('id_paciente'),
            antecedentes=data.get('antecedentes')
        )
        
        if repo.actualizar(historia_actualizado):
            return jsonify({'message': 'HistoriasClinicas actualizado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al actualizar historia', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@historias_clinicas_bp.route('/<int:id>', methods=['DELETE'])
@token_required
def delete_historia(id):
    try:
        db = next(get_db())
        repo = HistoriasClinicasRepositorio(db)
        
        if repo.eliminar(id):
            return jsonify({'message': 'HistoriasClinicas eliminado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al eliminar historia', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500
