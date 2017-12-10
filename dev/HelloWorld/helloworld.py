# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helloworld.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from welcome import Ui_MainWindow
import MySQLdb
import traceback

class Ui_Dialog(object):

    def loginCheck(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()

        db = MySQLdb.connect(host="localhost",
                             user="root",
                             passwd="zaq12wsx",
                             db="sakila")

        cursor = db.cursor()
        cursor.execute("SELECT * FROM actor WHERE user_name = %s AND password = %s", (username, password))
        numrows = cursor.rowcount
        if numrows > 0:
            print("User found!")

            try:
                self.app2 = QtWidgets.QApplication(sys.argv)
                self.Dialog2 = QtWidgets.QMainWindow()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self.Dialog2)
                self.Dialog2.show()
            except:
                traceback.print_exc()

        else:
            print("User not found!")


    def signUpCheck(self):
        print("Sign Up Button Clicked !")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.u_name_label = QtWidgets.QLabel(Dialog)
        self.u_name_label.setGeometry(QtCore.QRect(140, 140, 64, 16))
        self.u_name_label.setObjectName("u_name_label")
        self.username_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.username_lineEdit.setGeometry(QtCore.QRect(220, 140, 113, 22))
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QtCore.QRect(220, 180, 113, 22))
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.login_button = QtWidgets.QPushButton(Dialog)
        self.login_button.setGeometry(QtCore.QRect(130, 250, 93, 28))
        self.login_button.setObjectName("login_button")
        #################### Button Event #####################
        self.login_button.clicked.connect(self.loginCheck)
        #######################################################
        self.signup_button = QtWidgets.QPushButton(Dialog)
        self.signup_button.setGeometry(QtCore.QRect(240, 250, 93, 28))
        self.signup_button.setObjectName("signup_button")
        #################### Button Event #####################
        self.signup_button.clicked.connect(self.signUpCheck)
        #######################################################
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 50, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pass_label = QtWidgets.QLabel(Dialog)
        self.pass_label.setGeometry(QtCore.QRect(130, 180, 68, 16))
        self.pass_label.setObjectName("pass_label")
        self.u_name_label.raise_()
        self.pass_label.raise_()
        self.username_lineEdit.raise_()
        self.password_lineEdit.raise_()
        self.pass_label.raise_()
        self.login_button.raise_()
        self.signup_button.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login Form"))
        self.u_name_label.setText(_translate("Dialog", "USERNAME"))
        self.login_button.setText(_translate("Dialog", "Login"))
        self.signup_button.setText(_translate("Dialog", "Sign Up"))
        self.label.setText(_translate("Dialog", "Login Form"))
        self.pass_label.setText(_translate("Dialog", "PASSWORD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exit")

