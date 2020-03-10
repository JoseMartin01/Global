from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QAction, QMdiSubWindow, QTextEdit, QLabel, QWidget, QComboBox, QRadioButton, QVBoxLayout, QPushButton, QHBoxLayout, QGridLayout
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap

import sys
from factory import *
from bridge import *
from command1 import*
from state1 import *
from decorator import *
from prototype import *
from abstractFactory import *

 
class MDIWindow(QMainWindow):
 
    count = 0
    countBridge = 5
    countCommand = 0
    countState = 0
    countDecorator = 0
    countPrototype = 0
    countAbstractFactory = 0




    def __init__(self):
        super().__init__()
 
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
 
        file = bar.addMenu("Patrones")
        file.addAction("Factory")
        file.addAction("Bridge")
        file.addAction("Command")
        file.addAction("State")
        file.addAction("Decorator")
        file.addAction("Prototype")
        file.addAction("AbstractFactory")


        file.triggered[QAction].connect(self.WindowTrig)
        self.setWindowTitle("Pantalla Principal")
 
    def WindowTrig(self, p):
 
#======================================================================================================================================================================
#Factory Window
        #print("Eleccion " + p.text())
        if p.text() == "Factory":
            sub = QMdiSubWindow()
            widget = QWidget()
            sub.resize(400,400)
            self.layoutFactory = QVBoxLayout(widget)
            self.layoutImagenes = QHBoxLayout()
            self.layoutImagenes.addStretch(1)

            labelTitulo = QLabel()
            labelTitulo.setText("Selecciona el carro")

            self.comboTipo = QComboBox()
            self.comboTipo.addItem("Nissan")
            self.comboTipo.addItem("Chevrolet")

            buttonCreate = QPushButton('Crear')
            buttonCreate.clicked.connect(self.button_factory_crear);
            self.layoutFactory.addWidget(labelTitulo)
            self.layoutFactory.addWidget(self.comboTipo)
            self.layoutFactory.addWidget(buttonCreate)
            self.layoutFactory.addLayout(self.layoutImagenes)

            sub.setWidget(widget)
            sub.setWindowTitle("Patrón Factory")
            self.mdi.addSubWindow(sub)
            sub.show()

#======================================================================================================================================================================
#Abstract Factory Window
        if p.text() == "AbstractFactory":
            subAbstractFactory = QMdiSubWindow()
            subAbstractFactory.resize(575, 443)
            widgetAbstractFactory = QWidget()
            self.gridAbstractLayout = QGridLayout(widgetAbstractFactory)
            self.gridAbstractLayout.setContentsMargins(0, 0, 0, 0)
            self.gridAbstractLayout.setObjectName("layoutAbstractFactory")

            labelFabricante = QLabel()
            labelFabricante.setText("Fabricante")
            self.gridAbstractLayout.addWidget(labelFabricante, 0, 0, 1, 1)


            labelTipo = QLabel()
            labelTipo.setText("Tipo")
            self.gridAbstractLayout.addWidget(labelTipo,1,0,1,1)


            self.comboFabricante = QComboBox()
            self.comboFabricante.addItem("Samsung")
            self.comboFabricante.addItem("Apple")
            self.gridAbstractLayout.addWidget(self.comboFabricante,0,1,1,1)


            self.comboTipo = QComboBox()
            self.comboTipo.addItem("Telefono")
            self.comboTipo.addItem("Tablet")
            self.gridAbstractLayout.addWidget(self.comboTipo,1,1,1,1)


            buttonCreate = QPushButton('Crear')
            buttonCreate.clicked.connect(self.button_abstractfactory_crear)
            self.gridAbstractLayout.addWidget(buttonCreate,2,1,1,1)

            subAbstractFactory.setWidget(widgetAbstractFactory)

            subAbstractFactory.setWindowTitle("Patrón Abstract Factory")
            self.mdi.addSubWindow(subAbstractFactory)
            subAbstractFactory.show()

