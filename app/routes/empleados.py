from flask import Blueprint, request, jsonify
from app import get_db
from app.repositories.empleados import EmpleadosRepositorio
from app.models.models import Empleados
from app.utils.decorators import token_required

empleados_bp = Blueprint('empleados', __name__)

@empleados_bp.route('/', methods=['GET'])
@token_required
def get_empleados():
    try:
        db = next(get_db())
        repo = EmpleadosRepositorio(db)
        entidades = repo.leer_todos()
        return jsonify({"Entidades": entidades, "Respuesta": "OK"})
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@empleados_bp.route('/<int:id>', methods=['GET'])
@token_required
def get_empleado(id):
    try:
        db = next(get_db())
        repo = EmpleadosRepositorio(db)
        empleado = repo.leer_por_id(id)
        
        if empleado:
            empleado_dict = {
                'id_empleado': empleado.id_empleado,
                'documento': empleado.documento,
                'nombres': empleado.nombres,
                'apellidos': empleado.apellidos,
                'id_departamento': empleado.id_departamento,
                'cargo': empleado.cargo,
                'fecha_contratacion': empleado.fecha_contratacion,
            }
            return jsonify({"Entidad": empleado_dict, "Respuesta": "OK"})
        else:
            return jsonify({"Error": "Empleados no encontrado", "Respuesta": "Error"}), 404
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@empleados_bp.route('/', methods=['POST'])
@token_required
def create_empleado():
    try:
        data = request.get_json()
        db = next(get_db())
        repo = EmpleadosRepositorio(db)
        
        nuevo_empleado = Empleados(
            documento=data.get('documento'),
            nombres=data.get('nombres'),
            apellidos=data.get('apellidos'),
            id_departamento=data.get('id_departamento'),
            cargo=data.get('cargo'),
            fecha_contratacion=data.get('fecha_contratacion')
        )
        
        if repo.crear(nuevo_empleado):
            return jsonify({'message': 'Empleados creado exitosamente', 'Respuesta': 'OK'}), 201
        else:
            return jsonify({'error': 'Error al crear empleado', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@empleados_bp.route('/<int:id>', methods=['PUT'])
@token_required
def update_empleado(id):
    try:
        data = request.get_json()
        db = next(get_db())
        repo = EmpleadosRepositorio(db)
        
        empleado_actualizado = Empleados(
            id_empleado=id,
            documento=data.get('documento'),
            nombres=data.get('nombres'),
            apellidos=data.get('apellidos'),
            id_departamento=data.get('id_departamento'),
            cargo=data.get('cargo'),
            fecha_contratacion=data.get('fecha_contratacion')
        )
        
        if repo.actualizar(empleado_actualizado):
            return jsonify({'message': 'Empleados actualizado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al actualizar empleado', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@empleados_bp.route('/<int:id>', methods=['DELETE'])
@token_required
def delete_empleado(id):
    try:
        db = next(get_db())
        repo = EmpleadosRepositorio(db)
        
        if repo.eliminar(id):
            return jsonify({'message': 'Empleados eliminado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al eliminar empleado', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500
