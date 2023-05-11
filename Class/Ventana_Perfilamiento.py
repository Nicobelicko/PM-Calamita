import tkinter
from tkinter import *
from tkinter import messagebox
from Empresa import Empresa
from tkinter.filedialog import askopenfile 
import pandas as pd
from pandastable import Table
import matplotlib.pyplot as plt
import matplotlib
import customtkinter
#from Ventana_Principal import Ventana_Principal
# https://github.com/TomSchimansky/CustomTkinter/wiki
#customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
font_tuple1 = ("Times New Roman",30)
font_tuple2 = ("Times New Roman",15)
buttoncolor ="#45494f"
file_path = None 


class Ventana_Perfilamiento(tkinter.Toplevel):
        
        def __init__(self, lista):
            super().__init__() 
            matplotlib.use('TkAgg')
            self.listaEmpresas = lista
            
            self.title("Calamita")
            self.fotosapo = tkinter.PhotoImage(file='images/SaposiluetaBlanco.png')
            self.MINIfotosapo = tkinter.PhotoImage(file='images/MINISaposiluetaBlanco.png')  
            self.iconphoto(False,self.fotosapo)
            self.geometry("600x512")
            self.configure(background="#23272a")
            self.rowconfigure(0, weight=0)
            self.columnconfigure((0,2),weight=1)

            customtkinter.CTkButton(self, image=self.MINIfotosapo,text="",fg_color="#23272a",state="DISABLED").grid(column=1,row=2) #imagen sapo
            customtkinter.CTkLabel(self,width=250,height=52,text="CALAMITA", fg_color="#23272a",text_color="#FFFFFF",font=font_tuple1).grid(column=1,row=3)
           
           
            customtkinter.CTkButton(self,width=250,height=52,border_width=0,corner_radius=8,command=self.helpWindow, text="Ayuda",fg_color=buttoncolor,font=font_tuple2).grid(column=2,row=4,pady=20)
            
            self.clustering = customtkinter.CTkButton(self,width=250,height=52,border_width=0,corner_radius=8, command=self.clusteringModel, text= "Perfilar base de datos",state="DISABLED",fg_color=buttoncolor,font=font_tuple2)
            self.clustering.grid(column=0,row=2,pady=20)

            self.predictive = customtkinter.CTkButton(self,width=250,height=52,border_width=0,corner_radius=8, command=self.predictiveModel, text= "Modelo predictivo",state="DISABLED",fg_color=buttoncolor,font=font_tuple2)
            self.predictive.grid(column=0,row=3,pady=20)

            self.exportButton = customtkinter.CTkButton(self,width=250,height=52,border_width=0,corner_radius=8, command=self.exportModels, text= "Descargar bundle de modelos",state="DISABLED",fg_color=buttoncolor,font=font_tuple2)
            self.exportButton.grid(column=2,row=2,pady=20)

            self.exportDataButton = customtkinter.CTkButton(self,width=250,height=52,border_width=0,corner_radius=8, command=self.exportData, text= "Exportar el perfilado a excel",state="DISABLED",fg_color=buttoncolor,font=font_tuple2)
            self.exportDataButton.grid(column=2,row=3,pady=20)

            self.analisisButton = customtkinter.CTkButton(self,width=250,height=52,border_width=0,corner_radius=8, command=self.dataAnalysis,text="Analizar datos",state="DISABLED",fg_color=buttoncolor,font=font_tuple2)
            self.analisisButton.grid(column=0,row=4,pady=20)

            self.preparacion_automatica()
        

        
    #region normal WorkFlow
        def helpWindow(self):
            messagebox.showinfo("Ayuda funcionamiento", "1. Registrarse \n 2. Subir los datos de la empresa \n 3. Puedes analizar los datos ingresados con un CRUD integrado de excel \n 4. Realizar el entrenamiento de los modelos de clustering y luego el modelo predictivo \n 5. Se habilita la opción de descargar un bundle (Pickle) de los modelos \n 6.Descargar la data con los clusters calculados")

        
        def preparacion_automatica(self):
            self.listaEmpresas[0].preparacionData()
            self.analisisButton.configure(state="normal")
            self.clustering.configure(state="normal")
               
                    
        def exportModels(self):
            self.listaEmpresas[0].exportModels()
            messagebox.showinfo(message="Pickle descargado", title="Update")
        
        def exportData(self):
            self.listaEmpresas[0].exportData()
            messagebox.showinfo(message="Excel exportado", title="Update")
    
        def dataAnalysis(self):
            data = self.listaEmpresas[0].dataStatistics() #data.describe() #Buscar como mostrar el describe
            f = customtkinter.CTkToplevel(self)
            table = pt = Table(f, dataframe=self.listaEmpresas[0].data,
                                        showtoolbar=True, showstatusbar=True)
            pt.show()
            if "Clusters" in self.listaEmpresas[0].data:
                data_tmp = self.listaEmpresas[0].data
                #centroids_datafralistaEmpresas[0].clusterDescription()
                #clusters_profiling = Toplevel(self)
                #table = pc = Table(clusters_profiling, dataframe=centroids_dataframe)
                #pc.show()
                plt.figure("Clusters en pie chart")
                labels = ["C1","C2","C3","C4","C5"]
                values=self.listaEmpresas[0].data['Clusters'].value_counts() 
                plt.pie(self.listaEmpresas[0].data['Clusters'].value_counts(),labels=["C1","C2","C3","C4","C5"],autopct=lambda p : '{:.2f}%  ({:,.0f})'.format(p,p * sum(values)/100))
                #plt.xlabel("Clusters")
                #plt.ylabel("# de clusters")
                plt.title("Distribución de clusters")
                plt.show()
                
                #centroids_datafralistaEmpresas[0].clusterDescription()
                #clusters_profiling = Toplevel(self)
                #table = pc = Table(clusters_profiling, dataframe=centroids_dataframe)
                #pc.show()
                bar_chart = plt.figure(figsize=(10,5))
                plt.bar(["C1","C2","C3","C4","C5"], [data_tmp[data_tmp.Clusters == 0].shape[0],data_tmp[data_tmp.Clusters == 1].shape[0],data_tmp[data_tmp.Clusters == 2].shape[0],data_tmp[data_tmp.Clusters == 3].shape[0],data_tmp[data_tmp.Clusters == 4].shape[0]])
                plt.xlabel("Clusters")
                plt.ylabel("# de empleados por cluster")
                plt.title("Distribución de clusters")
                plt.show()
            
            
        #endregion
        
        #region ML Models
        def clusteringModel(self):
            self.listaEmpresas[0].clusteringModel()
            self.predictive.configure(state="normal")
            self.exportDataButton.configure(state="normal")
            
        def predictiveModel(self):
            self.listaEmpresas[0].predictiveModel()
            self.exportButton.configure(state="normal")
        #endregion
        
        
        
if __name__ == "__main__":
    p = Ventana_Perfilamiento()
    p.mainloop()
    

