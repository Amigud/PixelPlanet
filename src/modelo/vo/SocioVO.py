class SocioVO:
    def __init__(self, id, nombre, apellido, email, telefono, fecha_nacimiento, puntos=0):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono
        self._fecha_nacimiento = fecha_nacimiento
        self._puntos = puntos

    @property
    def id(self): return self._id

    @property
    def nombre(self): return self._nombre

    @property
    def apellido(self): return self._apellido

    @property
    def email(self): return self._email

    @property
    def telefono(self): return self._telefono

    @property
    def fecha_nacimiento(self): return self._fecha_nacimiento

    @property
    def puntos(self): return self._puntos
