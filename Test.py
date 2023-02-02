#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ME2AutoCrackerUI import Ui_me2

class MainLoop(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainLoop, self).__init__()
        self.clc_gui = Ui_Form()
        self.clc_gui.setupUi(self)


def MainWork():
    pass


app = QtWidgets.QApplication([])

application = MainLoop()
application.show()
MainWork()
sys.exit(app.exec())
