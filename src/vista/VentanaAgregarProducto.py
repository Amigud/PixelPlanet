from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from src.controlador.ControladorProducto import ControladorProducto

class VentanaAgregarProducto(QtWidgets.QMainWindow):
    def __init__(self, empleado, parent=None):
        super().__init__(parent)
        uic.loadUi("./src/Ui/AnadirProducto.ui", self)

        self.empleado = empleado
        self.parent = parent
        self.controlador = ControladorProducto()

        self.setWindowTitle(f"Agregar producto")
        self.aceptarBoton.clicked.connect(self.registrar_producto)
        self.regresarBoton.clicked.connect(self.regresar)

    def registrar_producto(self):
        nombre = self.nombreEdit.text().strip()
        descripcion = self.descrEdit.text().strip()
        precio_texto = self.precioEdit.text().strip()
        cantidad = self.cantBox.value()

        if self.controlador.registrar_producto(nombre, descripcion, precio_texto, cantidad):
            QMessageBox.information(self, "Éxito", "Producto registrado correctamente.")
            self.limpiar()
        else:
            QMessageBox.warning(self, "Error", "Datos inválidos o error al registrar producto.")

        

    def limpiar(self):
        self.nombreEdit.clear()
        self.descrEdit.clear()
        self.precioEdit.clear()
        self.cantBox.setValue(1)

    def regresar(self):
        if self.parent:
            self.parent.show()
        self.close()
