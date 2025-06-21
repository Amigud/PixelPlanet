from src.modelo.logica.LogicaTorneo import LogicaTorneo

class ControladorTorneo:
    def __init__(self):
        self.logica = LogicaTorneo()

    def crear_torneo(self, nombre: str, juego: str, fecha: str, empleado_id: int, participantes: list) -> bool:
        
        if not nombre or not juego or not fecha or not participantes:
            print("Faltan campos obligatorios.")
            return False
        
        if not isinstance(empleado_id, int) or empleado_id <= 0:
            print("ID de empleado inválido.")
            return False

        if not all(self.validar_email(p) for p in participantes):
            print("Hay correos inválidos.")
            return False

        return self.logica.crear_torneo(nombre, juego, fecha, empleado_id, participantes)

    def validar_email(self, email: str) -> bool:
        return '@' in email and '.' in email.split('@')[-1]
