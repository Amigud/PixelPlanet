from PyQt5 import uic, QtWidgets
from src.controlador.ControladorProducto import ControladorProducto

class VentanaDisponibilidadProducto(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("src/Ui/VentanaDisponibilidadProducto.ui", self)
        self.controlador = ControladorProducto()

        # Conectar botones
        self.BuscarProducto.clicked.connect(self.buscar_producto)
        self.RegresarProducto.clicked.connect(self.close)

    def buscar_producto(self):
        nombre = self.InsNombreProducto.text().strip()

        if not nombre:
            QtWidgets.QMessageBox.warning(self, "Campo vacío", "Por favor, introduce un nombre de producto.")
            return

        cantidad = self.controlador.obtener_cantidad_producto(nombre)

        if cantidad is not None:
            QtWidgets.QMessageBox.information(
                self,
                "Cantidad disponible",
                f"Hay {cantidad} unidades disponibles del producto '{nombre}'."
            )
        else:
            QtWidgets.QMessageBox.warning(
                self,
                "Producto no encontrado",
                f"No se encontró ningún producto con el nombre '{nombre}'."
            )

