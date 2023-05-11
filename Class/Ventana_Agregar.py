from tkinter import *
from customtkinter import *
import customtkinter
import tkinter
from Empleado import Empleado
from tkinter import messagebox

class Ventana_Agregar(customtkinter.CTk,tkinter.Tk):
        def __init__(self):
            super().__init__()
            self.empresas = []
            self.geometry("600x512")
            self.title("Editar Nómina")
            self.config(background="#EDF2FA")
            self.grid_columnconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=2)

            self.label_nombre_empleado= customtkinter.CTkLabel(self, text="Nombre del empleado")
            self.label_nombre_empleado.grid(row=1, column=0, padx=3, pady=3,sticky="ew")

            self.label_edad_empleado= customtkinter.CTkLabel(self, text="Edad del empleado")
            self.label_edad_empleado.grid(row=2, column=0, padx=3, pady=3,sticky="ew")

            self.label_cargo_empleado= customtkinter.CTkLabel(self, text="Cargo del empleado")
            self.label_cargo_empleado.grid(row=3, column=0, padx=3, pady=3,sticky="ew")
            
            self.nombre_empleado = customtkinter.CTkEntry(self)
            self.nombre_empleado.grid(row=1, column=1,padx=3,pady=3, sticky="ew")

            self.edad_empleado = customtkinter.CTkEntry(self)
            self.edad_empleado.grid(row=2, column=1,padx=3,pady=3, sticky="ew")

            self.cargo_empleado = customtkinter.CTkEntry(self)
            self.cargo_empleado.grid(row=3, column=1,padx=3,pady=3, sticky="ew")


            self.boton_agregar_empleado = customtkinter.CTkButton(self, text="Agregar empleado", command=lambda: self.crearEmpleado(self.nombre_empleado, self.edad_empleado, self.cargo_empleado))
            self.boton_agregar_empleado.grid(row=4,column=1,padx=3, pady=3,sticky="ew")

        def crearEmpleado(self,nombre_empleado,edad_empleado,cargo_empleado):
            
            nombre_obj = nombre_empleado.get()
            edad_obj = edad_empleado.get()
            cargo_obj = cargo_empleado
            if nombre_obj != "" and edad_obj!= "":      
                nombre_empleado.configure(state=DISABLED)
                edad_empleado.configure(state=DISABLED)
                self.empresas.append(Empleado(nombre_obj, edad_obj, cargo_obj)) 
                messagebox.showinfo(message="Registro exitoso", title="Update")
                self.upload_data.configure(state="normal")
                    #Habilitar botón en el self principal para upload data manejar un flujo permisivo con estados de botones
                self.registrobutton.configure(state="disabled")  
            else:
                messagebox.showerror(message="Por favor llenar los datos necesarios", title="Warning")    
        

if __name__ == "__main__":
    va = Ventana_Agregar()
    va.mainloop()