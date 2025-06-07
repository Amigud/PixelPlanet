from src.modelo.conexion.Conexion import Conexion
from src.modelo.dao.EmpleadoDAO import EmpleadoDAO
from src.modelo.vo.EmpleadoVO import EmpleadoVO

class EmpleadoDAOJDBC(EmpleadoDAO, Conexion):
    SQL_LOGIN = "SELECT EmpleadoID, Email, Rol FROM empleados WHERE Email = ? AND Contrasenia = ?"

    def login(self, email: str, contrasena: str) -> EmpleadoVO | None:
        cursor = self.getCursor()
        try:
            cursor.execute(self.SQL_LOGIN, (email, contrasena))
            row = cursor.fetchone()
            if row:
                print(f"El email es : {email} y contraseña: {contrasena}")
                return EmpleadoVO(row[0], row[1], row[2])
            return None
        except Exception as e:
            print("Error al hacer login:", e)
            return None
        finally:
            if cursor:
                cursor.close()
            self.closeConnection()
