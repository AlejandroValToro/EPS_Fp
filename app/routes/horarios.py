from flask import Blueprint, request, jsonify
from app import get_db
from app.repositories.horarios import HorariosRepositorio
from app.models.models import Horarios
from app.utils.decorators import token_required

horarios_bp = Blueprint('horarios', __name__)

@horarios_bp.route('/', methods=['GET'])
@token_required
def get_horarios():
    try:
        db = next(get_db())
        repo = HorariosRepositorio(db)
        entidades = repo.leer_todos()
        return jsonify({"Entidades": entidades, "Respuesta": "OK"})
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@horarios_bp.route('/<int:id>', methods=['GET'])
@token_required
def get_horario(id):
    try:
        db = next(get_db())
        repo = HorariosRepositorio(db)
        horario = repo.leer_por_id(id)
        
        if horario:
            horario_dict = {
                'id_horario': horario.id_horario,
                'id_medico': horario.id_medico,
                'dia_semana': horario.dia_semana,
                'hora_inicio': horario.hora_inicio,
                'hora_fin': horario.hora_fin,
            }
            return jsonify({"Entidad": horario_dict, "Respuesta": "OK"})
        else:
            return jsonify({"Error": "Horarios no encontrado", "Respuesta": "Error"}), 404
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@horarios_bp.route('/', methods=['POST'])
@token_required
def create_horario():
    try:
        data = request.get_json()
        db = next(get_db())
        repo = HorariosRepositorio(db)
        
        nuevo_horario = Horarios(
            id_medico=data.get('id_medico'),
            dia_semana=data.get('dia_semana'),
            hora_inicio=data.get('hora_inicio'),
            hora_fin=data.get('hora_fin')
        )
        
        if repo.crear(nuevo_horario):
            return jsonify({'message': 'Horarios creado exitosamente', 'Respuesta': 'OK'}), 201
        else:
            return jsonify({'error': 'Error al crear horario', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@horarios_bp.route('/<int:id>', methods=['PUT'])
@token_required
def update_horario(id):
    try:
        data = request.get_json()
        db = next(get_db())
        repo = HorariosRepositorio(db)
        
        horario_actualizado = Horarios(
            id_horario=id,
            id_medico=data.get('id_medico'),
            dia_semana=data.get('dia_semana'),
            hora_inicio=data.get('hora_inicio'),
            hora_fin=data.get('hora_fin')
        )
        
        if repo.actualizar(horario_actualizado):
            return jsonify({'message': 'Horarios actualizado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al actualizar horario', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@horarios_bp.route('/<int:id>', methods=['DELETE'])
@token_required
def delete_horario(id):
    try:
        db = next(get_db())
        repo = HorariosRepositorio(db)
        
        if repo.eliminar(id):
            return jsonify({'message': 'Horarios eliminado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al eliminar horario', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500
