from PyQt5 import uic, QtWidgets
import sys
from src.controlador.ControladorLogin import ControladorLogin

class VentanaLogin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./src/Ui/Login.ui", self)
        self.controlador = ControladorLogin()
        self.botonLogin.clicked.connect(self.intentar_login)

    def intentar_login(self):
        email = self.emailEdit.text()
        contrasena = self.contrasenaEdit.text()
        empleado = self.controlador.validar_credenciales(email, contrasena)

        if empleado:
            QtWidgets.QMessageBox.information(self, "Éxito", f"Bienvenido {empleado.rol}")
            
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Credenciales inválidas")
