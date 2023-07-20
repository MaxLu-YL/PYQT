import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QAction
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
from Src.Ui.Ui_MainWindow import Ui_MainWindow
from Src.Ui.Ui_MainWidget import Ui_MainWidget

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

class MyMainWidget(QWidget, Ui_MainWidget):
    def __init__(self):
        super(MyMainWidget, self).__init__()
        self.setupUi(self)
        self.seleteAlgButton.clicked.connect(self.openAlgDefFile)
        self.seleteOutZipButton.clicked.connect(self.setOutZipFilePath)

        self.cwd = os.getcwd()

    def onFileChoose(self):
        filePath, filetype = QFileDialog.getOpenFileName(self, '选择行为自定义算法行为定义文件', 
                                                         self.cwd, #起始路径
                                                         'All Files(*)') #文件扩展名过滤器\\
        print(filePath, filetype)
        return filePath

    def openAlgDefFile(self):
        # aFileChoose = QAction('选择一个文件...', self)
        # aFileChoose.triggered.connect(self.onFileChoose)

        filePath = self.onFileChoose()
        self.inAlgFilePath.setText(filePath)
        pass


        
    def onFileChooseDir(self):
        dir_choose = QFileDialog.getExistingDirectory(self,
                                               '选择导出文件夹',
                                               self.cwd)
        if dir_choose == '':
            # print('取消选择')
            return

        return dir_choose

    def setOutZipFilePath(self):
        outZipFilePath = self.onFileChooseDir()
        self.outZipFilePath.setText(outZipFilePath)
        pass
        
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # window = MyMainWindow()
    # window.show()

    window = MyMainWidget()
    window.show()
    sys.exit(app.exec_())