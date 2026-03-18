from flask import Blueprint, request, jsonify
from controllers.doctor_controller import DoctorController

doctor_bp = Blueprint('doctor', __name__)

@doctor_bp.route('/', methods=['GET'])
def get_doctores():
    """GET - Listar todos los doctores"""
    doctores = DoctorController.get_all()
    return jsonify({'success': True, 'data': doctores}), 200

@doctor_bp.route('/', methods=['POST'])
def create_doctor():
    """POST - Crear un nuevo doctor"""
    data = request.get_json()
    
    # Validación básica
    if not data.get('nombre') or not data.get('apellidos') or not data.get('especialidad'):
        return jsonify({'success': False, 'error': 'Faltan campos requeridos'}), 400
    
    doctor = DoctorController.create(data)
    return jsonify({'success': True, 'data': doctor}), 200