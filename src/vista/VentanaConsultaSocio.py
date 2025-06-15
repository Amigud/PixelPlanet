from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from src.modelo.dao.SocioDAOJDBC import SocioDAOJDBC

class VentanaConsultaSocio(QtWidgets.QMainWindow):
    def __init__(self, empleado, parent=None):
        super().__init__(parent)
        uic.loadUi("./src/Ui/ConsultarSocio.ui", self)

        self.empleado = empleado
        self.parent = parent
        self.dao = SocioDAOJDBC()

        
        self.aceptarBoton.clicked.connect(self.consultar_socio)
        self.regresarBoton.clicked.connect(self.regresar)

    def consultar_socio(self):
        email = self.emailEdit.text().strip()
        if not email:
            QMessageBox.warning(self, "Campo vacío", "Por favor, introduce un email.")
            return

        socio = self.dao.buscar_por_email(email)
        if socio:
            mensaje = (
                f"ID: {socio.id}\n"
                f"Nombre: {socio.nombre}\n"
                f"Apellidos: {socio.apellido}\n"
                f"Email: {socio.email}\n"
                f"Teléfono: {socio.telefono}\n"
                f"Fecha de nacimiento: {socio.fecha_nacimiento if socio.fecha_nacimiento else 'N/D'}"
            )
            QMessageBox.information(self, "Datos del Socio", mensaje)
        else:
            QMessageBox.warning(self, "No encontrado", "No se encontró un socio con ese email.")

    def regresar(self):
        if self.parent:
            self.parent.show()
        self.close()
