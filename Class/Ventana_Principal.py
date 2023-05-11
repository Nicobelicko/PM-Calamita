import tkinter
import customtkinter
from customtkinter import *
from Ventana_Perfilamiento import Ventana_Perfilamiento
from PIL import Image, ImageTk
from Empleado import Empleado
import pandas as pd

font_tuple1 = ("bold",30)
font_tuple2 = ("bold",15)
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
listaEmpresas = []


class Ventana_Principal(tkinter.Toplevel):

    def __init__(self, lista):
        super().__init__()
        listaEmpresas = lista
        self.geometry("600x512")
        self.title("Calamita")
        self.config(background="#EDF2FA")
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0,1,2), weight=1)

        self.fotosapo = tkinter.PhotoImage(file="images/MINISaposiluetaBlanco.png")
        self.icono_button_visualizar = tkinter.PhotoImage(file="icons/icon_visualizar.png")
        self.icono_button_perfilamiento = tkinter.PhotoImage(file="icons/icon_perfil.png")
        self.icono_button_editar = tkinter.PhotoImage(file="icons/icon_editar.png")

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0,fg_color="#09184d")
        self.sidebar_frame.grid(row=0, column=0, rowspan=3, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure((0,1,2,3),weight=1)

     
        self.boton_visualizar = customtkinter.CTkButton(self.sidebar_frame, command=self.click_visualizar,image=self.icono_button_visualizar, text="", font=font_tuple2, fg_color="#ffffff", hover_color="#7b5bf2", border_width=5,border_color="#ffffff")
        self.boton_visualizar.grid(row=0, column=0, padx=20, pady=0)
        self.boton_visualizar.bind('<Enter>',self.hover_boton_visualizar)
        self.boton_visualizar.bind('<Leave>',self.leave_boton_visualizar)

        self.boton_perfilamiento_empleados = customtkinter.CTkButton(self.sidebar_frame, command=self.click_perfilamiento_empleados,image=self.icono_button_perfilamiento,text="", font= font_tuple2, fg_color="#ffffff",border_width=5, border_color="#ffffff")
        self.boton_perfilamiento_empleados.grid(row=1, column=0, padx=20, pady=0)
        self.boton_perfilamiento_empleados.bind('<Enter>',self.hover_boton_perfilar_empleados)
        self.boton_perfilamiento_empleados.bind('<Leave>',self.leave_boton_perfilar_empleados)

        self.boton_editar_nomina = customtkinter.CTkButton(self.sidebar_frame, command=self.click_editar_nomina,image=self.icono_button_editar, text="", font= font_tuple2,fg_color="#ffffff",border_width=5, border_color="#ffffff")
        self.boton_editar_nomina.grid(row=2, column=0, padx=20, pady=0)
        self.boton_editar_nomina.bind('<Enter>',self.hover_boton_editar_nomina)
        self.boton_editar_nomina.bind('<Leave>',self.leave_boton_editar_nomina)

        


    def click_visualizar(self):
        print("click en visualizar")
    
    def click_perfilamiento_empleados(self):
        Ventana_Perfilamiento(listaEmpresas)


    def click_editar_nomina(self):
        print("click editar nómina")

    def hover_boton_visualizar(self, btn):
        self.boton_visualizar.configure(border_color="black")
        self.boton_visualizar.configure(fg_color="#7b5bf2")
        
        
        
    def leave_boton_visualizar(self, btn):
        self.boton_visualizar.configure(border_color="#ffffff")
        self.boton_visualizar.configure(fg_color="#ffffff")
        self.boton_visualizar.configure(text="")
        self.boton_visualizar.configure(image=self.icono_button_visualizar)
        
    def hover_boton_perfilar_empleados(self, btn):
        self.boton_perfilamiento_empleados.configure(border_color="black")
        self.boton_perfilamiento_empleados.configure(fg_color="#7b5bf2")
        
    def leave_boton_perfilar_empleados(self, btn):
        self.boton_perfilamiento_empleados.configure(border_color="#ffffff")
        self.boton_perfilamiento_empleados.configure(fg_color="#ffffff")

    def hover_boton_editar_nomina(self, btn):
        self.boton_editar_nomina.configure(border_color="black")
        self.boton_editar_nomina.configure(fg_color="#7b5bf2")
        
    def leave_boton_editar_nomina(self, btn):
        self.boton_editar_nomina.configure(border_color="#ffffff")
        self.boton_editar_nomina.configure(fg_color="#ffffff")
 
    def ventana_subir_datos(self):
        newWindow = customtkinter.CTkToplevel(self)
        newWindow.geometry("600x512")
        newWindow.title("Subir datos")
        newWindow.config(background="#EDF2FA")

    def openFileExplorer(self):
        filetypes = (
            ('Excel','*.xlsx'),
            ('CSV','*.csv')
        )
        file_path = askopenfile(mode='r', filetypes=filetypes)
        if file_path is not None:
            if file_path.name.endswith(".csv"):
                listaEmpleados = pd.read_csv(file_path.name)
            
                messagebox.showinfo(message="Subida exitosa, archivo: "+file_path.name, title="Update")

            elif file_path.name.endswith(".xlsx"):
                listaEmpleados = pd.read_excel(file_path.name, sheet_name=0)
                messagebox.showinfo(message="Subida exitosa, archivo: "+file_path.name, title="Update")
               
            else:
                messagebox.showerror(message="Solo son validos formatos xlsx o csv", title="Warning")


if __name__ == "__main__":
    vp = Ventana_Principal()
    vp.mainloop()


    ##AVISO, QUEDASTE EN QUE IBAS A HACER LOS BOTONES CON TKINTER NORMAL PARA VER SI LA ANIMACIÓN POR DEFECTO SE QUITA
    