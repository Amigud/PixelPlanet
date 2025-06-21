from src.modelo.dao.EmpleadoDAOJDBC import EmpleadoDAOJDBC
from src.modelo.vo.EmpleadoVO import EmpleadoVO

class LogicaLogin:
    def __init__(self):
        self.dao = EmpleadoDAOJDBC()

    def autenticar(self, email: str, contrasena: str) -> EmpleadoVO | None:
        return self.dao.login(email, contrasena)
