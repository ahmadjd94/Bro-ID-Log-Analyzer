# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(759, 518)
        MainWindow.setStyleSheet("background-color: rgb(51, 51, 51);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.analysis = QtWidgets.QTabWidget(self.centralWidget)
        self.analysis.setGeometry(QtCore.QRect(10, 0, 721, 481))
        self.analysis.setMouseTracking(False)
        self.analysis.setAcceptDrops(False)
        self.analysis.setAutoFillBackground(False)
        self.analysis.setStyleSheet("color:rgb(255, 153, 0 );\n"
"border-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.analysis.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.analysis.setDocumentMode(False)
        self.analysis.setTabsClosable(False)
        self.analysis.setMovable(False)
        self.analysis.setObjectName("analysis")
        self.tab = QtWidgets.QWidget()
        self.tab.setMouseTracking(True)
        self.tab.setObjectName("tab")
        self.radioButton = QtWidgets.QRadioButton(self.tab)
        self.radioButton.setGeometry(QtCore.QRect(109, 110, 198, 19))
        self.radioButton.setStyleSheet("color:rgb(255, 153, 0 );\n"
"")
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_2.setGeometry(QtCore.QRect(110, 220, 198, 18))
        self.radioButton_2.setStyleSheet("color:rgb(255, 153, 0 );\n"
"")
        self.radioButton_2.setObjectName("radioButton_2")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(140, 370, 511, 23))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setStyleSheet("color:rgb(255, 153, 0 );\n"
"")
        self.progressBar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(319, 100, 281, 25))
        self.lineEdit.setStyleSheet("background-color: rgb(186, 186, 186);\n"
"border-color: rgb(0, 0, 0);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(550, 290, 97, 27))
        self.pushButton.setStyleSheet("background-color: rgb(186, 186, 186);\n"
"color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 210, 281, 25))
        self.lineEdit_2.setStyleSheet("background-color: rgb(186, 186, 186);\n"
"border-color: rgb(0, 0, 0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(140, 340, 351, 17))
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 120, 29, 27))
        self.pushButton_2.setStyleSheet("background-color: rgb(186, 186, 186);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(621, 211, 29, 27))
        self.pushButton_3.setStyleSheet("background-color: rgb(186, 186, 186);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.analysis.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 711, 351))
        self.graphicsView.setStyleSheet("background-color: rgb(188, 188, 188);\n"
"border-color: rgb(0, 0, 0);")
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(600, 390, 97, 27))
        self.pushButton_4.setStyleSheet("background-color: rgb(186, 186, 186);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.analysis.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableView = QtWidgets.QTableView(self.tab_3)
        self.tableView.setGeometry(QtCore.QRect(60, 150, 641, 291))
        self.tableView.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableView.setAutoFillBackground(False)
        self.tableView.setStyleSheet("border-color:rgb(255, 153, 0 );\n"
"")
        self.tableView.setFrameShape(QtWidgets.QFrame.Box)
        self.tableView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableView.setObjectName("tableView")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(64, 136, 59, 14))
        self.label_3.setObjectName("label_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(500, 50, 141, 27))
        self.pushButton_5.setStyleSheet("background-color: rgb(186, 186, 186);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.textEdit = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 391, 91))
        self.textEdit.setStyleSheet("border-color:rgb(255, 153, 0 );")
        self.textEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(480, 100, 191, 20))
        self.label_2.setStyleSheet("color: rgb(68, 206, 0);\n"
"border-color:rgb(255, 153, 0 );\n"
"")
        self.label_2.setObjectName("label_2")
        self.analysis.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 759, 19))
        self.menuBar.setObjectName("menuBar")
        self.menuBRO_visualizer = QtWidgets.QMenu(self.menuBar)
        self.menuBRO_visualizer.setObjectName("menuBRO_visualizer")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
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
        self.label.setText(_translate("MainWindow", "unable to load file , please check your file directory"))
        self.pushButton_2.setText(_translate("MainWindow", "..."))
        self.pushButton_3.setText(_translate("MainWindow", "..."))
        self.analysis.setTabText(self.analysis.indexOf(self.tab), _translate("MainWindow", "Load Files"))
        self.pushButton_4.setText(_translate("MainWindow", "draw timeline"))
        self.analysis.setTabText(self.analysis.indexOf(self.tab_2), _translate("MainWindow", "Timeline"))
        self.label_3.setText(_translate("MainWindow", "Results"))
        self.pushButton_5.setText(_translate("MainWindow", "Execute Command"))
        self.label_2.setText(_translate("MainWindow", "command executed successfully"))
        self.analysis.setTabText(self.analysis.indexOf(self.tab_3), _translate("MainWindow", "SQL commands "))
        self.menuBRO_visualizer.setTitle(_translate("MainWindow", "BRO visualizer"))
        self.menuHelp.setTitle(_translate("MainWindow", "help"))
        self.actionAbout.setText(_translate("MainWindow", "about"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

