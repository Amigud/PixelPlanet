from src.modelo.conexion.Conexion import Conexion
from modelo.dao.ProductoDAO import ProductoDAO
from src.modelo.vo.ProductoVO_a import ProductoVO

class ProductoDAOJDBC(ProductoDAO, Conexion):
    SQL_SELECT = "SELECT ProductoID, Nombre, Descripcion, Precio, Cantidad FROM productos"
    SQL_INSERT = "INSERT INTO productos(Nombre, Descripcion, Precio, Cantidad) VALUES (?, ?, ?, ?)"

    def select(self) -> list[ProductoVO]:
        cursor = self.getCursor()
        productos = []
        try:
            cursor.execute(self.SQL_SELECT)
            rows = cursor.fetchall()
            for row in rows:
                id_prod, nombre, descripcion, precio, cantidad = row
                producto = ProductoVO(id_prod, nombre, descripcion, precio, cantidad)
                productos.append(producto)
        except Exception as e:
            print("Error al seleccionar productos:", e)
        finally:
            if cursor:
                cursor.close()
            self.closeConnection()
        return productos

    def insert(self, producto: ProductoVO) -> int:
        cursor = self.getCursor()
        rows = 0
        try:
            cursor.execute(
                self.SQL_INSERT,
                (producto.nombre, producto.descripcion, producto.precio, producto.cantidad)
            )
            rows = cursor.rowcount
        except Exception as e:
            print("Error al insertar producto:", e)
        finally:
            if cursor:
                cursor.close()
            self.closeConnection()
        return rows

    def devolver_producto(self, nombre: str, cantidad: int) -> bool:
        cursor = self.getCursor()
        try:
            # Buscar cantidad actual
            cursor.execute("SELECT Cantidad FROM productos WHERE Nombre = ?", (nombre,))
            row = cursor.fetchone()
            if not row:
                print("Producto no encontrado")
                return False

            cantidad_actual = row[0]
            nueva_cantidad = max(0, cantidad_actual + cantidad) 

            # Actualizar cantidad
            cursor.execute(
                "UPDATE productos SET Cantidad = ? WHERE Nombre = ?",
                (nueva_cantidad, nombre)
            )
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al devolver producto: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            self.closeConnection()
