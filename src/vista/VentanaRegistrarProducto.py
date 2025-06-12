from PyQt5 import uic, QtWidgets
from src.controlador.ControladorProducto import ControladorProducto

class VentanaRegistrarProducto(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("src/Ui/VentanaRegistrarProducto.ui", self)
        self.controlador = ControladorProducto()

        self.setWindowTitle(f"Registrar un producto")
        self.botonRegistrar.clicked.connect(self.registrar)

    def registrar(self):
        nombre = self.nombreEdit.text()
        descripcion = self.descripcionEdit.toPlainText()
        precio = self.precioEdit.text()
        genero = self.generoEdit.text()

        if not nombre or not precio or not genero:
            QtWidgets.QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        if self.controlador.registrar_producto(nombre, descripcion, precio, genero):
            QtWidgets.QMessageBox.information(self, "Éxito", "Producto registrado.")
            self.close()
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Error al registrar.")
