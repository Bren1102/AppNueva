from reportlab.pdfgen import canvas

def generar_pdf(datos, nombre_archivo):
    c = canvas.Canvas(nombre_archivo)
    c.drawString(100, 750, f"Nombre: {datos['nombre']}")
    c.drawString(100, 730, f"Dirección: {datos['direccion']}")
    c.save()