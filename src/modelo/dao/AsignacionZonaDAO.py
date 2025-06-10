from abc import ABC, abstractmethod
from src.modelo.vo.AsignacionZonaVO import AsignacionZonaVO

class AsignacionZonaDAO(ABC):

    @abstractmethod
    def asignar_zona(self, asignacion: AsignacionZonaVO) -> bool:
        pass

    @abstractmethod
    def eliminar_asignacion(self, zona_id: int, email_socio: str) -> bool:
        pass

    @abstractmethod
    def verificar_disponibilidad(self, zona_id: int, horario: str) -> bool:
        pass

    @abstractmethod
    def obtener_horarios_disponibles(self, zona_id: int) -> list:
        pass
