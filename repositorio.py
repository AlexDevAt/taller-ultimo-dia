from mysql.connector import MySQLConnection
from database import DataBase

class RepositorioMySql:

    def conectarDb(self):
        return DataBase.obtenerConexion()

    def crearUsuario(self,usuario):
        conx:MySQLConnection = self.conectarDb()
        cursor = conx.cursor(dictionary=True)
        query = """
                INSERT INTO Usuarios(nombres,correo,edad,contraHash)
                VALUES(%s,%s,%s,%s)
                """
        values = (usuario.nombre,usuario.email,usuario.edad,usuario.contra)
        cursor.execute(query,values)
        id= cursor.lastrowid
        conx.commit()
        cursor.close()
        conx.close()
        return usuario,id

    def obtenerUsuarios(self):
        conx:MySQLConnection = self.conectarDb()
        cursor = conx.cursor(dictionary=True)

        query = '''
                    SELECT * FROM Usuarios;
                '''
        cursor.execute(query)
        res = cursor.fetchall()
        cursor.close()
        conx.close()
        return res

    def obtenerUsuarioId(self,id:int):
        conx:MySQLConnection = self.conectarDb()
        cursor = conx.cursor(dictionary=True)
        
        query = '''
                SELECT * FROM Usuarios WHERE id=%s;
                '''
        cursor.execute(query,(id,))
        res = cursor.fetchone()
        cursor.close()
        conx.close()
        return res

    def actualizarUsuario(self,usuario,id):
        conx:MySQLConnection = self.conectarDb()
        cursor = conx.cursor(dictionary=True)
        query = '''
                UPDATE Usuarios 
                SET nombres=%s,correo=%s,contraHash=%s
                WHERE id = %s;
                '''
        values=(usuario.nombre,usuario.email,usuario.contra,id)
        cursor.execute(query,values)
        filasAfectadas = cursor.rowcount
        cursor.close()
        conx.commit()
        conx.close()
        if (filasAfectadas == 0 ):
            return False,None
        return True,usuario

    def eliminarUsuario(self,id):
        conx:MySQLConnection = self.conectarDb()
        cursor = conx.cursor(dictionary=True)
        query = '''
                DELETE FROM Usuarios WHERE id = %s
                '''
        cursor.execute(query,(id,))
        filasAfectadas = cursor.rowcount
        cursor.close()
        conx.commit()
        conx.close()
        if (filasAfectadas == 0 ):
            return False
        return True


