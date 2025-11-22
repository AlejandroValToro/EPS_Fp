from flask import Blueprint, request, jsonify
from app import get_db
from app.repositories.laboratorios import LaboratoriosRepositorio
from app.models.models import Laboratorios
from app.utils.decorators import token_required

laboratorios_bp = Blueprint('laboratorios', __name__)

@laboratorios_bp.route('/', methods=['GET'])
@token_required
def get_laboratorios():
    try:
        db = next(get_db())
        repo = LaboratoriosRepositorio(db)
        entidades = repo.leer_todos()
        return jsonify({"Entidades": entidades, "Respuesta": "OK"})
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@laboratorios_bp.route('/<int:id>', methods=['GET'])
@token_required
def get_laboratorio(id):
    try:
        db = next(get_db())
        repo = LaboratoriosRepositorio(db)
        laboratorio = repo.leer_por_id(id)
        
        if laboratorio:
            laboratorio_dict = {
                'id_laboratorio': laboratorio.id_laboratorio,
                'nombre': laboratorio.nombre,
                'direccion': laboratorio.direccion,
                'telefono': laboratorio.telefono,
            }
            return jsonify({"Entidad": laboratorio_dict, "Respuesta": "OK"})
        else:
            return jsonify({"Error": "Laboratorios no encontrado", "Respuesta": "Error"}), 404
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@laboratorios_bp.route('/', methods=['POST'])
@token_required
def create_laboratorio():
    try:
        data = request.get_json()
        db = next(get_db())
        repo = LaboratoriosRepositorio(db)
        
        nuevo_laboratorio = Laboratorios(
            nombre=data.get('nombre'),
            direccion=data.get('direccion'),
            telefono=data.get('telefono')
        )
        
        if repo.crear(nuevo_laboratorio):
            return jsonify({'message': 'Laboratorios creado exitosamente', 'Respuesta': 'OK'}), 201
        else:
            return jsonify({'error': 'Error al crear laboratorio', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@laboratorios_bp.route('/<int:id>', methods=['PUT'])
@token_required
def update_laboratorio(id):
    try:
        data = request.get_json()
        db = next(get_db())
        repo = LaboratoriosRepositorio(db)
        
        laboratorio_actualizado = Laboratorios(
            id_laboratorio=id,
            nombre=data.get('nombre'),
            direccion=data.get('direccion'),
            telefono=data.get('telefono')
        )
        
        if repo.actualizar(laboratorio_actualizado):
            return jsonify({'message': 'Laboratorios actualizado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al actualizar laboratorio', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@laboratorios_bp.route('/<int:id>', methods=['DELETE'])
@token_required
def delete_laboratorio(id):
    try:
        db = next(get_db())
        repo = LaboratoriosRepositorio(db)
        
        if repo.eliminar(id):
            return jsonify({'message': 'Laboratorios eliminado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al eliminar laboratorio', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500
