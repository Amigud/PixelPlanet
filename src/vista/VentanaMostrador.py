from PyQt5 import uic, QtWidgets
from src.vista.VentanaRegistrarProducto import VentanaRegistrarProducto
from src.vista.VentanaActualizarProducto import VentanaActualizarProducto
from src.vista.VentanaDisponibilidadProducto import VentanaDisponibilidadProducto

class VentanaMostrador(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("src/Ui/VentanaMostrador.ui", self)

        # Conectar botones a funciones
        self.botonRegistrarProducto.clicked.connect(self.abrir_registro)
        self.botonActualizarProducto.clicked.connect(self.abrir_actualizar)
        self.botonVerDisponibilidad.clicked.connect(self.abrir_disponibilidad)

        # Inicializar ventanas hijas
        self.ventana_registrar = None
        self.ventana_actualizar = None
        self.ventana_disponibilidad = None

    def abrir_registro(self):
        self.ventana_registrar = VentanaRegistrarProducto()
        self.ventana_registrar.show()

    def abrir_actualizar(self):
        self.ventana_actualizar = VentanaActualizarProducto()
        self.ventana_actualizar.show()

    def abrir_disponibilidad(self):
        self.ventana_disponibilidad = VentanaDisponibilidadProducto()
        self.ventana_disponibilidad.show()
