# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hatamesaj.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form(object):
    def setupUi(self, form):
        form.setObjectName("form")
        form.resize(283, 162)
        self.label = QtWidgets.QLabel(form)
        self.label.setGeometry(QtCore.QRect(20, 30, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(form)
        self.label_2.setGeometry(QtCore.QRect(74, 69, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_error = QtWidgets.QPushButton(form)
        self.pushButton_error.setGeometry(QtCore.QRect(90, 120, 93, 28))
        self.pushButton_error.setObjectName("pushButton_error")

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "Form"))
        self.label.setText(_translate("form", "Kullanıcı adı veya şifreniz hatalı."))
        self.label_2.setText(_translate("form", "Üye değilseniz üye olun."))
        self.pushButton_error.setText(_translate("form", "Tamam"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()
    ui = Ui_form()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())
