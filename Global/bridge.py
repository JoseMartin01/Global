import abc

class Color(metaclass=abc.ABCMeta):
    def __init__(self):
        self.name = None
        
    @abc.abstractmethod
    def fill_color(self):
        pass

    def getColor(self):
        return self.name;

class Forma(metaclass=abc.ABCMeta):
    def __init__(self, color):
        self.color = color
        self.imagen = None


    @abc.abstractmethod
    def color_it(self):
        pass

    def getImagen(self):
        return self.imagen

class Cubo(Forma):
    def __init__(self, color):
        super(Cubo, self).__init__(color)
        self.name = 'cubo'
        if color.name == 'amarillo':
            self.imagen = "./imagenes/cuboAmarillo.jpg"
            print ('Forma Cubo Amarillo')
        if color.name == 'azul':
            self.imagen = "./imagenes/cuboAzul.jpg"
            print('Forma cubo Azul')

    def color_it(self):
        print("Cubo relleno con ", end="")
        self.color.fill_color()

class Esfera(Forma):
    def __init__(self, color):
        super(Esfera, self).__init__(color)
        self.name = 'esfera'
        if color.name == 'amarillo':
            self.imagen = "./imagenes/esferaAmarilla.jpg"
            print ('Forma Esfera Amarilla')
        if color.name == 'azul':
            self.imagen = "./imagenes/esferaAzul.jpg"
            print('Forma Esfera Azul')

    def color_it(self):
        print("Esfera rellena con ", end="")
        self.color.fill_color()

class Amarillo(Color):
    def fill_color(self):
        print("Amarillo")

class Azul(Color):
    def fill_color(self):
        print("Azul")

if __name__ == '__main__':
    s1 = Cubo(Amarillo())
    s1.color_it()
    s1 = Cubo(Azul())
    s1.color_it()

    s2 = Esfera(Amarillo())
    s2.color_it()
    s2 = Esfera(Azul())
    s2.color_it()
