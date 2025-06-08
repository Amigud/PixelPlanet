from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from src.controlador.ControladorZonaJuego import ControladorZonaJuego

class VentanaElimZonaSocio(QtWidgets.QMainWindow):
    def __init__(self, empleado, parent=None):
        super().__init__(parent)
        uic.loadUi("./src/Ui/ElimZonaSocio.ui", self)
        
        self.empleado = empleado
        self.parent = parent
        self.controlador = ControladorZonaJuego()
        
        
        self.aceptarElimBoton.clicked.connect(self.eliminar_asignacion)
        self.regresarElimBoton.clicked.connect(self.regresar)

    def eliminar_asignacion(self):
        zona_id = self.zonaElimEdit.text().strip()
        email = self.emailElimEdit.text().strip()
        
        if not all([zona_id, email]):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios")
            return
            
        try:
            zona_id = int(zona_id)
        except ValueError:
            QMessageBox.warning(self, "Error", "ID de zona debe ser un número")
            return
            
        success, message = self.controlador.eliminar_asignacion(zona_id, email)
        
        if success:
            QMessageBox.information(self, "Éxito", message)
            self.limpiar_campos()
        else:
            QMessageBox.warning(self, "Error", message)

    def limpiar_campos(self):
        self.zonaElimEdit.clear()
        self.emailElimEdit.clear()

    def regresar(self):
        if self.parent:
            self.parent.show()
        self.close()