#======================================================================================================================================================================
#Bridge Window
        if p.text().lower() == "bridge":
            subBridge = QMdiSubWindow()
            subBridge.resize(575, 443)
            widgetBridge = QWidget()

            self.gridLayout = QGridLayout(widgetBridge)
            self.gridLayout.setContentsMargins(0, 0, 0, 0)
            self.gridLayout.setObjectName("layoutBridge")

            labelTitulo = QLabel()
            labelTitulo.setText("Selecciona la figura")
            self.gridLayout.addWidget(labelTitulo, 0, 0, 1, 1)


            labelColor = QLabel()
            labelColor.setText("Selecciona el color")
            self.gridLayout.addWidget(labelColor,1,0,1,1)


            self.comboForma = QComboBox()
            self.comboForma.addItem("Cubo")
            self.comboForma.addItem("Esfera")
            self.gridLayout.addWidget(self.comboForma,0,1,1,1)


            self.comboColor = QComboBox()
            self.comboColor.addItem("Amarillo")
            self.comboColor.addItem("Azul")
            self.gridLayout.addWidget(self.comboColor,1,1,1,1)


            buttonDraw = QPushButton('Dibujar')
            buttonDraw.clicked.connect(self.button_bridge)
            self.gridLayout.addWidget(buttonDraw,2,1,1,1)

            subBridge.setWidget(widgetBridge)

            subBridge.setWindowTitle("Patrón Bridge")
            self.mdi.addSubWindow(subBridge)
            subBridge.show()       
#======================================================================================================================================================================
#Command Window
        if p.text() == "Command":
            subCommand = QMdiSubWindow()
            subCommand.resize(350,350)
            widgetCommand = QWidget()
            
            self.layoutCommand = QGridLayout(widgetCommand)
            self.layoutCommand.setContentsMargins(0,0,0,0)
            self.layoutCommand.setObjectName("gridCommand")

            labelTitle = QLabel()
            labelTitle.setText("Laptop")
            self.layoutCommand.addWidget(labelTitle,0,0,1,1)

            labelAccion = QLabel()
            labelAccion.setText("Elije un comando")
            self.layoutCommand.addWidget(labelAccion,1,0,1,1)

            self.encenderradio = QRadioButton('Encender')
            self.encenderradio.setChecked(False)
            self.encenderradio.accion="Encender"
            self.encenderradio.toggled.connect(self.onClickedAccion)
            self.layoutCommand.addWidget(self.encenderradio,1,1,1,1)

            self.suspenderradio = QRadioButton('Suspender')
            self.suspenderradio.setChecked(False)
            self.suspenderradio.accion="Suspender"
            self.suspenderradio.toggled.connect(self.onClickedAccion)
            self.layoutCommand.addWidget(self.suspenderradio,2,1,1,1)

            self.apagarradio = QRadioButton('Apagar')
            self.apagarradio.setChecked(False)
            self.apagarradio.accion="Apagar"
            self.apagarradio.toggled.connect(self.onClickedAccion)
            self.layoutCommand.addWidget(self.apagarradio,3,1,1,1)

            self.reiniciarradio = QRadioButton('Reiniciar')
            self.reiniciarradio.setChecked(False)
            self.reiniciarradio.accion="Reiniciar"
            self.reiniciarradio.toggled.connect(self.onClickedAccion)
            self.layoutCommand.addWidget(self.reiniciarradio,4,1,1,1)
            
            self.labelMensaje = QLabel()
            
            self.labelMensaje.setText("MSJ: ")
            self.layoutCommand.addWidget(self.labelMensaje,4,0,1,1)

            subCommand.setWidget(widgetCommand)
            subCommand.setWindowTitle("Patrón Command")
            self.mdi.addSubWindow(subCommand)
            subCommand.show()

