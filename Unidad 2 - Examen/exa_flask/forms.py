from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired

class ProductoForm(FlaskForm):
    nombre_pr = StringField('Nombre del Producto', validators=[DataRequired()])
    categoria = StringField('Categoría', validators=[DataRequired()])
    precio = FloatField('Precio', validators=[DataRequired()])
    peso_kg = FloatField('Peso en kg', validators=[DataRequired()])
    enviar = SubmitField("Enviar")
