from flask import Blueprint, request, redirect, render_template, url_for
from models import Empleado
from forms import EmpleadoForm
from app import db

appEmpleado = Blueprint('appEmpleado', __name__, template_folder='templates')

@appEmpleado.route('/empleado/index')
def Inicio():
    empleados = Empleado.query.all()
    return render_template('empleadoIndex.html', empleados = empleados)

@appEmpleado.route('/empleado/agregar', methods = ['GET', 'POST'])
def Agregar():
    empleado = Empleado()
    newEmpleado = EmpleadoForm(obj = empleado)
    if request.method == 'POST':
        if newEmpleado.validate_on_submit():
            newEmpleado.populate_obj(empleado)
            db.session.add(empleado)
            db.session.commit()
            return RedirectIndex()
    return render_template('empleadoAgregar.html', newEmpleado = newEmpleado)

@appEmpleado.route('/empleado/editar/<int:id>',methods=["GET", "POST"])
def Editar(id):
    empleado = Empleado.query.get_or_404(id)
    editEmpleado = EmpleadoForm(obj = empleado)
    if request.method == 'POST':
        if editEmpleado.validate_on_submit():
            editEmpleado.populate_obj(empleado)
            db.session.commit()
            return RedirectIndex()
    return render_template('empleadoEditar.html', editEmpleado = editEmpleado)

@appEmpleado.route('/empleado/eliminar/<int:id>')
def Eliminar(id):
    empleado = Empleado.query.get_or_404(id)
    db.session.delete(empleado)
    db.session.commit()
    return RedirectIndex()

def RedirectIndex():
    return redirect(url_for('appEmpleado.Inicio'))