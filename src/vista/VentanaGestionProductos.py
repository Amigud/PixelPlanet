from PyQt5 import QtWidgets, uic

from src.vista.VentanaAgregarProducto import VentanaAgregarProducto
from src.vista.VentanaEliminarProducto import VentanaEliminarProducto
from src.vista.VentanaDisponibilidadProducto import VentanaDisponibilidadProducto
from src.vista.VentanaDevolucion import VentanaDevolucion

class VentanaGestionProductos(QtWidgets.QMainWindow):
    def __init__(self, empleado, parent=None):
        super().__init__(parent)
        uic.loadUi("./src/Ui/Gestproductos.ui", self)

        self.empleado = empleado
        self.parent = parent

        # Conectar botones
        self.anadirProdBoton.clicked.connect(self.abrir_agregar_producto)
        self.elimProdBoton.clicked.connect(self.abrir_eliminar_producto)
        self.consProdBoton.clicked.connect(self.abrir_consultar_producto)
        self.devolBoton.clicked.connect(self.abrir_devolucion)
        self.regresarBoton.clicked.connect(self.regresar)

    def abrir_agregar_producto(self):
        self.hide()
        self.ventana_agregar = VentanaAgregarProducto(self.empleado, self)
        self.ventana_agregar.show()
        print("Abrir: Añadir Producto")

    def abrir_eliminar_producto(self):
        self.hide()
        self.ventana_eliminar = VentanaEliminarProducto(self.empleado, self)
        self.ventana_eliminar.show()
        print("Abrir: Eliminar Producto")

    def abrir_consultar_producto(self):
        self.hide()
        self.ventana_consultar = VentanaDisponibilidadProducto(self.empleado, self)
        self.ventana_consultar.show()
        print("Abrir: Consultar Producto")

    def abrir_devolucion(self):
        self.hide()
        self.ventana_devolucion = VentanaDevolucion(self.empleado, self)
        self.ventana_devolucion.show()
        print("Abrir: Devolución de Producto")
    
    def regresar(self):
        if self.parent:
            self.parent.show()
        self.close()
