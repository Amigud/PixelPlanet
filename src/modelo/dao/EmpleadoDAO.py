from src.modelo.vo.EmpleadoVO import EmpleadoVO

class EmpleadoDAO:
    def login(self, email: str, contrasena: str) -> EmpleadoVO | None:
        raise NotImplementedError("login() no implementado")
