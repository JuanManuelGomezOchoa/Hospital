from extensions import db

class Doctor(db.Model):
    __tablename__ = 'doctores'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    especialidad = db.Column(db.String(100), nullable=False)
    consultorio = db.Column(db.String(50))
    telefono = db.Column(db.String(20))
    horario_id = db.Column(db.Integer, db.ForeignKey('horarios.id'))
    
    # Relacion 
    horario = db.relationship('Horario', backref='doctores')
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellidos': self.apellidos,
            'especialidad': self.especialidad,
            'consultorio': self.consultorio,
            'telefono': self.telefono,
            'horario_id': self.horario_id,
            'horario_nombre': self.horario.nombre_horario if self.horario else None
        }