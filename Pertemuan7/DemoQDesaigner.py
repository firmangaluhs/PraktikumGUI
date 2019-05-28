import sys

from Design2 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
	def __init__ (self,parent = None):
		QDialog.__init__(self,parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.ui.Hello.clicked.connect(self.HelloClicked)

	def HelloClicked(self):
		QMessageBox.information(self,' Demo Qt Designer', ' Hello %s , apa kabar?' %self.ui.NameEdit.text())

if __name__ =='__main__':
	a = QApplication(sys.argv)
	form = MainForm()
	form.show()
	a.exec_()
