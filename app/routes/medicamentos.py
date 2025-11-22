from flask import Blueprint, request, jsonify
from app import get_db
from app.repositories.medicamentos import MedicamentosRepositorio
from app.models.models import Medicamentos
from app.utils.decorators import token_required

medicamentos_bp = Blueprint('medicamentos', __name__)

@medicamentos_bp.route('/', methods=['GET'])
@token_required
def get_medicamentos():
    try:
        db = next(get_db())
        repo = MedicamentosRepositorio(db)
        entidades = repo.leer_todos()
        return jsonify({"Entidades": entidades, "Respuesta": "OK"})
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@medicamentos_bp.route('/<int:id>', methods=['GET'])
@token_required
def get_medicamento(id):
    try:
        db = next(get_db())
        repo = MedicamentosRepositorio(db)
        medicamento = repo.leer_por_id(id)
        
        if medicamento:
            medicamento_dict = {
                'id_medicamento': medicamento.id_medicamento,
                'nombre': medicamento.nombre,
                'descripcion': medicamento.descripcion,
                'fabricante': medicamento.fabricante,
                'stock': medicamento.stock,
            }
            return jsonify({"Entidad": medicamento_dict, "Respuesta": "OK"})
        else:
            return jsonify({"Error": "Medicamentos no encontrado", "Respuesta": "Error"}), 404
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@medicamentos_bp.route('/', methods=['POST'])
@token_required
def create_medicamento():
    try:
        data = request.get_json()
        db = next(get_db())
        repo = MedicamentosRepositorio(db)
        
        nuevo_medicamento = Medicamentos(
            nombre=data.get('nombre'),
            descripcion=data.get('descripcion'),
            fabricante=data.get('fabricante'),
            stock=data.get('stock')
        )
        
        if repo.crear(nuevo_medicamento):
            return jsonify({'message': 'Medicamentos creado exitosamente', 'Respuesta': 'OK'}), 201
        else:
            return jsonify({'error': 'Error al crear medicamento', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@medicamentos_bp.route('/<int:id>', methods=['PUT'])
@token_required
def update_medicamento(id):
    try:
        data = request.get_json()
        db = next(get_db())
        repo = MedicamentosRepositorio(db)
        
        medicamento_actualizado = Medicamentos(
            id_medicamento=id,
            nombre=data.get('nombre'),
            descripcion=data.get('descripcion'),
            fabricante=data.get('fabricante'),
            stock=data.get('stock')
        )
        
        if repo.actualizar(medicamento_actualizado):
            return jsonify({'message': 'Medicamentos actualizado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al actualizar medicamento', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@medicamentos_bp.route('/<int:id>', methods=['DELETE'])
@token_required
def delete_medicamento(id):
    try:
        db = next(get_db())
        repo = MedicamentosRepositorio(db)
        
        if repo.eliminar(id):
            return jsonify({'message': 'Medicamentos eliminado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al eliminar medicamento', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500
