import jaydebeapi

class Conexion:
    _instancia = None  

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._init_conexion(*args, **kwargs)
        return cls._instancia

    def _init_conexion(self, host='localhost', database='pixelplanet', user='root', password='changeme'):
        self._host = host
        self._database = database
        self._user = user
        self._password = password
        self.conexion = self.createConnection()

    def createConnection(self):
        try:
            jdbc_driver = "com.mysql.cj.jdbc.Driver"
            jar_file = "lib/mysql-connector-j-9.3.0.jar"
            self.conexion = jaydebeapi.connect(
                jdbc_driver,
                f"jdbc:mysql://{self._host}/{self._database}",
                [self._user, self._password],
                jar_file
            )
            return self.conexion
        except Exception as e:
            print("Error creando conexión:", e)
            return None

    def getCursor(self):
        if self.conexion is None:
            self.createConnection()
        return self.conexion.cursor()

    def closeConnection(self):
        try:
            if self.conexion:
                self.conexion.close()
                self.conexion = None
                Conexion._instancia = None  
        except Exception as e:
            print("Error cerrando conexión:", e)


if __name__ == "__main__":
    c = Conexion()
    cursor = c.getCursor()
    if cursor:
        nombre_tabla = "resenas"
            
        
        cursor.execute(f"SHOW COLUMNS FROM {nombre_tabla};")
        print("\nColumnas de la tabla:")
        for columna in cursor.fetchall():
            print(columna[0])
        
        cursor.execute(f"SELECT * FROM {nombre_tabla};")
        print("\nDatos de la tabla:")
        
        
        column_names = [desc[0] for desc in cursor.description]
        print("\t".join(column_names))
        for registro in cursor.fetchall():
            print("\t".join(str(valor) for valor in registro))
        c.closeConnection()
    
