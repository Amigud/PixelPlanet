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

    def obtener_productos(self):
        return self.dao.obtener_todos()

    def buscar_producto_por_id(self, pid):
        return self.dao.buscar_por_id(pid)

    def actualizar_producto(self, pid, nombre, descripcion, precio):
        try:
            return self.dao.actualizar(pid, nombre, descripcion, float(precio))
        except:
            return False

    def obtener_cantidad_producto(self, nombre):
        return self.dao.obtener_cantidad_por_nombre(nombre)

    def obtener_info_producto(self, nombre):
        return self.logica.obtener_id_y_cantidad(nombre)
    
    def restar_stock(self, producto_id, cantidad):
        return self.dao.restar_cantidad(producto_id, cantidad)
    
    def aumentar_stock(self, producto_id, cantidad):
        return self.dao.sumar_cantidad(producto_id, cantidad)
    
    def obtener_productos_stock_bajo(self, umbral=10):
        return self.dao.obtener_productos_stock_bajo(umbral)
    
    def eliminar_producto(self, producto_id):
        return self.logica.eliminar_producto(producto_id)
    
    def eliminar_unidades(self, producto_id, cantidad):
        if not isinstance(producto_id, int) or producto_id <= 0:
            return False, "ID inválido"

        if not isinstance(cantidad, int) or cantidad <= 0:
            return False, "Cantidad inválida"

        resultado, _ = self.logica.eliminar_unidades(producto_id, cantidad)
        return resultado




