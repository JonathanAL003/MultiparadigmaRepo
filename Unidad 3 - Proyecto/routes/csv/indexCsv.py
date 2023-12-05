from flask import Blueprint, Response, redirect, url_for, request, render_template, jsonify
from models import Producto
import csv
from app import db, flash
import os

appcsv=Blueprint("appcsv",__name__,template_folder="templates")
def generate_csv():
    # Create a CSV string or generate data dynamically
    # csv_data = [
    #     ['Name', 'Age', 'Country'],
    #     ['John', '25', 'USA'],
    #     ['Alice', '30', 'Canada'],
    #     ['Bob', '28', 'UK']
    # ]
    csv_data = []
    csv_data.append(['ID', 'Nombre', 'Descripcion', 'Precio Por Kg', 'Peso Por Kg', 'Marca'])
    productos = Producto.query.order_by("id").all()
    for p in productos:
        lista = []
        lista.append(str(p.id))
        lista.append(p.nombre)
        lista.append(p.descripcion)
        lista.append(str(p.precio_kg))
        lista.append(str(p.peso_kg))
        lista.append(p.marca)
        csv_data.append(lista)
    
    # Create a generator to yield CSV rows
    def generate():
        for row in csv_data:
            yield ','.join(row) + '\n'
    
    # Set response headers to indicate CSV content
    headers = {
        'Content-Disposition': 'attachment; filename=Productos.csv',
        'Content-Type': 'text/csv'
    }
    
    # Return a Flask response object with the CSV generator
    return Response(generate(), headers=headers)

@appcsv.route('/download-csv')
def download_csv():
    return generate_csv()

@appcsv.route('/import-csv/json', methods=["POST"])
def import_json():
    try:
        data = request.files['inputFile']
        cont = 0
        print(data)
        ruta = os.path.join(os.path.dirname(__file__), 'layout.csv')
        data.save(ruta)                  #Guarda la ruta en el mismo directorio para procesarlo
        with open(ruta, 'r') as archivito_csv:          #Procesa el CSV desde el mismo 
            csv_reader = csv.DictReader(archivito_csv)
            for row in csv_reader:
                cont += 1
                prod = Producto()
                prod.nombre = row['Nombre']
                prod.descripcion = row['Descripcion']
                prod.precio_kg = float(row['Precio Por Kg'])
                prod.peso_kg = float(row['Peso Por Kg'])
                prod.marca = row['Marca']
                db.session.add(prod)
                db.session.commit()
        return jsonify({"status":200, "message":f"Se han importado {cont} productos por CSV"})
    except Exception as ex:
        return jsonify({"status":500, "message":"Ha ocurrido un incidente :c", "error":str(ex)})

@appcsv.route('/import-csv', methods = ["GET", "POST"])
def import_csv():
    try:
        if request.method == "GET":
            return render_template('importCsv.html')
        else:
            cont = 0
            dataCsv = request.files['file_csv']
            ruta = os.path.join(os.path.dirname(__file__), 'layout.csv')
            dataCsv.save(ruta)                  #Guarda la ruta en el mismo directorio para procesarlo
            with open(ruta, 'r') as archivito_csv:          #Procesa el CSV desde el mismo 
                csv_reader = csv.DictReader(archivito_csv)
                for row in csv_reader:
                    cont += 1
                    prod = Producto()
                    prod.nombre = row['Nombre']
                    prod.descripcion = row['Descripcion']
                    prod.precio_kg = float(row['Precio Por Kg'])
                    prod.peso_kg = float(row['Peso Por Kg'])
                    prod.marca = row['Marca']
                    db.session.add(prod)
                    db.session.commit()
            flash(f"Se han importado {cont} productos desde el archivo CSV.")
            return redirect(url_for('appProducto.Index'))
    except Exception as ex:
        print(str(ex))
        return redirect(url_for('appuser.Error'))