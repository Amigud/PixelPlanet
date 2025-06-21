from src.modelo.logica.LogicaLogin import LogicaLogin

class ControladorLogin:
    def __init__(self):
        self.logica = LogicaLogin()

    def validar_credenciales(self, email: str, contrasena: str):
        if not email or "@" not in email:
            return None
        if not contrasena:
            return None
        return self.logica.autenticar(email, contrasena)
