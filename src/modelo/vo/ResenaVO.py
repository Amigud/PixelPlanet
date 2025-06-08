class ResenaVO:
    def __init__(self, estrellas, comentario, cod_producto):
        self._estrellas = estrellas
        self._comentario = comentario
        self._cod_producto = cod_producto

    @property
    def estrellas(self): return self._estrellas
    @property
    def comentario(self): return self._comentario
    @property
    def cod_producto(self): return self._cod_producto
