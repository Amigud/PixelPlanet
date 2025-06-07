from src.modelo.conexion.Conexion import Conexion
from src.modelo.dao.EmpleadoDAO import EmpleadoDAO
from src.modelo.vo.EmpleadoVO import EmpleadoVO

class EmpleadoDAOJDBC(EmpleadoDAO, Conexion):
    SQL_LOGIN = "SELECT EmpleadoID, Email, Rol FROM empleados WHERE Email = %s AND Contrasenia = %s"

    def login(self, email: str, contrasena: str) -> EmpleadoVO | None:
        cursor = self.getCursor()
        try:
            cursor.execute(self.SQL_LOGIN, (email, contrasena))
            row = cursor.fetchone()
            if row:
                id_empleado, email, rol = row
                return EmpleadoVO(id_empleado, email, rol)
            return None
        except Exception as e:
            print("Error al hacer login:", e)
            return None
        finally:
            if cursor:
                cursor.close()
            self.closeConnection()
