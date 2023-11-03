#4. Utilizar al menos 3 entidades
from app import db

class Departamento(db.Model):
    id_departamento = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(60), nullable=False)
    cant_empleados = db.Column(db.Integer)

class Empleado(db.Model):
    id_empleado = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(60), nullable=False)
    apellido = db.Column(db.String(60), nullable=False)
    puesto = db.Column(db.String(60))
    sueldo = db.Column(db.Float)

class Cliente(db.Model):
    id_cliente = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(60), nullable=False)
    apellido = db.Column(db.String(60), nullable=False)
    telefono = db.Column(db.String(10))
    email = db.Column(db.String(120))