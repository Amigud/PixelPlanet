from src.modelo.conexion.Conexion import Conexion
from src.modelo.dao.SocioDAO import SocioDAO
from src.modelo.vo.SocioVO import SocioVO

class SocioDAOJDBC(SocioDAO):
    SQL_BUSCAR_EMAIL = "SELECT ClienteID, NombreSocio, Apellidos, Email, Telefono, FechaNacim, Puntos FROM socios WHERE Email = ?"
    SQL_INSERTAR_SOCIO = """
    INSERT INTO socios (NombreSocio, Apellidos, Email, Telefono, FechaNacim)
    VALUES (?, ?, ?, ?, ?)
    """

    def buscar_por_email(self, email: str) -> SocioVO | None:
        conexion = Conexion()
        cursor = conexion.getCursor()
        try:
            cursor.execute(self.SQL_BUSCAR_EMAIL, (email,))
            row = cursor.fetchone()
            if row:
                id_socio, nombre, apellido, email, telefono, fecha_nacimiento, puntos = row
                return SocioVO(id_socio, nombre, apellido, email, telefono, fecha_nacimiento, puntos)

            return None
        except Exception as e:
            print(f"Error al buscar socio por email: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            conexion.closeConnection()
    
    def insertar_socio(self, socio: SocioVO) -> bool:
        conexion = Conexion()
        cursor = conexion.getCursor()
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
            conexion.closeConnection()
    
    def obtener_puntos_por_email(self, email):
        conexion = Conexion()
        cursor = conexion.getCursor()
        try:
            cursor.execute("SELECT Puntos FROM socios WHERE Email = ?", (email,))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else None
        except Exception as e:
            print(f"Error al obtener puntos del socio: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            conexion.closeConnection()

    def sumar_puntos(self, email, puntos):
        conexion = Conexion()
        cursor = conexion.getCursor()
        try:
            cursor.execute("UPDATE socios SET Puntos = Puntos + ? WHERE Email = ?", (puntos, email))
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al sumar puntos: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            conexion.closeConnection()

