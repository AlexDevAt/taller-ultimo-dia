import mysql.connector

class DataBase:
    @classmethod
    def obtenerConexion(self): 
        try:
            return mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="root",
            database="taller"
            )
        except Exception as ex:
            print(str(ex))