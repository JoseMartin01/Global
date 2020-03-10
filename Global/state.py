from abc import ABC, abstractmethod

class Ciudad():
    """
    Define the interface of interest to clients.
    Maintain an instance of a ConcreteState subclass that defines the
    current state.
    """

    def __init__(self, stateWeather):
        self.imagen = None
        self.stateWeather = stateWeather

    def getImagen(self):
        return self.imagen
    
    def cambiar(self):
        self.stateWeather.cambiar()


class StateWeather(ABC):
    @abstractmethod
    def cambiar(self, estado):
        pass        
        if estado== "Soleado":
            return Soleado()
        if estado == "Nublado":
            return Nublado()
        if estado == "Lluvioso":
            return Lluvioso()
        if estado == "Nevado":
            return Nevado()


class Soleado(StateWeather):
    """
    Implement a behavior associated with a state of the Context.
    """
    def __init__(self):
        self.imagen = "./imagenes/nySoleado.jfif"
    
    def cambiar(self):
        print("Cambiar a estado soleado")


class Nublado(StateWeather):
    """
    Implement a behavior associated with a state of the Context.
    """
    def __init__(self):
        self.imagen = "./imagenes/nyNublado.jpg"

    def cambiar(self):
        print("Cambiar a estado nublado")

class Lluvioso(StateWeather):
    """
    Implement a behavior associated with a state of the Context.
    """

    def __init__(self):
        self.imagen = "./imagenes/nyLluvioso.jpg"

    def cambiar(self):
        print("Cambiar a estado lluvioso")

class Nevado(StateWeather):
    """
    Implement a behavior associated with a state of the Context.
    """

    def __init__(self):
        self.imagen = "./imagenes/nyNevado.jpg"

    def cambiar(self):
        print("Cambiar a estado nevado")


def main():
    soleado = Soleado()
    ciudad = Ciudad(soleado)
    ciudad.cambiar()

    nublado = Nublado()
    ciudad = Ciudad(nublado)
    ciudad.cambiar()

    lluvioso = Lluvioso()
    ciudad = Ciudad(lluvioso)
    ciudad.cambiar()

    nevado = Nevado()
    ciudad = Ciudad(nevado)
    ciudad.cambiar()

if __name__ == "__main__":
  soleado = Soleado()
  soleado.cambiar()

  nublado = Nublado()
  nublado.cambiar()

  lluvioso = Lluvioso()
  lluvioso.cambiar()

  nevado = Nevado()
  nevado.cambiar()

  
