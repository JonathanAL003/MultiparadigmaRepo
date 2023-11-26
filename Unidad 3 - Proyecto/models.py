import jwt
import datetime
from config import BaseConfig
from app import db,bcrypt

class User(db.Model):
    __tablename__="users"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    email=db.Column(db.String(255),unique=True,nullable=False)
    password=db.Column(db.String(255),nullable=False)
    registered_on=db.Column(db.DateTime,nullable=False)
    admin=db.Column(db.Boolean,nullable=False,default=False)

    def __init__(self,email,password,admin=False) -> None:
        self.email=email
        self.password=bcrypt.generate_password_hash(
            password,BaseConfig.BCRYPT_LOG_ROUNDS
        ).decode()

        self.registered_on=datetime.datetime.now()
        self.admin=admin
        
    def encodePassword(self, password):
        self.password = bcrypt.generate_password_hash(password, BaseConfig.BCRYPT_LOG_ROUNDS).decode()

    def encode_auth_token(self,user_id):
        try:
            print('USER',user_id)
            payload={
                'exp':datetime.datetime.utcnow()+datetime.timedelta(hours=5),
                'iat':datetime.datetime.utcnow(),
                'sub':user_id
            }
            print("PAYLOAD",payload)
            return jwt.encode(
                payload,
                BaseConfig.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            print("EXCEPTION")
            print(e)
            return e
        
    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token,BaseConfig.SECRET_KEY,algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError as e:
            return 'Signature Expired Please log in again'

        except jwt.InvalidTokenError as e:
            return 'Invalid token'

class Images(db.Model):
    __tablename__='user_images'
    id_images = db.Column(db.Integer,primary_key=True)
    type = db.Column(db.String(128),nullable=False)
    data = db.Column(db.LargeBinary,nullable=False)
    rendered_data=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    region=db.relationship('User',backref='users')

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nombre = db.Column(db.String(80), nullable = False)
    descripcion = db.Column(db.String(250))
    precio_kg = db.Column(db.Float)
    peso_kg = db.Column(db.Float)
    marca = db.Column(db.String(60))

class Venta(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id'))
    nombre_cliente = db.Column(db.String(250))
    cantidad = db.Column(db.Integer)
    precio_total = db.Column(db.Float)
    rel_prod=db.relationship('Producto',backref='producto')

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nombre = db.Column(db.String(120), nullable = False)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(250))