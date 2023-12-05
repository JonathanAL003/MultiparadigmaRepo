from flask import Flask, flash
from flask_cors import CORS
from database import db
from encriptador import bcrypt
from flask_migrate import Migrate
from config import BaseConfig
from routes.user.user import appuser
from routes.imagenes.imagen import imagesUser
from routes.producto.productos import appProducto
from routes.venta.ventas import appVenta
from routes.proveedor.proveedores import appProveedor
from routes.csv.indexCsv import appcsv 
from routes.pdf.pdf import apppdf
app=Flask(__name__)
app.register_blueprint(appuser)
app.register_blueprint(imagesUser)
app.register_blueprint(appProducto)
app.register_blueprint(appVenta)
app.register_blueprint(appProveedor)
app.register_blueprint(appcsv)
app.register_blueprint(apppdf)
app.config.from_object(BaseConfig)
CORS(app)
bcrypt.init_app(app)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)
