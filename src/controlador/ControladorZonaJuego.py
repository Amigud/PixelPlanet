from src.modelo.dao.AsignacionZonaDAOJDBC import AsignacionZonaDAOJDBC
from src.modelo.dao.SocioDAOJDBC import SocioDAOJDBC
from src.modelo.vo.AsignacionZonaVO import AsignacionZonaVO

class ControladorZonaJuego:
    def __init__(self):
        self.asignacion_dao = AsignacionZonaDAOJDBC()
        self.socio_dao = SocioDAOJDBC()

    def asignar_zona(self, zona_id: int, email_socio: str, horario: str, trae_juego: bool) -> tuple:
        
        if not self.asignacion_dao.verificar_disponibilidad(zona_id, horario):
            return False, "La zona no está disponible en ese horario"

        
        socio = self.socio_dao.buscar_por_email(email_socio)
        if not socio:
            return False, "Socio no encontrado"

        
        asignacion = AsignacionZonaVO(
            zona_id=zona_id,
            cliente_id=socio.id,
            horario=horario,
            trae_juego=trae_juego
        )

        if self.asignacion_dao.asignar_zona(asignacion):
            return True, f"Zona {zona_id} asignada exitosamente a las {horario}"
        return False, "Error al asignar la zona"

    def eliminar_asignacion(self, zona_id: int, email_socio: str) -> tuple:
        success = self.asignacion_dao.eliminar_asignacion(zona_id, email_socio)
        if success:
            return True, f"Asignación de zona {zona_id} eliminada"
        return False, "No se encontró la asignación o ocurrió un error"

    def obtener_horarios_disponibles(self, zona_id: int) -> list:
        return self.asignacion_dao.obtener_horarios_disponibles(zona_id)