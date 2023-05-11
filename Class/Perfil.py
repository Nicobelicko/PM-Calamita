import tkinter as tk
import customtkinter
from customtkinter import *
import matplotlib

customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: blue (default), dark-blue, green
font_tuple1 = ("Times New Roman", 30)
font_tuple2 = ("Times New Roman", 15)
buttoncolor = "#45494f"
file_path = None


class Perfil(tk.Toplevel):
    def __init__(self):
        super().__init__()
        matplotlib.use("TkAgg")

        self.title("Calamita")
        self.fotosapo = tk.PhotoImage(file="images/Saposilueta.png")
        self.MINIfotosapo = tk.PhotoImage(file="images/MINISaposiluetaBlanco.png")
        self.iconphoto(False, self.fotosapo)
        self.geometry("1100x700")
        self.configure(background="#FFFFFF")
        self.rowconfigure(0, weight=0)
        self.columnconfigure((0, 2), weight=1)

        self.atrasbutton = customtkinter.CTkButton(
            self,
            width=100,
            height=20,
            border_width=0,
            corner_radius=8,
            command=self.destroy,
            text="Salir",
            fg_color="#000000",
            font=font_tuple2,
        )
        self.atrasbutton.place(x=10, y=20)

        self.nombre = customtkinter.CTkButton(
            self,
            state="DISABLED",
            width=250,
            height=42,
            bg_color="#FFFFFF",
            fg_color="#042f66",
            font=("Arial", 16),
            text="Aca va el nombre del empleado",
        )
        self.nombre.place(x=30, y=100)
        self.salarioBase = customtkinter.CTkButton(
            self,
            state="DISABLED",
            width=200,
            height=32,
            text=("Sueldo:"),  # Poner varible sueldo
            bg_color="#FFFFFF",
            fg_color="#042f66",
            font=("Arial", 16),
        )
        self.salarioBase.place(x=55, y=350)

        self.tContrato = customtkinter.CTkButton(
            self,
            text=("Contrato: "),  # Poner varible contrato
            state="DISABLED",
            width=200,
            height=32,
            bg_color="#FFFFFF",
            fg_color="#042f66",
            font=("Arial", 16),
        )
        self.tContrato.place(x=55, y=250)
        self.anosenempresa = customtkinter.CTkButton(
            self,
            text=(
                "Tiempo Laborado: "
            ),  # Poner varible de tiempo que lleva el trabajdor en la emnpresa
            state="DISABLED",
            width=200,
            height=32,
            bg_color="#FFFFFF",
            fg_color="#042f66",
            font=("Arial", 16),
        )
        self.anosenempresa.place(x=55, y=450)
        self.anosdelempleado = customtkinter.CTkButton(
            self,
            text=("años del empleado" + "Años"),  ##Poner varible años del empleado
            state="DISABLED",
            width=250,
            height=42,
            bg_color="#FFFFFF",
            fg_color="#042f66",
            font=("Arial", 16),
        )
        self.anosdelempleado.place(x=600, y=100)
        self.cesantias = customtkinter.CTkButton(
            self,
            text=(
                "Cesantias"
            ),  # Realizar formula cesantias cesantias = (salriobase)*diastrabajados/360
            state="DISABLED",
            width=200,
            height=32,
            bg_color="#FFFFFF",
            fg_color="#042f66",
            font=("Arial", 16),
        )
        self.cesantias.place(x=625, y=250)
        self.primas = customtkinter.CTkButton(
            self,
            text=("Primas"),
            state="DISABLED",
            width=200,
            height=32,
            bg_color="#FFFFFF",
            fg_color="#042f66",
            font=("Arial", 16),
        )
        self.primas.place(x=625, y=350)
        self.vaciones = customtkinter.CTkButton(
            self,
            text=("Vaciones: "),
            state="DISABLED",
            width=200,
            height=32,
            bg_color="#FFFFFF",
            fg_color="#042f66",
            font=("Arial", 16),
        )
        self.vaciones.place(x=625, y=450)
        self.titulo = customtkinter.CTkButton(
            self,
            text="Perfil del Empleado",
            state="DISABLED",
            width=250,
            height=52,
            bg_color="#FFFFFF",
            fg_color="#042f66",
            font=("Arial", 16),
        )
        self.titulo.place(x=315, y=20)


if __name__ == "__main__":
    ventana = Perfil()
    ventana.mainloop()
