class Automovil():
    def __init__(self):
        self.imagen = None

    def getImagen(self):
        return self.imagen


class Nissan(Automovil):
    def __init__(self):
        self.imagen = "./imagenes/sentra.png"
        print ('Creando un auto Nissan')

class Chevrolet(Automovil):
    def __init__(self):
        self.imagen = "./imagenes/spark.jfif"
        print ('Creando un auto Chevrolet')

class Factory:
     def getAutomovil(self, tipo):
        
        if tipo== "Nissan":
            return Nissan()
        if tipo == "Chevrolet":
            return Chevrolet()
