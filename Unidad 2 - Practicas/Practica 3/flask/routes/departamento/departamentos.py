from flask import Blueprint, request, redirect, render_template, url_for, jsonify
from models import Departamento
from app import db

appDepartamento = Blueprint('appDepartamento', __name__, template_folder='templates')

@appDepartamento.route('/departamento/json/index')
def Inicio():
    try:
        json = request.get_json()
        listDepa = []
        departamentos = Departamento.query.all()
        for dep in departamentos:
            departamento = {}
            departamento['id_departamento'] = dep.id_departamento
            departamento['nombre'] = dep.nombre
            departamento['cant_empleados'] = dep.cant_empleados
            listDepa.append(departamento)
        return jsonify({'departamentos' : listDepa})
    except Exception as ex:
        return jsonify({'status':400, 'mensaje':ex})
    
@appDepartamento.route('/departamento/json/agregar', methods=["POST","GET"])
def Agregar():
    try:
        if request.method == "POST":
            json = request.get_json()
            depa = Departamento()
            depa.nombre = json['nombre']
            depa.cant_empleados = json['cant_empleados']
            db.session.add(depa)
            db.session.commit()
            return jsonify({'status':200, 'mensaje':'Departamento agregado por peticion HTTP'})
    except Exception as ex:
        return jsonify({'status':400, 'mensaje':ex})
    
@appDepartamento.route('/departamento/json/editar', methods=["POST","GET"])
def Editar():
    try:
        if request.method == "POST":
            json = request.get_json()
            depa = Departamento.query.get_or_404(json['id_departamento'])
            depa.nombre = json['nombre']
            depa.cant_empleados = json['cant_empleados']
            db.session.commit()
            return jsonify({'status':200, 'mensaje':'Departamento editado por peticion HTTP'})
    except Exception as ex:
        return jsonify({'status':400, 'mensaje':ex})
@appDepartamento.route('/departamento/json/eliminar', methods=["POST","GET"])
def Eliminar():
    try:
        if request.method == "POST":
            json = request.get_json()
            depa = Departamento.query.get_or_404(json['id_departamento'])
            db.session.delete(depa)
            db.session.commit()
            return jsonify({'status':200, 'mensaje':f'Departamento {json["id_departamento"]} eliminado por peticion HTTP'})
    except Exception as ex:
        return jsonify({'status':400, 'mensaje':ex})