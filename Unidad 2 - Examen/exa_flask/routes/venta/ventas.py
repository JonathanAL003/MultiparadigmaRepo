from flask import Blueprint, request, jsonify
from app import db
from models import Venta

appVenta = Blueprint('appVenta', __name__, template_folder='templates')

# Ruta para mostrar todas las ventas
@appVenta.route('/venta/json/index')
def VentaIndex():
    try:
        ventas = Venta.query.all()
        listVenta = []
        for ven in ventas:
            venta = {
                'id_venta': ven.id_venta,
                'fecha_venta': ven.fecha_venta,
                'cant_prod': ven.cant_prod,
                'total_venta': ven.total_venta,
                'metodo_pago': ven.metodo_pago
            }
            listVenta.append(venta)
        return jsonify({'ventas': listVenta})
    except Exception as ex:
        return jsonify({'status': 400, 'mensaje': str(ex)})

# Ruta para agregar una nueva venta
@appVenta.route('/venta/json/agregar', methods=["POST"])
def VentaAgregar():
    try:
        if request.method == "POST":
            json_data = request.get_json()
            venta = Venta(
                fecha_venta=json_data['fecha_venta'],
                cant_prod=json_data['cant_prod'],
                total_venta=json_data['total_venta'],
                metodo_pago=json_data['metodo_pago']
            )
            db.session.add(venta)
            db.session.commit()
            return jsonify({'status': 200, 'mensaje': 'Venta agregada por petición HTTP'})
    except Exception as ex:
        return jsonify({'status': 400, 'mensaje': str(ex)})

# Ruta para editar una venta por su ID
@appVenta.route('/venta/json/editar/<int:id>', methods=["PUT"])
def VentaEditar(id):
    try:
        if request.method == "PUT":
            venta = Venta.query.get_or_404(id)
            json_data = request.get_json()
            venta.fecha_venta = json_data['fecha_venta']
            venta.cant_prod = json_data['cant_prod']
            venta.total_venta = json_data['total_venta']
            venta.metodo_pago = json_data['metodo_pago']
            db.session.commit()
            return jsonify({'status': 200, 'mensaje': 'Venta editada por petición HTTP'})
    except Exception as ex:
        return jsonify({'status': 400, 'mensaje': str(ex)})

# Ruta para eliminar una venta por su ID
@appVenta.route('/venta/json/eliminar/<int:id>', methods=["DELETE"])
def VentaEliminar(id):
    try:
        if request.method == "DELETE":
            venta = Venta.query.get_or_404(id)
            db.session.delete(venta)
            db.session.commit()
            return jsonify({'status': 200, 'mensaje': f'Venta {id} eliminada por petición HTTP'})
    except Exception as ex:
        return jsonify({'status': 400, 'mensaje': str(ex)})
