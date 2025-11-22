from flask import Blueprint, request, jsonify
from app import get_db
from app.repositories.examenes_laboratorio import ExamenesLaboratorioRepositorio
from app.models.models import ExamenesLaboratorio
from app.utils.decorators import token_required
from datetime import datetime

examenes_laboratorio_bp = Blueprint('examenes_laboratorio', __name__)

@examenes_laboratorio_bp.route('/', methods=['GET'])
@token_required
def get_examenes():
    try:
        db = next(get_db())
        repo = ExamenesLaboratorioRepositorio(db)
        entidades = repo.leer_todos()
        return jsonify({"Entidades": entidades, "Respuesta": "OK"})
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@examenes_laboratorio_bp.route('/<int:id>', methods=['GET'])
@token_required
def get_examen(id):
    try:
        db = next(get_db())
        repo = ExamenesLaboratorioRepositorio(db)
        examen = repo.leer_por_id(id)
        
        if examen:
            examen_dict = {
                'id_examen': examen.id_examen,
                'id_consulta': examen.id_consulta,
                'id_laboratorio': examen.id_laboratorio,
                'tipo_examen': examen.tipo_examen,
                'resultado': examen.resultado,
            }
            return jsonify({"Entidad": examen_dict, "Respuesta": "OK"})
        else:
            return jsonify({"Error": "ExamenesLaboratorio no encontrado", "Respuesta": "Error"}), 404
    except Exception as ex:
        return jsonify({"Error": str(ex), "Respuesta": "Error"}), 500

@examenes_laboratorio_bp.route('/', methods=['POST'])
@token_required
def create_examen():
    try:
        data = request.get_json()
        db = next(get_db())
        repo = ExamenesLaboratorioRepositorio(db)
        
        nuevo_examen = ExamenesLaboratorio(
            id_consulta=data.get('id_consulta'),
            id_laboratorio=data.get('id_laboratorio'),
            tipo_examen=data.get('tipo_examen'),
            resultado=data.get('resultado')
        )
        
        if repo.crear(nuevo_examen):
            return jsonify({'message': 'ExamenesLaboratorio creado exitosamente', 'Respuesta': 'OK'}), 201
        else:
            return jsonify({'error': 'Error al crear examen', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@examenes_laboratorio_bp.route('/<int:id>', methods=['PUT'])
@token_required
def update_examen(id):
    try:
        data = request.get_json()
        db = next(get_db())
        repo = ExamenesLaboratorioRepositorio(db)
        
        examen_actualizado = ExamenesLaboratorio(
            id_examen=id,
            id_consulta=data.get('id_consulta'),
            id_laboratorio=data.get('id_laboratorio'),
            tipo_examen=data.get('tipo_examen'),
            resultado=data.get('resultado')
        )
        
        if repo.actualizar(examen_actualizado):
            return jsonify({'message': 'ExamenesLaboratorio actualizado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al actualizar examen', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500

@examenes_laboratorio_bp.route('/<int:id>', methods=['DELETE'])
@token_required
def delete_examen(id):
    try:
        db = next(get_db())
        repo = ExamenesLaboratorioRepositorio(db)
        
        if repo.eliminar(id):
            return jsonify({'message': 'ExamenesLaboratorio eliminado exitosamente', 'Respuesta': 'OK'}), 200
        else:
            return jsonify({'error': 'Error al eliminar examen', 'Respuesta': 'Error'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex), 'Respuesta': 'Error'}), 500
