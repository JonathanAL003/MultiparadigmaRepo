
#pip install reportlab
from flask import Blueprint,make_response,render_template, redirect, url_for
from models import Venta, Producto
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
import datetime
apppdf = Blueprint('apppdf',__name__,template_folder="templates")


@apppdf.route('/generatePdf')
def generate_pdf():
    try:
        doc = SimpleDocTemplate("Ventas.pdf", pagesize=letter)
        ventas = Venta.query.all()
        listaVentas=[["ID", "Producto", "Nombre Del Cliente", "Cantidad", "Precio Total"]]
        for venta in ventas:
            prod = Producto.query.filter_by(id = venta.id_producto).first()
            listaVentas.append([venta.id, prod.nombre, venta.nombre_cliente, venta.cantidad, venta.precio_total])
        table = Table(listaVentas)

        style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 16),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])
        
        table.setStyle(style)
        # Add the table to the PDF document

        text = f"Registro De Todas Las Ventas."
        text += f"Reporte Generado El: {datetime.datetime.utcnow()}"
        # Create a paragraph object
        style = getSampleStyleSheet()["Normal"]
        style.alignment = TA_CENTER 
        paragraph = Paragraph(text, style)
        elements = [paragraph,table]

        doc.build(elements)
        # Create a response with the PDF file
        response = make_response(open("Ventas.pdf", "rb").read())
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=Ventas.pdf'
        return response
    except Exception as ex:
        print(str(ex))
        return redirect(url_for('appuser.Error'))

@apppdf.route('/mainPdf')
def index():
    return render_template('indexPdf.html')