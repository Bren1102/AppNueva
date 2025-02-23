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
            'I.1 Expedidor/Exportador': r'I\.1 Expedidor/Exportador\s*(.*)',
            'I.2 Referencia del certificado': r'I\.2 Referencia del certificado\s*(.*)',
            'I.3 Autoridad central competente': r'I\.3 Autoridad central competente\s*(.*)',
            'I.4 Autoridad local competente': r'I\.4 Autoridad local competente\s*(.*)',
            'I.5 Destinatario/Importador': r'I\.5 Destinatario/Importador\s*(.*)',
            'I.6 Operador responsable de la partida': r'I\.6 Operador responsable de la partida\s*(.*)',
            'I.7 País de origen': r'I\.7 País de origen\s*(.*)',
            'I.8 Región de origen': r'I\.8 Región de origen\s*(.*)',
            'I.9 País de destino': r'I\.9 País de destino\s*(.*)',
            'I.10 Región de destino': r'I\.10 Región de destino\s*(.*)',
            'I.11 Lugar de Expedición': r'I\.11 Lugar de Expedición\s*(.*)',
            'I.12 Lugar de destino': r'I\.12 Lugar de destino\s*(.*)',
            'I.13 Lugar de carga': r'I\.13 Lugar de carga\s*(.*)',
            'I.14 Fecha y hora de salida': r'I\.14 Fecha y hora de salida\s*(.*)',
            'I.15 Medio de transporte': r'I\.15 Medio de transporte\s*(.*)',
            'I.16 Puesto Control fronterizo de entrada': r'I\.16 Puesto Control fronterizo de entrada\s*(.*)',
            'I.17 Documentos de acompañamiento': r'I\.17 Documentos de acompañamiento\s*(.*)',
            'I.18 Condiciones de transporte': r'I\.18 Condiciones de transporte\s*(.*)',
            'I.19 Número de recipiente/Número de precinto': r'I\.19 Número de recipiente/Número de precinto\s*(.*)',
            'I.20 Certificados como o a efectos de': r'I\.20 Certificados como o a efectos de\s*(.*)',
            'I.21 Para tránsito': r'I\.21 Para tránsito\s*(.*)',
            'I.22 Para el mercado interior': r'I\.22 Para el mercado interior\s*(.*)',
            'I.23': r'I\.23\s*(.*)',
            'I.24 Número total de bultos': r'I\.24 Número total de bultos\s*(.*)',
            'I.25 Cantidad Total': r'I\.25 Cantidad Total\s*(.*)',
            'I.26 Peso neto/Peso bruto total (kg)': r'I\.26 Peso neto/Peso bruto total (kg)\s*(.*)',
            'I.27 Descripción de la partida': r'I\.27 Descripción de la partida\s*(.*)',
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