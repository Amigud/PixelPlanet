from PyQt5 import QtWidgets, uic
from src.controlador.ControladorTorneo import ControladorTorneo
from src.modelo.vo.TorneoVO import TorneoVO

class VentanaTorneo(QtWidgets.QMainWindow):
    def __init__(self, empleado, parent=None):
        super().__init__(parent)
        uic.loadUi("./src/Ui/Torneo.ui", self)
        
        self.empleado = empleado
        self.parent = parent
        self.controlador = ControladorTorneo()
        self.participantes = []
        
        
        self.setWindowTitle(f"Crear Torneo")
        self.aceptarBoton.clicked.connect(self.agregar_participante)
        self.regresarBoton.clicked.connect(self.regresar)
        

    def agregar_participante(self):
        """Añade un participante al torneo o crea el torneo si ya hay datos"""
        nombre = self.torneoEdit.text().strip()
        juego = self.videojuegoEdit.text().strip()
        fecha = self.fechaEdit.date().toString("yyyy-MM-dd")
        email = self.emailEdit.text().strip()
        
        
        if not email:
            QtWidgets.QMessageBox.warning(self, "Error", "El email del participante es obligatorio")
            return
            
        if not self.validar_email(email):
            QtWidgets.QMessageBox.warning(self, "Error", "Formato de email inválido")
            return
        
        
        if nombre and juego and not self.participantes:
            self.participantes.append(email)
            QtWidgets.QMessageBox.information(
                self, 
                "Participante añadido",
                f"Torneo: {nombre}\nJuego: {juego}\nPrimer participante: {email}"
            )
            self.emailEdit.clear()
        
        elif nombre and juego:
            self.participantes.append(email)
            QtWidgets.QMessageBox.information(
                self,
                "Participante añadido",
                f"Participante {email} añadido al torneo"
            )
            self.emailEdit.clear()
        
        else:
            QtWidgets.QMessageBox.warning(
                self,
                "Error",
                "Complete nombre del torneo y juego primero"
            )

    def validar_email(self, email):
        """Validación simple de email"""
        return '@' in email and '.' in email.split('@')[-1]

    def regresar(self):
        """Regresa a la ventana anterior creando el torneo si hay datos"""
        nombre = self.torneoEdit.text().strip()
        juego = self.videojuegoEdit.text().strip()
        fecha = self.fechaEdit.date().toString("yyyy-MM-dd")
        
        if nombre and juego and self.participantes:
            respuesta = QtWidgets.QMessageBox.question(
                self,
                "Confirmar",
                f"¿Crear torneo {nombre} con {len(self.participantes)} participantes?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
            )
            
            if respuesta == QtWidgets.QMessageBox.Yes:
                if self.controlador.crear_torneo(
                    nombre=nombre,
                    juego=juego,
                    fecha=fecha,
                    empleado_id=self.empleado.id,
                    participantes=self.participantes
                ):
                    QtWidgets.QMessageBox.information(self, "Éxito", "Torneo creado correctamente")
                else:
                    QtWidgets.QMessageBox.critical(self, "Error", "No se pudo crear el torneo")
        
        if self.parent:
            self.parent.show()
        self.close()