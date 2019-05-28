# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(641, 456)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 60, 351, 31))
        self.label.setObjectName("label")
        self.NameEdit = QtWidgets.QLineEdit(Form)
        self.NameEdit.setGeometry(QtCore.QRect(190, 100, 361, 20))
        self.NameEdit.setObjectName("NameEdit")
        self.Exit = QtWidgets.QPushButton(Form)
        self.Exit.setGeometry(QtCore.QRect(320, 210, 75, 23))
        self.Exit.setObjectName("Exit")
        self.Hello = QtWidgets.QPushButton(Form)
        self.Hello.setGeometry(QtCore.QRect(270, 160, 75, 23))
        self.Hello.setObjectName("Hello")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 160, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        self.Exit.clicked.connect(Form.close)
        self.pushButton_3.clicked.connect(self.NameEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Masukan Nama Anda :</span></p></body></html>"))
        self.Exit.setText(_translate("Form", "Exit"))
        self.Hello.setText(_translate("Form", "Hello"))
        self.pushButton_3.setText(_translate("Form", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
