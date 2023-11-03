from flask import Blueprint, request, redirect, render_template, url_for
from app import db

appInicio = Blueprint('appInicio', __name__, template_folder="templates")

@appInicio.route('/')
def Inicio():
    return render_template('inicio.html')