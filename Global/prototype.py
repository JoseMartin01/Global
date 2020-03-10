from abc import ABC, abstractmethod

class Cliente():
    """
    Define the interface of interest to clients.
    Maintain an instance of a ConcreteState subclass that defines the
    current state.
    """

    def __init__(self, mouse):
        self.mouse = mouse
    
    def crear(self):
        self.mouse.crear()
        pass

    def clonar(self):
        self.mouse.clonar()
        pass

class Mouse(ABC):
    color='Blanco'
    marca='Apple'
    @abstractmethod
    def crear(self):
        pass        
        
    @abstractmethod
    def clonar(self):
        pass

class MouseAlambrico(Mouse):
    """
    Implement a behavior associated with a state of the Context.
    """
    def __init__(self):
        self.imagen = "./imagenes/mouseAlambrico.jpg"
    
    def crear(self):
        print('Color: ',Mouse.color)
        print('Marca: ',Mouse.marca)
        print("Crear mouse alambrico")

    def clonar(self):
        print('Color: ',Mouse.color)
        print('Marca: ',Mouse.marca)
        print("Clonar mouse alambrico")


class MouseInalambrico(Mouse):
    """
    Implement a behavior associated with a state of the Context.
    """
    def __init__(self):
        self.imagen = "./imagenes/mouseInalambrico.jfif"

    def crear(self):
        print('Color: ',Mouse.color)
        print('Marca: ',Mouse.marca)
        print("Crear mouse inalambrico")


    def clonar(self):
        print('Color: ',Mouse.color)
        print('Marca: ',Mouse.marca)
        print("Clonar mouse inalambrico")


if __name__ == "__main__":
  mouseAlambrico = MouseAlambrico()
  mouseAlambrico.crear()
  mouseAlambrico = MouseAlambrico()
  mouseAlambrico.clonar()
  
  mouseInalambrico = MouseInalambrico()
  mouseInalambrico.crear()
  mouseInalambrico = MouseInalambrico()
  mouseInalambrico.clonar()



