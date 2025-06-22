from src.modelo.vo.ResenaVO import ResenaVO

class ResenaDAO:
    def insertar_resena(self, resena: ResenaVO) -> bool:
        raise NotImplementedError()

    def obtener_valoraciones_por_producto(self, producto_id: int) -> list[int]:
        raise NotImplementedError()