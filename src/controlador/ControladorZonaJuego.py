from src.modelo.logica.LogicaZonaJuego import LogicaZonaJuego
from src.modelo.vo.AsignacionZonaVO import AsignacionZonaVO

class ControladorZonaJuego:
    def __init__(self):
        self.logica = LogicaZonaJuego()

    def asignar_zona(self, zona_id: int, email_socio: str, horario: str, trae_juego: bool) -> tuple:
        
        if not email_socio or '@' not in email_socio or '.' not in email_socio.split('@')[-1]:
            return False, "Email no válido"

        if not isinstance(zona_id, int) or zona_id <= 0:
            return False, "ID de zona inválido"

        if not horario:
            return False, "Horario requerido"
 
        asignacion = AsignacionZonaVO(
            zona_id=zona_id,
            horario=horario,
            trae_juego=trae_juego
        )

        return self.logica.asignar_zona(asignacion, email_socio)

    def eliminar_asignacion(self, zona_id: int, email_socio: str) -> tuple:
        
        if not isinstance(zona_id, int) or zona_id <= 0:
            return False, "ID de zona inválido"
        if not email_socio or '@' not in email_socio or '.' not in email_socio.split('@')[-1]:
            return False, "Email no válido"

        return self.logica.eliminar_asignacion(zona_id, email_socio)

    def obtener_horarios_disponibles(self, zona_id: int) -> list:
        if isinstance(zona_id, int) and zona_id > 0:
            return self.logica.obtener_horarios_disponibles(zona_id)
        return []