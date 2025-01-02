import PyPDF2

def leer_pdf(archivo):
    with open(archivo, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        texto = ''
        for page_num in range(reader.numPages):
            texto += reader.getPage(page_num).extract_text()
        return texto
    

    