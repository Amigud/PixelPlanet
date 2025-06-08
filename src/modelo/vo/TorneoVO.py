class TorneoVO:
    def __init__(self, torneo_id=None, nombre=None, juego=None, fecha=None, empleado_id=None, participantes=None):
        self._id = torneo_id
        self._nombre = nombre
        self._juego = juego
        self._fecha = fecha
        self._empleado_id = empleado_id
        self._participantes = participantes or []

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def juego(self):
        return self._juego

    @property
    def fecha(self):
        return self._fecha

    @property
    def empleado_id(self):
        return self._empleado_id

    @property
    def participantes(self):
        return self._participantes

    def agregar_participante(self, email):
        """Añade un email a la lista de participantes"""
        if email and email not in self._participantes:
            self._participantes.append(email)