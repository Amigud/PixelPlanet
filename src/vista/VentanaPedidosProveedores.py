from PyQt5 import uic, QtWidgets
from src.controlador.ControladorProducto import ControladorProducto

class VentanaPedidosProveedores(QtWidgets.QMainWindow):
    def __init__(self, empleado=None, parent=None):
        super().__init__(parent)
        uic.loadUi("src/Ui/ProveedorPedido.ui", self)
        self.controlador = ControladorProducto()
        self.empleado = empleado
        self.parent = parent

        # Botones
        self.Comprar.clicked.connect(self.realizar_pedido)
        self.RegresarProveedor.clicked.connect(self.regresar)

    def realizar_pedido(self):
        proveedor = self.InsNombreProveedor.text().strip()
        producto = self.InsNombreProduct.text().strip()
        cantidad_str = self.InscantProducto.text().strip()

        # Validaciones
        if not proveedor or not producto or not cantidad_str:
            QtWidgets.QMessageBox.warning(self, "Campos incompletos", "Por favor, completa todos los campos.")
            return

        try:
            cantidad = int(cantidad_str)
            if cantidad <= 0:
                raise ValueError
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Cantidad inválida", "Introduce una cantidad válida (mayor que 0).")
            return

        # Verificamos si el producto existe
        info = self.controlador.obtener_info_producto(producto)
        if info:
            producto_id, _ = info
            actualizado = self.controlador.aumentar_stock(producto_id, cantidad)

            if actualizado:
                QtWidgets.QMessageBox.information(
                    self,
                    "Pedido Completado",
                    f"¡Enhorabuena!\nSe ha realizado el pedido de {cantidad} unidades de '{producto}' al proveedor '{proveedor}'."
                )
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "No se pudo realizar el pedido.")
        else:
            QtWidgets.QMessageBox.warning(self, "Producto no encontrado", f"No se encontró el producto '{producto}'.")

    def regresar(self):
        if self.parent:
            self.parent.show()
        self.close()
