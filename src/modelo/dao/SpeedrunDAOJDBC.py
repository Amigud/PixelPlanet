from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.SpeedrunVO import SpeedrunVO
from src.modelo.dao.SpeedrunDAO import SpeedrunDAO

class SpeedrunDAOJDBC(SpeedrunDAO, Conexion):
    def registrar_speedrun(self, speedrun: SpeedrunVO) -> bool:
        cursor = None
        try:
    
            self.conexion = self.createConnection()
            self.conexion.jconn.setAutoCommit(False)  
            
            cursor = self.conexion.cursor()
            cursor.execute(
                "INSERT INTO speedruns (Juego, EmailSocio, Tiempo, CodEmpleado) VALUES (?, ?, ?, ?)",
                (speedrun.juego, speedrun.email_socio, speedrun.tiempo, speedrun.empleado_id)
            )
            
           
            self.conexion.commit()
            return True
            
        except Exception as e:
            
            if self.conexion:
                self.conexion.rollback()
            print(f"Error al registrar speedrun: {e}")
            return False
        finally:
           
            if self.conexion:
                try:
                    self.conexion.jconn.setAutoCommit(True)  
                except:
                    pass
                self.closeConnection()
            if cursor:
                cursor.close()