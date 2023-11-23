from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, SelectField, IntegerField
from wtforms.validators import DataRequired
from models import Producto
class ProductoForm(FlaskForm):
    nombre = StringField("Nombre: ", validators=[DataRequired()])
    descripcion = StringField("Descripción: ")
    precio_kg = FloatField("Precio Por Kg: ", validators=[DataRequired()])
    peso_kg = FloatField("Peso En Kg: ", validators=[DataRequired()])
    marca = StringField("Marca: ")
    enviar = SubmitField("Enviar")

class VentaForm(FlaskForm):
    id_producto = SelectField("Producto: ", Producto.query.all(), validate_choice = True, validators=[DataRequired()])
    nombre_cliente = StringField("Nombre Del Cliente: ")
    cantidad = IntegerField("Cantidad: ")
    precio_total = FloatField("Precio Total: ")
    enviar = SubmitField("Enviar")