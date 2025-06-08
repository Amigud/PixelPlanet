from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from modelo.dao.ProductoDAOJDBC import ProductoDAOJDBC

class VentanaDevolucion(QtWidgets.QMainWindow):
    def __init__(self, empleado, parent=None):
        super().__init__(parent)
        uic.loadUi("./src/Ui/Devolucion.ui", self)

        self.empleado = empleado
        self.parent = parent
        self.dao = ProductoDAOJDBC()

        self.aceptarBoton.clicked.connect(self.procesar_devolucion)
        self.regresarBoton.clicked.connect(self.regresar)

    def procesar_devolucion(self):
        nombre = self.nombreProdEdit.text().strip()
        cantidad = self.cantBox.value()

        if not nombre or cantidad <= 0:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        exito = self.dao.devolver_producto(nombre, cantidad)

        if exito:
            QMessageBox.information(self, "Éxito", "Devolución registrada y stock actualizado.")
            self.nombreProdEdit.clear()
            self.cantBox.setValue(1)
        else:
            QMessageBox.critical(self, "Error", "No se pudo procesar la devolución.")

    def regresar(self):
        if self.parent:
            self.parent.show()
        self.close()
