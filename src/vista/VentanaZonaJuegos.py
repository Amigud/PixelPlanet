from PyQt5 import QtWidgets, uic
from src.vista.dialogs import SpeedrunDialog, TorneoDialog, ZonaJuegoDialog

class VentanaZonaJuegos(QtWidgets.QMainWindow):
    def __init__(self, empleado_id):
        super().__init__()
        uic.loadUi("./src/Ui/ZonaJuegos.ui", self)
        self.empleado_id = empleado_id
        
        # Conectar botones
        self.speedrunBoton.clicked.connect(self.abrir_speedrun)
        self.torneoBoton.clicked.connect(self.abrir_torneo)
        self.zonajuegoBoton.clicked.connect(self.abrir_zona_juego)

    def abrir_speedrun(self):
        dialog = SpeedrunDialog(self.empleado_id, self)
        dialog.exec_()

    def abrir_torneo(self):
        dialog = TorneoDialog(self.empleado_id, self)
        dialog.exec_()

    def abrir_zona_juego(self):
        dialog = ZonaJuegoDialog(self.empleado_id, self)
        dialog.exec_()