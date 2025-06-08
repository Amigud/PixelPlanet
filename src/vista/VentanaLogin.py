from PyQt5 import uic, QtWidgets
import sys
from src.controlador.ControladorLogin import ControladorLogin
from src.vista.VentanaZonaJuegos import VentanaZonaJuegos
from src.vista.VentanaMostrador import VentanaMostrador

class VentanaLogin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./src/Ui/Login.ui", self)
        self.controlador = ControladorLogin()
        self.botonLogin.clicked.connect(self.intentar_login)
        self.ventana_mostrador = None
        self.ventana_zona_juegos = None

    def intentar_login(self):
        email = self.emailEdit.text()
        contrasena = self.contrasenaEdit.text()
        empleado = self.controlador.validar_credenciales(email, contrasena)

        if empleado:
            self.hide()

            if empleado.rol == 'mostrador':
                if not self.ventana_mostrador:
                    self.ventana_mostrador = VentanaMostrador()
                self.ventana_mostrador.show()
                print("mostrador")
                
        
            elif empleado.rol == 'zona_juegos':
                if not self.ventana_zona_juegos:
                    self.ventana_zona_juegos = VentanaZonaJuegos(empleado)
                self.ventana_zona_juegos.show()
                
            
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Credenciales inválidas")
