import sqlite3
from sqlite3 import Error
from typing import Type
from .coneccion import crearConeccion

#!USUARIO
def InsertUsuario(data):
      conn = crearConeccion()
      sql = """INSERT INTO Usuarios (Nombre,Usuario,Correo,Password) VALUES (?,?,?,?)"""
      try:
          cur = conn.cursor()
          cur.execute(sql,data)
          conn.commit()
          print("NUEVO USUARIO REGISTRADO")
          return True
      except Error as e :
          print("error en insertar usuario >> "+str(e))
          return False
      finally:
            if conn:
                  cur.close()
                  conn.close()
                  

def EditUsuario(id,data):
      conn = crearConeccion()
      sql = f"""UPDATE Usuarios SET Nombre = ?, Usuario = ?, Correo = ?, Password = ? WHERE ID = {id}"""
      
      try:
            cur = conn.cursor()
            cur.execute(sql,data)
            conn.commit()
            print("USUARIO EDITADO")
            return True
      except Error as e:
            print("ERROR EN EDITAR USUARIO "+str(e))
      finally:
            if conn:
                  cur.close()
                  conn.close()

def DeleteUsuario(id):
      conn = crearConeccion()
      sql = f"""DELETE FROM Usuarios WHERE ID = {id}"""
      try:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            print("USUARIO ELIMINADO")
            return True
      except Error as e:
            print("ERROR EN BORRAR USUARIO "+str(e))
      finally:
            if conn:
                  cur.close()
                  conn.close()
                  
def SelectUser():
      conn = crearConeccion()
      sql = """SELECT *  FROM Usuarios"""
      try:
            cur = conn.cursor()
            cur.execute(sql)
            usuarios = cur.fetchall()
            print(usuarios,"<<<USER")
            return usuarios
      except Error as e:
            print("ERROR EN MOSTRAR TODOS LOS USUARIOS "+str(e))
      finally:
            if conn:
                  cur.close()
                  conn.close()
                  
def SelectUsuarioID(id):
      conn = crearConeccion()
      sql = f"""SELECT * FROM Usuarios WHERE ID = {id}"""
      try:
            cur = conn.cursor()
            cur.execute(sql)
            usuarios = cur.fetchone()
            return usuarios
      except Error as e:
            print("ERROR EN SELECCIONAR UN USUARIO "+str(e))
      finally:
            if conn:
                  cur.close()
                  conn.close() 
                  
def BuscarUsuario(id):
      conn = crearConeccion()
      sql = f"""SELECT * FROM Usuarios WHERE ID LIKE '%{id}%'"""
      try:
            cur = conn.cursor()
            cur.execute(sql)
            usuarios = cur.fetchall()
            return usuarios
      except Error as e:
            print("ERROR EN BUSCAR UN USUARIO "+str(e))
      finally:
            if conn:
                  cur.close()
                  conn.close() 
                  
#! FIN USUARIO        
         
#! LOGIN
def IniciarSesion(data):
      conn = crearConeccion()
      sql = """SELECT * FROM Usuarios WHERE Usuario = ? and Password = ?"""
      try:
            cur = conn.cursor()
            cur.execute(sql,data)
            usuario = cur.fetchall()
            if len(usuario) == 0:
                  return False
            else:
                  return True
      except Error as e:
          print("ERROR EN INICAR SESION >>"+str(e))
      finally:
            if conn:
                  cur.close()
                  conn.close()   
#!FIN LOGIN

#!INICIO PRODUCTO
def InsertProducto(data):
      conn = crearConeccion()
      sql = """INSERT INTO Productos (Nombre,Codigo,Precio) VALUES (?,?,?)"""
      try:
            cur = conn.cursor()
            cur.execute(sql,data)
            conn.commit()
            return True
      except Error as e:
            print("ERROR EN INSERTAR PRODUCTO "+str(e))
            return False
      finally:
            if conn:
                  cur.close()
                  conn.close()
                  

def EditProducto(id,data):
      conn = crearConeccion()
      sql = f"""UPDATE Productos SET Nombre = ?, Codigo = ?, Precio = ? WHERE ID ={id} """
      try:
          cur = conn.cursor()
          cur.execute(sql,data)
          conn.commit()
          return True
      except Error as e :
          print("ERROR EDITAR PRODUCTO "+str(e))


def EliminarProducto(id):
      conn = crearConeccion()
      sql = f"""DELETE FROM Productos WHERE ID = {id}"""
      try:
          cur = conn.cursor()
          cur.execute(sql)
          conn.commit()
          return True
      except Error as e:
            print("ERROR EN ELIMINAR PRODUCTO "+str(e))
      finally:
            if conn:
                  cur.close()
                  conn.close()

def SelectProducto():
      conn = crearConeccion()
      sql = """SELECT Nombre,Codigo,Precio FROM Productos"""
      try:
          cur = conn.cursor()
          cur.execute(sql)
          producto = cur.fetchall()
          print(producto)
          return producto
      except Error as e:
          print("ERROR EN SELECCIONAR PRODUCTO"+str(e))
      finally:
            if conn:
                  cur.close()
                  conn.close()
                  
def BuscarProduct(codigo):
      conn = crearConeccion()
      sql = f"""SELECT Nombre,Codigo,Precio FROM Productos WHERE Codigo = '{codigo}'"""
      try:
          cur = conn.cursor()
          cur.execute(sql)
          producto = cur.fetchone()

          return producto
      except Error as e :
          print("ERROR EN BUSCAR "+str(e))
      finally:
            if conn:
                  cur.close()
                  conn.close()

def BuscarPrecio(codigo):
      total = 0
      conn = crearConeccion()
      sql =  f"""SELECT Precio FROM Productos WHERE Codigo = '{codigo}'"""
      try:
          cur = conn.cursor()
          cur.execute(sql)
          precio = cur.fetchone()
          precio = int(precio[0])  
          total = total + precio
          return total
      except Error as e :
          print("ERROR EN PRECIO "+str(e))
      finally:
            if conn:
                  cur.close()
                  conn.close()
#!FIN DE PRODUCTO