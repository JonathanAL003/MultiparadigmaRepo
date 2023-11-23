from flask import Blueprint,request,jsonify,render_template,redirect, url_for
from sqlalchemy import exc 
from models import Venta, Producto
from forms import VentaForm
from app import db,bcrypt
from auth import tokenCheck,verificar

appVenta = Blueprint('appVenta', __name__, template_folder='templates')

@appVenta.route('/venta')
def Index():
    ventas = Venta.query.all()
    return render_template('indexVenta.html', ventas = ventas)

@appVenta.route('/venta/404')
def Error():
    return render_template('errorVenta.html')

#RUTAS PARA FORMULARIOS
@appVenta.route('/venta/add', methods = ["GET", "POST"])
def Agregar():
    venta = Venta()
    ventaForm = VentaForm(obj = venta)
    if request.method == "POST":
        if ventaForm.validate_on_submit():
            ventaForm.populate_obj(venta)
            db.session.add(venta)
            db.session.commit()
            return redirect(url_for('appVenta.Index'))
        else:
            return redirect(url_for('appVenta.Error'))
    else:
        return render_template("agregarVenta.html", nuevaVenta = ventaForm)

@appVenta.route("/venta/edit/<int:id>", methods = ["GET", "POST"])
def Editar(id):
    try:
        venta = Venta.query.get_or_404(id)
        ventaForm = VentaForm(obj = venta)
        if request.method == "POST":
            if ventaForm.validate_on_submit():
                ventaForm.populate_obj(venta)
                db.session.commit()
                return redirect(url_for('appVenta.Index'))
        else:
            return render_template("editarVenta.html", editarVenta = ventaForm)
    except Exception as e:
        print(e)
        return redirect(url_for('appVenta.Error'))
    
@appVenta.route('/venta/delete/<int:id>', methods = ["GET", "POST"])
def Eliminar():
    try:
        venta = Venta.query.get_or_404(id)
        db.session.delete(venta)
        db.session.commit()
        return redirect(url_for('appVenta.Index'))
    except Exception as e:
        print(e)
        return redirect(url_for('appVenta.Error'))

#RUTAS PARA PETICIONES HTTP (JSON)
@appVenta.route('/venta/add/json', methods = ["POST"])
def AgregarJson():
    try:
        json = request.get_json()
        venta = Venta()
        venta.id_producto = json["id_producto"]
        venta.nombre_cliente = json["nombre_cliente"]
        venta.cantidad = json["cantidad"]
        producto = Producto.query.filter_by(id = venta.id_producto).first()
        total = (producto.peso_kg * venta.cantidad) * producto.precio_kg
        venta.precio_total = total
        db.session.add(venta)
        db.session.commit()
        return jsonify({"status" : 200, "message" : "Venta Registrada Correctamente"})
    except Exception as e:
        return jsonify({"status" : 400, "message" : "Ha Ocurrido Un Incidente"})
    
@appVenta.route('/venta/edit/json', methods = ["POST"])
def EditarJson():
    try:
        json = request.get_json()
        venta = Venta.query.filter_by(id = json["id"]).first()
        venta.id_producto = json["id_producto"]
        venta.nombre_cliente = json["nombre_cliente"]
        venta.cantidad = json["cantidad"]
        producto = Producto.query.filter_by(id = venta.id_producto).first()
        total = (producto.peso_kg * venta.cantidad) * producto.precio_kg
        venta.precio_total = total
        db.session.commit()
        return jsonify({"status" : 200, "message" : "Venta Actualizada Correctamente"})
    except Exception as e:
        return jsonify({"status" : 400, "message" : "Ha Ocurrido Un Incidente"})

@appVenta.route('/venta/delete/json', methods = ["POST"])
def EliminarJson():
    try:
        json = request.get_json()
        venta = Venta.query.filter_by(id = json["id"]).first()
        db.session.delete(venta)
        return jsonify({"status" : 200, "message" : "Venta Eliminada Correctamente"})
    except Exception as e:
        return jsonify({"status" : 400, "message" : "Ha Ocurrido Un Incidente"})