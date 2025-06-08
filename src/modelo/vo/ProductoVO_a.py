class ProductoVO:
    def __init__(self, id_producto, nombre, descripcion, precio, cantidad):
        self._id_producto = id_producto
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio
        self._cantidad = cantidad

    @property
    def id_producto(self):
        return self._id_producto

    @property
    def nombre(self):
        return self._nombre

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def precio(self):
        return self._precio

    @property
    def cantidad(self):
        return self._cantidad