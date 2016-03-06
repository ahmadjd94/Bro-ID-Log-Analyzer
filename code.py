# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, 
    QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
import sqlite3
import os
import fnmatch

class Ui_MainWindow(object): # Qt creator generated functions and classes
    #openCaller=''
    global con
    count=0
    valid=[]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(646, 434)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.analysis = QtWidgets.QTabWidget(self.centralWidget)
        self.analysis.setGeometry(QtCore.QRect(0, 30, 641, 351))
        self.analysis.setMouseTracking(False)
        self.analysis.setObjectName("analysis")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.radioButton = QtWidgets.QRadioButton(self.tab)
        self.radioButton.setGeometry(QtCore.QRect(70, 100, 198, 19))

        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_2.setGeometry(QtCore.QRect(70, 180, 198, 18))
        self.radioButton_2.setObjectName("radioButton_2")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(70, 280, 511, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(280, 90, 281, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(480, 230, 97, 27))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 170, 281, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(70, 260, 351, 17))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(581, 90, 29, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(581, 171, 29, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.analysis.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.analysis.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 646, 27))
        self.menuBar.setObjectName("menuBar")
        self.menuBRO_visualizer = QtWidgets.QMenu(self.menuBar)
        self.menuBRO_visualizer.setObjectName("menuBRO_visualizer")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.message=QtWidgets.QMessageBox(MainWindow)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuBRO_visualizer.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.retranslateUi(MainWindow)
        self.analysis.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.radioButton.setText(_translate("MainWindow", "load single file"))
        self.radioButton_2.setText(_translate("MainWindow", "load directory of log files"))
        self.pushButton.setText(_translate("MainWindow", "Load"))
        self.label.setVisible(False)
        self.label.setText(_translate("MainWindow", "unable to load file , please check your file directory"))
        self.pushButton_2.setText(_translate("MainWindow", "..."))
        self.pushButton_3.setText(_translate("MainWindow", "..."))
        self.analysis.setTabText(self.analysis.indexOf(self.tab), _translate("MainWindow", "Load Files"))
        self.analysis.setTabText(self.analysis.indexOf(self.tab_2), _translate("MainWindow", "analyses"))
        self.menuBRO_visualizer.setTitle(_translate("MainWindow", "BRO visualizer"))
        self.menuHelp.setTitle(_translate("MainWindow", "help"))
        self.mainToolBar.setWindowTitle(_translate("MainWindow", "BRO Log file analyzer and visualizer"))
        self.actionAbout.setText(_translate("MainWindow", "about"))
        self.analysis.setTabEnabled(1,False)
        self.radioButton.clicked.connect(self.switch1)  # connect event click to function switch1
        self.radioButton_2.clicked.connect(self.switch2)    # connect event click to function switch2)
        self.pushButton_2.clicked.connect(self.openFileDialog)  # connect event click to function openfile dialog
        self.actionAbout.triggered.connect(self.about)  # connect event triggered to function about
        self.lineEdit.textChanged.connect(self.openFile)    # connect event text-changed to function openFile
        self.pushButton_3.clicked.connect(self.openDirDialog)   # connect event click to function openDirDialog
        self.pushButton.clicked.connect(self.load)   # # connect event click to function load
        self.radioButton.click()

    def load(self):     # this function loads the content of the log files into the DB
        self.progressBar.setValue(0)
        if self.radioButton.isChecked():
            f=open(self.lineEdit.text(),'r')
            i=1
            print(self.count)
            while (i<=self.count):
                #self.progressBar.setValue(self.progressBar.value()+(i/self.count))
                self.progressBar.setValue((i/self.count)*100)
                print(f.readline())
                i+=1
            f.close()
        elif self.radioButton_2.isChecked():
            v=100/len(self.valid)
            for each in self.valid:
                f=open(each,'r')
                for i in f:
                    f.readline()
                f.close()
                self.progressBar.setValue(self.progressBar.value()+v)
        self.analysis.setTabEnabled(1,True)


    def switch1(self):       #functions switch1 and switch 2 disables the objects of GUI accoridng to radiobuttons
        self.lineEdit_2.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.lineEdit.setDisabled(False)
        self.pushButton_2.setDisabled(False)
    def switch2(self):
        self.lineEdit.setDisabled(True)
        self.pushButton_2.setDisabled(True)
        self.lineEdit_2.setDisabled(False)
        self.pushButton_3.setDisabled(False)
    def about(self): #displays the about message if the user selected it from main menu
        self.message.setText("this is a graduation project as a requirment for PSUT \n for more info visit the github link below")
        self.message.setDetailedText("https://github.com/ahmadjd94/BRO-IDS-Log-files-visualizer-and-analyzer")
        self.message.show()
    def openFile(self): # function used to open files (single files and files inside working directory )
        self.label.setVisible(False)
        try:
                file=open(self.lineEdit.text())
                print (file)
                self.count=0
                for i in file:
                    self.count+=1
                self.label.setText("the selected file has "+str(self.count)+" lines")
                self.label.setVisible(True)
                file.close()
        except FileNotFoundError: # handling incrorrect file directories / paths
                self.label.show()

    def openFileDialog(self):  # displays open file dialog for user to select the required log file

            fname = QFileDialog.getOpenFileName(None, 'Open file', '/home','*.log') # error in params
            print(fname)
            self.lineEdit.setText(fname[0])
            try:
                file=open(fname[0])
                count=0
                for i in file:
                    count+=1
                self.label.setText("the selected file has "+str(count)+" lines")
                self.label.setVisible(True)
                self.lineEdit.setText(fname[0])
            except FileNotFoundError:
                self.label.show()

    def openDirDialog(self):
        try:
            di=QFileDialog.getExistingDirectory(None,'open dir of log files', '/home', QFileDialog.ShowDirsOnly) #error in params
            print(di)
            os.chdir(di) # change current working directory
            files=(os.listdir()) # make a list of files inside current working dir
            for each in files :
                if fnmatch.fnmatch(each,"*.log"):
                    print(each)
                    self.valid.append(each)
            self.label.setText("the directory you have selected have "+str(len(self.valid))+" files")
            self.lineEdit_2.setText(di)
        except NotADirectoryError:   # exception raised if the selection was not a dir
            self.label.setText("make sure you are entering a dir")
        except :
            self.label.setText("make sure you have selected a directory")
        finally:
            self.label.show()


if __name__ == "__main__": # main module
    import sys

    try :
        con=sqlite3.connect('analyze.db') # initializing connection to DB // should be in UI init ??
    except :
        # showmessgae box to tell the user to use the program with admin permissions 
        sys.exit()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

