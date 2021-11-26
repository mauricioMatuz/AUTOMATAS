from PySide2.QtWidgets import QWidget,QMessageBox
from PySide2.QtCore import Qt
from views.producto import ProductoVentana
from db.PuntoVenta import InsertProducto
import re


class Productos(QWidget,ProductoVentana):
      def __init__(self, parent = None) -> None:
            super().__init__(parent)
            self.setupUi(self)
            self.setWindowFlag(Qt.Window)
            self.AgregarProducto.clicked.connect(self.AddProducto)
            
      def checkInput(self):
            nombre = self.NombreProducto.text()
            precio = self.PrecioProducto.text()
            codigo = self.CodigoProducto.text()
            if nombre == "" or precio == "" or codigo == "":
                  return False
            else:
                  return True
      
      def AddProducto(self):
            nombre = self.NombreProducto.text()
            precio = self.PrecioProducto.text()
            codigo = self.CodigoProducto.text()
            REnombre = re.compile("^[\s\S]{6,25}$")
            matchNombre = REnombre.match(nombre)
            if not matchNombre :
                  QMessageBox.information(self,"ERROR EN NOMBRE","Debe ser de 6 a 12 caracteres")
            else:
                  if self.checkInput():
                        data = (nombre,codigo,precio)
                        if InsertProducto(data):
                              QMessageBox.information(self,"PRODUCTO","Producto Agregado")
                              self.CleanInput()
                        else:
                              QMessageBox.information(self,"UPSS!!","Ocurrio algun error")

      def CleanInput(self):
            self.NombreProducto.clear()
            self.PrecioProducto.clear()
            self.CodigoProducto.clear()
      