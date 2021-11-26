# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editar_productos.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class VentanaEditarProductos(object):
    def setupUi(self, VentanaEditarProductos):
        if not VentanaEditarProductos.objectName():
            VentanaEditarProductos.setObjectName(u"VentanaEditarProductos")
        VentanaEditarProductos.resize(400, 300)
        self.label = QLabel(VentanaEditarProductos)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 90, 161, 16))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(12)
        self.label.setFont(font)
        self.Field_NombreProducto = QLineEdit(VentanaEditarProductos)
        self.Field_NombreProducto.setObjectName(u"Field_NombreProducto")
        self.Field_NombreProducto.setGeometry(QRect(190, 90, 171, 20))
        self.Field_CodigoProducto = QLineEdit(VentanaEditarProductos)
        self.Field_CodigoProducto.setObjectName(u"Field_CodigoProducto")
        self.Field_CodigoProducto.setGeometry(QRect(190, 50, 101, 20))
        self.label_2 = QLabel(VentanaEditarProductos)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 50, 161, 16))
        self.label_2.setFont(font)
        self.Field_PrecioProducto = QLineEdit(VentanaEditarProductos)
        self.Field_PrecioProducto.setObjectName(u"Field_PrecioProducto")
        self.Field_PrecioProducto.setGeometry(QRect(190, 130, 171, 20))
        self.label_3 = QLabel(VentanaEditarProductos)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 130, 161, 16))
        self.label_3.setFont(font)
        self.Boton_GuardarCambios = QPushButton(VentanaEditarProductos)
        self.Boton_GuardarCambios.setObjectName(u"Boton_GuardarCambios")
        self.Boton_GuardarCambios.setGeometry(QRect(100, 200, 191, 51))
        self.Boton_GuardarCambios.setFont(font)
        self.Boton_BucsarProducto = QPushButton(VentanaEditarProductos)
        self.Boton_BucsarProducto.setObjectName(u"Boton_BucsarProducto")
        self.Boton_BucsarProducto.setGeometry(QRect(290, 50, 75, 23))

        self.retranslateUi(VentanaEditarProductos)

        QMetaObject.connectSlotsByName(VentanaEditarProductos)
    # setupUi

    def retranslateUi(self, VentanaEditarProductos):
        VentanaEditarProductos.setWindowTitle(QCoreApplication.translate("VentanaEditarProductos", u"EDITAR PRODUCTOS", None))
        self.label.setText(QCoreApplication.translate("VentanaEditarProductos", u"Nombre del producto:", None))
        self.label_2.setText(QCoreApplication.translate("VentanaEditarProductos", u"C\u00f3digo del producto:", None))
        self.label_3.setText(QCoreApplication.translate("VentanaEditarProductos", u"Precio del producto:", None))
        self.Boton_GuardarCambios.setText(QCoreApplication.translate("VentanaEditarProductos", u"CONFIRMAR EDICION", None))
        self.Boton_BucsarProducto.setText(QCoreApplication.translate("VentanaEditarProductos", u"Buscar", None))
    # retranslateUi

