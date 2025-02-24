
"""
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
            'PORT OF LOADING': r'PORT OF LOADING\s*(.*)',
            'PORT OF DISCHARGE': r'PORT OF DISCHARGE\s*(.*)',
            'FINAL DESTINATION': r'FINAL DESTINATION\s*(.*)',
            'PRODUCT DESCRIPTION': r'PRODUCT DESCRIPTION\s*(.*)',
            'CARGO DETAILS NET WEIGHT MAX ALLOWED PER FCL': r'CARGO DETAILS NET WEIGHT MAX ALLOWED PER FCL\s*(.*)',
            'CARGO DETAILS GROSS WEIGHT MAX ALLOWED PER FCL': r'CARGO DETAILS GROSS WEIGHT MAX ALLOWED PER FCL\s*(.*)',
            'BILL OF LADING': r'BILL OF LADING\s*(.*)',
            'CONSIGNEE': r'CONSIGNEE\s*(.*)',
            '1ST NOTIFY PARTY': r'1ST NOTIFY PARTY\s*(.*)',
            'HEALTH CERTIFICATE CONSIGNEE': r'HEALTH CERTIFICATE CONSIGNEE\s*(.*)',
            'ORIGIN CERTIFICATE CONSIGNEE': r'ORIGIN CERTIFICATE CONSIGNEE\s*(.*)',
            'COMMERCIAL INVOICE NAME': r'COMMERCIAL INVOICE NAME\s*(.*)',
            'COMMERCIAL INVOICE ADDRESS': r'COMMERCIAL INVOICE ADDRESS\s*(.*)',
            'COMMERCIAL INVOICE CITY': r'COMMERCIAL INVOICE CITY\s*(.*)',
            'COMMERCIAL INVOICE COUNTRY': r'COMMERCIAL INVOICE COUNTRY\s*(.*)',
            'PACKING LIST CONSIGNEE': r'PACKING LIST CONSIGNEE\s*(.*)',
            'OTHER REQUIRED DOCUMENTS': r'OTHER REQUIRED DOCUMENTS\s*(.*)',
            'ADDRESS TO SEND THE ORIGINAL DOCUMENTATION': r'ADDRESS TO SEND THE ORIGINAL DOCUMENTATION\s*(.*)',
            'CONTACT PERSON TO CONFIRM THE DRAFTS': r'CONTACT PERSON TO CONFIRM THE DRAFTS\s*(.*)',
            'SHIPPING LINE CONTRACT NUMBER': r'SHIPPING LINE CONTRACT NUMBER\s*(.*)',
            'TEMPERATURE OF CONTAINER': r'TEMPERATURE OF CONTAINER\s*(.*)',
            'LABELLNG': r'LABELLNG\s*(.*)',
            'DOCUMENTARY SET PER CONTAINER': r'DOCUMENTARY SET PER CONTAINER\s*(.*)',
            'OBSERVATIONS': r'OBSERVATIONS\s*(.*)',
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
"""








import PyPDF2
import pdfplumber
from PyPDF2 import PdfFileWriter, PdfFileReader
from pdfplumber import open as pdf_open
import re
import tkinter as tk
from tkinter import filedialog

