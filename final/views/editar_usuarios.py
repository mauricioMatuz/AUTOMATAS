# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editar_usuarios.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class FormularioEditarUsuario(object):
    def setupUi(self, FormularioEditarUsuario):
        if not FormularioEditarUsuario.objectName():
            FormularioEditarUsuario.setObjectName(u"FormularioEditarUsuario")
        FormularioEditarUsuario.resize(400, 300)
        self.label = QLabel(FormularioEditarUsuario)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 90, 71, 16))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(12)
        self.label.setFont(font)
        self.textField_nombre = QLineEdit(FormularioEditarUsuario)
        self.textField_nombre.setObjectName(u"textField_nombre")
        self.textField_nombre.setGeometry(QRect(130, 90, 241, 20))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        self.textField_nombre.setFont(font1)
        self.label_2 = QLabel(FormularioEditarUsuario)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 50, 71, 16))
        self.label_2.setFont(font)
        self.textField_Usuario = QLineEdit(FormularioEditarUsuario)
        self.textField_Usuario.setObjectName(u"textField_Usuario")
        self.textField_Usuario.setGeometry(QRect(130, 50, 151, 20))
        self.textField_Usuario.setFont(font1)
        self.label_3 = QLabel(FormularioEditarUsuario)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 130, 71, 16))
        self.label_3.setFont(font)
        self.textField_Email = QLineEdit(FormularioEditarUsuario)
        self.textField_Email.setObjectName(u"textField_Email")
        self.textField_Email.setGeometry(QRect(130, 130, 241, 20))
        self.textField_Email.setFont(font1)
        self.label_4 = QLabel(FormularioEditarUsuario)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 170, 101, 16))
        self.label_4.setFont(font)
        self.textField_Password = QLineEdit(FormularioEditarUsuario)
        self.textField_Password.setObjectName(u"textField_Password")
        self.textField_Password.setGeometry(QRect(160, 170, 211, 20))
        self.textField_Password.setFont(font1)
        self.Boton_ConfirmarCambios = QPushButton(FormularioEditarUsuario)
        self.Boton_ConfirmarCambios.setObjectName(u"Boton_ConfirmarCambios")
        self.Boton_ConfirmarCambios.setGeometry(QRect(130, 230, 151, 51))
        self.Boton_ConfirmarCambios.setFont(font)
        self.Boton_BuscarUsuario = QPushButton(FormularioEditarUsuario)
        self.Boton_BuscarUsuario.setObjectName(u"Boton_BuscarUsuario")
        self.Boton_BuscarUsuario.setGeometry(QRect(280, 50, 75, 23))

        self.retranslateUi(FormularioEditarUsuario)

        QMetaObject.connectSlotsByName(FormularioEditarUsuario)
    # setupUi

    def retranslateUi(self, FormularioEditarUsuario):
        FormularioEditarUsuario.setWindowTitle(QCoreApplication.translate("FormularioEditarUsuario", u"EDITAR USUARIO", None))
        self.label.setText(QCoreApplication.translate("FormularioEditarUsuario", u"Nombre:", None))
        self.label_2.setText(QCoreApplication.translate("FormularioEditarUsuario", u"Usuario:", None))
        self.label_3.setText(QCoreApplication.translate("FormularioEditarUsuario", u"Email:", None))
        self.label_4.setText(QCoreApplication.translate("FormularioEditarUsuario", u"Contrase\u00f1a:", None))
        self.Boton_ConfirmarCambios.setText(QCoreApplication.translate("FormularioEditarUsuario", u"Confirmar", None))
        self.Boton_BuscarUsuario.setText(QCoreApplication.translate("FormularioEditarUsuario", u"Buscar", None))
    # retranslateUi

