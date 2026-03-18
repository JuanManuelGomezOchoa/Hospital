from flask import Flask
from config import Config
from extensions import db  # Cambia esta línea

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    from routes.doctor_routes import doctor_bp
    from routes.horario_routes import horario_bp
    
    app.register_blueprint(doctor_bp, url_prefix='/api/doctores')
    app.register_blueprint(horario_bp, url_prefix='/api/horarios')
    
    @app.route('/')
    def home():
        return {"mensaje": "API funcionando", "status": "ok"}
    
    with app.app_context():
        db.create_all()
        print("✅ Base de datos lista")
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)