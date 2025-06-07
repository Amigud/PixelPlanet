class EmpleadoVO:
    def __init__(self, id_empleado, email, rol):
        self._id = id_empleado
        self._email = email
        self._rol = rol

    @property
    def id(self):
        return self._id

    @property
    def email(self):
        return self._email

    @property
    def rol(self):
        return self._rol
