import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
from Resource.Ui.Ui_MainWindow import Ui_MainWindow

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.showText)
        self.pushButton_2.clicked.connect(self.clearText)
        self.pushButton_login.clicked.connect(self.login)

    def showText(self):
        print('press pushButton 1')
        self.textEdit.setText("1223")

    def clearText(self):
        print('press pushButton 2')
        self.textEdit.clear()

    def login(self):
        print(self.lineEdit_account.text())
        print(self.lineEdit_password.text())

        self.textEdit.append(self.lineEdit_account.text())
        self.textEdit.append(self.lineEdit_password.text())

        self.textEdit.grabKeyboard()

        self.textEdit.keyPressEvent()

    
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            print("单击鼠标左键2")

        
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())