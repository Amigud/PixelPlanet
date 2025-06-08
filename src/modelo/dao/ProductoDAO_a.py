from src.modelo.vo.ProductoVO_a import ProductoVO

class ProductoDAO:
    def select(self) -> list[ProductoVO]:
        """
        Recupera todos los productos de la base de datos.
        """
        raise NotImplementedError()

    def insert(self, producto: ProductoVO) -> int:
        """
        Inserta un nuevo producto en la base de datos.
        """
        raise NotImplementedError()

    def devolver_producto(self, nombre: str, cantidad: int) -> bool:
        """
        Procesa la devolución restando cantidad a un producto existente.
        """
        raise NotImplementedError()
