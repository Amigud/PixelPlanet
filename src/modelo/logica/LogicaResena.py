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
            return False, None

        producto_id, _ = info
        resena = ResenaVO(estrellas, comentario, producto_id, cod_empleado)
        exito = self.dao_resena.insertar_resena(resena)
        if exito:
            media = self.calcular_media_valoraciones(producto_id)
            return True, media
        return False, None

    
    def calcular_media_valoraciones(self, producto_id):
        valoraciones = self.dao_resena.obtener_valoraciones_por_producto(producto_id)
        if not valoraciones:
            return 0.0
        return round(sum(valoraciones) / len(valoraciones), 2)

