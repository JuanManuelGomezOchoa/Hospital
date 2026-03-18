from flask import Blueprint, request, jsonify
from controllers.horario_controller import HorarioController

horario_bp = Blueprint('horario', __name__)

@horario_bp.route('/', methods=['GET'])
def get_horarios():
    """GET - Listar todos los horarios"""
    horarios = HorarioController.get_all()
    return jsonify({'success': True, 'data': horarios}), 200

@horario_bp.route('/', methods=['POST'])
def create_horario():
    """POST - Crear un nuevo horario"""
    data = request.get_json()
    
    if not data.get('nombre_horario') or not data.get('duracion'):
        return jsonify({'success': False, 'error': 'Nombre y duración son requeridos'}), 400
    
    horario = HorarioController.create(data)
    return jsonify({'success': True, 'data': horario}), 200