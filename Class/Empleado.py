import random

class Empleado:
    
    def __init__(self, nombreEmpleado, edadEmpleado, cargoEmpleado):
        self.idEmpleado = random.randrange(0000,9999)
        self.nombreEmpleado = nombreEmpleado
        self.edadEmpleado = edadEmpleado
        self.cargoEmpleado = cargoEmpleado
    

