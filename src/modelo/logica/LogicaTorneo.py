from src.modelo.vo.TorneoVO import TorneoVO
from src.modelo.dao.TorneoDAOJDBC import TorneoDAOJDBC
from src.modelo.dao.SocioDAOJDBC import SocioDAOJDBC

class LogicaTorneo:
    def __init__(self):
        self.dao_torneo = TorneoDAOJDBC()
        self.dao_socio = SocioDAOJDBC()

    def crear_torneo(self, nombre: str, juego: str, fecha: str, empleado_id: int, emails_participantes: list[str]) -> bool:

        for email in emails_participantes:
            socio = self.dao_socio.buscar_por_email(email)
            if not socio:
                print(f"Socio no encontrado: {email}")
                return False

        torneo_vo = TorneoVO(
            nombre=nombre,
            juego=juego,
            fecha=fecha,
            empleado_id=empleado_id,
            participantes=emails_participantes
        )

        return self.dao_torneo.crear_torneo(torneo_vo)
