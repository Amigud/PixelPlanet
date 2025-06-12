from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from src.modelo.dao.ResenaDAOJDBC import ResenaDAOJDBC
from src.modelo.vo.ResenaVO import ResenaVO

class VentanaResena(QtWidgets.QMainWindow):
    def __init__(self, empleado, parent=None):
        super().__init__(parent)
        uic.loadUi("./src/Ui/Resena.ui", self)

        self.empleado = empleado
        self.parent = parent
        self.dao = ResenaDAOJDBC()

        self.setWindowTitle(f"Insertar una Reseña")
        self.aceptarBoton.clicked.connect(self.insertar_resena)
        self.regresarBoton.clicked.connect(self.regresar)

    def insertar_resena(self):
        nombre_producto = self.nombreProdEdit.text().strip()
        comentario = self.comentEdit.text().strip()
        estrellas = self.estrellasBox.value()

        if not nombre_producto or not comentario:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        try:
            
            cursor = self.dao.getCursor()
            cursor.execute("SELECT ProductoID FROM productos WHERE Nombre = ?", (nombre_producto,))
            row = cursor.fetchone()
            if not row:
                QMessageBox.warning(self, "Error", "Producto no encontrado.")
                return
            producto_id = row[0]
            cursor.close()
            self.dao.closeConnection()
        except Exception as e:
            print(f"Error al buscar producto: {e}")
            QMessageBox.critical(self, "Error", "Error al buscar el producto.")
            return

        resena = ResenaVO(estrellas, comentario, producto_id, self.empleado.id)
        if self.dao.insertar_resena(resena):
            QMessageBox.information(self, "Éxito", "Reseña registrada correctamente.")
            self.limpiar()
        else:
            QMessageBox.critical(self, "Error", "No se pudo registrar la reseña.")

    def limpiar(self):
        self.nombreProdEdit.clear()
        self.comentEdit.clear()
        self.estrellasBox.setValue(1)

    def regresar(self):
        if self.parent:
            self.parent.show()
        self.close()
