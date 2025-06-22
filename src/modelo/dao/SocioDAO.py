from src.modelo.vo.SocioVO import SocioVO

class SocioDAO:
    def buscar_por_email(self, email: str) -> SocioVO | None:
        raise NotImplementedError("Método buscar_por_email() no implementado")
    
    def insertar_socio(self, socio: SocioVO) -> bool:
        raise NotImplementedError()

    def obtener_puntos_por_email(self, email: str) -> int | None:
        raise NotImplementedError()
    
    def sumar_puntos(self, email: str, puntos: int) -> bool:
        raise NotImplementedError()