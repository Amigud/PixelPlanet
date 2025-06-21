from src.modelo.dao.SocioDAOJDBC import SocioDAOJDBC
from src.modelo.vo.SocioVO import SocioVO

class LogicaSocio:
    def __init__(self):
        self.dao = SocioDAOJDBC()

    def registrar_socio(self, socio: SocioVO) -> bool:
        existente = self.dao.buscar_por_email(socio.email)
        if existente:
            print(f"Ya existe un socio con el email {socio.email}")
            return False
        return self.dao.insertar_socio(socio)
