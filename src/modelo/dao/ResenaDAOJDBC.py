from src.modelo.conexion.Conexion import Conexion
from src.modelo.dao.ResenaDAO import ResenaDAO
from src.modelo.vo.ResenaVO import ResenaVO

class ResenaDAOJDBC(ResenaDAO):
    SQL_INSERT = """
    INSERT INTO resenas (Estrellas, Comentario, Fecha, CodProducto, CodEmpleado)
    VALUES (?, ?, CURDATE(), ?, ?)
    """

    def insertar_resena(self, resena: ResenaVO) -> bool:
        conexion = Conexion()
        cursor = conexion.getCursor()
        try:
            cursor.execute(self.SQL_INSERT, (
                resena.estrellas,
                resena.comentario,
                resena.cod_producto,
                resena.cod_empleado
            ))
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al insertar reseña: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            conexion.closeConnection()
    
    def obtener_valoraciones_por_producto(self, producto_id):
        conexion = Conexion()
        cursor = conexion.getCursor()
        try:
            cursor.execute("SELECT Estrellas FROM resenas WHERE CodProducto = ?", (producto_id,))
            rows = cursor.fetchall()
            return [row[0] for row in rows]
        except Exception as e:
            print(f"Error al obtener valoraciones: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            conexion.closeConnection()
