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
            self.hide()

            if empleado.rol == 'mostrador':
                #if not self.ventana_mostrador:
                    #self.ventana_mostrador = VentanaMostrador()
                #self.ventana_mostrador.show()
                QtWidgets.QMessageBox.information(self, "Éxito", f"Bienvenido {empleado.rol}")
        
            elif empleado.rol == 'zona_juegos':
                #if not self.ventana_zona_juegos:
                    #self.ventana_zona_juegos = VentanaZonaJuegos()
                #self.ventana_zona_juegos.show()
                print("zona_juegos")
            
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Credenciales inválidas")
