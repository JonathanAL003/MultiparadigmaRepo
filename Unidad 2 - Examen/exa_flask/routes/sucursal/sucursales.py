from flask import Blueprint, request, jsonify
from app import db
from models import Sucursal

appSucursal = Blueprint('appSucursal', __name__, template_folder='templates')

# Ruta para mostrar todas las sucursales
@appSucursal.route('/sucursal/json/index')
def SucursalIndex():
    try:
        sucursales = Sucursal.query.all()
        listSucursal = []
        for suc in sucursales:
            sucursal = {
                'id_suc': suc.id_suc,
                'nombre_s': suc.nombre_s,
                'direccion_s': suc.direccion_s,
                'telefono_s': suc.telefono_s,
                'horario': suc.horario
            }
            listSucursal.append(sucursal)
        return jsonify({'sucursales': listSucursal})
    except Exception as ex:
        return jsonify({'status': 400, 'mensaje': str(ex)})

# Ruta para agregar una nueva sucursal
@appSucursal.route('/sucursal/json/agregar', methods=["POST"])
def SucursalAgregar():
    try:
        if request.method == "POST":
            json_data = request.get_json()
            sucursal = Sucursal(
                nombre_s=json_data['nombre_s'],
                direccion_s=json_data['direccion_s'],
                telefono_s=json_data['telefono_s'],
                horario=json_data['horario']
            )
            db.session.add(sucursal)
            db.session.commit()
            return jsonify({'status': 200, 'mensaje': 'Sucursal agregada por petición HTTP'})
    except Exception as ex:
        return jsonify({'status': 400, 'mensaje': str(ex)})

# Ruta para editar una sucursal por su ID
@appSucursal.route('/sucursal/json/editar/<int:id>', methods=["PUT"])
def SucursalEditar(id):
    try:
        if request.method == "PUT":
            sucursal = Sucursal.query.get_or_404(id)
            json_data = request.get_json()
            sucursal.nombre_s = json_data['nombre_s']
            sucursal.direccion_s = json_data['direccion_s']
            sucursal.telefono_s = json_data['telefono_s']
            sucursal.horario = json_data['horario']
            db.session.commit()
            return jsonify({'status': 200, 'mensaje': 'Sucursal editada por petición HTTP'})
    except Exception as ex:
        return jsonify({'status': 400, 'mensaje': str(ex)})

# Ruta para eliminar una sucursal por su ID
@appSucursal.route('/sucursal/json/eliminar/<int:id>', methods=["DELETE"])
def SucursalEliminar(id):
    try:
        if request.method == "DELETE":
            sucursal = Sucursal.query.get_or_404(id)
            db.session.delete(sucursal)
            db.session.commit()
            return jsonify({'status': 200, 'mensaje': f'Sucursal {id} eliminada por petición HTTP'})
    except Exception as ex:
        return jsonify({'status': 400, 'mensaje': str(ex)})
