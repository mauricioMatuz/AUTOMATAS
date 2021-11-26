# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class NuevoUsuario(object):
    def setupUi(self, NuevoUsuario):
        if not NuevoUsuario.objectName():
            NuevoUsuario.setObjectName(u"NuevoUsuario")
        NuevoUsuario.resize(405, 472)
        self.label = QLabel(NuevoUsuario)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 381, 20))
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(NuevoUsuario)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 61, 13))
        self.NombreLine = QLineEdit(NuevoUsuario)
        self.NombreLine.setObjectName(u"NombreLine")
        self.NombreLine.setGeometry(QRect(30, 80, 351, 20))
        self.label_3 = QLabel(NuevoUsuario)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 61, 13))
        self.UsuarioLine = QLineEdit(NuevoUsuario)
        self.UsuarioLine.setObjectName(u"UsuarioLine")
        self.UsuarioLine.setGeometry(QRect(30, 130, 271, 20))
        self.CorreoLine = QLineEdit(NuevoUsuario)
        self.CorreoLine.setObjectName(u"CorreoLine")
        self.CorreoLine.setGeometry(QRect(30, 180, 271, 20))
        self.label_4 = QLabel(NuevoUsuario)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 160, 61, 13))
        self.label_5 = QLabel(NuevoUsuario)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 220, 91, 16))
        self.PasswordLine = QLineEdit(NuevoUsuario)
        self.PasswordLine.setObjectName(u"PasswordLine")
        self.PasswordLine.setGeometry(QRect(30, 240, 271, 20))
        self.PasswordLine.setEchoMode(QLineEdit.Password)
        self.label_6 = QLabel(NuevoUsuario)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 290, 171, 16))
        self.PasswordLine2 = QLineEdit(NuevoUsuario)
        self.PasswordLine2.setObjectName(u"PasswordLine2")
        self.PasswordLine2.setGeometry(QRect(30, 310, 271, 20))
        self.PasswordLine2.setEchoMode(QLineEdit.Password)
        self.RegistrarBoton = QPushButton(NuevoUsuario)
        self.RegistrarBoton.setObjectName(u"RegistrarBoton")
        self.RegistrarBoton.setGeometry(QRect(64, 362, 231, 41))
        font = QFont()
        font.setPointSize(12)
        self.RegistrarBoton.setFont(font)
        self.RegistrarBoton.setStyleSheet(u"\n"
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
        icon.addFile(u"./assets/register.png", QSize(), QIcon.Normal, QIcon.Off)
        self.RegistrarBoton.setIcon(icon)
        self.RegistrarBoton.setIconSize(QSize(30, 30))

        self.retranslateUi(NuevoUsuario)

        QMetaObject.connectSlotsByName(NuevoUsuario)
    # setupUi

    def retranslateUi(self, NuevoUsuario):
        NuevoUsuario.setWindowTitle(QCoreApplication.translate("NuevoUsuario", u"NUEVO USUARIO", None))
        self.label.setText(QCoreApplication.translate("NuevoUsuario", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">NUEVO USUARIO</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("NuevoUsuario", u"<html><head/><body><p><span style=\" font-weight:600;\">NOMBRE:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("NuevoUsuario", u"<html><head/><body><p><span style=\" font-weight:600;\">USUARIO:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("NuevoUsuario", u"<html><head/><body><p><span style=\" font-weight:600;\">CORREO </span><span style=\" font-size:10pt; font-weight:600;\">:</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("NuevoUsuario", u"<html><head/><body><p><span style=\" font-weight:600;\">CONTRASE\u00d1A </span><span style=\" font-size:10pt; font-weight:600;\">:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("NuevoUsuario", u"<html><head/><body><p><span style=\" font-weight:600;\">CONFIRMAR CONTRASE\u00d1A </span><span style=\" font-size:10pt; font-weight:600;\">:</span></p></body></html>", None))
        self.RegistrarBoton.setText(QCoreApplication.translate("NuevoUsuario", u"REGISTRAR", None))
    # retranslateUi

