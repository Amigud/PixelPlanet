from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from src.controlador.ControladorResena import ControladorResena

class VentanaResena(QtWidgets.QMainWindow):
    def __init__(self, empleado, parent=None):
        super().__init__(parent)
        uic.loadUi("./src/Ui/Resena.ui", self)

        self.empleado = empleado
        self.parent = parent
        self.controlador = ControladorResena()

        self.setWindowTitle(f"Insertar una Reseña")
        self.aceptarBoton.clicked.connect(self.insertar_resena)
        self.regresarBoton.clicked.connect(self.regresar)

    def insertar_resena(self):
        nombre_producto = self.nombreProdEdit.text().strip()
        comentario = self.comentEdit.text().strip()
        estrellas = self.estrellasBox.value()

        if self.controlador.insertar_resena(nombre_producto, comentario, estrellas, self.empleado.id):
            QMessageBox.information(self, "Éxito", "Reseña registrada correctamente.")
            self.limpiar()
        else:
            QMessageBox.critical(self, "Error", "No se pudo registrar la reseña.")

    def limpiar(self):
        self.nombreProdEdit.clear()
        self.comentEdit.clear()
        self.estrellasBox.setValue(1)

    def regresar(self):
        if self.parent:
            self.parent.show()
        self.close()
