from models import Proveedor
from forms import ProveedorForm
from flask import Blueprint,request,jsonify,render_template, redirect, url_for
from sqlalchemy import exc
from app import db, flash

appProveedor = Blueprint('appProveedor', __name__, template_folder="templates")

@appProveedor.route('/proveedor')
def Index():
    proves = Proveedor.query.order_by("id").all()
    return render_template('indexProveedor.html', proveedores = proves)

@appProveedor.route('/proveedor/404')
def Error():
    return render_template('errorProveedor.html')

@appProveedor.route('/proveedor/add', methods = ["GET", "POST"])
def Agregar():
    try:
        proveedor = Proveedor()
        formProveedor = ProveedorForm(obj = proveedor)
        if request.method == "POST":
            if formProveedor.validate_on_submit():
                formProveedor.populate_obj(proveedor)
                db.session.add(proveedor)
                db.session.commit()
                return redirect(url_for('appProveedor.Index'))
        else:
            return render_template('agregarProveedor.html', nuevoProv = formProveedor)
    except Exception as ex:
        print(str(ex))
        return redirect(url_for('appuser.Error'))
    
@appProveedor.route('/proveedor/edit/<int:id>', methods = ["GET", "POST"])
def Editar(id):
    try:
        proveedor = Proveedor.query.filter_by(id = id).first()
        formProveedor = ProveedorForm(obj = proveedor)
        if request.method == "POST":
            if formProveedor.validate_on_submit():
                formProveedor.populate_obj(proveedor)
                db.session.commit()
                return redirect(url_for('appProveedor.Index'))
        else:
            return render_template('editarProveedor.html', editarProv = formProveedor)
    except Exception as ex:
        print(str(ex))
        return redirect(url_for('appuser.Error'))

@appProveedor.route('/proveedor/delete/<int:id>', methods = ["GET"])
def Eliminar(id):
    try:
        proveedor = Proveedor.query.filter_by(id = id).first()
        db.session.delete(proveedor)
        db.session.commit()
        return redirect(url_for('appProducto.Index'))
    except Exception as ex:
        print(str(ex))
        return redirect(url_for('appuser.Error'))