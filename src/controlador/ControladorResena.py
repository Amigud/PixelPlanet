from src.modelo.logica.LogicaResena import LogicaResena

class ControladorResena:
    def __init__(self):
        self.logica = LogicaResena()

    def insertar_resena(self, nombre_producto, comentario, estrellas, empleado_id):
        if not nombre_producto:
            return False, None
        if not (1 <= estrellas <= 5):
            return False, None
        
        comentario = comentario.strip() if comentario else ""

        return self.logica.insertar_resena(nombre_producto.strip(), comentario, estrellas, empleado_id)
