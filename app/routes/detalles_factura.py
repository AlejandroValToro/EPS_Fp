from flask import Blueprint, request, jsonify
from app import get_db
from app.repositories.detalles_factura import DetallesFacturaRepositorio
from app.models.models import DetallesFactura
from app.utils.decorators import token_required

detalles_factura_bp = Blueprint('detalles_factura', __name__)

@detalles_factura_bp.route('/', methods=['GET'])
@token_required
def get_detalles():
    try:
        db = next(get_db())
        repo = DetallesFacturaRepositorio(db)
        entidades = repo.leer_todos()
        return jsonify({"Entidades": entidades, "Respuesta": "OK"})
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@detalles_factura_bp.route('/<int:id>', methods=['GET'])
@token_required
def get_detalle(id):
    try:
        db = next(get_db())
        repo = DetallesFacturaRepositorio(db)
        detalle = repo.leer_por_id(id)
        
        if detalle:
            detalle_dict = {
                'id_detalle': detalle.id_detalle,
                'id_factura': detalle.id_factura,
                'concepto': detalle.concepto,
                'cantidad': detalle.cantidad,
                'precio_unitario': detalle.precio_unitario,
                'subtotal': detalle.subtotal,
            }
            return jsonify({"Entidad": detalle_dict, "Respuesta": "OK"})
        else:
            return jsonify({"Error": "DetallesFactura no encontrado", "Respuesta": "Error"}), 404
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@detalles_factura_bp.route('/', methods=['POST'])
@token_required
def create_detalle():
    try:
        data = request.get_json()
        db = next(get_db())
        repo = DetallesFacturaRepositorio(db)
        
        nuevo_detalle = DetallesFactura(
            id_factura=data.get('id_factura'),
            concepto=data.get('concepto'),
            cantidad=data.get('cantidad'),
            precio_unitario=data.get('precio_unitario'),
            subtotal=data.get('subtotal')
        )
        
        if repo.crear(nuevo_detalle):
            return jsonify({'message': 'DetallesFactura creado exitosamente', 'Respuesta': 'OK'}), 201
        else:
            return jsonify({'error': 'Error al crear detalle', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@detalles_factura_bp.route('/<int:id>', methods=['PUT'])
@token_required
def update_detalle(id):
    try:
        data = request.get_json()
        db = next(get_db())
        repo = DetallesFacturaRepositorio(db)
        
        detalle_actualizado = DetallesFactura(
            id_detalle=id,
            id_factura=data.get('id_factura'),
            concepto=data.get('concepto'),
            cantidad=data.get('cantidad'),
            precio_unitario=data.get('precio_unitario'),
            subtotal=data.get('subtotal')
        )
        
        if repo.actualizar(detalle_actualizado):
            return jsonify({'message': 'DetallesFactura actualizado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al actualizar detalle', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@detalles_factura_bp.route('/<int:id>', methods=['DELETE'])
@token_required
def delete_detalle(id):
    try:
        db = next(get_db())
        repo = DetallesFacturaRepositorio(db)
        
        if repo.eliminar(id):
            return jsonify({'message': 'DetallesFactura eliminado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al eliminar detalle', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500
