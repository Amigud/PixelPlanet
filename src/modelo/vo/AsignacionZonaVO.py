class AsignacionZonaVO:
    def __init__(self, id=None, zona_id=None, cliente_id=None, horario=None, trae_juego=False):
        self._id = id
        self._zona_id = zona_id
        self._cliente_id = cliente_id
        self._horario = horario
        self._trae_juego = trae_juego

    @property
    def id(self):
        return self._id

    @property
    def zona_id(self):
        return self._zona_id

    @property
    def cliente_id(self):
        return self._cliente_id

    @property
    def horario(self):
        return self._horario

    @property
    def trae_juego(self):
        return self._trae_juego