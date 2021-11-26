# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'producto.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ProductoVentana(object):
    def setupUi(self, ProductoVentana):
        if not ProductoVentana.objectName():
            ProductoVentana.setObjectName(u"ProductoVentana")
        ProductoVentana.resize(545, 625)
        self.label = QLabel(ProductoVentana)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 40, 241, 51))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label_2 = QLabel(ProductoVentana)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 170, 91, 51))
        self.label_2.setFont(font)
        self.label_3 = QLabel(ProductoVentana)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 290, 241, 51))
        self.label_3.setFont(font)
        self.NombreProducto = QLineEdit(ProductoVentana)
        self.NombreProducto.setObjectName(u"NombreProducto")
        self.NombreProducto.setGeometry(QRect(120, 90, 301, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.NombreProducto.setFont(font1)
        self.PrecioProducto = QLineEdit(ProductoVentana)
        self.PrecioProducto.setObjectName(u"PrecioProducto")
        self.PrecioProducto.setGeometry(QRect(120, 220, 301, 31))
        self.PrecioProducto.setFont(font1)
        self.CodigoProducto = QLineEdit(ProductoVentana)
        self.CodigoProducto.setObjectName(u"CodigoProducto")
        self.CodigoProducto.setGeometry(QRect(120, 340, 301, 31))
        self.CodigoProducto.setFont(font1)
        self.AgregarProducto = QPushButton(ProductoVentana)
        self.AgregarProducto.setObjectName(u"AgregarProducto")
        self.AgregarProducto.setGeometry(QRect(180, 420, 171, 51))
        self.AgregarProducto.setCursor(QCursor(Qt.PointingHandCursor))
        self.AgregarProducto.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #0069c0;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"./assets/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AgregarProducto.setIcon(icon)
        self.AgregarProducto.setIconSize(QSize(25, 25))

        self.retranslateUi(ProductoVentana)

        QMetaObject.connectSlotsByName(ProductoVentana)
    # setupUi

    def retranslateUi(self, ProductoVentana):
        ProductoVentana.setWindowTitle(QCoreApplication.translate("ProductoVentana", u"PRODUCTO", None))
        self.label.setText(QCoreApplication.translate("ProductoVentana", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Nombre del Producto:</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("ProductoVentana", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Precio:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("ProductoVentana", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">CODIGO DE BARRA:</span></p></body></html>", None))
        self.AgregarProducto.setText(QCoreApplication.translate("ProductoVentana", u"PushButton", None))
    # retranslateUi

