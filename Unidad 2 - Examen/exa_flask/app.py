from flask import Flask
from database import db
from config import BasicConfig
from flask_migrate import Migrate
import logging
from routes.producto.productos import appProducto
from routes.inventario.inventarios import appInventario
from routes.proveedor.proveedores import appProveedor
from routes.sucursal.sucursales import appSucursal
from routes.venta.ventas import appVenta

app= Flask(__name__)
app.register_blueprint(appProducto)
app.register_blueprint(appInventario)
app.register_blueprint(appProveedor)
app.register_blueprint(appSucursal)
app.register_blueprint(appVenta)
app.config.from_object(BasicConfig)
db.init_app(app)
migrate=Migrate()
migrate.init_app(app,db)
logging.basicConfig(level=logging.DEBUG,filename="logs.log")