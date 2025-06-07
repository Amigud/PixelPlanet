from PyQt5.QtWidgets import QApplication
from src.vista.VentanaLogin import VentanaLogin

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaLogin()
    ventana.show()
    app.exec_()
