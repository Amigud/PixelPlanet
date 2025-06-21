from src.modelo.dao.ResenaDAOJDBC import ResenaDAOJDBC
from src.modelo.dao.ProductoDAOJDBC import ProductoDAOJDBC
from src.modelo.vo.ResenaVO import ResenaVO

class LogicaResena:
    def __init__(self):
        self.dao_resena = ResenaDAOJDBC()
        self.dao_producto = ProductoDAOJDBC()

    def insertar_resena(self, nombre_producto, comentario, estrellas, cod_empleado):
        info = self.dao_producto.obtener_id_y_cantidad_por_nombre(nombre_producto)
        if not info:
            print("Producto no encontrado para reseña.")
            return False

        producto_id, _ = info
        resena = ResenaVO(estrellas, comentario, producto_id, cod_empleado)
        return self.dao_resena.insertar_resena(resena)
