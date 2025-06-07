from src.modelo.dao.SpeedrunDAOJDBC import SpeedrunDAOJDBC
from src.modelo.vo.SpeedrunVO import SpeedrunVO

class ControladorSpeedrun:
    def __init__(self):
        self.dao = SpeedrunDAOJDBC()

    def registrar_speedrun(self, juego, email_socio, tiempo, empleado_id):
        speedrun = SpeedrunVO(
            juego=juego,
            email_socio=email_socio,
            tiempo=tiempo,
            empleado_id=empleado_id
        )
        return self.dao.registrar_speedrun(speedrun)