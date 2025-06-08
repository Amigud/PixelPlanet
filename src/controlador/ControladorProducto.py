from src.modelo.dao.ProductoDAO import ProductoDAO

class ControladorProducto:
    def __init__(self):
        self.dao = ProductoDAO()

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
