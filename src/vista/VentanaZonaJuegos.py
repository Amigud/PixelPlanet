from PyQt5 import uic, QtWidgets
from src.vista.VentanaSpeedrun import VentanaSpeedrun
from src.vista.VentanaTorneo import VentanaTorneo
from src.vista.VentanaAsignarZona import VentanaAsignarZona
from src.vista.VentanaSocio import VentanaSocio
from src.vista.VentanaConsultaSocio import VentanaConsultaSocio


class VentanaZonaJuegos(QtWidgets.QMainWindow):
    def __init__(self, empleado):
        super().__init__()
        uic.loadUi("./src/Ui/ZonaJuegos.ui", self)
        self.empleado = empleado
        self.setWindowTitle(f"Zona de Juegos - {self.empleado.email}")
        
        
        self.ventana_speedrun = None
        self.ventana_torneo = None
        self.ventana_asignar_zona = None
        
        self.setWindowTitle(f"Menu Zona de Juegos")
        self.consSocioBoton.clicked.connect(self.abrir_consultar_socio)
        self.socioBoton.clicked.connect(self.abrir_socio)
        self.speedrunBoton.clicked.connect(self.abrir_speedrun)
        self.torneoBoton.clicked.connect(self.abrir_torneo)
        self.zonajuegoBoton.clicked.connect(self.abrir_asignar_zona)

    def abrir_socio(self):
        self.hide()
        self.ventana_socio = VentanaSocio(self.empleado, self)
        self.ventana_socio.show()

    def abrir_consultar_socio(self):
        self.hide()
        self.ventana_consulta = VentanaConsultaSocio(self.empleado, self)
        self.ventana_consulta.show()

    def abrir_speedrun(self):
        self.hide()
        if not self.ventana_speedrun:
            self.ventana_speedrun = VentanaSpeedrun(self.empleado, self)
        self.ventana_speedrun.show()

    def abrir_torneo(self):
        self.hide()
        if not self.ventana_torneo:
            self.ventana_torneo = VentanaTorneo(self.empleado, self)
        self.ventana_torneo.show()
        
    def abrir_asignar_zona(self):
        self.hide()
        if not self.ventana_asignar_zona:
            self.ventana_asignar_zona = VentanaAsignarZona(self.empleado, self)
        self.ventana_asignar_zona.show()
        
        