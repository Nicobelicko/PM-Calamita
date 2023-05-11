from tkinter import *
from customtkinter import *
import customtkinter
import tkinter
from Empleado import Empleado
from tkinter import messagebox
import pandas as pd

class Ventana_Agregar(customtkinter.CTk,tkinter.Tk):
        def __init__(self, lista):
            super().__init__()
            self.listaEmpresas = lista
            self.geometry("600x512")
            self.title("Editar Nómina")
            self.config(background="#EDF2FA")
            self.grid_columnconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=2)

            self.label_sueldo_empleado= customtkinter.CTkLabel(self, text="Sueldo del empleado")
            self.label_sueldo_empleado.grid(row=1, column=0, padx=3, pady=3,sticky="ew")

            self.label_casado_empleado= customtkinter.CTkLabel(self, text="Casado")
            self.label_casado_empleado.grid(row=2, column=0, padx=3, pady=3,sticky="ew")

            self.label_carro_empleado= customtkinter.CTkLabel(self, text="Carro")
            self.label_carro_empleado.grid(row=3, column=0, padx=3, pady=3,sticky="ew")

            self.label_hijos_empleado= customtkinter.CTkLabel(self, text="Número de hijos del empleado")
            self.label_hijos_empleado.grid(row=4, column=0, padx=3, pady=3,sticky="ew")

            self.label_alq_prop_empleado= customtkinter.CTkLabel(self, text="Vivienda")
            self.label_alq_prop_empleado.grid(row=5, column=0, padx=3, pady=3,sticky="ew")

            self.label_sindicato_empleado= customtkinter.CTkLabel(self, text="Sindicato")
            self.label_sindicato_empleado.grid(row=6, column=0, padx=3, pady=3,sticky="ew")

            self.label_incapacidades_empleado= customtkinter.CTkLabel(self, text="Número de incapacidades del empleado")
            self.label_incapacidades_empleado.grid(row=7, column=0, padx=3, pady=3,sticky="ew")

            self.label_antiguedad_empleado= customtkinter.CTkLabel(self, text="Antiguedad del empleado")
            self.label_antiguedad_empleado.grid(row=8, column=0, padx=3, pady=3,sticky="ew")

            self.label_sexo_empleado= customtkinter.CTkLabel(self, text="Sexo del empleado")
            self.label_sexo_empleado.grid(row=9, column=0, padx=3, pady=3,sticky="ew")
            
            self.sueldo_empleado = customtkinter.CTkEntry(self)
            self.sueldo_empleado.grid(row=1, column=1,padx=3,pady=3, sticky="ew")

            self.casado_combobox = customtkinter.CTkComboBox(self, values=["Sí","No"])
            self.casado_combobox.grid(row=2, column=1,padx=3,pady=3, sticky="ew")

            self.carro_combobox = customtkinter.CTkComboBox(self, values=["Sí","No"])
            self.carro_combobox.grid(row=3, column=1,padx=3,pady=3, sticky="ew")

            self.hijos_empleado = customtkinter.CTkEntry(self)
            self.hijos_empleado.grid(row=4, column=1,padx=3,pady=3, sticky="ew")

            self.alq_prop_combobox = customtkinter.CTkComboBox(self, values=["Alquiler","Prop"])
            self.alq_prop_combobox.grid(row=5, column=1,padx=3,pady=3, sticky="ew")

            self.sindicato_combobox = customtkinter.CTkComboBox(self, values=["Sí","No"])
            self.sindicato_combobox.grid(row=6, column=1,padx=3,pady=3, sticky="ew")

            self.incapacidades_empleado = customtkinter.CTkEntry(self)
            self.incapacidades_empleado.grid(row=7, column=1,padx=3,pady=3, sticky="ew")

            self.antiguedad_empleado = customtkinter.CTkEntry(self)
            self.antiguedad_empleado.grid(row=8, column=1,padx=3,pady=3, sticky="ew")

            self.sexo_combobox = customtkinter.CTkComboBox(self, values=["H","M"])
            self.sexo_combobox.grid(row=9, column=1,padx=3,pady=3, sticky="ew")



            self.boton_agregar_empleado = customtkinter.CTkButton(self, text="Agregar empleado", command=lambda: self.crearEmpleado(self.sueldo_empleado,self.casado_combobox,self.carro_combobox,self.hijos_empleado,self.alq_prop_combobox,self.sindicato_combobox,self.incapacidades_empleado,self.antiguedad_empleado,self.sexo_combobox))
            self.boton_agregar_empleado.grid(row=10,column=1,padx=3, pady=3,sticky="ew")

        def crearEmpleado(self,sueldo_empleado,Casado,Carro,hijos_empleado,Alq_Prop,Sindicato,incapacidades_empleado,Antiguedad,Sexo):
            
            valor_sueldo = sueldo_empleado.get()
            valor_Casado = Casado.get()
            valor_Carro = Carro.get()
            valor_hijos_empleado = hijos_empleado.get()
            valor_Alq_Prop = Alq_Prop.get()
            valor_Sindicato = Sindicato.get()
            valor_incapacidades_empleado = incapacidades_empleado.get()
            valor_Antiguedad = Antiguedad.get()
            valor_Sexo = Sexo.get()

            lista_aux = [(valor_sueldo,valor_Casado,valor_Carro,valor_hijos_empleado,valor_Alq_Prop,valor_Sindicato,valor_incapacidades_empleado,valor_Antiguedad,valor_Sexo)]

            df = pd.DataFrame(lista_aux, columns= ['Sueldo','Casado','Carro','Hijos','Alq_Prop','Sindicato','Incapacidades','Antiguedad','Sexo'])


            if valor_sueldo != "" and valor_Casado!= "" and valor_Carro!= ""  and valor_hijos_empleado!= ""  and valor_Alq_Prop!= ""  and valor_Sindicato!= ""  and valor_incapacidades_empleado!= ""  and valor_Antiguedad!= ""  and valor_Sexo!= "":      
                self.listaEmpresas[0].listaEmpleados = self.listaEmpresas[0].listaEmpleados.append(df, ignore_index=True)
               
                messagebox.showinfo(message="Registro exitoso", title="Update") 
            else:
                messagebox.showerror(message="Por favor llenar los datos necesarios", title="Warning")    
        

if __name__ == "__main__":
    va = Ventana_Agregar()
    va.mainloop()