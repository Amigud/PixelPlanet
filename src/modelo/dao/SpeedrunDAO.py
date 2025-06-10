from abc import ABC, abstractmethod
from src.modelo.vo.SpeedrunVO import SpeedrunVO

class SpeedrunDAO(ABC):
    
    @abstractmethod
    def registrar_speedrun(self, speedrun: SpeedrunVO) -> bool:
        raise NotImplementedError()