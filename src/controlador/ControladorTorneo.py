from src.modelo.dao.TorneoDAOJDBC import TorneoDAOJDBC
from src.modelo.vo.TorneoVO import TorneoVO

class ControladorTorneo:
    def __init__(self):
        self.dao = TorneoDAOJDBC()

    def crear_torneo(self, nombre: str, juego: str, fecha: str, empleado_id: int, participantes: list) -> bool:
        torneo = TorneoVO(
            nombre=nombre,
            juego=juego,
            fecha=fecha,
            empleado_id=empleado_id,
            participantes=participantes
        )
        return self.dao.crear_torneo(torneo)