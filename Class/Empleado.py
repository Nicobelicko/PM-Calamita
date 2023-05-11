import random

class Empleado:
    
    def __init__(self,sueldo_empleado,Casado,Carro,hijos_empleado,Alq_Prop,Sindicato,incapacidades_empleado,Antiguedad,Sexo):
        self.idEmpleado = random.randrange(0000,9999)
        self.sueldo = sueldo_empleado
        self.Casado = Casado
        self.Carro =Carro
        self.hijos = hijos_empleado
        self.Alq_Prop = Alq_Prop
        self.Sindicato = Sindicato
        self.Incapacidades = incapacidades_empleado
        self.Antiguedad = Antiguedad
        self.Sexo = Sexo
    

