from src.modelo.logica.LogicaSpeedrun import LogicaSpeedrun
from src.modelo.vo.SpeedrunVO import SpeedrunVO

class ControladorSpeedrun:
    def __init__(self):
        self.logica = LogicaSpeedrun()

    def registrar_speedrun(self, juego, email_socio, tiempo, empleado_id):
        
        if not all([juego.strip(), email_socio.strip(), tiempo.strip()]):
            return False
        if '@' not in email_socio or '.' not in email_socio.split('@')[-1]:
            return False
        if len(tiempo.split(':')) != 3:
            return False
        
        speedrun = SpeedrunVO(
            juego=juego.strip(),
            email_socio=email_socio.strip(),
            tiempo=tiempo.strip(),
            empleado_id=empleado_id
        )
        return self.logica.registrar_speedrun(speedrun)