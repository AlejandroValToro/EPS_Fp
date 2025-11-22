from flask import Blueprint, request, jsonify
from app import get_db
from app.repositories.medicos import MedicosRepositorio
from app.models.models import Medicos
from app.utils.decorators import token_required

medicos_bp = Blueprint('medicos', __name__)

@medicos_bp.route('/', methods=['GET'])
@token_required
def get_medicos():
    try:
        db = next(get_db())
        repo = MedicosRepositorio(db)
        entidades = repo.leer_todos()
        return jsonify({"Entidades": entidades, "Respuesta": "OK"})
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@medicos_bp.route('/<int:id>', methods=['GET'])
@token_required
def get_medico(id):
    try:
        db = next(get_db())
        repo = MedicosRepositorio(db)
        medico = repo.leer_por_id(id)
        
        if medico:
            medico_dict = {
                'id_medico': medico.id_medico,
                'documento': medico.documento,
                'nombres': medico.nombres,
                'apellidos': medico.apellidos,
                'id_especialidad': medico.id_especialidad,
                'telefono': medico.telefono,
                'email': medico.email,
                'tarjeta_profesional': medico.tarjeta_profesional
            }
            return jsonify({"Entidad": medico_dict, "Respuesta": "OK"})
        else:
            return jsonify({"Error": "Médico no encontrado", "Respuesta": "Error"}), 404
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@medicos_bp.route('/', methods=['POST'])
@token_required
def create_medico():
    try:
        data = request.get_json()
        db = next(get_db())
        repo = MedicosRepositorio(db)
        
        nuevo_medico = Medicos(
            documento=data.get('documento'),
            nombres=data.get('nombres'),
            apellidos=data.get('apellidos'),
            id_especialidad=data.get('id_especialidad'),
            telefono=data.get('telefono'),
            email=data.get('email'),
            tarjeta_profesional=data.get('tarjeta_profesional')
        )
        
        if repo.crear(nuevo_medico):
            return jsonify({'message': 'Médico creado exitosamente', 'Respuesta': 'OK'}), 201
        else:
            return jsonify({'error': 'Error al crear médico', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@medicos_bp.route('/<int:id>', methods=['PUT'])
@token_required
def update_medico(id):
    try:
        data = request.get_json()
        db = next(get_db())
        repo = MedicosRepositorio(db)
        
        medico_actualizado = Medicos(
            id_medico=id,
            documento=data.get('documento'),
            nombres=data.get('nombres'),
            apellidos=data.get('apellidos'),
            id_especialidad=data.get('id_especialidad'),
            telefono=data.get('telefono'),
            email=data.get('email'),
            tarjeta_profesional=data.get('tarjeta_profesional')
        )
        
        if repo.actualizar(medico_actualizado):
            return jsonify({'message': 'Médico actualizado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al actualizar médico', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@medicos_bp.route('/<int:id>', methods=['DELETE'])
@token_required
def delete_medico(id):
    try:
        db = next(get_db())
        repo = MedicosRepositorio(db)
        
        if repo.eliminar(id):
            return jsonify({'message': 'Médico eliminado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al eliminar médico', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500
