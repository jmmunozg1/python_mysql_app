import mysql.connector

class Conexion:

    def __init__(self):
        self.conexion = mysql.connector.connect(
            host = "localhost",
            username = "root",
            password = "Ingmunoz0206*",
            database = "sistema_tickets"
        )
     
    def insertar_registro(self,identificacion, nombre, correo, telefono, salario):
        cur = self.conexion.cursor()
        sql='''INSERT INTO ingeniero (id_ingeniero, nombre_ing, correo_ing, telefono_ing, salario) 
        VALUES('{}', '{}','{}', '{}','{}')'''.format(identificacion, nombre, correo, telefono, salario)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()
    
    def actualizar(self,identificacion, nombre, correo, telefono, salario):
        cursor = self.conexion.cursor()
        sql="UPDATE ingeniero SET nombre_ing= '{}', correo_ing='{}', telefono_ing='{}', salario = '{}' WHERE id_ingeniero='{}'".format(nombre, correo, telefono, salario,identificacion)
        cursor.execute(sql)
        self.conexion.commit()    
        cursor.close()


    def mostrar_registro(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM ingeniero " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_registro(self, nombre_ingeniero):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM ingeniero WHERE nombre_ing = {}".format(nombre_ingeniero)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX 

    def eliminar_registro(self,nombre):
        cur = self.conexion.cursor()
        sql='''DELETE FROM ingeniero WHERE nombre_ing = {}'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()