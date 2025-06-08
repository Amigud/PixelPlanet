from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.TorneoVO import TorneoVO

class TorneoDAOJDBC(Conexion):
    def crear_torneo(self, torneo: TorneoVO) -> bool:
        cursor = None
        try:
            
            self.conexion = self.createConnection()
            self.conexion.jconn.setAutoCommit(False)  
            
            cursor = self.conexion.cursor()
            
            # 1. Insertar el torneo
            cursor.execute(
                "INSERT INTO torneos (NombreTorneo, Juego, Fecha, CodEmpleado) VALUES (?, ?, ?, ?)",
                (torneo.nombre, torneo.juego, torneo.fecha, torneo.empleado_id)
            )
            
            
            cursor.execute("SELECT LAST_INSERT_ID()")
            torneo_id = cursor.fetchone()[0]
            
            
            for email in torneo.participantes:
                
                cursor.execute("SELECT ClienteID FROM socios WHERE Email = ?", (email,))
                resultado = cursor.fetchone()
                if resultado:
                    cliente_id = resultado[0]
                    cursor.execute(
                        "INSERT INTO participantes (TorneoID, ClienteID) VALUES (?, ?)",
                        (torneo_id, cliente_id)
                    )
            
            
            self.conexion.commit()
            return True
            
        except Exception as e:
            
            if self.conexion:
                try:
                    self.conexion.rollback()
                except:
                    pass  
            print(f"Error al crear torneo: {e}")
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