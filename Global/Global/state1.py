from abc import ABC, abstractmethod

class Agua():
    """
    Define the interface of interest to clients.
    Maintain an instance of a ConcreteState subclass that defines the
    current state.
    """

    def __init__(self, state):
        self.imagen = None
        self.state = state

    def getImagen(self):
        return self.imagen
    
    def cambiar(self):
        self.state.cambiar()


class State(ABC):
    @abstractmethod
    def cambiar(self):
        pass        


class Solido(State):
    """
    Implement a behavior associated with a state of the Context.
    """
    def __init__(self):
        self.imagen = "./imagenes/solido.jpg"
    
    def cambiar(self):
        print("Cambiar a estado solido")


class Liquido(State):
    """
    Implement a behavior associated with a state of the Context.
    """
    def __init__(self):
        self.imagen = "./imagenes/liquido.jpg"

    def cambiar(self):
        print("Cambiar a estado liquido")

class Gaseoso(State):
    """
    Implement a behavior associated with a state of the Context.
    """

    def __init__(self):
        self.imagen = "./imagenes/gaseoso.jpg"

    def cambiar(self):
        print("Cambiar a estado gaseoso")


def main():
    solido = Solido()
    agua = Agua(solido)
    agua.cambiar()

    liquido = Liquido()
    agua = Agua(liquido)
    agua.cambiar()

    gaseoso = Gaseoso()
    agua = Agua(gaseoso)
    agua.cambiar()

if __name__ == "__main__":
  solido = Solido()
  solido.cambiar()

  #liquido = Liquido()
  #liquido.cambiar()

  #gaseoso = Gaseoso()
  #gaseoso.cambiar()


  
