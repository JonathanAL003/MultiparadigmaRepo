from flask import Blueprint,request,jsonify,render_template,redirect, url_for
from sqlalchemy import exc 
from models import Producto
from forms import ProductoForm
from app import db,bcrypt
from auth import tokenCheck,verificar

appProducto = Blueprint('appProducto', __name__, template_folder="templates")

@appProducto.route('/producto')
def Index():
    productos = Producto.query.all()
    return render_template("indexProducto.html", productos = productos)

@appProducto.route('/producto/add', methods = ["GET", "POST"])
def Agregar():
    producto = Producto()
    newProducto = ProductoForm(obj = producto)
    if request.method == "POST":
        if newProducto.validate_on_submit():
            newProducto.populate_obj(producto)
            db.session.add(producto)
            db.session.commit()
            return redirect(url_for('appProducto.Index'))
    return render_template('agregarProducto.html', nuevoProd = newProducto)

@appProducto.route('/producto/edit/<int:id>', methods = ["GET", "POST"])
def Editar(id):
    producto = Producto.query.get_or_404(id)
    editProducto = ProductoForm(obj = producto)
    if request.method == "POST":
        if editProducto.validate_on_submit():
            editProducto.populate_obj(producto)
            db.session.commit()
            return redirect(url_for('appProducto.Index'))
    return render_template('editarProducto.html')

@appProducto.route('/producto/delete/<int:id>', methods = ["POST"])
def Eliminar(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('appProducto.Index'))

@appProducto.route('/producto/add/json', methods = ["POST"])
def AgregarJson():
    if request.method == "POST":
        json = request.get_json()
        producto = Producto()
        producto.nombre = json["nombre"]
        producto.descripcion = json["descripcion"]
        producto.precio_kg = json["precio_kg"]
        producto.peso_kg = json["peso_kg"]
        producto.marca = json["marca"]
        db.session.add(producto)
        db.session.commit()
        return jsonify({"status":200, "Message":"Producto Agregado Correctamente"})

@appProducto.route('/producto/edit/json', methods=["POST"])
def EditarJson():
    json = request.get_json()
    producto = Producto.query.get_or_404(json["id"])
    producto.nombre = json["nombre"]
    producto.descripcion = json["descripcion"]
    producto.precio_kg = json["precio_kg"]
    producto.peso_kg = json["peso_kg"]
    producto.marca = json["marca"]
    db.session.commit()
    return jsonify({"status":200, "message":"Producto Actualizado Correctamente"})

@appProducto.route('/producto/delete/json', methods = ["POST"])
def EliminarJson():
    json = request.get_json()
    producto = Producto.query.get_or_404(json['id'])
    db.session.delete(producto)
    db.session.commit()
    return jsonify({"status":200, "message":"Producto Eliminado Correctamente"})