#=====================================================================================================================================================================
#State Window
        if p.text() == "State":
            subState = QMdiSubWindow()
            subState.resize(450,450)
            widgetState = QWidget()
            
            self.layoutState = QGridLayout(widgetState)
            self.layoutState.setContentsMargins(0,0,0,0)
            self.layoutState.setObjectName("gridState")


            labelAgua = QLabel()
            labelAgua.setText("Agua")
            self.layoutState.addWidget(labelAgua,1,0,1,1)

            self.solidoradio = QRadioButton('Solido')
            self.solidoradio.setChecked(False)
            self.solidoradio.estado="Solido"
            self.solidoradio.toggled.connect(self.onClickedEstado)
            self.layoutState.addWidget(self.solidoradio,1,1,1,1)

            self.liquidoradio = QRadioButton('Liquido')
            self.liquidoradio.setChecked(False)
            self.liquidoradio.estado="Liquido"
            self.liquidoradio.toggled.connect(self.onClickedEstado)
            self.layoutState.addWidget(self.liquidoradio,2,1,1,1)

            self.gaseosoradio = QRadioButton('Gaseoso')
            self.gaseosoradio.setChecked(False)
            self.gaseosoradio.estado="Gaseoso"
            self.gaseosoradio.toggled.connect(self.onClickedEstado)
            self.layoutState.addWidget(self.gaseosoradio,3,1,1,1)
            
            self.labelMensaje = QLabel()
            
            self.labelMensaje.setText("MSJ: ")
            self.layoutState.addWidget(self.labelMensaje,4,0,1,1)

            subState.setWidget(widgetState)
            subState.setWindowTitle("Patrón State")
            self.mdi.addSubWindow(subState)
            subState.show()
#=====================================================================================================================================================================
#Prototype Window
        if p.text() == "Prototype":
            subPrototype = QMdiSubWindow()
            subPrototype.resize(575, 443)
            widgetPrototype = QWidget()
            self.gridPrototypeLayout = QGridLayout(widgetPrototype)
            self.gridPrototypeLayout.setContentsMargins(0, 0, 0, 0)
            self.gridPrototypeLayout.setObjectName("layoutPrototype")

            labelMouse = QLabel()
            labelMouse.setText("Mouse")
            self.gridPrototypeLayout.addWidget(labelMouse, 0, 0, 1, 1)

            self.comboMouse = QComboBox()
            self.comboMouse.addItem("Alambrico")
            self.comboMouse.addItem("Inalambrico")
            self.gridPrototypeLayout.addWidget(self.comboMouse,0,1,1,1)

            buttonCreate = QPushButton('Crear')
            buttonCreate.clicked.connect(self.button_prototype_crear)
            self.gridPrototypeLayout.addWidget(buttonCreate,2,1,1,1)

            buttonClone = QPushButton('Clonar')
            buttonClone.clicked.connect(self.button_prototype_clonar)
            self.gridPrototypeLayout.addWidget(buttonClone,3,1,1,1)

            subPrototype.setWidget(widgetPrototype)
            subPrototype.setWindowTitle("Patrón Prototype")
            self.mdi.addSubWindow(subPrototype)
            subPrototype.show() 
            
#=====================================================================================================================================================================
#Decorator Window
        if p.text() == "Decorator":
            subDecorator = QMdiSubWindow()
            subDecorator.resize(575, 443)
            widgetDecorator = QWidget()
            self.gridDecoratorLayout = QGridLayout(widgetDecorator)
            self.gridDecoratorLayout.setContentsMargins(0, 0, 0, 0)
            self.gridDecoratorLayout.setObjectName("layoutDecorator")

            labelCondimentos = QLabel()
            labelCondimentos.setText("Elije un condimento")
            self.gridDecoratorLayout.addWidget(labelCondimentos, 0, 0, 1, 1)

            self.comboCondimentos = QComboBox()
            self.comboCondimentos.addItem("Cueritos")
            self.comboCondimentos.addItem("Jicama")
            self.comboCondimentos.addItem("Pepino")
            self.comboCondimentos.addItem("Mango")
            self.comboCondimentos.addItem("Cacahuate")
            self.comboCondimentos.addItem("DulcesTamarindo")
            self.comboCondimentos.addItem("Chamoy")
            self.comboCondimentos.addItem("Salsa")
            self.comboCondimentos.addItem("Limon")

            self.gridDecoratorLayout.addWidget(self.comboCondimentos,0,1,1,1)

            buttonAdd = QPushButton('Agregar')
            buttonAdd.clicked.connect(self.button_decorator_agregar)
            self.gridDecoratorLayout.addWidget(buttonAdd,2,1,1,1)

            subDecorator.setWidget(widgetDecorator)
            subDecorator.setWindowTitle("Patrón Decorator")
            self.mdi.addSubWindow(subDecorator)
            subDecorator.show() 

