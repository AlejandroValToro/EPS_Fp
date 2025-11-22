from flask import Blueprint, request, jsonify
from app import get_db
from app.repositories.pacientes_v2 import PacientesRepositorioModified as PacientesRepositorio
from app.models.models import Pacientes
from app.utils.decorators import token_required
from datetime import datetime

pacientes_bp = Blueprint('pacientes', __name__)

@pacientes_bp.route('/', methods=['GET'])
@token_required
def get_pacientes():
    respuesta = {}
    try:
        db = next(get_db())
        repo = PacientesRepositorio(db)
        entidades = repo.leer_todos()
        
        respuesta["Entidades"] = entidades
        respuesta["Respuesta"] = "OK"
        return jsonify(respuesta)
    except Exception as ex:
        respuesta["Error"] = str(ex)
        respuesta["Respuesta"] = "Error"
        return jsonify(respuesta), 500

@pacientes_bp.route('/<int:id>', methods=['GET'])
@token_required
def get_paciente(id):
    respuesta = {}
    try:
        db = next(get_db())
        repo = PacientesRepositorio(db)
        paciente = repo.leer_por_id(id)
        
        if paciente:
            paciente_dict = {
                'id_paciente': paciente.id_paciente,
                'documento': paciente.documento,
                'tipo_documento': paciente.tipo_documento,
                'nombres': paciente.nombres,
                'apellidos': paciente.apellidos,
                'fecha_nacimiento': paciente.fecha_nacimiento.isoformat() if paciente.fecha_nacimiento else None,
                'genero': paciente.genero,
                'direccion': paciente.direccion,
                'telefono': paciente.telefono,
                'email': paciente.email
            }
            respuesta["Entidad"] = paciente_dict
            respuesta["Respuesta"] = "OK"
            return jsonify(respuesta)
        else:
            respuesta["Error"] = "Paciente no encontrado"
            respuesta["Respuesta"] = "Error"
            return jsonify(respuesta), 404
    except Exception as ex:
        respuesta["Error"] = str(ex)
        respuesta["Respuesta"] = "Error"
        return jsonify(respuesta), 500

@pacientes_bp.route('/', methods=['POST'])
@token_required
def create_paciente():
    try:
        data = request.get_json()
        db = next(get_db())
        repo = PacientesRepositorio(db)
        
        nuevo_paciente = Pacientes(
            documento=data.get('documento'),
            tipo_documento=data.get('tipo_documento'),
            nombres=data.get('nombres'),
            apellidos=data.get('apellidos'),
            fecha_nacimiento=datetime.strptime(data.get('fecha_nacimiento'), '%Y-%m-%d').date(),
            genero=data.get('genero'),
            direccion=data.get('direccion'),
            telefono=data.get('telefono'),
            email=data.get('email')
        )
        
        if repo.crear(nuevo_paciente):
            return jsonify({'message': 'Paciente creado exitosamente', 'Respuesta': 'OK'}), 201
        else:
            return jsonify({'error': 'Error al crear paciente', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@pacientes_bp.route('/<int:id>', methods=['PUT'])
@token_required
def update_paciente(id):
    try:
        data = request.get_json()
        db = next(get_db())
        repo = PacientesRepositorio(db)
        
        paciente_actualizado = Pacientes(
            id_paciente=id,
            documento=data.get('documento'),
            tipo_documento=data.get('tipo_documento'),
            nombres=data.get('nombres'),
            apellidos=data.get('apellidos'),
            fecha_nacimiento=datetime.strptime(data.get('fecha_nacimiento'), '%Y-%m-%d').date(),
            genero=data.get('genero'),
            direccion=data.get('direccion'),
            telefono=data.get('telefono'),
            email=data.get('email')
        )
        
        if repo.actualizar(paciente_actualizado):
            return jsonify({'message': 'Paciente actualizado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al actualizar paciente', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@pacientes_bp.route('/<int:id>', methods=['DELETE'])
@token_required
def delete_paciente(id):
    try:
        db = next(get_db())
        repo = PacientesRepositorio(db)
        
        if repo.eliminar(id):
            return jsonify({'message': 'Paciente eliminado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al eliminar paciente', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500
