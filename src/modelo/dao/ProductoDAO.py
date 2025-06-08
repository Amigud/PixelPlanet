from src.modelo.conexion.Conexion import Conexion

class ProductoDAO:
    def __init__(self):
        self.db = Conexion()

    def insertar_producto(self, nombre, descripcion, precio):
        cursor = self.db.getCursor()
        cursor.execute("INSERT INTO productos (Nombre, Descripcion, Precio) VALUES (?, ?, ?)", 
                       (nombre, descripcion, precio))
        self.db.conexion.commit()
        cursor.execute("SELECT LAST_INSERT_ID()")
        return cursor.fetchone()[0]

    def insertar_generos(self, producto_id, generos):
        cursor = self.db.getCursor()
        for genero in generos:
            cursor.execute("INSERT INTO genero_prod (ProductoID, Genero) VALUES (?, ?)", 
                           (producto_id, genero.strip()))
        self.db.conexion.commit()

    def obtener_todos(self):
        cursor = self.db.getCursor()
        cursor.execute("SELECT ProductoID, Nombre, Precio FROM productos")
        return cursor.fetchall()

    def buscar_por_id(self, pid):
        cursor = self.db.getCursor()
        cursor.execute("SELECT * FROM productos WHERE ProductoID = ?", (pid,))
        return cursor.fetchone()

    def actualizar(self, pid, nombre, descripcion, precio):
        cursor = self.db.getCursor()
        cursor.execute("UPDATE productos SET Nombre = ?, Descripcion = ?, Precio = ? WHERE ProductoID = ?",
                       (nombre, descripcion, precio, pid))
        self.db.conexion.commit()
        return cursor.rowcount > 0

    def obtener_cantidad_por_nombre(self, nombre):
        cursor = self.db.getCursor()
        cursor.execute("SELECT Cantidad FROM productos WHERE Nombre = ?", (nombre,))
        resultado = cursor.fetchone()
        return resultado[0] if resultado else None

    def obtener_id_y_cantidad_por_nombre(self, nombre):
        cursor = self.db.getCursor()
        cursor.execute("SELECT ProductoID, Cantidad FROM productos WHERE Nombre = ?", (nombre,))
        return cursor.fetchone()  # Devuelve (ID, Cantidad) o None

