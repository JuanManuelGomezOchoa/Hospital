import os
from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db

def create_app():
    app = Flask(__name__)
    CORS(app)
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
        print("Base de datos lista")
    
    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)