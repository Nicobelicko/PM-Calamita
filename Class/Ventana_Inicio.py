import tkinter
import customtkinter
from customtkinter import *
from Ventana_Principal import Ventana_Principal
from Empresa import Empresa
import pandas as pd
from tkinter import messagebox

class Ventana_Inicio(customtkinter.CTk,tkinter.Tk):
    listaEmpleados = pd.DataFrame()
    listaEmpresas = []
    def __init__(self):
        super().__init__()
        self.geometry("600x512")
        self.title("Subir datos")
        self.config(background="#EDF2FA")
        

        self.label_nombre_empresa = customtkinter.CTkLabel(self, text="Nombre Empresa")
        self.label_nombre_empresa.grid(row=0, column=0)

        self.label_sector_empresa = customtkinter.CTkLabel(self, text="Sector Empresa")
        self.label_sector_empresa.grid(row=1, column=0)

        self.nombre_empresa = customtkinter.CTkEntry(self)
        self.nombre_empresa.grid(row=0, column=1)

        self.sector_empresa = customtkinter.CTkEntry(self)
        self.sector_empresa.grid(row=1, column=1)

        self.boton_subir_datos = customtkinter.CTkButton(self, text="Crear Empresa", command= lambda: self.createEmpresa(self.nombre_empresa, self.sector_empresa))
        self.boton_subir_datos.grid(row=2,column=2, sticky="nsew")

    
    def subir_datos(self):
        
        filetypes = (
            ('Excel','*.xlsx'),
            ('CSV','*.csv')
        )
        file_path = tkinter.filedialog.askopenfile(mode='r', filetypes=filetypes)
        if file_path is not None:
            if file_path.name.endswith(".csv"):
                self.listaEmpleados = pd.read_csv(file_path.name)
                tkinter.messagebox.showinfo(message="Subida exitosa, archivo: "+file_path.name, title="Update")
                
            elif file_path.name.endswith(".xlsx"):
                self.listaEmpleados = pd.read_excel(file_path.name, sheet_name=0)
                tkinter.messagebox.showinfo(message="Subida exitosa, archivo: "+file_path.name, title="Update")
                
            else:
                messagebox.showerror(message="Solo son validos formatos xlsx o csv", title="Warning")

        

    def createEmpresa(self,nombre_empresa,sector_empresa):
            name_obj = nombre_empresa.get()
            sector_obj = sector_empresa.get()
            
            messagebox.showinfo(message="Ahora debes cargar el archivo con los datos de tus empleados", title="Update")
            self.subir_datos()
            self.listaEmpresas.append(Empresa(name_obj, sector_obj, self.listaEmpleados))
            self.abrir_ventana_principal(self.listaEmpresas)

    def abrir_ventana_principal(self, lista):
        vp = Ventana_Principal(lista)
        vp.mainloop()



if __name__ == "__main__":
    vsd = Ventana_Inicio()
    vsd.mainloop()