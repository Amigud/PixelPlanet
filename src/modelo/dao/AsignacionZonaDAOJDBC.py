from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.AsignacionZonaVO import AsignacionZonaVO
from src.modelo.dao.AsignacionZonaDAO import AsignacionZonaDAO

class AsignacionZonaDAOJDBC(AsignacionZonaDAO):
    def asignar_zona(self, asignacion: AsignacionZonaVO) -> bool:
        conexion = Conexion()
        cursor = None
        try:
            cursor = conexion.getCursor()
            cursor.execute(
                """INSERT INTO asignzona (ZonaID, ClienteID, Horario, TraeJuego)
                VALUES (?, ?, ?, ?)""",
                (asignacion.zona_id, asignacion.cliente_id, asignacion.horario, asignacion.trae_juego)
            )
            return True
        except Exception as e:
            print(f"Error al asignar zona: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            conexion.closeConnection()

    def eliminar_asignacion(self, zona_id: int, email_socio: str) -> bool:
        conexion = Conexion()
        cursor = None
        try:
            cursor = conexion.getCursor()
            
            cursor.execute("SELECT ClienteID FROM socios WHERE Email = ?", (email_socio,))
            resultado = cursor.fetchone()
            if resultado:
                cliente_id = resultado[0]
                cursor.execute(
                    "DELETE FROM asignzona WHERE ZonaID = ? AND ClienteID = ?",
                    (zona_id, cliente_id)
                )
                return cursor.rowcount > 0
            return False
        except Exception as e:
            print(f"Error al eliminar asignación: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            conexion.closeConnection()

    def verificar_disponibilidad(self, zona_id: int, horario: str) -> bool:
        conexion = Conexion()
        cursor = None
        try:
            cursor = conexion.getCursor()
            cursor.execute(
                "SELECT COUNT(*) FROM asignzona WHERE ZonaID = ? AND Horario = ?",
                (zona_id, horario)
            )
            return cursor.fetchone()[0] == 0
        except Exception as e:
            print(f"Error al verificar disponibilidad: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            conexion.closeConnection()

    def obtener_horarios_disponibles(self, zona_id: int) -> list:
        conexion = Conexion()
        cursor = None
        try:
            cursor = conexion.getCursor()
            cursor.execute(
                "SELECT Horario FROM asignzona WHERE ZonaID = ? ORDER BY Horario",
                (zona_id,)
            )
            ocupados = [row[0] for row in cursor.fetchall()]
            todos_horarios = [f"{h}:00" for h in range(16, 22)] 
            return [h for h in todos_horarios if h not in ocupados]
        except Exception as e:
            print(f"Error al obtener horarios disponibles: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            conexion.closeConnection()