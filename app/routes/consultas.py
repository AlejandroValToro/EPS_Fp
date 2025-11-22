from flask import Blueprint, request, jsonify
from app import get_db
from app.repositories.consultas import ConsultasRepositorio
from app.models.models import Consultas
from app.utils.decorators import token_required

consultas_bp = Blueprint('consultas', __name__)

@consultas_bp.route('/', methods=['GET'])
@token_required
def get_consultas():
    try:
        db = next(get_db())
        repo = ConsultasRepositorio(db)
        entidades = repo.leer_todos()
        return jsonify({"Entidades": entidades, "Respuesta": "OK"})
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@consultas_bp.route('/<int:id>', methods=['GET'])
@token_required
def get_consulta(id):
    try:
        db = next(get_db())
        repo = ConsultasRepositorio(db)
        consulta = repo.leer_por_id(id)
        
        if consulta:
            consulta_dict = {
                'id_consulta': consulta.id_consulta,
                'id_cita': consulta.id_cita,
                'id_historia': consulta.id_historia,
                'diagnostico': consulta.diagnostico,
                'tratamiento': consulta.tratamiento,
                'observaciones': consulta.observaciones,
            }
            return jsonify({"Entidad": consulta_dict, "Respuesta": "OK"})
        else:
            return jsonify({"Error": "Consultas no encontrado", "Respuesta": "Error"}), 404
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@consultas_bp.route('/', methods=['POST'])
@token_required
def create_consulta():
    try:
        data = request.get_json()
        db = next(get_db())
        repo = ConsultasRepositorio(db)
        
        nuevo_consulta = Consultas(
            id_cita=data.get('id_cita'),
            id_historia=data.get('id_historia'),
            diagnostico=data.get('diagnostico'),
            tratamiento=data.get('tratamiento'),
            observaciones=data.get('observaciones')
        )
        
        if repo.crear(nuevo_consulta):
            return jsonify({'message': 'Consultas creado exitosamente', 'Respuesta': 'OK'}), 201
        else:
            return jsonify({'error': 'Error al crear consulta', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@consultas_bp.route('/<int:id>', methods=['PUT'])
@token_required
def update_consulta(id):
    try:
        data = request.get_json()
        db = next(get_db())
        repo = ConsultasRepositorio(db)
        
        consulta_actualizado = Consultas(
            id_consulta=id,
            id_cita=data.get('id_cita'),
            id_historia=data.get('id_historia'),
            diagnostico=data.get('diagnostico'),
            tratamiento=data.get('tratamiento'),
            observaciones=data.get('observaciones')
        )
        
        if repo.actualizar(consulta_actualizado):
            return jsonify({'message': 'Consultas actualizado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al actualizar consulta', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@consultas_bp.route('/<int:id>', methods=['DELETE'])
@token_required
def delete_consulta(id):
    try:
        db = next(get_db())
        repo = ConsultasRepositorio(db)
        
        if repo.eliminar(id):
            return jsonify({'message': 'Consultas eliminado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al eliminar consulta', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500
