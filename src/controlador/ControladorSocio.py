from src.modelo.logica.LogicaSocio import LogicaSocio
from src.modelo.vo.SocioVO import SocioVO

class ControladorSocio:
    def __init__(self):
        self.logica = LogicaSocio()

    def registrar_socio(self, nombre, apellido, email, telefono, fecha_nacimiento):
        if not all([nombre, apellido, email, telefono]):
            return False, "Todos los campos son obligatorios."

        if '@' not in email or '.' not in email.split('@')[-1]:
            return False, "Email no válido."

        if not telefono.isdigit() or len(telefono) < 7:
            return False, "Teléfono inválido."

        socio = SocioVO(
            id=None,
            nombre=nombre.strip(),
            apellido=apellido.strip(),
            email=email.strip(),
            telefono=telefono.strip(),
            fecha_nacimiento=fecha_nacimiento
        )

        if self.logica.registrar_socio(socio):
            return True, "Socio registrado correctamente."
        else:
            return False, "Error al registrar socio."
