# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class MenuEditar(object):
    def setupUi(self, MenuEditar):
        if not MenuEditar.objectName():
            MenuEditar.setObjectName(u"MenuEditar")
        MenuEditar.resize(415, 420)
        self.BotonActivar = QPushButton(MenuEditar)
        self.BotonActivar.setObjectName(u"BotonActivar")
        self.BotonActivar.setGeometry(QRect(90, 50, 241, 61))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(15)
        self.BotonActivar.setFont(font)
        self.BotonActivar.setCursor(QCursor(Qt.OpenHandCursor))
        icon = QIcon()
        icon.addFile(u"./assets/icon_user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BotonActivar.setIcon(icon)
        self.BotonActivar.setIconSize(QSize(20, 20))
        self.BotonActivar_2 = QPushButton(MenuEditar)
        self.BotonActivar_2.setObjectName(u"BotonActivar_2")
        self.BotonActivar_2.setEnabled(True)
        self.BotonActivar_2.setGeometry(QRect(90, 160, 241, 61))
        self.BotonActivar_2.setFont(font)
        self.BotonActivar_2.setCursor(QCursor(Qt.OpenHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"./assets/icon_producto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BotonActivar_2.setIcon(icon1)
        self.BotonActivar_2.setIconSize(QSize(30, 30))
        self.BotonActivar_3 = QPushButton(MenuEditar)
        self.BotonActivar_3.setObjectName(u"BotonActivar_3")
        self.BotonActivar_3.setEnabled(True)
        self.BotonActivar_3.setGeometry(QRect(90, 270, 241, 61))
        self.BotonActivar_3.setFont(font)
        self.BotonActivar_3.setCursor(QCursor(Qt.OpenHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"./assets/icon_providder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BotonActivar_3.setIcon(icon2)
        self.BotonActivar_3.setIconSize(QSize(30, 30))

        self.retranslateUi(MenuEditar)

        QMetaObject.connectSlotsByName(MenuEditar)
    # setupUi

    def retranslateUi(self, MenuEditar):
        MenuEditar.setWindowTitle(QCoreApplication.translate("MenuEditar", u"Edición", None))
        self.BotonActivar.setText(QCoreApplication.translate("MenuEditar", u"Usuarios", None))
        self.BotonActivar_2.setText(QCoreApplication.translate("MenuEditar", u"Productos", None))
        self.BotonActivar_3.setText(QCoreApplication.translate("MenuEditar", u"Proveedores", None))
    # retranslateUi

