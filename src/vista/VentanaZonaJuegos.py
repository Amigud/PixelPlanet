from PyQt5 import uic, QtWidgets
from src.vista.VentanaSpeedrun import VentanaSpeedrun


class VentanaZonaJuegos(QtWidgets.QMainWindow):
    def __init__(self, empleado):
        super().__init__()
        uic.loadUi("./src/Ui/ZonaJuegos.ui", self)
        self.empleado = empleado
        self.setWindowTitle(f"Zona de Juegos - {self.empleado.email}")
        
        
        self.ventana_speedrun = None
        self.ventana_torneo = None
        self.ventana_asignar_zona = None
        
        
        self.speedrunBoton.clicked.connect(self.abrir_speedrun)

    def abrir_speedrun(self):
        self.hide()
        if not self.ventana_speedrun:
            self.ventana_speedrun = VentanaSpeedrun(self.empleado, self)
        self.ventana_speedrun.show()
        