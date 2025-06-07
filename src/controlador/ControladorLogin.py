from src.modelo.dao.EmpleadoDAOJDBC import EmpleadoDAOJDBC

class ControladorLogin:
    def __init__(self):
        self.dao = EmpleadoDAOJDBC()

    def validar_credenciales(self, email: str, contrasena: str):
        empleado = self.dao.login(email, contrasena)
        return empleado
