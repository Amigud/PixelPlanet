from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from src.controlador.ControladorSocio import ControladorSocio

class VentanaConsultaSocio(QtWidgets.QMainWindow):
    def __init__(self, empleado, parent=None):
        super().__init__(parent)
        uic.loadUi("./src/Ui/ConsultarSocio.ui", self)

        self.empleado = empleado
        self.parent = parent
        self.controlador = ControladorSocio()

        self.setWindowTitle(f"Consultar Socio")
        self.aceptarBoton.clicked.connect(self.consultar_socio)
        self.regresarBoton.clicked.connect(self.regresar)

    def consultar_socio(self):
        email = self.emailEdit.text().strip()
        
        exito, resultado = self.controlador.consultar_socio(email)

        if exito:
            socio, tipo = resultado
            mensaje = (
                f"ID: {socio.id}\n"
                f"Nombre: {socio.nombre}\n"
                f"Apellidos: {socio.apellido}\n"
                f"Email: {socio.email}\n"
                f"Teléfono: {socio.telefono}\n"
                f"Fecha de nacimiento: {socio.fecha_nacimiento if socio.fecha_nacimiento else 'N/D'}\n"
                f"Tipo de Socio: {tipo}\n"
            )
            QMessageBox.information(self, "Datos del Socio", mensaje)
        else:
            QMessageBox.warning(self, "Error", resultado)

    def regresar(self):
        if self.parent:
            self.parent.show()
        self.close()
