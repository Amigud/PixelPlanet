from PyQt5 import uic, QtWidgets
from src.controlador.ControladorProducto import ControladorProducto

class VentanaActualizarProducto(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("src/Ui/VentanaActualizarProducto.ui", self)
        self.controlador = ControladorProducto()
        self.botonBuscar.clicked.connect(self.buscar)
        self.botonActualizar.clicked.connect(self.actualizar)

    def buscar(self):
        producto_id = self.idEdit.text()
        producto = self.controlador.buscar_producto_por_id(producto_id)
        if producto:
            self.nombreEdit.setText(producto[1])
            self.descripcionEdit.setPlainText(producto[2])
            self.precioEdit.setText(str(producto[3]))
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Producto no encontrado.")

    def actualizar(self):
        pid = self.idEdit.text()
        nombre = self.nombreEdit.text()
        descripcion = self.descripcionEdit.toPlainText()
        precio = self.precioEdit.text()
        if self.controlador.actualizar_producto(pid, nombre, descripcion, precio):
            QtWidgets.QMessageBox.information(self, "Actualizado", "Producto actualizado correctamente.")
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "No se pudo actualizar.")
