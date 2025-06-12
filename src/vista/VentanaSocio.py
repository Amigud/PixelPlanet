from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from src.modelo.vo.SocioVO import SocioVO
from src.modelo.dao.SocioDAOJDBC import SocioDAOJDBC

class VentanaSocio(QtWidgets.QMainWindow):
    def __init__(self, empleado, parent=None):
        super().__init__(parent)
        uic.loadUi("./src/Ui/RegistroSocios.ui", self)

        self.empleado = empleado
        self.parent = parent
        self.dao = SocioDAOJDBC()

        self.setWindowTitle(f"Añadir a Socio")
        self.aceptarBoton.clicked.connect(self.registrar_socio)
        self.regresarBoton.clicked.connect(self.regresar)

    def registrar_socio(self):
        nombre = self.nombreEdit.text().strip()
        apellido = self.ApellidoEdit.text().strip()
        email = self.emailEdit.text().strip()
        telefono = self.telefonoEdit.text().strip()
        fecha_nacim = self.fechanacimEdit.date().toPyDate()

        if not all([nombre, apellido, email, telefono]):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        socio = SocioVO(
            id=None,
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            fecha_nacimiento=fecha_nacim
        )

        if self.dao.insertar_socio(socio):
            QMessageBox.information(self, "Éxito", "Socio registrado con éxito.")
            self.limpiar_campos()
        else:
            QMessageBox.critical(self, "Error", "No se pudo registrar el socio.")

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
