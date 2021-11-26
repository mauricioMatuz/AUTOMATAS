# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ListUsuarios.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ListUser(object):
    def setupUi(self, ListUser):
        if not ListUser.objectName():
            ListUser.setObjectName(u"ListUser")
        ListUser.resize(685, 501)
        self.ListaUsuarios = QTableWidget(ListUser)
        self.ListaUsuarios.setObjectName(u"ListaUsuarios")
        self.ListaUsuarios.setGeometry(QRect(30, 91, 631, 261))
        self.EditarBtn = QPushButton(ListUser)
        self.EditarBtn.setObjectName(u"EditarBtn")
        self.EditarBtn.setGeometry(QRect(40, 360, 111, 51))

        self.retranslateUi(ListUser)

        QMetaObject.connectSlotsByName(ListUser)
    # setupUi

    def retranslateUi(self, ListUser):
        ListUser.setWindowTitle(QCoreApplication.translate("ListUser", u"Lista Usuario", None))
        self.EditarBtn.setText(QCoreApplication.translate("ListUser", u"EDITAR", None))
    # retranslateUi

