from PyQt5 import QtWidgets, uic
from src.vista.VentanaAsignZonaSocio import VentanaAsignZonaSocio
from src.vista.VentanaElimZonaSocio import VentanaElimZonaSocio

class VentanaAsignarZona(QtWidgets.QMainWindow):
    def __init__(self, empleado, parent=None):
        super().__init__(parent)
        uic.loadUi("./src/Ui/AsigZona.ui", self)
        
        self.empleado = empleado
        self.parent = parent
        
        
        self.asignarBoton.clicked.connect(self.abrir_asignar)
        self.eliminarBoton.clicked.connect(self.abrir_eliminar)
        self.btn_regresar.clicked.connect(self.regresar)

    def abrir_asignar(self):
        self.hide()
        self.ventana_asignar = VentanaAsignZonaSocio(self.empleado, self)
        self.ventana_asignar.show()

    def abrir_eliminar(self):
        self.hide()
        self.ventana_eliminar = VentanaElimZonaSocio(self.empleado, self)
        self.ventana_eliminar.show()

    def regresar(self):
        
        if self.parent:
            self.parent.show()
        self.close()
        