#======================================================================================================================================================================            
    def button_factory_crear(self):
        tipo = self.comboTipo.currentText()
        factory = Factory()
        auto = factory.getAutomovil(tipo)
        #clo = auto.copy()

        imagen = QLabel()
        imagen.setGeometry(0,0,300,300)
        pixmap = QPixmap(auto.getImagen())
        imagen.setPixmap(pixmap)
        self.layoutImagenes.addWidget(imagen)

#======================================================================================================================================================================
    def button_abstractfactory_crear(self):
        fabricante = self.comboFabricante.currentText()
        tipo = self.comboTipo.currentText()
        samsungFactory = SamsungFactory()
        appleFactory = AppleFactory()
        print("Eligiendo " + fabricante + " tipo " + tipo)
        product = None

        imagen = QLabel()
        imagen.setGeometry(0,0,300,300)
        pixmap = None
        if fabricante.lower() == 'samsung' and tipo.lower() == 'telefono':
           print("Crear telefono Samsung")
           telefono = samsungFactory.createTelefonoSamsung()
           #print(telefono.getImagen())
           print("Product: " + telefono.getTelefonoSamsung())
           pixmap = QPixmap(telefono.getImagen())
           imagen.setPixmap(pixmap)
           #print('No imagen', self.countbridge)
           self.gridAbstractLayout.addWidget(imagen, self.countAbstractFactory,0,1,1)
           self.countAbstractFactory = self.countAbstractFactory + 1


        if fabricante.lower() == 'samsung' and tipo.lower() == 'tablet':
           print("Crear tablet Samsung")
           tablet = samsungFactory.createTabletSamsung()
           #print(tablet.getImagen())
           print("Product: " + tablet.getTabletSamsung())
           pixmap = QPixmap(tablet.getImagen())
           imagen.setPixmap(pixmap)
           self.gridAbstractLayout.addWidget(imagen, self.countAbstractFactory,0,1,1)
           self.countAbstractFactory = self.countAbstractFactory + 1


        if fabricante.lower() == 'apple' and tipo.lower() == 'telefono':
           print("Crear telefono Apple")
           telefono = appleFactory.createTelefonoApple()
           #print(telefono.getImagen())
           print("Product: " + telefono.getTelefonoApple())
           pixmap = QPixmap(telefono.getImagen())
           imagen.setPixmap(pixmap)
           self.gridAbstractLayout.addWidget(imagen, self.countAbstractFactory,0,1,1)
           self.countAbstractFactory = self.countAbstractFactory + 1

        if fabricante.lower() == 'apple' and tipo.lower() == 'tablet':
           print("Crear tablet Apple")
           tablet = appleFactory.createTabletApple()
           #print(tablet.getImagen())
           print("Product: " + tablet.getTabletApple())
           pixmap = QPixmap(tablet.getImagen())
           imagen.setPixmap(pixmap)
           self.gridAbstractLayout.addWidget(imagen, self.countAbstractFactory,0,1,1)
           self.countAbstractFactory = self.countAbstractFactory + 1
        
#======================================================================================================================================================================
    def button_bridge(self):
        forma = self.comboForma.currentText()
        color = self.comboColor.currentText()
        print("Eligiendo " + forma + " de color " + color)
        shape = None

        imagen = QLabel()
        imagen.setGeometry(0,0,300,300)
        pixmap = None
        if forma.lower() == 'cubo' and color.lower() == 'amarillo':
           print("Colorea cubo Amarillo")
           shape = Cubo(Amarillo())
           shape.color_it()
           #print(shape.getImagen())
           pixmap = QPixmap("./imagenes/cuboAmarillo.jpg")
           imagen.setPixmap(pixmap)
           #print('No imagen', self.countbridge)
           self.gridLayout.addWidget(imagen, self.countBridge,0,1,1)
           #self.countBridge = self.countBridge + 1


        if forma.lower() == 'cubo' and color.lower() == 'azul':
           print("Colorea cubo Azul")
           shape = Cubo(Azul())
           shape.color_it()
           #print(shape.getImagen())
           pixmap = QPixmap("./imagenes/cuboAzul.jpg")
           imagen.setPixmap(pixmap)
           self.gridLayout.addWidget(imagen, self.countBridge,0,1,1)
           #self.countBridge = self.countBridge + 1


        if forma.lower() == 'esfera' and color.lower() == 'amarillo':
           print("Colorea Esfera Amarilla")
           shape = Esfera(Amarillo())
           shape.color_it()
           #print(shape.getImagen())
           pixmap = QPixmap("./imagenes/esferaAmarilla.jpg")
           imagen.setPixmap(pixmap)
           self.gridLayout.addWidget(imagen, self.countBridge,0,1,1)
           #self.countBridge = self.countBridge + 1

        if forma.lower() == 'esfera' and color.lower() == 'azul':
           print("Colorea Esfera Azul")
           shape = Esfera(Azul())
           shape.color_it()
           #print(shape.getImagen())
           pixmap = QPixmap("./imagenes/esferaAzul.jpg")
           
           imagen.setPixmap(pixmap)
           self.gridLayout.addWidget(imagen, self.countBridge,0,1,1)
           #self.countBridge = self.countBridge + 1
