from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from src.controlador.ControladorProducto import ControladorProducto

class VentanaDevolucion(QtWidgets.QMainWindow):
    def __init__(self, empleado, parent=None):
        super().__init__(parent)
        uic.loadUi("./src/Ui/Devolucion.ui", self)

        self.empleado = empleado
        self.parent = parent
        self.controlador = ControladorProducto()

        self.setWindowTitle(f"Realizar Devolución")
        self.aceptarBoton.clicked.connect(self.procesar_devolucion)
        self.regresarBoton.clicked.connect(self.regresar)

    def procesar_devolucion(self):
        nombre = self.nombreProdEdit.text().strip()
        cantidad = self.cantBox.value()

        if not nombre or cantidad <= 0:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        exito, mensaje = self.controlador.devolver_producto(nombre, cantidad)

        if exito:
            QMessageBox.information(self, "Éxito", mensaje)
            self.nombreProdEdit.clear()
            self.cantBox.setValue(1)
        else:
            QMessageBox.critical(self, "Error", mensaje)

    def regresar(self):
        if self.parent:
            self.parent.show()
        self.close()
