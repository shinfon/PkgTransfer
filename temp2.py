# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.resize(400,200)
        self.status = self.statusBar()
        self.status.showMessage("test string",5000)
        self.setWindowTitle("PyQt MainWindow test")
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
