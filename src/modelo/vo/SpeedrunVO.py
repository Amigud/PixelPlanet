class SpeedrunVO:
    def __init__(self, speedrun_id=None, juego=None, email_socio=None, tiempo=None, empleado_id=None):
        self._id = speedrun_id
        self._juego = juego
        self._email_socio = email_socio
        self._tiempo = tiempo
        self._empleado_id = empleado_id

    @property
    def id(self):
        return self._id

    @property
    def juego(self):
        return self._juego

    @property
    def email_socio(self):
        return self._email_socio

    @property
    def tiempo(self):
        return self._tiempo

    @property
    def empleado_id(self):
        return self._empleado_id