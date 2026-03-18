from models.doctor import Doctor
from extensions import db

class DoctorController:
    
    @staticmethod
    def get_all():
        """GET - Obtener todos los doctores"""
        doctores = Doctor.query.all()
        return [doctor.to_dict() for doctor in doctores]
    
    @staticmethod
    def create(data):
        """POST - Crear un nuevo doctor"""
        doctor = Doctor(
            nombre=data.get('nombre'),
            apellidos=data.get('apellidos'),
            especialidad=data.get('especialidad'),
            consultorio=data.get('consultorio'),
            telefono=data.get('telefono'),
            horario_id=data.get('horario_id')
        )
        db.session.add(doctor)
        db.session.commit()
        return doctor.to_dict()