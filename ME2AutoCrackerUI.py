# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ME2AutoCracker.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_me2(object):
    def setupUi(self, me2):
        me2.setObjectName("me2")
        me2.resize(512, 320)
        me2.setStyleSheet("background-image: url(:/images/images/bg512_320.jpg);")
        me2.setIconSize(QtCore.QSize(64, 64))
        self.centralwidget = QtWidgets.QWidget(me2)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 0, 421, 41))
        self.label.setMaximumSize(QtCore.QSize(511, 16777215))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(0,0,0,0%);\n"
"color: white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 260, 371, 21))
        self.label_2.setMaximumSize(QtCore.QSize(511, 16777215))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(0,0,0,0%);\n"
"color: white;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 290, 411, 21))
        self.label_3.setMaximumSize(QtCore.QSize(511, 16777215))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(0,0,0,0%);\n"
"color: white;")
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 230, 111, 17))
        self.checkBox.setStyleSheet("background-color: rgba(0,0,0,0%);\n"
"color: white;")
        self.checkBox.setObjectName("checkBox")
        me2.setCentralWidget(self.centralwidget)

        self.retranslateUi(me2)
        QtCore.QMetaObject.connectSlotsByName(me2)

    def retranslateUi(self, me2):
        _translate = QtCore.QCoreApplication.translate
        me2.setWindowTitle(_translate("me2", "Mass Effect 2 | Safe Autocracker 1.0"))
        self.label.setText(_translate("me2", "Mass Effect 2 - Autocracker 1.0"))
        self.label_2.setText(_translate("me2", "Активация программы - Двойной ALT"))
        self.label_3.setText(_translate("me2", "Деактивация программы - Двойной CTRL"))
        self.checkBox.setText(_translate("me2", "Тестовый режим"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    me2 = QtWidgets.QMainWindow()
    ui = Ui_me2()
    ui.setupUi(me2)
    me2.show()
    sys.exit(app.exec_())
