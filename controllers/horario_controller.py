from models.horario import Horario
from extensions import db

class HorarioController:
    
    @staticmethod
    def get_all():
        """GET - Obtener todos los horarios"""
        horarios = Horario.query.all()
        return [horario.to_dict() for horario in horarios]
    
    @staticmethod
    def create(data):
        """POST - Crear un nuevo horario"""
        horario = Horario(
            nombre_horario=data.get('nombre_horario'),
            duracion=data.get('duracion')
        )
        db.session.add(horario)
        db.session.commit()
        return horario.to_dict()