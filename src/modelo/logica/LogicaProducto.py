from src.modelo.dao.ProductoDAOJDBC import ProductoDAOJDBC
from src.modelo.vo.ProductoVO import ProductoVO

class LogicaProducto:
    def __init__(self):
        self.dao = ProductoDAOJDBC()

    def obtener_id_y_cantidad(self, nombre):
        return self.dao.obtener_id_y_cantidad_por_nombre(nombre)
    
    def obtener_cantidad_por_id(self, producto_id):
        return self.dao.obtener_cantidad_por_id(producto_id)

    def registrar_producto(self, producto: ProductoVO):
        return self.dao.insert(producto) > 0
    
    def eliminar_unidades(self, producto_id, cantidad):
        
        cantidad_actual = self.dao.obtener_cantidad_por_id(producto_id)

        if cantidad_actual is None:
            return False, "Producto no encontrado"

        if cantidad > cantidad_actual:
            return False, "No puedes eliminar más de las disponibles"

        
        else:
            exito = self.dao.restar_cantidad(producto_id, cantidad)
            if exito:
                return True, f"Se eliminaron {cantidad} unidades"
            return False, "Error al restar unidades"
        
    def eliminar_producto(self, producto_id):
        return self.dao.eliminar_producto(producto_id)
    
    def devolver_producto(self, nombre, cantidad):
        producto_info = self.dao.obtener_id_y_cantidad_por_nombre(nombre)

        if not producto_info:
            return False, "Producto no encontrado"

        exito = self.dao.devolver_producto(nombre, cantidad)
        if exito:
            return True, f"Se añadieron {cantidad} unidades al stock del producto '{nombre}'."
        return False, "No se pudo registrar la devolución"

    def procesar_pedido_proveedor(self, nombre_producto, nombre_proveedor, cantidad):
        
        producto_info = self.dao.obtener_id_y_cantidad_por_nombre(nombre_producto)
        
        if not producto_info:
            return False, "Producto no encontrado"

        producto_id, cantidad_actual = producto_info

        exito = self.dao.sumar_cantidad(producto_id, cantidad)
        if exito:
            return True, f"Se ha actualizado el stock de '{nombre_producto}' con {cantidad} unidades."
        return False, "Error al actualizar el stock"

    def obtener_productos_stock_bajo(self, umbral):
        return self.dao.obtener_productos_stock_bajo(umbral)
    
    def obtener_precio_producto(self, nombre):
        return self.dao.obtener_precio_por_nombre(nombre)
