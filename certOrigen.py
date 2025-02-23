import PyPDF2
import pdfplumber
from PyPDF2 import PdfFileWriter, PdfFileReader
from pdfplumber import open as pdf_open
import re

class PDFCompleter:
    def __init__(self, pdf_entrada, pdf_salida):
        self.pdf_entrada = pdf_entrada
        self.pdf_salida = pdf_salida
        self.datos = {}

    def leer_pdf(self):
        with pdf_open(self.pdf_entrada) as pdf:
            texto = ''
            for pagina in pdf.pages:
                texto += pagina.extract_text()
            return texto

    def extraer_datos(self, texto):
        # Definir patrones de búsqueda para cada campo
        patrones = {
            'Exportador (Nombre)': r'Exportador \(Nombre\)\s*(.*)',
            'Exportador (Domicilio)': r'Exportador \(Domicilio\)\s*(.*)',
            'Exportador (País)': r'Exportador \(País\)\s*(.*)',
            'Identificación del Certificado(Número)': r'Identificación del Certificado\(Número\)\s*(.*)',
            'Importador (Nombre)': r'Importador \(Nombre\)\s*(.*)',
            'Importador (Domicilio)': r'Importador \(Domicilio\)\s*(.*)',
            'Importador (País)': r'Importador \(País\)\s*(.*)',
            'Nombre de la Entidad Emisora del Certificado': r'Nombre de la Entidad Emisora del Certificado\s*(.*)',
            'Consignatario (Nombre)': r'Consignatario \(Nombre\)\s*(.*)',
            'Consignatario (Domicilio)': r'Consignatario \(Domicilio\)\s*(.*)',
            'Consignatario (País)': r'Consignatario \(País\)\s*(.*)',
            'Lugar de Embarque Previsto': r'Lugar de Embarque Previsto\s*(.*)',
            'Medio de Transporte Previsto': r'Medio de Transporte Previsto\s*(.*)',
            'País de Destino Final': r'País de Destino Final\s*(.*)',
            'N O de Orde N O Order': r'N O de Orde N O Order\s*(.*)',
            'Código Arancelario Tarrif Item Number': r'Código Arancelario Tarrif Item Number\s*(.*)',
            'Denominación de Mercadería Description of Goods': r'Denominación de Mercadería Description of Goods\s*(.*)',
            'Peso o Cantidad': r'Peso o Cantidad\s*(.*)',
            'Observaciones - Observations': r'Observaciones - Observations\s*(.*)',
        }

        # Buscar y extraer los datos del texto
        for campo, patron in patrones.items():
            match = re.search(patron, texto)
            if match:
                self.datos[campo] = match.group(1).strip()
            else:
                self.datos[campo] = ''

    def completar_pdf(self):
        with open(self.pdf_salida, 'rb') as archivo_salida:
            pdf_salida = PdfFileReader(archivo_salida)
            writer = PdfFileWriter()
            for pagina in pdf_salida.pages:
                writer.addPage(pagina)
            # Completar los campos del PDF
            for campo, valor in self.datos.items():
                writer.addPage(pagina)
                writer.updatePageFormFieldValues({campo: valor})
            with open('pdf_completado.pdf', 'wb') as archivo_completado:
                writer.write(archivo_completado)

    def run(self):
        texto = self.leer_pdf()
        self.extraer_datos(texto)
        self.completar_pdf()

# Ejemplo de uso
pdf_completer = PDFCompleter('pdf_entrada.pdf', 'pdf_salida.pdf')
pdf_completer.run()