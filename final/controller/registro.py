from PySide2.QtWidgets import QWidget,QMessageBox
from PySide2.QtCore import Qt
from controller.afnd import proceso
from views.registro import NuevoUsuario
from db.PuntoVenta import InsertUsuario
import re


class Registrar(QWidget,NuevoUsuario):
      def __init__(self,parent = None) -> None:
            super().__init__(parent)
            self.setupUi(self)
            self.setWindowFlag(Qt.Window)
            self.RegistrarBoton.clicked.connect(self.addUsuario)
       
      def checkInput(self):
            nombre = self.NombreLine.text()
            usuario = self.UsuarioLine.text()
            correo = self.CorreoLine.text()
            password = self.PasswordLine.text()
            password2 = self.PasswordLine2.text()
            if nombre == "" or usuario == "" or correo == "" or password == "" or password2 == "":
                  return False
            else:
                  return True
            
      def addUsuario(self):
            REnombre = re.compile("^([a-zA-Z]{2,}\s[a-zA-z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{10,25})?)")
            REcorreo = re.compile("^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")
            REpassword = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
            REusuario = re.compile("^[\s\S]{6,12}$")
            nombre = self.NombreLine.text()
            usuario = self.UsuarioLine.text()
            correo = self.CorreoLine.text()
            password = self.PasswordLine.text()
            password2 = self.PasswordLine2.text()
            matchNombre = REnombre.match(nombre)
            matchUsuario = REusuario.match(usuario)
            matchEmail = REcorreo.match(correo)
            matchPassword = REpassword.match(password)
            if password != password2:
                  QMessageBox.information(self, "ERROR", "CONTRASEÑA NO COINCIDEN")
            else:
                  if not matchNombre:
                        QMessageBox.information(self,"ERROR EN NOMBRE","Debe de ser de 10 a 25 caracteres")
                  if not matchUsuario:
                        QMessageBox.information(self,"ERROR EN USUARIO","Debe ser de 6 a 12 caracteres")
                  if not matchEmail:
                        QMessageBox.information(self,"ERROR EN EMAIL","Ingreso correo erroneo ")
                  if not matchPassword:
                        QMessageBox.information(self,"ERROR EN CONTRASEÑA","Mínimo ocho caracteres, al menos una letra mayúscula, una letra minúscula, un número y un carácter especial")
                  else:
                        evalua = correo.split(".")
                        bandera = proceso(evalua[0])
                        if bandera:
                              if self.checkInput():
                                    data = (nombre,usuario,correo,password)
                                    if InsertUsuario(data):
                                          self.CleanInput()
                                    else:
                                          QMessageBox.information(self,"UPSS!!","Ocurrio algun error")
                        else:
                              QMessageBox.information(self,"ERROR EN CORREO","Use dependencias de GMAIL, HOTMAIL,OUTLOOK,YAHOO")                  
      
      def CleanInput(self):
            self.NombreLine.clear()
            self.UsuarioLine.clear()
            self.CorreoLine.clear()
            self.PasswordLine.clear()
            self.PasswordLine2.clear()
      
    
          