from PyQt5 import QtWidgets, uic
from src.controlador.ControladorSpeedrun import ControladorSpeedrun

class VentanaSpeedrun(QtWidgets.QMainWindow):
    def __init__(self, empleado, parent = None):
        super().__init__()
        uic.loadUi("./src/Ui/Speedrun.ui", self)
        
        
        self.empleado = empleado
        self.controlador = ControladorSpeedrun()
        self.parent = parent
       
        self.aceptarBoton.clicked.connect(self.registrar_speedrun)
        self.regresarBoton.clicked.connect(self.regresar)
        
        
        self.setWindowTitle(f"Registrar Speedrun")

    def registrar_speedrun(self):
        """Recoge los datos del formulario y los guarda en la base de datos"""
        
        tiempo = self.tiempoEdit.text()
        email = self.emailEdit.text()
        juego = self.juegoEdit.text()
        
        
        if not all([tiempo, email, juego]):
            QtWidgets.QMessageBox.warning(self, "Error", "Todos los campos son obligatorios")
            return
        
        
        if len(tiempo.split(':')) != 3:
            QtWidgets.QMessageBox.warning(self, "Error", "Formato de tiempo inválido. Use HH:MM:SS")
            return
        
        
        if self.controlador.registrar_speedrun(
            juego=juego,
            email_socio=email,
            tiempo=tiempo,
            empleado_id=self.empleado.id
        ):
            QtWidgets.QMessageBox.information(self, "Éxito", "Speedrun registrado correctamente")
            self.limpiar_campos()
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "No se pudo registrar el speedrun")

    def limpiar_campos(self):
        """Limpia todos los campos del formulario"""
        self.tiempoEdit.clear()
        self.emailEdit.clear()
        self.juegoEdit.clear()

    def regresar(self):
        """Cierra esta ventana y vuelve a ZonaJuegos"""
        if self.parent:
            self.parent.show()  
        self.close()