# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import traceback
import re, os
from OracleDatabase import OracleDatabase

class Ui_Welcome(object):


    def setupUi(self, Welcome):
        Welcome.setObjectName("Welcome")
        Welcome.resize(521, 414)
        self.gridLayout = QtWidgets.QGridLayout(Welcome)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Welcome)
        self.groupBox.setObjectName("groupBox")
        self.userNameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.userNameLineEdit.setGeometry(QtCore.QRect(110, 40, 301, 22))
        self.userNameLineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.userNameLineEdit.setInputMask("")
        self.userNameLineEdit.setText("")
        self.userNameLineEdit.setMaxLength(32767)
        self.userNameLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.userNameLineEdit.setObjectName("userNameLineEdit")
        self.passwordLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.passwordLineEdit.setGeometry(QtCore.QRect(110, 80, 301, 22))
        self.passwordLineEdit.setInputMask("")
        self.passwordLineEdit.setText("")
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LoginButton = QtWidgets.QPushButton(Welcome)
        self.LoginButton.setGeometry(QtCore.QRect(220, 360, 93, 28))
        self.LoginButton.setObjectName("login")
        self.LoginButton.clicked.connect(self.loginUser)
        self.userNameLineEdit.raise_()
        self.passwordLineEdit.raise_()
        self.LoginButton.raise_()
        self.groupBox_2 = QtWidgets.QGroupBox(Welcome)
        self.groupBox_2.setObjectName("groupBox_2")
        self.connTypeComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.connTypeComboBox.setGeometry(QtCore.QRect(170, 20, 171, 22))
        self.connTypeComboBox.setObjectName("connTypeComboBox")
        self.connTypeComboBox.addItem("")
        self.connTypeComboBox.addItem("")
        self.connTypeComboBox.addItem("")
        self.setBasicChoiceFiled()
        self.connTypeComboBox.activated.connect(self.onActivated)

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 3)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 3)
        self.gridLayout.addWidget(self.LoginButton, 2, 1, 1, 1)

        self.retranslateUi(Welcome)
        QtCore.QMetaObject.connectSlotsByName(Welcome)

    def retranslateUi(self, Welcome):
        _translate = QtCore.QCoreApplication.translate
        Welcome.setWindowTitle(_translate("Welcome", "Authorization"))
        self.groupBox.setTitle(_translate("Welcome", "User"))
        self.userNameLineEdit.setPlaceholderText(_translate("Welcome", "User Name"))
        self.passwordLineEdit.setPlaceholderText(_translate("Welcome", "Password"))
        self.groupBox_2.setTitle(_translate("Welcome", "Connection type"))
        self.connTypeComboBox.setItemText(0, _translate("Welcome", "Basic"))
        self.connTypeComboBox.setItemText(1, _translate("Welcome", "TNS"))
        self.connTypeComboBox.setItemText(2, _translate("Welcome", "Advanced"))
        self.LoginButton.setText(_translate("Welcome", "Login"))

    def onActivated(self, index):
        try:
            if index == 0:
                self.setBasicChoiceFiled()
            elif index == 1:
                self.setTNSChoiceField()

            elif index == 2:
                self.setAdvancedChoiceFiled()
        except:
            traceback.print_exc()

    def setTNSChoiceField(self):
        self.clearGroupBoxChild(self.groupBox_2)
        self.TNSLabel = QtWidgets.QLabel(self.groupBox_2)
        self.TNSLabel.setGeometry(QtCore.QRect(50, 52, 90, 16))
        self.TNSLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.TNSLabel.setObjectName("TNSLabel")
        self.TNSLabel.setText("Network Alias")
        self.TNSLabel.show()

        self.TNSComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.TNSComboBox.setGeometry(QtCore.QRect(170, 50, 171, 22))
        self.TNSComboBox.setObjectName("TNSComboBox")

        script_dir = os.path.dirname(__file__)
        rel_path = "C:\oracle\ora10\network\ADMIN\tnsnames.ora"
        abs_file_path = os.path.join(script_dir, rel_path)
        file = open(r"C:/oracle/ora10/network/ADMIN/tnsnames.ora", "r")
        for line in file:
            matchLine = re.match('^[a-zA-Z0-9]*', line, flags=0)
            if matchLine.group(0):
                self.TNSComboBox.addItem(matchLine.group(0))

        self.TNSComboBox.show()

    def setAdvancedChoiceFiled(self):
        self.clearGroupBoxChild(self.groupBox_2)
        self.DBC_Label = QtWidgets.QLabel(self.groupBox_2)
        self.DBC_Label.setGeometry(QtCore.QRect(50, 50, 100, 16))
        self.DBC_Label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.DBC_Label.setObjectName("TNSLabel")
        self.DBC_Label.setText("Custom DBC URL")
        self.DBC_Label.show()
        self.DBC_URLTextEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.DBC_URLTextEdit.setGeometry(QtCore.QRect(50, 75, 400, 60))
        self.DBC_URLTextEdit.setObjectName("JDBC_URLTextEdit")
        self.DBC_URLTextEdit.show()

    def setBasicChoiceFiled(self):
        self.clearGroupBoxChild(self.groupBox_2)

        self.HostnameLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.HostnameLineEdit.setGeometry(QtCore.QRect(150, 50, 261, 22))
        self.HostnameLineEdit.setFrame(True)
        self.HostnameLineEdit.setObjectName("HostnameLineEdit")
        self.HostnameLineEdit.show()
        self.PortLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.PortLineEdit.setGeometry(QtCore.QRect(150, 80, 261, 22))
        self.PortLineEdit.setObjectName("PortLineEdit")
        self.PortLineEdit.show()
        self.SIDLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.SIDLineEdit.setGeometry(QtCore.QRect(150, 110, 261, 22))
        self.SIDLineEdit.setObjectName("SIDLineEdit")
        self.SIDLineEdit.show()
        self.hostnameLabel = QtWidgets.QLabel(self.groupBox_2)
        self.hostnameLabel.setGeometry(QtCore.QRect(70, 52, 71, 16))
        self.hostnameLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.hostnameLabel.setObjectName("hostnameLabel")
        self.hostnameLabel.setText("Hostname: ")
        self.hostnameLabel.show()
        self.portLabel = QtWidgets.QLabel(self.groupBox_2)
        self.portLabel.setGeometry(QtCore.QRect(70, 82, 71, 16))
        self.portLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.portLabel.setObjectName("PortLabel")
        self.portLabel.setText("Port: ")
        self.portLabel.show()
        self.sIDLabel = QtWidgets.QLabel(self.groupBox_2)
        self.sIDLabel.setGeometry(QtCore.QRect(70, 112, 71, 16))
        self.sIDLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sIDLabel.setObjectName("sIDLabel")
        self.sIDLabel.setText("SID: ")
        self.sIDLabel.show()

    def clearGroupBoxChild(self, object):
        if object:
            list = object.children()
            for i in reversed(range(len(list))):
                if list[i].objectName() != "connTypeComboBox":
                    list[i].deleteLater()

    def loginUser(self):

        login       = self.userNameLineEdit
        password    = self.passwordLineEdit

        if self.connTypeComboBox.currentIndex() == 0:
            print("Connect to database")
            try:
                OD = OracleDatabase()
                OD.get_connection()
            except:
                traceback.print_exc()
                print("Connection Error!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Welcome = QtWidgets.QDialog()
    ui = Ui_Welcome()
    ui.setupUi(Welcome)
    Welcome.show()
    sys.exit(app.exec_())

