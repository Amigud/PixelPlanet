from src.modelo.conexion.Conexion import Conexion
from src.modelo.dao.SocioDAO import SocioDAO
from src.modelo.vo.SocioVO import SocioVO

class SocioDAOJDBC(SocioDAO, Conexion):
    SQL_BUSCAR_EMAIL = "SELECT ClienteID, NombreSocio, Apellidos, Email, Telefono, FechaNacim FROM socios WHERE Email = ?"
    SQL_INSERTAR_SOCIO = """
    INSERT INTO socios (NombreSocio, Apellidos, Email, Telefono, FechaNacim)
    VALUES (?, ?, ?, ?, ?)
    """

    def buscar_por_email(self, email: str) -> SocioVO | None:
        cursor = self.getCursor()
        try:
            cursor.execute(self.SQL_BUSCAR_EMAIL, (email,))
            row = cursor.fetchone()
            if row:
                id_socio, nombre, apellido, email, telefono, fecha_nacimiento = row
                return SocioVO(id_socio, nombre, apellido, email, telefono, fecha_nacimiento)

            return None
        except Exception as e:
            print(f"Error al buscar socio por email: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            self.closeConnection()
    
    def insertar_socio(self, socio: SocioVO) -> bool:
        cursor = self.getCursor()
        try:
            cursor.execute(self.SQL_INSERTAR_SOCIO, (
                socio.nombre,
                socio.apellido,
                socio.email,
                socio.telefono,
                socio.fecha_nacimiento.strftime("%Y-%m-%d")
            ))
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al insertar socio: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            self.closeConnection()
