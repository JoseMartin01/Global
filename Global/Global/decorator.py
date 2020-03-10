from abc import ABC, abstractmethod

class Botana(ABC):
    """
    Define the interface for objects that can have responsibilities
    added to them dynamically.
    """

    @abstractmethod
    def agregarCondimento(self):
        pass


class Condimentos(Botana, ABC):
    """
    Maintain a reference to a Component object and define an interface
    that conforms to Component's interface.
    """

    def __init__(self, botana):
        self.botana = botana

    @abstractmethod
    def agregarCondimento(self, condimento):
        pass


class Cueritos(Condimentos):
    """
    Add responsibilities to the component.
    """

    def agregarCondimento(self):
        # ...
        self.imagen = "./imagenes/cueritos.png"
        self.botana.agregarCondimento()
        print("Agregando cueritos")
        # ...


class Jicama(Condimentos):
    """
    Add responsibilities to the component.
    """

    def agregarCondimento(self):
        # ...
        self.imagen = "./imagenes/jicama.png"
        self.botana.agregarCondimento()
        print("Agregando jicama")
        # ...

class Pepino(Condimentos):
    """
    Add responsibilities to the component.
    """

    def agregarCondimento(self):
        # ...
        self.imagen = "./imagenes/pepino.png"
        self.botana.agregarCondimento()
        print("Agregando pepino")
        # ...

class Mango(Condimentos):
    """
    Add responsibilities to the component.
    """

    def agregarCondimento(self):
        # ...
        self.imagen = "./imagenes/mango.png"
        self.botana.agregarCondimento()
        print("Agregando mango")
        # ...

class Cacahuate(Condimentos):
    """
    Add responsibilities to the component.
    """

    def agregarCondimento(self):
        # ...
        self.imagen = "./imagenes/cacahuate.png"
        self.botana.agregarCondimento()
        print("Agregando cacahuate")
        # ...

class DulcesTamarindo(Condimentos):
    """
    Add responsibilities to the component.
    """

    def agregarCondimento(self):
        # ...
        self.imagen = "./imagenes/dulcesTamarindo.png"
        self.botana.agregarCondimento()
        print("Agregando dulces tamarindo")
        # ...

class Chamoy(Condimentos):
    """
    Add responsibilities to the component.
    """

    def agregarCondimento(self):
        # ...
        self.imagen = "./imagenes/chamoy.png"
        self.botana.agregarCondimento()
        print("Agregando chamoy")
        # ...

class Salsa(Condimentos):
    """
    Add responsibilities to the component.
    """

    def agregarCondimento(self):
        # ...
        self.imagen = "./imagenes/salsa.png"
        self.botana.agregarCondimento()
        print("Agregando salsa")
        # ...

class Limon(Condimentos):
    """
    Add responsibilities to the component.
    """

    def agregarCondimento(self):
        # ...
        self.imagen = "./imagenes/limon.png"
        self.botana.agregarCondimento()
        print("Agregando limon")
        # ...

        
class Tostitos(Botana):
    """
    Define an object to which additional responsibilities can be
    attached.
    """
    def __init__(self):
        self.imagen = None

    def getImagen(self):
        return self.imagen

    def agregarCondimento(self):
        print("Agregando condimentos")


def main():
    tostitos = Tostitos()
    cueritos= Cueritos(tostitos)
    jicama = Jicama(cueritos)
    jicama.agregarCondimento()
    pepino = Pepino(jicama)
    pepino.agregarCondimento()
    mango = Mango(pepino)
    mango.agregarCondimento()
    cacahuate = Cacahuate(mango)
    cacahuate.agregarCondimento()
    dulcestamarindo = DulcesTamarindo(cacahuate)
    dulcestamarindo.agregarCondimento()
    chamoy = Chamoy(dulcestamarindo)
    chamoy.agregarCondimento()
    salsa = Salsa(chamoy)
    salsa.agregarCondimento()
    limon = Limon(salsa)
    limon.agregarCondimento()

if __name__ == "__main__":
    main()
