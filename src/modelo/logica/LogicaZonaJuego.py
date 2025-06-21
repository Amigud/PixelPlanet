from src.modelo.dao.AsignacionZonaDAOJDBC import AsignacionZonaDAOJDBC
from src.modelo.dao.SocioDAOJDBC import SocioDAOJDBC

class LogicaZonaJuego:
    def __init__(self):
        self.dao_zona = AsignacionZonaDAOJDBC()
        self.dao_socio = SocioDAOJDBC()

    def asignar_zona(self, asignacion_vo, email_socio: str) -> tuple:
        if not self.dao_zona.verificar_disponibilidad(asignacion_vo.zona_id, asignacion_vo.horario):
            return False, "Zona no disponible en ese horario"

        socio = self.dao_socio.buscar_por_email(email_socio)
        if not socio:
            return False, "Socio no encontrado"

        
        asignacion_vo._cliente_id = socio.id

        if self.dao_zona.asignar_zona(asignacion_vo):
            return True, f"Zona {asignacion_vo.zona_id} asignada exitosamente"
        return False, "Error al asignar la zona"

    def eliminar_asignacion(self, zona_id: int, email_socio: str) -> tuple:
        
        socio = self.dao_socio.buscar_por_email(email_socio)
        if not socio:
            return False, "Socio no encontrado"

        success = self.dao_zona.eliminar_asignacion(zona_id, email_socio)

        if success:
            return True, f"Asignación de zona {zona_id} eliminada"
        return False, "No se encontró la asignación o ocurrió un error"


    def obtener_horarios_disponibles(self, zona_id: int) -> list:
        return self.dao_zona.obtener_horarios_disponibles(zona_id)
