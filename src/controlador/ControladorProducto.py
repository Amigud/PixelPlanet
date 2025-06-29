from src.modelo.logica.LogicaProducto import LogicaProducto
from src.modelo.vo.ProductoVO import ProductoVO

class ControladorProducto:
    def __init__(self):
        self.logica = LogicaProducto()

    def registrar_producto(self, nombre, descripcion, precio_texto, cantidad):
        
        if not all([nombre.strip(), precio_texto.strip()]):
            return False
        
        try:
            precio = float(precio_texto)
            if precio < 0 or cantidad <= 0:
                return False
        except ValueError:
            return False
        
        descripcion_text = descripcion if descripcion else ""

        producto_vo = ProductoVO(
            id_producto=None,
            nombre=nombre.strip(),
            descripcion=descripcion_text,
            precio=precio,
            cantidad=cantidad
        )

        return self.logica.registrar_producto(producto_vo)

    def obtener_info_producto(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            return None
        return self.logica.obtener_id_y_cantidad(nombre)
    
    def obtener_productos_stock_bajo(self, umbral=10):
        if not isinstance(umbral,int) or umbral < 0:
            return False        
        return self.logica.obtener_productos_stock_bajo(umbral)
    
    def eliminar_producto(self, producto_id):
        return self.logica.eliminar_producto(producto_id)
    
    def eliminar_unidades(self, producto_id, cantidad):
        if not isinstance(producto_id, int) or producto_id <= 0:
            return False, "ID inválido"

        if not isinstance(cantidad, int) or cantidad <= 0:
            return False, "Cantidad inválida"

        resultado, _ = self.logica.eliminar_unidades(producto_id, cantidad)
        return resultado
    
    def devolver_producto(self, nombre, cantidad):
        if not isinstance(nombre, str) or not nombre.strip():
            return False, "Nombre no válido"

        if not isinstance(cantidad, int) or cantidad <= 0:
            return False, "Cantidad inválida"

        return self.logica.devolver_producto(nombre.strip(), cantidad)
    
    def realizar_pedido_proveedor(self, nombre_producto, nombre_proveedor, cantidad):
        if not nombre_producto.strip() or not nombre_proveedor.strip():
            return False, "Nombre de producto o proveedor no válido."

        if not isinstance(cantidad, int) or cantidad <= 0:
            return False, "Cantidad inválida"

        return self.logica.procesar_pedido_proveedor(nombre_producto.strip(), nombre_proveedor.strip(), cantidad)
    
    def obtener_precio_producto(self, nombre):
        return self.logica.obtener_precio_producto(nombre)






