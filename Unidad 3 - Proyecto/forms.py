from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, SelectField, IntegerField, EmailField, PasswordField, RadioField
from wtforms.validators import DataRequired

class ProductoForm(FlaskForm):
    nombre = StringField("Nombre: ", validators=[DataRequired()])
    descripcion = StringField("Descripción: ")
    precio_kg = FloatField("Precio Por Kg: ", validators=[DataRequired()])
    peso_kg = FloatField("Peso En Kg: ", validators=[DataRequired()])
    marca = StringField("Marca: ")
    enviar = SubmitField("Enviar")

class VentaForm(FlaskForm):
    id_producto = SelectField("Producto: ", validators = [DataRequired()])
    nombre_cliente = StringField("Nombre Del Cliente: ")
    cantidad = IntegerField("Cantidad: ")
    precio_total = FloatField("Precio Total: ")
    encargado = StringField("Encargado: ")
    enviar = SubmitField("Enviar")

class UserForm(FlaskForm):
    email = EmailField("E-Mail: ", validators=[DataRequired()])
    password = PasswordField("Password: ")
    admin = RadioField("Administrador: ", choices=[(True, "Si"), (False, "No")])
    enviar = SubmitField("Enviar")

class ProveedorForm(FlaskForm):
    nombre = StringField("Nombre: ", validators=[DataRequired()])
    rfc = StringField("rfc: ", validators=[DataRequired()])
    telefono = StringField("telefono: ", validators=[DataRequired()])
    direccion = StringField("direccion: ", validators=[DataRequired()])
    enviar = SubmitField("Enviar")