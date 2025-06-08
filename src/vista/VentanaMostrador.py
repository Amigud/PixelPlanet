from PyQt5 import uic, QtWidgets
from src.vista.VentanaMenuProductos import VentanaMenuProductos
from src.vista.VentanaGestionResenas import VentanaGestionResenas
from src.vista.VentanaDevoluciones import VentanaDevoluciones
from src.vista.VentanaPedidosProveedores import VentanaPedidosProveedores

class VentanaMostrador(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("src/Ui/VentanaMostrador.ui", self)

        # Conexión de botones a funciones
        self.botonGestionProductos.clicked.connect(self.abrir_menu_productos)
        self.botonGestionResenas.clicked.connect(self.abrir_gestion_resenas)
        self.botonDevoluciones.clicked.connect(self.abrir_gestion_devoluciones)
        self.botonProveedores.clicked.connect(self.abrir_gestion_pedidos)

        # Ventanas hijas (para mantener referencias)
        self.ventana_productos = None
        self.ventana_resenas = None
        self.ventana_devoluciones = None
        self.ventana_pedidos = None

    def abrir_menu_productos(self):
        if not self.ventana_productos:
            self.ventana_productos = VentanaMenuProductos()
        self.ventana_productos.show()

    def abrir_gestion_resenas(self):
        if not self.ventana_resenas:
            self.ventana_resenas = VentanaGestionResenas()
        self.ventana_resenas.show()

    def abrir_gestion_devoluciones(self):
        if not self.ventana_devoluciones:
            self.ventana_devoluciones = VentanaDevoluciones()
        self.ventana_devoluciones.show()

    def abrir_gestion_pedidos(self):
        if not self.ventana_pedidos:
            self.ventana_pedidos = VentanaPedidosProveedores()
        self.ventana_pedidos.show()
