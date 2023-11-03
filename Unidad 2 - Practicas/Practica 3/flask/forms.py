from flask_wtf import FlaskForm                             #Formulario de flask
from wtforms import StringField, SubmitField, FloatField    #Campos a utilizar
from wtforms.validators import DataRequired                 #Evitar campos vacíos

class EmpleadoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    puesto = StringField('Puesto')
    sueldo = FloatField('Sueldo')
    enviar = SubmitField('Enviar')

class ClienteForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    telefono = StringField('Telefono')
    email = StringField('E-Mail')
    enviar = SubmitField('Enviar')