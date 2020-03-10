import abc

#
# Receiver
# knows how to perform the operations associated 
# with carrying out a request
#
class Laptop:
  def apagar(self):
    print("Apagando laptop")
  def reiniciar(self):
    print("Reiniciando laptop")
  def suspender(self):
    print("Suspendiendo laptop")
  def encender(self):
    print("Encendiendo Laptop")

#
# Command
# declares an interface for all commands
#
class Command(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def execute(self):
    pass

#
# Concrete Command
# implements execute by invoking the corresponding 
# operation(s) on Receiver 
#
class LaptopSuspender(Command):
  
  def __init__(self, laptop):
    self.laptop = laptop

  def execute(self):
    self.laptop.suspender()
    print("Recibiendo señal")

class LaptopEncender(Command):
  def __init__(self, laptop):
    self.laptop = laptop

  def execute(self):
    self.laptop.encender()
    print("Recibiendo señal")

class LaptopApagar(Command):
  def __init__(self, laptop):
    self.laptop = laptop

  def execute(self):
    self.laptop.apagar()
    print("Recibiendo señal")

class LaptopReiniciar(Command):
  def __init__(self, laptop):
    self.laptop = laptop

  def execute(self):
    self.laptop.reiniciar()
    print("Recibiendo señal")

#
# Invoker
# asks the command to carry out the request
#
class MenuAcciones:
  def __init__(self):
      self.command = None  

  
  def set(self, command):
    self.command = command

  def confirm(self):
    if (self.command is not None):
      self.command.execute()


if __name__ == "__main__":
  laptop = Laptop()
  command = MenuAcciones()
  command.set(LaptopEncender(laptop))
  command.confirm()

