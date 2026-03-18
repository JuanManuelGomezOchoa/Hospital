from extensions import db
class Horario(db.Model):
    __tablename__ = 'horarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre_horario = db.Column(db.String(100), nullable=False)
    duracion = db.Column(db.String(50), nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre_horario': self.nombre_horario,
            'duracion': self.duracion
        }