#======================================================================================================================================================================
    def onClickedAccion(self):
        radioButton = self.sender()
        self.labelMensaje.setText(radioButton.accion)


        if radioButton.accion == "Encender":
            laptop = Laptop()
            command = MenuAcciones()
            command.set(LaptopEncender(laptop))
            command.confirm()

        if radioButton.accion == "Suspender":
            laptop = Laptop()
            command = MenuAcciones()
            command.set(LaptopSuspender(laptop))
            command.confirm()


        if radioButton.accion == "Apagar":
            laptop = Laptop()
            command = MenuAcciones()
            command.set(LaptopApagar(laptop))
            command.confirm()


        if radioButton.accion == "Reiniciar":
            laptop = Laptop()
            command = MenuAcciones()
            command.set(LaptopReiniciar(laptop))
            command.confirm()

#======================================================================================================================================================================
    def onClickedEstado(self):
        imagen = QLabel()
        imagen.setGeometry(0,0,300,300)
        radioButton = self.sender()
        self.labelMensaje.setText(radioButton.estado)


        if radioButton.estado == "Solido":
            pixmap = QPixmap("./imagenes/solido.jpg")
            solido = Solido()
            solido.cambiar()
            imagen.setPixmap(pixmap)
            self.layoutState.addWidget(imagen,self.countState,0,1,1)

        if radioButton.estado == "Liquido":
            pixmap = QPixmap("./imagenes/liquido.jpg")
            liquido = Liquido()
            liquido.cambiar()
            imagen.setPixmap(pixmap)
            self.layoutState.addWidget(imagen,self.countState,0,1,1)


        if radioButton.estado == "Gaseoso":
            pixmap = QPixmap("./imagenes/gaseoso.jpg")
            gaseoso = Gaseoso()
            gaseoso.cambiar()
            imagen.setPixmap(pixmap)
            self.layoutState.addWidget(imagen, self.countState,0,1,1)
            
