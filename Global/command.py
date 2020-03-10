import abc

#
# Receiver
# knows how to perform the operations associated 
# with carrying out a request
#
class Laptop:
  def action(self):
    print("Laptop: ejecutar accion.")

#
# Command
# declares an interface for all commands
#
class Command(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def execute(self, accion):
    if accion == "Suspender":
      return Suspender
    if accion == "Apagar":
      return Apagar
    if accion == "Reiniciar":
      return Reiniciar
    pass

#
# Concrete Command
# implements execute by invoking the corresponding 
# operation(s) on Receiver 
#
class Suspender(Command):
  def __init__(self, laptop):
    self.imagen = "./imagenes/suspender.png"
    self.laptop = laptop

  def execute(self):
    self.laptop.action()
    print("")


class Apagar(Command):
  def __init__(self, laptop):
    self.imagen = "./imagenes/apagar.png"
    self.laptop = laptop

  def execute(self):
    self.laptop.action()
    print("Apagando el equipo...")

class Reiniciar(Command):
  def __init__(self, laptop):
    self.imagen = "./imagenes/reiniciar.png"
    self.laptop = laptop

  def execute(self):
    self.laptop.action()
    print("Reiniciando")

#
# Invoker
# asks the command to carry out the request
#
class Acciones:
  def __init__(self):
      self.imagen = None
      self.command = None  


  def getImagen(self):
    return self.imagen

  
  def set(self, command):
    self.command = command

  def confirm(self):
    if (self.command is not None):
      self.command.execute()


if __name__ == "__main__":
  laptop = Laptop()
  command = Suspender(laptop)

  laptop = Laptop()
  command = Apagar(laptop)

  laptop = Laptop()
  command = Reiniciar(laptop)

  acciones = Acciones()
  acciones.set(command)
  acciones.confirm()
