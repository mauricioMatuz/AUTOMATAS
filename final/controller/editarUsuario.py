from PySide2.QtWidgets import QWidget,QMessageBox
from PySide2.QtCore import Qt
from controller.afnd import proceso
from views.editar_usuarios import FormularioEditarUsuario
from db.PuntoVenta import BuscarUsuario,EditUsuario
import  re

class editarUsuarios(QWidget, FormularioEditarUsuario):
    def __init__(self, parent=None, _id=None):
        self._id = _id
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.LlenarInput()
        self.Boton_ConfirmarCambios.clicked.connect(self.confirmar)

    def LlenarInput(self):
        data = BuscarUsuario(self._id)
        self.textField_nombre.setText(data[0][1])
        self.textField_Usuario.setText(data[0][2])
        self.textField_Email.setText(data[0][3])
        self.textField_Password.setText(data[0][4])
        
    def checkInput(self):
        nombre = self.textField_nombre.text()
        usuario = self.textField_Usuario.text()
        correo = self.textField_Email.text()
        password = self.textField_Password.text()
        if nombre == "" or usuario == "" or correo == "" or password == "" :
            return False
        else:
            return True
    
    def confirmar(self):
        REnombre = re.compile("^([a-zA-Z]{2,}\s[a-zA-z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{10,25})?)")
        REcorreo = re.compile("^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")
        REpassword = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
        REusuario = re.compile("^[\s\S]{6,12}$")
        nombre = self.textField_nombre.text()
        usuario = self.textField_Usuario.text()
        correo = self.textField_Email.text()
        password = self.textField_Password.text()
        matchNombre = REnombre.match(nombre)
        matchUsuario = REusuario.match(usuario)
        matchEmail = REcorreo.match(correo)
        matchPassword = REpassword.match(password)
        data = (nombre,usuario,correo,password)
        print(data,"<<<DATAAS>>>xdd")
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
                    
                    if EditUsuario(self._id,data):
                        self.CleanInput()
                    else:
                        QMessageBox.information(self,"UPSS!!","Ocurrio algun error")
                else:
                    QMessageBox.information(self,"ERROR EN CORREO","Use dependencias de GMAIL, HOTMAIL,OUTLOOK,YAHOO")

    def CleanInput(self):
        self.textField_nombre.clear()
        self.textField_Usuario.clear()
        self.textField_Email.clear()
        self.textField_Password.clear()
        
      