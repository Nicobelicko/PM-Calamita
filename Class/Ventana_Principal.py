import tkinter
import customtkinter


font_tuple1 = ("bold",30)
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")


class Ventana_Principal(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("600x512")
        self.title("Calamita")
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0,1,2), weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Calamita", text_font= font_tuple1)
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.boton_visualizar = customtkinter.CTkButton(self.sidebar_frame, command=self.click_visualizar, text="Visualizar nómina")
        self.boton_visualizar.grid(row=2, column=0, padx=20, pady=10)

        


    def click_visualizar(self):
        print("click en visualizar")

if __name__ == "__main__":
    vp = Ventana_Principal()
    vp.mainloop()