class PDFCompleter:
    def __init__(self):
        self.pdf_entrada = ''
        self.pdf_salida = ''
        self.datos = {}

        self.root = tk.Tk()
        self.root.title("PDF Completer")

        self.label_entrada = tk.Label(self.root, text="PDF de entrada:")
        self.label_entrada.pack()

        self.entry_entrada = tk.Entry(self.root, width=50)
        self.entry_entrada.pack()

        self.button_entrada = tk.Button(self.root, text="Seleccionar PDF de entrada", command=self.seleccionar_pdf_entrada)
        self.button_entrada.pack()

        self.label_salida = tk.Label(self.root, text="PDF de salida:")
        self.label_salida.pack()

        self.entry_salida = tk.Entry(self.root, width=50)
        self.entry_salida.pack()

        self.button_salida = tk.Button(self.root, text="Seleccionar PDF de salida", command=self.seleccionar_pdf_salida)
        self.button_salida.pack()

        self.button_completar = tk.Button(self.root, text="Completar PDF", command=self.completar_pdf)
        self.button_completar.pack()

        self.label_estado = tk.Label(self.root, text="")
        self.label_estado.pack()

    def seleccionar_pdf_entrada(self):
        self.pdf_entrada = filedialog.askopenfilename(title="Seleccionar PDF de entrada", filetypes=[("PDF files", "*.pdf")])
        self.entry_entrada.delete(0, tk.END)
        self.entry_entrada.insert(0, self.pdf_entrada)

    def seleccionar_pdf_salida(self):
        self.pdf_salida = filedialog.askopenfilename(title="Seleccionar PDF de salida", filetypes=[("PDF files", "*.pdf")])
        self.entry_salida.delete(0, tk.END)
        self.entry_salida.insert(0, self.pdf_salida)

    def leer_pdf(self):
        with pdf_open(self.pdf_entrada) as pdf:
            texto = ''
            for pagina in pdf.pages:
                texto += pagina.extract_text()
            return texto

    def extraer_datos(self, texto):
        # Definir patrones de búsqueda para cada campo
        patrones = {
            'PORT OF LOADING': r'PORT OF LOADING\s*(.*)',
            'PORT OF DISCHARGE': r'PORT OF DISCHARGE\s*(.*)',
            'FINAL DESTINATION': r'FINAL DESTINATION\s*(.*)',
            'PRODUCT DESCRIPTION': r'PRODUCT DESCRIPTION\s*(.*)',
            'CARGO DETAILS NET WEIGHT MAX ALLOWED PER FCL': r'CARGO DETAILS NET WEIGHT MAX ALLOWED PER FCL\s*(.*)',
            'CARGO DETAILS GROSS WEIGHT MAX ALLOWED PER FCL': r'CARGO DETAILS GROSS WEIGHT MAX ALLOWED PER FCL\s*(.*)',
            'BILL OF LADING': r'BILL OF LADING\s*(.*)',
            'CONSIGNEE': r'CONSIGNEE\s*(.*)',
            '1ST NOTIFY PARTY': r'1ST NOTIFY PARTY\s*(.*)',
            'HEALTH CERTIFICATE CONSIGNEE': r'HEALTH CERTIFICATE CONSIGNEE\s*(.*)',
            'ORIGIN CERTIFICATE CONSIGNEE': r'ORIGIN CERTIFICATE CONSIGNEE\s*(.*)',
            'COMMERCIAL INVOICE NAME': r'COMMERCIAL INVOICE NAME\s*(.*)',
            'COMMERCIAL INVOICE ADDRESS': r'COMMERCIAL INVOICE ADDRESS\s*(.*)',
            'COMMERCIAL INVOICE CITY': r'COMMERCIAL INVOICE CITY\s*(.*)',
            'COMMERCIAL INVOICE COUNTRY': r'COMMERCIAL INVOICE COUNTRY\s*(.*)',
            'PACKING LIST CONSIGNEE': r'PACKING LIST CONSIGNEE\s*(.*)',
            'OTHER REQUIRED DOCUMENTS': r'OTHER REQUIRED DOCUMENTS\s*(.*)',
            'ADDRESS TO SEND THE ORIGINAL DOCUMENTATION': r'ADDRESS TO SEND THE ORIGINAL DOCUMENTATION\s*(.*)',
            'CONTACT PERSON TO CONFIRM THE DRAFTS': r'CONTACT PERSON TO CONFIRM THE DRAFTS\s*(.*)',
            'SHIPPING LINE CONTRACT NUMBER': r'SHIPPING LINE CONTRACT NUMBER\s*(.*)',
            'TEMPERATURE OF CONTAINER': r'TEMPERATURE OF CONTAINER\s*(.*)',
            'LABELLNG': r'LABELLNG\s*(.*)',
            'DOCUMENTARY SET PER CONTAINER': r'DOCUMENTARY SET PER CONTAINER\s*(.*)',
        }