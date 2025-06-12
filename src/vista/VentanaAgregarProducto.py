from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from src.modelo.dao.ProductoDAOJDBC import ProductoDAOJDBC
from src.modelo.vo.ProductoVO import ProductoVO

class VentanaAgregarProducto(QtWidgets.QMainWindow):
    def __init__(self, empleado, parent=None):
        super().__init__(parent)
        uic.loadUi("./src/Ui/AnadirProducto.ui", self)

        self.empleado = empleado
        self.parent = parent
        self.dao = ProductoDAOJDBC()

        self.setWindowTitle(f"Agregar producto")
        self.aceptarBoton.clicked.connect(self.registrar_producto)
        self.regresarBoton.clicked.connect(self.regresar)

    def registrar_producto(self):
        nombre = self.nombreEdit.text().strip()
        descripcion = self.descrEdit.text().strip()
        precio_texto = self.precioEdit.text().strip()
        cantidad = self.cantBox.value()

        if not all([nombre, descripcion, precio_texto]):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        try:
            precio = float(precio_texto)
            if precio < 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Error", "El precio debe ser un número válido.")
            return

        producto = ProductoVO(
            id_producto=None,
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            cantidad=cantidad
        )

        resultado = self.dao.insert(producto)
        if resultado > 0:
            QMessageBox.information(self, "Éxito", "Producto registrado correctamente.")
            self.limpiar()
        else:
            QMessageBox.critical(self, "Error", "No se pudo registrar el producto.")

    def limpiar(self):
        self.nombreEdit.clear()
        self.descrEdit.clear()
        self.precioEdit.clear()
        self.cantBox.setValue(1)

    def regresar(self):
        if self.parent:
            self.parent.show()
        self.close()
