from flask import Blueprint, request, jsonify
from app import get_db
from app.repositories.departamentos import DepartamentosRepositorio
from app.models.models import Departamentos
from app.utils.decorators import token_required

departamentos_bp = Blueprint('departamentos', __name__)

@departamentos_bp.route('/', methods=['GET'])
@token_required
def get_departamentos():
    try:
        db = next(get_db())
        repo = DepartamentosRepositorio(db)
        entidades = repo.leer_todos()
        return jsonify({"Entidades": entidades, "Respuesta": "OK"})
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@departamentos_bp.route('/<int:id>', methods=['GET'])
@token_required
def get_departamento(id):
    try:
        db = next(get_db())
        repo = DepartamentosRepositorio(db)
        departamento = repo.leer_por_id(id)
        
        if departamento:
            dept_dict = {
                'id_departamento': departamento.id_departamento,
                'nombre': departamento.nombre,
                'descripcion': departamento.descripcion
            }
            return jsonify({"Entidad": dept_dict, "Respuesta": "OK"})
        else:
            return jsonify({"Error": "Departamento no encontrado", "Respuesta": "Error"}), 404
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@departamentos_bp.route('/', methods=['POST'])
@token_required
def create_departamento():
    try:
        data = request.get_json()
        db = next(get_db())
        repo = DepartamentosRepositorio(db)
        
        nuevo_departamento = Departamentos(
            nombre=data.get('nombre'),
            descripcion=data.get('descripcion')
        )
        
        if repo.crear(nuevo_departamento):
            return jsonify({'message': 'Departamento creado exitosamente', 'Respuesta': 'OK'}), 201
        else:
            return jsonify({'error': 'Error al crear departamento', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@departamentos_bp.route('/<int:id>', methods=['PUT'])
@token_required
def update_departamento(id):
    try:
        data = request.get_json()
        db = next(get_db())
        repo = DepartamentosRepositorio(db)
        
        departamento_actualizado = Departamentos(
            id_departamento=id,
            nombre=data.get('nombre'),
            descripcion=data.get('descripcion')
        )
        
        if repo.actualizar(departamento_actualizado):
            return jsonify({'message': 'Departamento actualizado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al actualizar departamento', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@departamentos_bp.route('/<int:id>', methods=['DELETE'])
@token_required
def delete_departamento(id):
    try:
        db = next(get_db())
        repo = DepartamentosRepositorio(db)
        
        if repo.eliminar(id):
            return jsonify({'message': 'Departamento eliminado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al eliminar departamento', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500