#======================================================================================================================================================================
    def button_decorator_agregar(self):
        condimentos = self.comboCondimentos.currentText()
        #print("Eligiendo mouse" +  condimentos)
        tostitos = None

        imagen = QLabel()
        imagen.setGeometry(0,0,300,300)
        pixmap = None
        if condimentos.lower() == 'cueritos' :
            tostitos = Tostitos()
            cueritos= Cueritos(tostitos)
            pixmap = QPixmap("./imagenes/cueritos.png")
            imagen.setPixmap(pixmap)
            self.gridDecoratorLayout.addWidget(imagen, self.countDecorator,0,1,1)
            #self.countPrototype = self.countPrototype + 1
        if condimentos.lower() == 'jicama' :
            tostitos = Tostitos()
            cueritos= Cueritos(tostitos)
            jicama = Jicama(cueritos)
            jicama.agregarCondimento()
            pixmap = QPixmap("./imagenes/jicama.png")
            imagen.setPixmap(pixmap)
            self.gridDecoratorLayout.addWidget(imagen, self.countDecorator,0,1,1)
        if condimentos.lower() == 'pepino' :
            tostitos = Tostitos()
            cueritos = Cueritos(tostitos)
            jicama = Jicama(cueritos)
            jicama.agregarCondimento()
            pepino = Pepino(jicama)
            pepino.agregarCondimento()
            pixmap = QPixmap("./imagenes/pepino.png")
            imagen.setPixmap(pixmap)
            self.gridDecoratorLayout.addWidget(imagen, self.countDecorator,0,1,1)
        if condimentos.lower() == 'mango' :
            tostitos = Tostitos()
            cueritos= Cueritos(tostitos)
            jicama = Jicama(cueritos)
            jicama.agregarCondimento()
            pepino = Pepino(jicama)
            pepino.agregarCondimento()
            mango = Mango(pepino)
            mango.agregarCondimento()
            pixmap = QPixmap("./imagenes/mango.png")
            imagen.setPixmap(pixmap)
            self.gridDecoratorLayout.addWidget(imagen, self.countDecorator,0,1,1)
        if condimentos.lower() == 'cacahuate' :
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
            pixmap = QPixmap("./imagenes/cacahuate.png")
            imagen.setPixmap(pixmap)
            self.gridDecoratorLayout.addWidget(imagen, self.countDecorator,0,1,1)
        if condimentos.lower() == 'dulcestamarindo' :
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
            pixmap = QPixmap("./imagenes/dulcesTamarindo.png")
            imagen.setPixmap(pixmap)
            self.gridDecoratorLayout.addWidget(imagen, self.countDecorator,0,1,1)
        if condimentos.lower() == 'chamoy' :
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
            pixmap = QPixmap("./imagenes/chamoy.png")
            imagen.setPixmap(pixmap)
            self.gridDecoratorLayout.addWidget(imagen, self.countDecorator,0,1,1)
        if condimentos.lower() == 'salsa' :
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
            pixmap = QPixmap("./imagenes/salsa.png")
            imagen.setPixmap(pixmap)
            self.gridDecoratorLayout.addWidget(imagen, self.countDecorator,0,1,1)
        if condimentos.lower() == 'limon' :
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
            pixmap = QPixmap("./imagenes/limon.png")
            imagen.setPixmap(pixmap)
            self.gridDecoratorLayout.addWidget(imagen, self.countDecorator,0,1,1)

#======================================================================================================================================================================
    def button_prototype_crear(self):
        mouse = self.comboMouse.currentText()
        print("Eligiendo mouse" +  mouse)
        product = None

        imagen = QLabel()
        imagen.setGeometry(0,0,300,300)
        pixmap = None
        if mouse.lower() == 'alambrico' :
            mouseAlambrico = MouseAlambrico()
            mouseAlambrico.crear()
            pixmap = QPixmap("./imagenes/mouseAlambrico.jpg")
            imagen.setPixmap(pixmap)
            self.gridPrototypeLayout.addWidget(imagen, self.countPrototype,0,1,1)
            self.countPrototype = self.countPrototype + 1

        if mouse.lower() == 'inalambrico' :
            mouseInalambrico = MouseInalambrico()
            mouseInalambrico.crear()
            pixmap = QPixmap("./imagenes/mouseInalambrico.jfif")
            imagen.setPixmap(pixmap)
            self.gridPrototypeLayout.addWidget(imagen, self.countPrototype,0,1,1)
            self.countPrototype = self.countPrototype + 1

    def button_prototype_clonar(self):
        mouse = self.comboMouse.currentText()
        print("Eligiendo mouse" +  mouse)
        product = None

        imagen = QLabel()
        imagen.setGeometry(0,0,300,300)
        pixmap = None
        if mouse.lower() == 'alambrico' :
            mouseAlambrico = MouseAlambrico()
            mouseAlambrico.clonar()
            pixmap = QPixmap("./imagenes/mouseAlambrico.jpg")
            imagen.setPixmap(pixmap)
            self.gridPrototypeLayout.addWidget(imagen, self.countPrototype,0,1,1)
            self.countPrototype = self.countPrototype + 1

        if mouse.lower() == 'inalambrico' :
            mouseInalambrico = MouseInalambrico()
            mouseInalambrico.clonar()
            pixmap = QPixmap("./imagenes/mouseInalambrico.jfif")
            imagen.setPixmap(pixmap)
            self.gridPrototypeLayout.addWidget(imagen, self.countPrototype,0,1,1)
            self.countPrototype = self.countPrototype + 1

           
app = QApplication(sys.argv)
mdi  =MDIWindow()
mdi.show()
app.exec_()
        


