# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'goruntule.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(871, 550)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 871, 481))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.pushButton_delete2 = QtWidgets.QPushButton(Form)
        self.pushButton_delete2.setGeometry(QtCore.QRect(380, 500, 93, 28))
        self.pushButton_delete2.setObjectName("pushButton_delete2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Sıra"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "İşlem Tarihi"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "O. Başlangıç Zamanı"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Olayın Tanımlanması"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Olay Tipi"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Olay Açıklaması"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Kullanıcıİd"))
        self.pushButton_delete2.setText(_translate("Form", "Sil"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
