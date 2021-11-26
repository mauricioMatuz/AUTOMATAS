# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editar_proveedores.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class VentanaProveeores(object):
    def setupUi(self, VentanaProveeores):
        if not VentanaProveeores.objectName():
            VentanaProveeores.setObjectName(u"VentanaProveeores")
        VentanaProveeores.resize(398, 229)
        self.label = QLabel(VentanaProveeores)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 60, 171, 16))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(12)
        self.label.setFont(font)
        self.Field_NombreProveedor = QLineEdit(VentanaProveeores)
        self.Field_NombreProveedor.setObjectName(u"Field_NombreProveedor")
        self.Field_NombreProveedor.setGeometry(QRect(200, 60, 161, 20))
        self.Field_Producto = QLineEdit(VentanaProveeores)
        self.Field_Producto.setObjectName(u"Field_Producto")
        self.Field_Producto.setGeometry(QRect(110, 100, 161, 20))
        self.label_2 = QLabel(VentanaProveeores)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 100, 171, 16))
        self.label_2.setFont(font)
        self.Field_CodigoProveedor = QLineEdit(VentanaProveeores)
        self.Field_CodigoProveedor.setObjectName(u"Field_CodigoProveedor")
        self.Field_CodigoProveedor.setGeometry(QRect(130, 20, 121, 20))
        self.label_3 = QLabel(VentanaProveeores)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 20, 61, 16))
        self.label_3.setFont(font)
        self.Boton_Confirmar = QPushButton(VentanaProveeores)
        self.Boton_Confirmar.setObjectName(u"Boton_Confirmar")
        self.Boton_Confirmar.setGeometry(QRect(130, 150, 151, 51))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(15)
        self.Boton_Confirmar.setFont(font1)
        self.Boton_Buscar = QPushButton(VentanaProveeores)
        self.Boton_Buscar.setObjectName(u"Boton_Buscar")
        self.Boton_Buscar.setGeometry(QRect(260, 20, 75, 23))

        self.retranslateUi(VentanaProveeores)

        QMetaObject.connectSlotsByName(VentanaProveeores)
    # setupUi

    def retranslateUi(self, VentanaProveeores):
        VentanaProveeores.setWindowTitle(QCoreApplication.translate("VentanaProveeores", u"Edici\u00f3n de proveedores", None))
        self.label.setText(QCoreApplication.translate("VentanaProveeores", u"Nombre del proveedor:", None))
        self.label_2.setText(QCoreApplication.translate("VentanaProveeores", u"Producto:", None))
        self.label_3.setText(QCoreApplication.translate("VentanaProveeores", u"C\u00f3digo:", None))
        self.Boton_Confirmar.setText(QCoreApplication.translate("VentanaProveeores", u"CONFIRMAR", None))
        self.Boton_Buscar.setText(QCoreApplication.translate("VentanaProveeores", u"Buscar", None))
    # retranslateUi

