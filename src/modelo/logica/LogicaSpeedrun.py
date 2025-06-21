from src.modelo.dao.SpeedrunDAOJDBC import SpeedrunDAOJDBC
from src.modelo.vo.SpeedrunVO import SpeedrunVO

class LogicaSpeedrun:
    def __init__(self):
        self.dao = SpeedrunDAOJDBC()

    def registrar_speedrun(self, speedrun: SpeedrunVO) -> bool:
        
        return self.dao.registrar_speedrun(speedrun)
