from PyQt5 import uic, QtWidgets
from src.controlador.ControladorProducto import ControladorProducto

class VentanaPedidosProveedores(QtWidgets.QMainWindow):
    def __init__(self, empleado=None, parent=None):
        super().__init__(parent)
        uic.loadUi("src/Ui/ProveedorPedido.ui", self)
        self.controlador = ControladorProducto()
        self.empleado = empleado
        self.parent = parent

        self.setWindowTitle(f"Realizar pedidos a proveedores")
        self.bajoStockBoton.clicked.connect(self.mostrar_stock_bajo)
        self.Comprar.clicked.connect(self.realizar_pedido)
        self.RegresarProveedor.clicked.connect(self.regresar)

    def realizar_pedido(self):
        proveedor = self.InsNombreProveedor.text().strip()
        producto = self.InsNombreProduct.text().strip()
        cantidad_str = self.InscantProducto.text().strip()

        
        if not proveedor or not producto or not cantidad_str:
            QtWidgets.QMessageBox.warning(self, "Campos incompletos", "Por favor, completa todos los campos.")
            return

        try:
            cantidad = int(cantidad_str)
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Cantidad inválida", "Introduce una cantidad válida (mayor que 0).")
            return

        
        exito, mensaje = self.controlador.realizar_pedido_proveedor(producto, proveedor, cantidad)
        if exito:
            QtWidgets.QMessageBox.information(self, "Pedido Completado", mensaje)
        else:
            QtWidgets.QMessageBox.critical(self, "Error", mensaje)

    def mostrar_stock_bajo(self):
        productos = self.controlador.obtener_productos_stock_bajo()
        if not productos:
            QtWidgets.QMessageBox.information(self, "Stock Crítico", "No hay productos con stock bajo.")
            return
        
        mensaje = "Productos con Stock Bajo:\n\n"
        for nombre, cantidad in productos:
            mensaje += f"- {nombre}: {cantidad} unidades\n"

        QtWidgets.QMessageBox.information(self, "Stock Crítico", mensaje)

    def regresar(self):
        if self.parent:
            self.parent.show()
        self.close()
