from src.modelo.vo.ProductoVO import ProductoVO

class ProductoDAO:
    def select(self) -> list[ProductoVO]:
        raise NotImplementedError()

    def insert(self, producto: ProductoVO) -> int:
        raise NotImplementedError()

    def devolver_producto(self, nombre: str, cantidad: int) -> bool:
        raise NotImplementedError()

    def obtener_id_y_cantidad_por_nombre(self, nombre: str):
        raise NotImplementedError()

    def obtener_cantidad_por_nombre(self, nombre: str):
        raise NotImplementedError()

    def buscar_por_id(self, producto_id: int):
        raise NotImplementedError()

    def restar_cantidad(self, producto_id: int, cantidad: int) -> bool:
        raise NotImplementedError()
