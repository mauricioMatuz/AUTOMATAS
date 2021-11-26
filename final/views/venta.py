# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'venta.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class PrincipalView(object):
    def setupUi(self, PrincipalView):
        if not PrincipalView.objectName():
            PrincipalView.setObjectName(u"PrincipalView")
        PrincipalView.setEnabled(True)
        PrincipalView.resize(961, 567)
        self.ButtonFrame = QFrame(PrincipalView)
        self.ButtonFrame.setObjectName(u"ButtonFrame")
        self.ButtonFrame.setGeometry(QRect(10, 10, 941, 91))
        self.ButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.ButtonFrame.setFrameShadow(QFrame.Raised)
        self.AgregarUsuario = QPushButton(self.ButtonFrame)
        self.AgregarUsuario.setObjectName(u"AgregarUsuario")
        self.AgregarUsuario.setGeometry(QRect(20, 10, 71, 51))
        self.AgregarUsuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.AgregarUsuario.setStyleSheet(u"\n"
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
        icon.addFile(u"./assets/addUser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AgregarUsuario.setIcon(icon)
        self.AgregarUsuario.setIconSize(QSize(50, 50))
        self.AgregarUsuario.setFlat(True)
        self.label = QLabel(self.ButtonFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 60, 121, 21))
        self.AgregarProve = QPushButton(self.ButtonFrame)
        self.AgregarProve.setObjectName(u"AgregarProve")
        self.AgregarProve.setGeometry(QRect(170, 10, 71, 51))
        self.AgregarProve.setCursor(QCursor(Qt.PointingHandCursor))
        self.AgregarProve.setStyleSheet(u"\n"
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
        icon1 = QIcon()
        icon1.addFile(u"./assets/addSupplier.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AgregarProve.setIcon(icon1)
        self.AgregarProve.setIconSize(QSize(50, 50))
        self.AgregarProve.setFlat(True)
        self.label_2 = QLabel(self.ButtonFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 60, 121, 21))
        self.label_3 = QLabel(self.ButtonFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 60, 71, 21))
        self.EditarBtn = QPushButton(self.ButtonFrame)
        self.EditarBtn.setObjectName(u"EditarBtn")
        self.EditarBtn.setGeometry(QRect(320, 10, 71, 51))
        self.EditarBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.EditarBtn.setStyleSheet(u"\n"
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
        icon2 = QIcon()
        icon2.addFile(u"./assets/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.EditarBtn.setIcon(icon2)
        self.EditarBtn.setIconSize(QSize(50, 50))
        self.EditarBtn.setFlat(True)
        self.label_4 = QLabel(self.ButtonFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(440, 60, 111, 21))
        self.AgregarProducto = QPushButton(self.ButtonFrame)
        self.AgregarProducto.setObjectName(u"AgregarProducto")
        self.AgregarProducto.setGeometry(QRect(460, 10, 71, 51))
        self.AgregarProducto.setCursor(QCursor(Qt.PointingHandCursor))
        self.AgregarProducto.setStyleSheet(u"\n"
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
        icon3 = QIcon()
        icon3.addFile(u"./assets/addProduct.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AgregarProducto.setIcon(icon3)
        self.AgregarProducto.setIconSize(QSize(50, 50))
        self.AgregarProducto.setFlat(True)
        self.label_5 = QLabel(self.ButtonFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(580, 60, 111, 21))
        self.Eliminar = QPushButton(self.ButtonFrame)
        self.Eliminar.setObjectName(u"Eliminar")
        self.Eliminar.setGeometry(QRect(600, 10, 71, 51))
        self.Eliminar.setCursor(QCursor(Qt.PointingHandCursor))
        self.Eliminar.setStyleSheet(u"\n"
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
        icon4 = QIcon()
        icon4.addFile(u"./assets/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Eliminar.setIcon(icon4)
        self.Eliminar.setIconSize(QSize(50, 50))
        self.Eliminar.setFlat(True)
        self.frame = QFrame(PrincipalView)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 110, 941, 41))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 151, 21))
        self.BarraCodigo = QLineEdit(self.frame)
        self.BarraCodigo.setObjectName(u"BarraCodigo")
        self.BarraCodigo.setGeometry(QRect(130, 10, 291, 20))
        self.AddBtn = QPushButton(self.frame)
        self.AddBtn.setObjectName(u"AddBtn")
        self.AddBtn.setEnabled(True)
        self.AddBtn.setGeometry(QRect(440, 10, 141, 25))
        icon5 = QIcon()
        icon5.addFile(u"./assets/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AddBtn.setIcon(icon5)
        self.AddBtn.setIconSize(QSize(25, 25))
        self.AddBtn.setFlat(False)
        self.ListaProducto = QTableWidget(PrincipalView)
        self.ListaProducto.setObjectName(u"ListaProducto")
        self.ListaProducto.setGeometry(QRect(10, 160, 941, 341))
        self.label_7 = QLabel(PrincipalView)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 515, 161, 21))
        self.ContadorProducto = QLabel(PrincipalView)
        self.ContadorProducto.setObjectName(u"ContadorProducto")
        self.ContadorProducto.setGeometry(QRect(190, 520, 47, 13))
        self.Cobrar = QPushButton(PrincipalView)
        self.Cobrar.setObjectName(u"Cobrar")
        self.Cobrar.setGeometry(QRect(780, 520, 151, 41))
        icon6 = QIcon()
        icon6.addFile(u"./assets/caja.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Cobrar.setIcon(icon6)
        self.Cobrar.setIconSize(QSize(27, 25))
        self.label_8 = QLabel(PrincipalView)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(350, 520, 131, 41))
        self.TotalLabel = QLabel(PrincipalView)
        self.TotalLabel.setObjectName(u"TotalLabel")
        self.TotalLabel.setGeometry(QRect(450, 520, 151, 41))

        self.retranslateUi(PrincipalView)

        QMetaObject.connectSlotsByName(PrincipalView)
    # setupUi

    def retranslateUi(self, PrincipalView):
        PrincipalView.setWindowTitle(QCoreApplication.translate("PrincipalView", u"Punto de Venta", None))
        self.AgregarUsuario.setText("")
        self.label.setText(QCoreApplication.translate("PrincipalView", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Registrar Usuario</span></p></body></html>", None))
        self.AgregarProve.setText("")
        self.label_2.setText(QCoreApplication.translate("PrincipalView", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Registrar Proveedor</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("PrincipalView", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Editar</span></p></body></html>", None))
        self.EditarBtn.setText("")
        self.label_4.setText(QCoreApplication.translate("PrincipalView", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Agregar Producto</span></p></body></html>", None))
        self.AgregarProducto.setText("")
        self.label_5.setText(QCoreApplication.translate("PrincipalView", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Eliminar</span></p></body></html>", None))
        self.Eliminar.setText("")
        self.label_6.setText(QCoreApplication.translate("PrincipalView", u"<html><head/><body><p><span style=\" font-size:12pt;\">Ingrese Codigo:</span></p></body></html>", None))
        self.AddBtn.setText(QCoreApplication.translate("PrincipalView", u"Agregar ", None))
        self.label_7.setText(QCoreApplication.translate("PrincipalView", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">CANTIDAD DE PRODUCTO:</span></p></body></html>", None))
        self.ContadorProducto.setText(QCoreApplication.translate("PrincipalView", u"#", None))
        self.Cobrar.setText(QCoreApplication.translate("PrincipalView", u"COBRAR", None))
        self.label_8.setText(QCoreApplication.translate("PrincipalView", u"<html><head/><body><p><span style=\" font-size:18pt;\">TOTAL = </span></p></body></html>", None))
        self.TotalLabel.setText(QCoreApplication.translate("PrincipalView", u"<html><head/><body><p><span style=\" font-size:20pt;\">TextLabel</span></p></body></html>", None))
    # retranslateUi

