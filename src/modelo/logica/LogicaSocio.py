from src.modelo.dao.SocioDAOJDBC import SocioDAOJDBC
from src.modelo.vo.SocioVO import SocioVO

class LogicaSocio:
    def __init__(self):
        self.dao = SocioDAOJDBC()

    def registrar_socio(self, socio: SocioVO) -> bool:
        existente = self.dao.buscar_por_email(socio.email)
        if existente:
            print(f"Ya existe un socio con el email {socio.email}")
            return False
        return self.dao.insertar_socio(socio)
    
    def consultar_socio(self, email: str):
        return self.dao.buscar_por_email(email)
    
    def agregar_puntos_por_compra(self, email: str, precio_unitario: float, cantidad: int):
        socio = self.dao.buscar_por_email(email)
        if not socio:
            return False, "El email no pertenece a ningún socio."

        total = precio_unitario * cantidad
        puntos = int(total) 

        if puntos <= 0:
            return False, "Compra demasiado baja para generar puntos."

        exito = self.dao.sumar_puntos(email, puntos)
        if exito:
            return True, f"Se han sumado {puntos} puntos al socio '{email}'."
        else:
            return False, "Error al actualizar los puntos del socio."

