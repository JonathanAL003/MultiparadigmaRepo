#Utilizar al menos 5 entidades, con 4 campos
from app import db

class Proveedor(db.Model):
    id_prov = db.Column(db.Integer, primary_key=True)
    nombre_pv = db.Column(db.String(250))
    telefono_pv = db.Column(db.String(20))
    direccion_pv = db.Column(db.String(250))

class Producto(db.Model):
    id_prod = db.Column(db.Integer, primary_key=True)
    nombre_pr = db.Column(db.String(255))
    categoria = db.Column(db.String(100))
    precio = db.Column(db.Float)
    peso_kg = db.Column(db.Float)

class Sucursal(db.Model):
    id_suc = db.Column(db.Integer, primary_key=True)
    nombre_s = db.Column(db.String(250))
    direccion_s = db.Column(db.String(250))
    telefono_s = db.Column(db.String(20))
    horario = db.Column(db.String(100))

class Inventario(db.Model):
    id_inv = db.Column(db.Integer, primary_key=True)
    stock = db.Column(db.Integer)
    precio_compra = db.Column(db.Float)
    fecha_reab = db.Column(db.String(20))
    niv_min = db.Column(db.Integer)

class Venta(db.Model):
    id_venta = db.Column(db.Integer, primary_key=True)
    fecha_venta = db.Column(db.String(20))
    cant_prod = db.Column(db.Integer)
    total_venta = db.Column(db.Float)
    metodo_pago = db.Column(db.String(50))
