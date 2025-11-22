from flask import Blueprint, request, jsonify
from app import get_db
from app.repositories.facturas import FacturasRepositorio
from app.models.models import Facturas
from app.utils.decorators import token_required

facturas_bp = Blueprint('facturas', __name__)

@facturas_bp.route('/', methods=['GET'])
@token_required
def get_facturas():
    try:
        db = next(get_db())
        repo = FacturasRepositorio(db)
        entidades = repo.leer_todos()
        return jsonify({"Entidades": entidades, "Respuesta": "OK"})
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@facturas_bp.route('/<int:id>', methods=['GET'])
@token_required
def get_factura(id):
    try:
        db = next(get_db())
        repo = FacturasRepositorio(db)
        factura = repo.leer_por_id(id)
        
        if factura:
            factura_dict = {
                'id_factura': factura.id_factura,
                'id_paciente': factura.id_paciente,
                'monto_total': factura.monto_total,
                'estado': factura.estado,
            }
            return jsonify({"Entidad": factura_dict, "Respuesta": "OK"})
        else:
            return jsonify({"Error": "Facturas no encontrado", "Respuesta": "Error"}), 404
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@facturas_bp.route('/', methods=['POST'])
@token_required
def create_factura():
    try:
        data = request.get_json()
        db = next(get_db())
        repo = FacturasRepositorio(db)
        
        nuevo_factura = Facturas(
            id_paciente=data.get('id_paciente'),
            monto_total=data.get('monto_total'),
            estado=data.get('estado')
        )
        
        if repo.crear(nuevo_factura):
            return jsonify({'message': 'Facturas creado exitosamente', 'Respuesta': 'OK'}), 201
        else:
            return jsonify({'error': 'Error al crear factura', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@facturas_bp.route('/<int:id>', methods=['PUT'])
@token_required
def update_factura(id):
    try:
        data = request.get_json()
        db = next(get_db())
        repo = FacturasRepositorio(db)
        
        factura_actualizado = Facturas(
            id_factura=id,
            id_paciente=data.get('id_paciente'),
            monto_total=data.get('monto_total'),
            estado=data.get('estado')
        )
        
        if repo.actualizar(factura_actualizado):
            return jsonify({'message': 'Facturas actualizado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al actualizar factura', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@facturas_bp.route('/<int:id>', methods=['DELETE'])
@token_required
def delete_factura(id):
    try:
        db = next(get_db())
        repo = FacturasRepositorio(db)
        
        if repo.eliminar(id):
            return jsonify({'message': 'Facturas eliminado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al eliminar factura', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500
