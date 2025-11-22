from flask import Blueprint, request, jsonify
from app import get_db
from app.repositories.citas import CitasRepositorio
from app.models.models import Citas
from app.utils.decorators import token_required
from datetime import datetime

citas_bp = Blueprint('citas', __name__)

@citas_bp.route('/', methods=['GET'])
@token_required
def get_citas():
    try:
        db = next(get_db())
        repo = CitasRepositorio(db)
        entidades = repo.leer_todos()
        return jsonify({"Entidades": entidades, "Respuesta": "OK"})
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@citas_bp.route('/<int:id>', methods=['GET'])
@token_required
def get_cita(id):
    try:
        db = next(get_db())
        repo = CitasRepositorio(db)
        cita = repo.leer_por_id(id)
        
        if cita:
            cita_dict = {
                'id_cita': cita.id_cita,
                'id_paciente': cita.id_paciente,
                'id_medico': cita.id_medico,
                'fecha_hora': cita.fecha_hora.isoformat() if cita.fecha_hora else None,
                'estado': cita.estado,
                'motivo': cita.motivo,
            }
            return jsonify({"Entidad": cita_dict, "Respuesta": "OK"})
        else:
            return jsonify({"Error": "Citas no encontrado", "Respuesta": "Error"}), 404
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@citas_bp.route('/', methods=['POST'])
@token_required
def create_cita():
    try:
        data = request.get_json()
        db = next(get_db())
        repo = CitasRepositorio(db)
        
        nuevo_cita = Citas(
            id_paciente=data.get('id_paciente'),
            id_medico=data.get('id_medico'),
            fecha_hora=datetime.fromisoformat(data.get('fecha_hora')) if data.get('fecha_hora') else None,
            estado=data.get('estado'),
            motivo=data.get('motivo')
        )
        
        if repo.crear(nuevo_cita):
            return jsonify({'message': 'Citas creado exitosamente', 'Respuesta': 'OK'}), 201
        else:
            return jsonify({'error': 'Error al crear cita', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@citas_bp.route('/<int:id>', methods=['PUT'])
@token_required
def update_cita(id):
    try:
        data = request.get_json()
        db = next(get_db())
        repo = CitasRepositorio(db)
        
        cita_actualizado = Citas(
            id_cita=id,
            id_paciente=data.get('id_paciente'),
            id_medico=data.get('id_medico'),
            fecha_hora=datetime.fromisoformat(data.get('fecha_hora')) if data.get('fecha_hora') else None,
            estado=data.get('estado'),
            motivo=data.get('motivo')
        )
        
        if repo.actualizar(cita_actualizado):
            return jsonify({'message': 'Citas actualizado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al actualizar cita', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@citas_bp.route('/<int:id>', methods=['DELETE'])
@token_required
def delete_cita(id):
    try:
        db = next(get_db())
        repo = CitasRepositorio(db)
        
        if repo.eliminar(id):
            return jsonify({'message': 'Citas eliminado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al eliminar cita', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500
