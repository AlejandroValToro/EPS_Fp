from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import Config

SessionLocal = None

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    global SessionLocal
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    from app.routes.auth import auth_bp
    from app.routes.pacientes_v2 import pacientes_bp
    from app.routes.especialidades import especialidades_bp
    from app.routes.medicos import medicos_bp
    from app.routes.departamentos import departamentos_bp
    from app.routes.empleados import empleados_bp
    from app.routes.medicamentos import medicamentos_bp
    from app.routes.laboratorios import laboratorios_bp
    from app.routes.citas import citas_bp
    from app.routes.historias_clinicas import historias_clinicas_bp
    from app.routes.consultas import consultas_bp
    from app.routes.recetas import recetas_bp
    from app.routes.examenes_laboratorio import examenes_laboratorio_bp
    from app.routes.facturas import facturas_bp
    from app.routes.detalles_factura import detalles_factura_bp
    from app.routes.horarios import horarios_bp
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(pacientes_bp, url_prefix='/pacientes')
    app.register_blueprint(especialidades_bp, url_prefix='/especialidades')
    app.register_blueprint(medicos_bp, url_prefix='/medicos')
    app.register_blueprint(departamentos_bp, url_prefix='/departamentos')
    app.register_blueprint(empleados_bp, url_prefix='/empleados')
    app.register_blueprint(medicamentos_bp, url_prefix='/medicamentos')
    app.register_blueprint(laboratorios_bp, url_prefix='/laboratorios')
    app.register_blueprint(citas_bp, url_prefix='/citas')
    app.register_blueprint(historias_clinicas_bp, url_prefix='/historias_clinicas')
    app.register_blueprint(consultas_bp, url_prefix='/consultas')
    app.register_blueprint(recetas_bp, url_prefix='/recetas')
    app.register_blueprint(examenes_laboratorio_bp, url_prefix='/examenes_laboratorio')
    app.register_blueprint(facturas_bp, url_prefix='/facturas')
    app.register_blueprint(detalles_factura_bp, url_prefix='/detalles_factura')
    app.register_blueprint(horarios_bp, url_prefix='/horarios')

    @app.route('/')
    def index():
        return "EPS API is running!"

    return app

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
