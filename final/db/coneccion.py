import sqlite3
from sqlite3 import Error

def crearConeccion():
      try:
            conn = sqlite3.connect('db\PuntoVenta.db')
            return conn
      except Error as e :
            print("ERROR EN CONEXION "+str(e))