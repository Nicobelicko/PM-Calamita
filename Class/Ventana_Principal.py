import tkinter
import customtkinter
from customtkinter import *
from PIL import Image, ImageTk
from Class.Ventana_Perfilamiento import Ventana_Perfilamiento
font_tuple1 = ("bold",30)
font_tuple2 = ("bold")
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")


class Ventana_Principal(customtkinter.CTk, tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("600x512")
        self.title("Calamita")
        self.config(background="#EDF2FA")
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0,1,2), weight=1)

        fotosapo = tkinter.PhotoImage(file="images/MINISaposiluetaBlanco.png")
        icono_button_visualizar = tkinter.PhotoImage(file="icons/icon_visualizar.png")
        icono_button_perfilamiento = tkinter.PhotoImage(file="icons/icon_perfil.png")
        icono_button_editar = tkinter.PhotoImage(file="icons/icon_editar.png")

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0,fg_color="#09184d")
        self.sidebar_frame.grid(row=0, column=0, rowspan=3, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure((0,1,2,3),weight=1)

     
        self.boton_visualizar = customtkinter.CTkButton(self.sidebar_frame, command=self.click_visualizar,image=icono_button_visualizar, text="", text_font=font_tuple2, fg_color="#ffffff", hover_color="#7b5bf2", border_width=5,border_color="#ffffff")
        self.boton_visualizar.grid(row=0, column=0, padx=20, pady=0)
        self.boton_visualizar.bind('<Enter>',self.hover_boton_visualizar)
        self.boton_visualizar.bind('<Leave>',self.leave_boton_visualizar)

        self.boton_perfilamiento_empleados = customtkinter.CTkButton(self.sidebar_frame, command=self.click_perfilamiento_empleados,image=icono_button_perfilamiento,text="", text_font= font_tuple2, fg_color="#ffffff", hover_color="#7b5bf2",border_width=5, border_color="#ffffff")
        self.boton_perfilamiento_empleados.grid(row=1, column=0, padx=20, pady=0)
        self.boton_perfilamiento_empleados.bind('<Enter>',self.hover_boton_perfilar_empleados)
        self.boton_perfilamiento_empleados.bind('<Leave>',self.leave_boton_perfilar_empleados)

        self.boton_editar_nomina = customtkinter.CTkButton(self.sidebar_frame, command=self.click_editar_nomina,image=icono_button_editar, text="", text_font= font_tuple2,fg_color="#ffffff", hover_color="#7b5bf2",border_width=5, border_color="#ffffff")
        self.boton_editar_nomina.grid(row=2, column=0, padx=20, pady=0)
        self.boton_editar_nomina.bind('<Enter>',self.hover_boton_editar_nomina)
        self.boton_editar_nomina.bind('<Leave>',self.leave_boton_editar_nomina)

        


    def click_visualizar(self):
        print("click en visualizar")
    
    def click_perfilamiento_empleados(self):
        print("click perfilamiento")

    def click_editar_nomina(self):
        print("click editar nómina")

    def hover_boton_visualizar(self, btn):
        self.boton_visualizar.configure(border_color="black")
        self.boton_visualizar.configure(text="Visualizar")
        
    def leave_boton_visualizar(self, btn):
        self.boton_visualizar.configure(border_color="#ffffff")
        self.boton_visualizar.configure(text="")
        
    def hover_boton_perfilar_empleados(self, btn):
        self.boton_perfilamiento_empleados.configure(border_color="black")
        self.boton_perfilamiento_empleados.configure(text="Perfilamiento")
        
    def leave_boton_perfilar_empleados(self, btn):
        self.boton_perfilamiento_empleados.configure(border_color="#ffffff")
        self.boton_perfilamiento_empleados.configure(text="")

    def hover_boton_editar_nomina(self, btn):
        self.boton_editar_nomina.configure(border_color="black")
        self.boton_editar_nomina.configure(text="Editar Nómina")
        
    def leave_boton_editar_nomina(self, btn):
        self.boton_editar_nomina.configure(border_color="#ffffff")
        self.boton_editar_nomina.configure(text="")
 
       



if __name__ == "__main__":
    vp = Ventana_Principal()
    vp.mainloop()


    ##AVISO, QUEDASTE EN QUE IBAS A HACER LOS BOTONES CON TKINTER NORMAL PARA VER SI LA ANIMACIÓN POR DEFECTO SE QUITA
    