from PyQt5 import QtWidgets, uic
from src.vista.VentanaSocio import VentanaSocio
from src.vista.VentanaGestionProductos import VentanaGestionProductos
from src.vista.VentanaResena import VentanaResena


class VentanaMostrador(QtWidgets.QMainWindow):
    def __init__(self, empleado, parent=None):
        super().__init__(parent)
        uic.loadUi("./src/Ui/Mostrador.ui", self)

        self.empleado = empleado
        self.parent = parent

        self.setWindowTitle(f"Menú Empleado del Mostrador")
        self.socioBoton.clicked.connect(self.abrir_socio)
        self.productoBoton.clicked.connect(self.abrir_producto)
        self.resenaBoton.clicked.connect(self.abrir_resena)

    
    def abrir_socio(self):
        self.hide()
        self.ventana_socio = VentanaSocio(self.empleado, self)
        self.ventana_socio.show()
    
    def abrir_resena(self):
        self.hide()
        self.ventana_resena = VentanaResena(self.empleado, self)
        self.ventana_resena.show()

    def abrir_producto(self):
        self.hide()
        self.ventana_producto = VentanaGestionProductos(self.empleado, self)
        self.ventana_producto.show()

        

    