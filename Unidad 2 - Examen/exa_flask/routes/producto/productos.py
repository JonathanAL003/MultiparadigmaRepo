from flask import Blueprint, request, redirect, render_template, url_for
from models import Producto
from forms import ProductoForm
from app import db

appProducto = Blueprint('appProducto', __name__, template_folder='templates')

@appProducto.route('/')
def Inicio():
    productos = Producto.query.all()
    return render_template('productoIndex.html', productos = productos)

@appProducto.route('/producto/agregar', methods = ['GET', 'POST'])
def Agregar():
    producto = Producto()
    newProducto = ProductoForm(obj = producto)
    if request.method == 'POST':
        if newProducto.validate_on_submit():
            newProducto.populate_obj(producto)
            db.session.add(producto)
            db.session.commit()
            return RedirectIndex()
    return render_template('productoAgregar.html', newProducto = newProducto)

@appProducto.route('/producto/editar/<int:id>',methods=["GET", "POST"])
def Editar(id):
    producto = Producto.query.get_or_404(id)
    editProducto = ProductoForm(obj = producto)
    if request.method == 'POST':
        if editProducto.validate_on_submit():
            editProducto.populate_obj(producto)
            db.session.commit()
            return RedirectIndex()
    return render_template('productoEditar.html', editProducto = editProducto)

@appProducto.route('/producto/eliminar/<int:id>')
def Eliminar(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return RedirectIndex()

def RedirectIndex():
    return redirect(url_for('appProducto.Inicio'))