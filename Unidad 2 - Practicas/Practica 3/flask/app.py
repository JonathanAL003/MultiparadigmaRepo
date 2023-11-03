#Jafet Sena 20100264 - Práctica 3 Flask
from flask import Flask
from database import db
from config import BasicConfig
from routes.inicio.inicios import appInicio
from routes.empleado.empleados import appEmpleado
from routes.cliente.clientes import appCliente
from routes.departamento.departamentos import appDepartamento
from flask_migrate import Migrate
import logging
app = Flask(__name__)
app.register_blueprint(appInicio)
app.register_blueprint(appEmpleado)
app.register_blueprint(appCliente)
app.register_blueprint(appDepartamento)
app.config.from_object(BasicConfig)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app, db)
logging.basicConfig(level=logging.DEBUG, filename="logs.log")