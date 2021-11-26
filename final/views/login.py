# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class LoginVentana(object):
    def setupUi(self, LoginVentana):
        if not LoginVentana.objectName():
            LoginVentana.setObjectName(u"LoginVentana")
        LoginVentana.resize(422, 468)
        self.label = QLabel(LoginVentana)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 60, 251, 81))
        self.label_3 = QLabel(LoginVentana)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 10, 411, 41))
        self.label_3.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(LoginVentana)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 180, 271, 81))
        self.UsuarioLine = QLineEdit(LoginVentana)
        self.UsuarioLine.setObjectName(u"UsuarioLine")
        self.UsuarioLine.setGeometry(QRect(80, 120, 261, 21))
        self.PasswordLine = QLineEdit(LoginVentana)
        self.PasswordLine.setObjectName(u"PasswordLine")
        self.PasswordLine.setGeometry(QRect(80, 250, 271, 21))
        self.PasswordLine.setEchoMode(QLineEdit.Password)
        self.Login = QPushButton(LoginVentana)
        self.Login.setObjectName(u"Login")
        self.Login.setGeometry(QRect(130, 330, 181, 51))
        self.Login.setCursor(QCursor(Qt.PointingHandCursor))
        self.Login.setStyleSheet(u"\n"
"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"./assets/login.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Login.setIcon(icon)
        self.Login.setIconSize(QSize(25, 25))

        self.retranslateUi(LoginVentana)

        QMetaObject.connectSlotsByName(LoginVentana)
    # setupUi

    def retranslateUi(self, LoginVentana):
        LoginVentana.setWindowTitle(QCoreApplication.translate("LoginVentana", u"Login", None))
        self.label.setText(QCoreApplication.translate("LoginVentana", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">INGRESE SU USUARIO</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("LoginVentana", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">LOGIN</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("LoginVentana", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">INGRESE SU CONTRASE\u00d1A</span></p></body></html>", None))
        self.PasswordLine.setText("")
        self.Login.setText(QCoreApplication.translate("LoginVentana", u"INICIAR SESION", None))
    # retranslateUi

