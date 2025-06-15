from src.modelo.conexion.Conexion import Conexion
from src.modelo.dao.ProductoDAO import ProductoDAO
from src.modelo.vo.ProductoVO import ProductoVO

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
            cursor.execute("SELECT Cantidad FROM productos WHERE Nombre = ?", (nombre,))
            row = cursor.fetchone()
            if not row:
                print("Producto no encontrado")
                return False

            cantidad_actual = row[0]
            nueva_cantidad = max(0, cantidad_actual + cantidad)

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

    def obtener_id_y_cantidad_por_nombre(self, nombre: str):
        cursor = self.getCursor()
        try:
            cursor.execute("SELECT ProductoID, Cantidad FROM productos WHERE Nombre = ?", (nombre,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al obtener ID y cantidad: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            self.closeConnection()

    def obtener_cantidad_por_nombre(self, nombre: str):
        cursor = self.getCursor()
        try:
            cursor.execute("SELECT Cantidad FROM productos WHERE Nombre = ?", (nombre,))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else None
        except Exception as e:
            print(f"Error al obtener cantidad: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            self.closeConnection()

    def buscar_por_id(self, producto_id: int):
        cursor = self.getCursor()
        try:
            cursor.execute("SELECT * FROM productos WHERE ProductoID = ?", (producto_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al buscar producto por ID: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            self.closeConnection()

    def restar_cantidad(self, producto_id: int, cantidad: int) -> bool:
        cursor = self.getCursor()
        try:
            cursor.execute("SELECT Cantidad FROM productos WHERE ProductoID = ?", (producto_id,))
            resultado = cursor.fetchone()

            if not resultado:
                return False

            cantidad_actual = resultado[0]
            if cantidad > cantidad_actual:
                return False

            cursor.execute(
                "UPDATE productos SET Cantidad = Cantidad - ? WHERE ProductoID = ?",
                (cantidad, producto_id)
            )
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al restar cantidad: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            self.closeConnection()
    
    def sumar_cantidad(self, producto_id, cantidad):
        cursor = self.getCursor()
        cursor.execute(
            "UPDATE productos SET Cantidad = Cantidad + ? WHERE ProductoID = ?",
            (cantidad, producto_id)
        )
        return cursor.rowcount > 0
    
    def obtener_productos_stock_bajo(self, umbral = 10) -> list:
        cursor = self.getCursor()
        try:
            cursor.execute(
                "SELECT Nombre, Cantidad FROM productos WHERE Cantidad < ?",
                (umbral,)
            )
            return cursor.fetchall() 
        except Exception as e:
            print(f"Error al obtener productos con stock bajo: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            self.closeConnection()


