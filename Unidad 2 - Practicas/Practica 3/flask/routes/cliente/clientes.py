from flask import Blueprint, request, redirect, render_template, url_for, jsonify
from models import Cliente
from forms import ClienteForm
from app import db

appCliente = Blueprint('appCliente', __name__, template_folder='templates')

@appCliente.route('/cliente/index')
def Inicio():
    listClientes = Cliente.query.all()
    return render_template('clienteIndex.html', clientes = listClientes)

@appCliente.route('/cliente/agregar', methods = ['GET', 'POST'])
def Agregar():
    cliente = Cliente()
    newCliente = ClienteForm(obj = cliente)
    if request.method == 'POST':
        if newCliente.validate_on_submit():
            newCliente.populate_obj(cliente)
            db.session.add(cliente)
            db.session.commit()
            return RedirectIndex()
    return render_template('clienteAgregar.html', newCliente = newCliente)

@appCliente.route('/cliente/editar/<int:id>',methods=["GET", "POST"])
def Editar(id):
    cliente = Cliente.query.get_or_404(id)
    editCliente = ClienteForm(obj = cliente)
    if request.method == 'POST':
        if editCliente.validate_on_submit():
            editCliente.populate_obj(cliente)
            db.session.commit()
            return RedirectIndex()
    return render_template('clienteEditar.html', editCliente = editCliente)

@appCliente.route('/cliente/eliminar/<int:id>')
def Eliminar(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return RedirectIndex()

#Rutas para peticiones HTTP (JSONs)
@appCliente.route('/cliente/json/index')
def InicioJson():
    try:
        clientes = Cliente.query.all()
        listCliente = []
        for c in clientes:
            cliente = {}                               #Diccionario vacío
            cliente["id_cliente"] = c.id_cliente       
            cliente["nombre"] = c.nombre               #Llena los campos para parsearlo a JSON
            cliente["apellido"] = c.apellido
            cliente["telefono"] = c.telefono
            cliente["email"] = c.email
            listCliente.append(cliente)
        return jsonify({'clientes':listCliente})
    except Exception as ex:
        return jsonify({"status" : 400, "mensaje" : ex})
    
@appCliente.route('/cliente/json/agregar', methods = ["POST"])
def AgregarJson():
    try:
        if request.method == "POST":
            cliente = Cliente()
            json = request.get_json()
            cliente.nombre = json['nombre']
            cliente.apellido = json['apellido']
            cliente.telefono = json['telefono']
            cliente.email = json['email']
            db.session.add(cliente)
            db.session.commit()
            return jsonify({'status':200, 'mensaje':'Cliente agregado por petición HTTP'})
    except Exception as ex:
        return jsonify({'status':400, 'mensaje':ex})
    
@appCliente.route('/cliente/json/editar', methods = ["POST"])
def EditarJson():
    try:
        if request.method == "POST":
            json = request.get_json()
            cliente = Cliente.query.get_or_404(json['id_cliente'])
            cliente.nombre = json['nombre']
            cliente.apellido = json['apellido']
            cliente.telefono = json['telefono']
            cliente.email = json['email']
            db.session.commit()
            return jsonify({'status':200, 'mensaje':'Cliente editado por petición HTTP'})
    except Exception as ex:
        return jsonify({'status':400, 'mensaje':ex})
    
@appCliente.route('/cliente/json/eliminar', methods = ["POST"])
def EliminarJson():
    try:
        json = request.get_json()
        cliente = Cliente.query.get_or_404(json['id_cliente'])
        db.session.delete(cliente)
        db.session.commit()
        return jsonify({"status":200, "mensaje":f"Cliente {json['id_cliente']} eliminado por peticion HTTP"})
    except Exception as ex:
        return jsonify({'status':400, 'mensaje':ex})
    
def RedirectIndex():
    return redirect(url_for('appCliente.Inicio'))