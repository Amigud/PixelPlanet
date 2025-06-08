class SocioVO:
    def __init__(self, id, nombre, email):
        self._id = id
        self._nombre = nombre
        self._email = email

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def email(self):
        return self._email
