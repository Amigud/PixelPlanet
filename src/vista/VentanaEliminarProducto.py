from PyQt5 import uic, QtWidgets
from src.controlador.ControladorProducto import ControladorProducto

class VentanaEliminarProducto(QtWidgets.QMainWindow):
    def __init__(self, empleado=None, parent=None):
        super().__init__(parent)
        uic.loadUi("src/Ui/EliminarProductos.ui", self)
        self.controlador = ControladorProducto()
        self.empleado = empleado
        self.parent = parent

        self.setWindowTitle(f"Eliminar producto")
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

            
            QtWidgets.QMessageBox.information(
                self,
                "Producto encontrado",
                f"Producto: '{nombre}'\nID: {producto_id}\nCantidad disponible: {cantidad_actual}"
            )

            
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
                    cantidad_restante = cantidad_actual - cantidad_eliminar

                    if cantidad_restante == 0:
                        respuesta2 = QtWidgets.QMessageBox.question(
                            self,
                            "Producto sin unidades",
                            f"El producto '{nombre}' se ha quedado sin unidades.\n¿Quieres eliminarlo completamente?",
                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
                        )
                        if respuesta2 == QtWidgets.QMessageBox.Yes:
                            eliminado = self.controlador.eliminar_producto(producto_id)
                            if eliminado:
                                QtWidgets.QMessageBox.information(self, "Eliminado", "Producto eliminado.")
                            else:
                                QtWidgets.QMessageBox.warning(self, "Error", "No se pudo eliminar el producto.")
                        else:
                            QtWidgets.QMessageBox.information(self, "Información", f"El producto se mantiene con 0 unidades.")

                    else:
                        QtWidgets.QMessageBox.information(self, "Éxito", f"Se eliminaron {cantidad_eliminar} unidades de '{nombre}'.")
                else:
                    QtWidgets.QMessageBox.critical(self, "Error", "No se pudo eliminar el producto.")
        else:
            QtWidgets.QMessageBox.warning(self, "No encontrado", f"No se encontró el producto '{nombre}'.")

    def regresar(self):
        if self.parent:
            self.parent.show()
        self.close()
