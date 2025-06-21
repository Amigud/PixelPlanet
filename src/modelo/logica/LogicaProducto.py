from src.modelo.dao.ProductoDAOJDBC import ProductoDAOJDBC
from src.modelo.vo.ProductoVO import ProductoVO

class LogicaProducto:
    def __init__(self):
        self.dao_producto = ProductoDAOJDBC()

    def registrar_producto(self, producto: ProductoVO):
        return self.dao_producto.insert(producto) > 0
