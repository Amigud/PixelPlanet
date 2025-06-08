from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from src.controlador.ControladorZonaJuego import ControladorZonaJuego

class VentanaAsignZonaSocio(QtWidgets.QMainWindow):
    def __init__(self, empleado, parent=None):
        super().__init__(parent)
        uic.loadUi("./src/Ui/AsignZonaSocio.ui", self)
        
        self.empleado = empleado
        self.parent = parent
        self.controlador = ControladorZonaJuego()
        
        
        self.cargar_horarios()
        
        
        self.aceptarBoton.clicked.connect(self.asignar_zona)
        self.regresarBoton.clicked.connect(self.regresar)
        self.zonaEdit.textChanged.connect(self.actualizar_horarios)

    def cargar_horarios(self, zona_id=None):
        self.horarioBox.clear()
        if zona_id:
            horarios_disponibles = self.controlador.obtener_horarios_disponibles(zona_id)
            if not horarios_disponibles:
                horarios_disponibles = [f"{h}:00" for h in range(16, 22)]
        else:
            horarios_disponibles = [f"{h}:00" for h in range(16, 22)]
        
        self.horarioBox.addItems(horarios_disponibles)

    def actualizar_horarios(self):
        zona_id = self.zonaEdit.text().strip()
        if zona_id:
            try:
                self.cargar_horarios(int(zona_id))
            except ValueError:
                pass

    def asignar_zona(self):
        zona_id = self.zonaEdit.text().strip()
        email = self.emailEdit.text().strip()
        horario = self.horarioBox.currentText()
        trae_juego = self.traejuegoBox.isChecked()
        
        if not all([zona_id, email, horario]):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios")
            return
            
        try:
            zona_id = int(zona_id)
        except ValueError:
            QMessageBox.warning(self, "Error", "ID de zona debe ser un número")
            return
            
        success, message = self.controlador.asignar_zona(
            zona_id=zona_id,
            email_socio=email,
            horario=horario,
            trae_juego=trae_juego
        )
        
        if success:
            QMessageBox.information(self, "Éxito", message)
            self.limpiar_campos()
        else:
            QMessageBox.warning(self, "Error", message)

    def limpiar_campos(self):
        self.zonaEdit.clear()
        self.emailEdit.clear()
        self.traejuegoBox.setChecked(False)

    def regresar(self):
        if self.parent:
            self.parent.show()
        self.close()