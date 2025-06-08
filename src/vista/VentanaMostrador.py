from PyQt5 import QtWidgets, uic
from src.vista.VentanaSocio import VentanaSocio


class VentanaMostrador(QtWidgets.QMainWindow):
    def __init__(self, empleado, parent=None):
        super().__init__(parent)
        uic.loadUi("./src/Ui/Mostrador.ui", self)

        self.empleado = empleado
        self.parent = parent

        
        self.socioBoton.clicked.connect(self.abrir_socio)

    
    def abrir_socio(self):
        self.hide()
        self.ventana_socio = VentanaSocio(self.empleado, self)
        self.ventana_socio.show()

        

    