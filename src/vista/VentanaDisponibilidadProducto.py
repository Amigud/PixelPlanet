from PyQt5 import uic, QtWidgets
from src.controlador.ControladorProducto import ControladorProducto

class VentanaDisponibilidadProducto(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("src/Ui/VentanaDisponibilidadProducto.ui", self)
        self.controlador = ControladorProducto()
        self.botonConsultar.clicked.connect(self.mostrar_productos)

    def mostrar_productos(self):
        productos = self.controlador.obtener_productos()
        self.tabla.setRowCount(0)
        for i, prod in enumerate(productos):
            self.tabla.insertRow(i)
            for j, dato in enumerate(prod):
                self.tabla.setItem(i, j, QtWidgets.QTableWidgetItem(str(dato)))
