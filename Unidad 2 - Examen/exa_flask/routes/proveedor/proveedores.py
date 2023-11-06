from flask import Blueprint, request, jsonify
from app import db
from models import Proveedor

appProveedor = Blueprint('appProveedor', __name__, template_folder='templates')

# Ruta para mostrar todos los proveedores
@appProveedor.route('/proveedor/json/index')
def ProveedorIndex():
    try:
        proveedores = Proveedor.query.all()
        listProveedor = []
        for prov in proveedores:
            proveedor = {
                'id_prov': prov.id_prov,
                'nombre_pv': prov.nombre_pv,
                'telefono_pv': prov.telefono_pv,
                'direccion_pv': prov.direccion_pv
            }
            listProveedor.append(proveedor)
        return jsonify({'proveedores': listProveedor})
    except Exception as ex:
        return jsonify({'status': 400, 'mensaje': str(ex)})

# Ruta para agregar un nuevo proveedor
@appProveedor.route('/proveedor/json/agregar', methods=["POST"])
def ProveedorAgregar():
    try:
        if request.method == "POST":
            json_data = request.get_json()
            proveedor = Proveedor(
                nombre_pv=json_data['nombre_pv'],
                telefono_pv=json_data['telefono_pv'],
                direccion_pv=json_data['direccion_pv']
            )
            db.session.add(proveedor)
            db.session.commit()
            return jsonify({'status': 200, 'mensaje': 'Proveedor agregado por petición HTTP'})
    except Exception as ex:
        return jsonify({'status': 400, 'mensaje': str(ex)})

# Ruta para editar un proveedor por su ID
@appProveedor.route('/proveedor/json/editar/<int:id>', methods=["PUT"])
def ProveedorEditar(id):
    try:
        if request.method == "PUT":
            proveedor = Proveedor.query.get_or_404(id)
            json_data = request.get_json()
            proveedor.nombre_pv = json_data['nombre_pv']
            proveedor.telefono_pv = json_data['telefono_pv']
            proveedor.direccion_pv = json_data['direccion_pv']
            db.session.commit()
            return jsonify({'status': 200, 'mensaje': 'Proveedor editado por petición HTTP'})
    except Exception as ex:
        return jsonify({'status': 400, 'mensaje': str(ex)})

# Ruta para eliminar un proveedor por su ID
@appProveedor.route('/proveedor/json/eliminar/<int:id>', methods=["DELETE"])
def ProveedorEliminar(id):
    try:
        if request.method == "DELETE":
            proveedor = Proveedor.query.get_or_404(id)
            db.session.delete(proveedor)
            db.session.commit()
            return jsonify({'status': 200, 'mensaje': f'Proveedor {id} eliminado por petición HTTP'})
    except Exception as ex:
        return jsonify({'status': 400, 'mensaje': str(ex)})
