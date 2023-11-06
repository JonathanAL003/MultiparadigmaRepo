from flask import Blueprint, request, redirect, render_template, url_for, jsonify
from app import db
from models import Inventario

appInventario = Blueprint('appInventario', __name__, template_folder='templates')

@appInventario.route('/inventario/json/index')
def InventarioIndex():
    try:
        inventarios = Inventario.query.all()
        listInventario = []
        for inv in inventarios:
            inventario = {
                'id_inv': inv.id_inv,
                'stock': inv.stock,
                'precio_compra': inv.precio_compra,
                'fecha_reab': inv.fecha_reab,
                'niv_min': inv.niv_min
            }
            listInventario.append(inventario)
        return jsonify({'inventarios': listInventario})
    except Exception as ex:
        return jsonify({'status': 400, 'mensaje': str(ex)})

@appInventario.route('/inventario/json/agregar', methods=["POST"])
def InventarioAgregar():
    try:
        if request.method == "POST":
            json_data = request.get_json()
            inventario = Inventario(
                stock=json_data['stock'],
                precio_compra=json_data['precio_compra'],
                fecha_reab=json_data['fecha_reab'],
                niv_min=json_data['niv_min']
            )
            db.session.add(inventario)
            db.session.commit()
            return jsonify({'status': 200, 'mensaje': 'Inventario agregado por petición HTTP'})
    except Exception as ex:
        return jsonify({'status': 400, 'mensaje': str(ex)})

@appInventario.route('/inventario/json/editar/<int:id>', methods=["POST"])
def InventarioEditar(id):
    try:
        if request.method == "POST":
            inventario = Inventario.query.get_or_404(id)
            json_data = request.get_json()
            inventario.stock = json_data['stock']
            inventario.precio_compra = json_data['precio_compra']
            inventario.fecha_reab = json_data['fecha_reab']
            inventario.niv_min = json_data['niv_min']
            db.session.commit()
            return jsonify({'status': 200, 'mensaje': 'Inventario editado por petición HTTP'})
    except Exception as ex:
        return jsonify({'status': 400, 'mensaje': str(ex)})

@appInventario.route('/inventario/json/eliminar/<int:id>', methods=["POST"])
def InventarioEliminar(id):
    try:
        if request.method == "POST":
            inventario = Inventario.query.get_or_404(id)
            db.session.delete(inventario)
            db.session.commit()
            return jsonify({'status': 200, 'mensaje': f'Inventario {id} eliminado por petición HTTP'})
    except Exception as ex:
        return jsonify({'status': 400, 'mensaje': str(ex)})
