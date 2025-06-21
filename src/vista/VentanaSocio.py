from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from src.controlador.ControladorSocio import ControladorSocio

class VentanaSocio(QtWidgets.QMainWindow):
    def __init__(self, empleado, parent=None):
        super().__init__(parent)
        uic.loadUi("./src/Ui/RegistroSocios.ui", self)

        self.empleado = empleado
        self.parent = parent
        self.controlador = ControladorSocio()

        self.setWindowTitle(f"Añadir a Socio")
        self.aceptarBoton.clicked.connect(self.registrar_socio)
        self.regresarBoton.clicked.connect(self.regresar)

    def registrar_socio(self):
        nombre = self.nombreEdit.text().strip()
        apellido = self.ApellidoEdit.text().strip()
        email = self.emailEdit.text().strip()
        telefono = self.telefonoEdit.text().strip()
        fecha_nacim = self.fechanacimEdit.date().toPyDate()

        exito, mensaje = self.controlador.registrar_socio(
            nombre, apellido, email, telefono, fecha_nacim
        )

        if exito:
            QMessageBox.information(self, "Éxito", mensaje)
            self.limpiar_campos()
        else:
            QMessageBox.warning(self, "Error", mensaje)


    def limpiar_campos(self):
        self.nombreEdit.clear()
        self.ApellidoEdit.clear()
        self.emailEdit.clear()
        self.telefonoEdit.clear()
        self.fechanacimEdit.setDate(self.fechanacimEdit.minimumDate())

    def regresar(self):
        if self.parent:
            self.parent.show()
        self.close()
