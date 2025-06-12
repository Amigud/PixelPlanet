from PyQt5 import uic, QtWidgets
from src.controlador.ControladorProducto import ControladorProducto

class VentanaDisponibilidadProducto(QtWidgets.QMainWindow):
    def __init__(self, empleado=None, parent=None):
        super().__init__(parent)
        uic.loadUi("src/Ui/DisponibilidadProductos.ui", self)  # Asegúrate que el archivo se llame exactamente así
        self.controlador = ControladorProducto()
        self.empleado = empleado
        self.parent = parent

        self.setWindowTitle(f"Disponibilidad de producto")
        self.BuscarProducto.clicked.connect(self.buscar_producto)
        self.RegresarProducto.clicked.connect(self.regresar)

    def buscar_producto(self):
        nombre = self.InsNombreProducto.text().strip()

        if not nombre:
            QtWidgets.QMessageBox.warning(self, "Campo vacío", "Por favor, introduce un nombre de producto.")
            return

        info = self.controlador.obtener_info_producto(nombre)

        if info:
            producto_id, cantidad = info
            QtWidgets.QMessageBox.information(
                self,
                "Cantidad disponible",
                f"Producto: '{nombre}'\nID: {producto_id}\nCantidad disponible: {cantidad}"
            )
        else:
            QtWidgets.QMessageBox.warning(
                self,
                "Producto no encontrado",
                f"No se encontró ningún producto con el nombre '{nombre}'."
            )

    def regresar(self):
        if self.parent:
            self.parent.show()
        self.close()



