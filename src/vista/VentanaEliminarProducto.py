from PyQt5 import uic, QtWidgets
from src.controlador.ControladorProducto import ControladorProducto

class VentanaEliminarProducto(QtWidgets.QMainWindow):
    def __init__(self, empleado=None, parent=None):
        super().__init__(parent)
        uic.loadUi("src/Ui/EliminarProductos.ui", self)
        self.controlador = ControladorProducto()
        self.empleado = empleado
        self.parent = parent

        self.BuscarProductoElim.clicked.connect(self.buscar_y_confirmar)
        self.RegresarProductoElim.clicked.connect(self.regresar)

    def buscar_y_confirmar(self):
        nombre = self.InsNombreProductoElim.text().strip()
        cantidad_eliminar = self.cantidadBox.value()

        if not nombre:
            QtWidgets.QMessageBox.warning(self, "Campo vacío", "Introduce el nombre del producto.")
            return

        info = self.controlador.obtener_info_producto(nombre)

        if info:
            producto_id, cantidad_actual = info

            # Primer mensaje: cantidad disponible
            QtWidgets.QMessageBox.information(
                self,
                "Producto encontrado",
                f"Producto: '{nombre}'\nID: {producto_id}\nCantidad disponible: {cantidad_actual}"
            )

            # Segundo mensaje: confirmación
            respuesta = QtWidgets.QMessageBox.question(
                self,
                "Confirmar eliminación",
                f"¿Deseas eliminar {cantidad_eliminar} unidades del producto '{nombre}'?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
            )

            if respuesta == QtWidgets.QMessageBox.Yes:
                if cantidad_eliminar > cantidad_actual:
                    QtWidgets.QMessageBox.warning(self, "Error", "No puedes eliminar más productos de los disponibles.")
                    return

                exito = self.controlador.restar_stock(producto_id, cantidad_eliminar)

                if exito:
                    QtWidgets.QMessageBox.information(self, "Éxito", f"Se eliminaron {cantidad_eliminar} unidades de '{nombre}'.")
                else:
                    QtWidgets.QMessageBox.critical(self, "Error", "No se pudo eliminar el producto.")
        else:
            QtWidgets.QMessageBox.warning(self, "No encontrado", f"No se encontró el producto '{nombre}'.")

    def regresar(self):
        if self.parent:
            self.parent.show()
        self.close()
