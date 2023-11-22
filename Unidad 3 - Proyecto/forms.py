from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired

class ProductoForm(FlaskForm):
    nombre = StringField("Nombre: ", validators=[DataRequired()])
    descripcion = StringField("Descripción: ")
    precio_kg = FloatField("Precio Por Kg: ", validators=[DataRequired()])
    peso_kg = FloatField("Peso En Kg: ", validators=[DataRequired()])
    marca = StringField("Marca: ")
    enviar = SubmitField("Enviar")