from abc import ABC, abstractmethod
from src.modelo.vo.TorneoVO import TorneoVO

class TorneoDAO(ABC):
    
    @abstractmethod
    def crear_torneo(self, torneo: TorneoVO) -> bool:
        raise NotImplementedError()
    