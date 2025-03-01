import tkinter as tk
from tkinter import filedialog
from certZoosan import PDFCompleter as PDFCompleter1
from certOrigen import PDFCompleter as PDFCompleter2
from shipmentInfo import PDFCompleter as PDFCompleter3
from newShipping import newShipping

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Completa PDF")
        self.geometry("300x200")

        self.label_entrada = tk.Label(self, text="Seleccione el PDF de entrada:")
        self.label_entrada.pack()

        self.entry_entrada = tk.Entry(self, width=50)
        self.entry_entrada.pack()

        self.button_entrada = tk.Button(self, text="Buscar", command=self.buscar_pdf_entrada)
        self.button_entrada.pack()

        self.label_salida = tk.Label(self, text="Seleccione el PDF de salida:")
        self.label_salida.pack()

        self.entry_salida = tk.Entry(self, width=50)
        self.entry_salida.pack()

        self.button_salida = tk.Button(self, text="Buscar", command=self.buscar_pdf_salida)
        self.button_salida.pack()

        self.button_completer_1 = tk.Button(self, text="Completa PDF 1", command=self.completa_pdf_1)
        self.button_completer_1.pack()

        self.button_completer_2 = tk.Button(self, text="Completa PDF 2", command=self.completa_pdf_2)
        self.button_completer_2.pack()

        self.button_completer_3 = tk.Button(self, text="Completa PDF 3", command=self.completa_pdf_3)
        self.button_completer_3.pack()

        self.button_completer_4 = tk.Button(self, text="Completa PDF 4 (newShipping)", command=self.completa_pdf_4)
        self.button_completer_4.pack()

    def buscar_pdf_entrada(self):
        archivo = filedialog.askopenfilename(title="Seleccione el PDF de entrada", filetypes=[("PDF", "*.pdf")])
        self.entry_entrada.delete(0, tk.END)
        self.entry_entrada.insert(0, archivo)

    def buscar_pdf_salida(self):
        archivo = filedialog.askopenfilename(title="Seleccione el PDF de salida", filetypes=[("PDF", "*.pdf")])
        self.entry_salida.delete(0, tk.END)
        self.entry_salida.insert(0, archivo)

    def completa_pdf_1(self):
        pdf_entrada = self.entry_entrada.get()
        pdf_salida = self.entry_salida.get()
        pdf_completer = PDFCompleter1(pdf_entrada, pdf_salida)
        pdf_completer.run()

    def completa_pdf_2(self):
        pdf_entrada = self.entry_entrada.get()
        pdf_salida = self.entry_salida.get()
        pdf_completer = PDFCompleter2(pdf_entrada, pdf_salida)
        pdf_completer.run()

    def completa_pdf_3(self):
        pdf_entrada = self.entry_entrada.get()
        pdf_salida = self.entry_salida.get()
        pdf_completer = PDFCompleter3(pdf_entrada, pdf_salida)
        pdf_completer.run()

    def completa_pdf_4(self):
        shipping = newShipping()
        shipping.completar_formulario()

if __name__ == "__main__":
    aplicacion = Aplicacion()
    aplicacion.mainloop()