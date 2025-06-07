from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.SpeedrunVO import SpeedrunVO

class SpeedrunDAOJDBC(Conexion):
    SQL_SPEEDRUN = "INSERT INTO speedruns (Juego, EmailSocio, Tiempo, CodEmpleado) VALUES (?, ?, ?, ?)"
    def registrar_speedrun(self, speedrun: SpeedrunVO) -> bool:
        cursor = self.getCursor()
        try:
            cursor.execute(self.SQL_SPEEDRUN
                ,
                (speedrun.juego, speedrun.email_socio, speedrun.tiempo, speedrun.empleado_id)
            )
            self.conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar speedrun: {e}")
            return False
        finally:
            cursor.close()