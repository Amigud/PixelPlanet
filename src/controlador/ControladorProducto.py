from src.modelo.dao.ProductoDAOJDBC import ProductoDAOJDBC

class ControladorProducto:
    def __init__(self):
        self.dao = ProductoDAOJDBC()

    def registrar_producto(self, nombre, descripcion, precio, generos):
        try:
            precio = float(precio)
            producto_id = self.dao.insertar_producto(nombre, descripcion, precio)
            self.dao.insertar_generos(producto_id, generos.split(","))
            return True
        except:
            return False

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
        return self.dao.obtener_id_y_cantidad_por_nombre(nombre)
    
    def restar_stock(self, producto_id, cantidad):
        return self.dao.restar_cantidad(producto_id, cantidad)
    
    def aumentar_stock(self, producto_id, cantidad):
        return self.dao.sumar_cantidad(producto_id, cantidad)
    
    def obtener_productos_stock_bajo(self, umbral=10):
        return self.dao.obtener_productos_stock_bajo(umbral)



