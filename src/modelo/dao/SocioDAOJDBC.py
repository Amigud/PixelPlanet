from src.modelo.conexion.Conexion import Conexion
from src.modelo.dao.SocioDAO import SocioDAO
from src.modelo.vo.SocioVO import SocioVO

class SocioDAOJDBC(SocioDAO, Conexion):
    SQL_BUSCAR_EMAIL = "SELECT ClienteID, NombreSocio, Email FROM socios WHERE Email = ?"

    def buscar_por_email(self, email: str) -> SocioVO | None:
        cursor = self.getCursor()
        try:
            cursor.execute(self.SQL_BUSCAR_EMAIL, (email,))
            row = cursor.fetchone()
            if row:
                id_socio, nombre, email = row
                return SocioVO(id_socio, nombre, email)
            return None
        except Exception as e:
            print(f"Error al buscar socio por email: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            self.closeConnection()
