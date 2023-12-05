from flask import Blueprint,request,jsonify,render_template,redirect, url_for
from sqlalchemy import exc 
from models import Venta, Producto
from forms import VentaForm
from app import db,bcrypt
from auth import tokenCheck,verificar

appVenta = Blueprint('appVenta', __name__, template_folder='templates')

@appVenta.route('/venta')
def Index():
    try:
        ventas = Venta.query.order_by("id").all()
        lista = []
        for v in ventas:
            prod = Producto.query.filter_by(id=v.id_producto).first()
            dicc = {}
            dicc["id"] = v.id
            dicc["nombre"] = prod.nombre
            dicc["nombre_cliente"] = v.nombre_cliente
            dicc["cantidad"] = v.cantidad
            dicc["precio_total"] = v.precio_total
            dicc["encargado"] = v.encargado
            lista.append(dicc)
        return render_template('indexVenta.html', ventas = lista)
    except Exception as ex:
        print(str(ex))
        return redirect(url_for('appuser.Error'))

# @appVenta.route('/venta/404')
# def Error():
#     return render_template('errorVenta.html')

#RUTAS PARA FORMULARIOS
@appVenta.route('/venta/add', methods = ["GET", "POST"])
def Agregar():
    try:
        venta = Venta()
        ventaForm = VentaForm(obj = venta)
        prod = Producto.query.all()
        listProducto = []
        for p in prod:
            op = (p.id, p.nombre)
            listProducto.append(op)
        ventaForm.id_producto.choices = listProducto
        if request.method == "POST":
            if ventaForm.validate_on_submit():
                producto = Producto.query.filter_by(id = ventaForm.id_producto.data).first()
                ventaForm.precio_total.data = (producto.peso_kg * float(ventaForm.cantidad.data)) * producto.precio_kg
                ventaForm.populate_obj(venta)
                print(venta.encargado)
                print(ventaForm.encargado.data)
                db.session.add(venta)
                db.session.commit()
                return redirect(url_for('appVenta.Index'))
            else:
                return redirect(url_for('appVenta.Error'))
        else:
            return render_template("agregarVenta.html", nuevaVenta = ventaForm)
    except Exception as e:
        print(e)
        return redirect(url_for('appuser.Error'))

@appVenta.route("/venta/edit/<int:id>", methods = ["GET", "POST"])
def Editar(id):
    try:
        venta = Venta.query.get_or_404(id)
        ventaForm = VentaForm(obj = venta)
        prod = Producto.query.all()
        listProducto = []
        for p in prod:
            op = (p.id, p.nombre)
            listProducto.append(op)
        ventaForm.id_producto.choices = listProducto
        if request.method == "POST":
            if ventaForm.validate_on_submit():
                producto = Producto.query.filter_by(id = ventaForm.id_producto.data).first()
                ventaForm.precio_total.data = (producto.peso_kg * float(ventaForm.cantidad.data)) * producto.precio_kg
                ventaForm.populate_obj(venta)
                print(venta.encargado)
                print(ventaForm.encargado.data)
                db.session.commit()
                return redirect(url_for('appVenta.Index'))
        else:
            return render_template("editarVenta.html", editarVenta = ventaForm)
    except Exception as e:
        print(e)
        return redirect(url_for('appuser.Error'))
    
@appVenta.route('/venta/delete/<int:id>', methods = ["GET"])
def Eliminar(id):
    try:
        venta = Venta.query.get_or_404(id)
        db.session.delete(venta)
        db.session.commit()
        return redirect(url_for('appVenta.Index'))
    except Exception as e:
        print(e)
        return redirect(url_for('appuser.Error'))

#RUTAS PARA PETICIONES HTTP (JSON)
@appVenta.route('/venta/json', methods = ["GET"])
def IndexJson():
    try:
        json = request.get_json()
        listVentas = []
        ventas = Venta.query.order_by("id").all()
        for v in ventas:
            d = {}
            d["id"] = v.id 
            d["id_producto"] = v.id_producto 
            d["nombre_cliente"] = v.nombre_cliente 
            d["cantidad"] = v.cantidad 
            d["precio_total"] = v.precio_total
            d["encargado"] = v.encargado
            listVentas.append(d)
        return jsonify({"status": 200, "ventas":listVentas})
    except Exception as ex:
        print(str(ex))
        return jsonify({"status":500, "message": "Ha Ocurrido Un Incidente :c", "error":str(ex)})

@appVenta.route('/venta/json', methods = ["POST"])
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
        venta.encargado = json["encargado"]
        db.session.add(venta)
        db.session.commit()
        return jsonify({"status" : 200, "message" : "Venta Registrada Correctamente"})
    except Exception as e:
        return jsonify({"status" : 500, "message" : "Ha Ocurrido Un Incidente :c", "error":str(e)})
    
@appVenta.route('/venta/json', methods = ["PUT"])
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
        venta.encargado = json["encargado"]
        db.session.commit()
        return jsonify({"status" : 200, "message" : "Venta Actualizada Correctamente"})
    except Exception as e:
        return jsonify({"status" : 500, "message" : "Ha Ocurrido Un Incidente :c", "error":str(e)})

@appVenta.route('/venta/json', methods = ["DELETE"])
def EliminarJson():
    try:
        json = request.get_json()
        venta = Venta.query.filter_by(id = json["id"]).first()
        db.session.delete(venta)
        db.session.commit()
        return jsonify({"status" : 200, "message" : "Venta Eliminada Correctamente"})
    except Exception as e:
        return jsonify({"status" : 500, "message" : "Ha Ocurrido Un Incidente :c", "error":str(e)})