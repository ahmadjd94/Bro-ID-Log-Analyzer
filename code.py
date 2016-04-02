# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication, QMessageBox)
from PyQt5.QtGui import QIcon
import sqlite3
import os  # module used for changing Current working directory of the program
import fnmatch  # module used for matching files names
# import pyqtgraph as pg
import re


class Ui_MainWindow(object):  # Qt and PYUIC creator generated functions and classes
    ################################  defining global variable ###################################
    global con  # connection to DB
    linesCount = 0  # count of lines
    loaded = False  # this variable stores if there is a file loaded into program or not
    validFiles = []
    valid = ['conn.log', 'dhcp.log', 'dnp3.log', 'dns.log', 'ftp.log', 'http.log', 'irc.log', 'kerberos.log',
             'modbus.log'
        , 'modbus_register_change.log', 'mysql.log', 'radius.log', 'rdp.log', 'sip.log', 'smtp.log', 'snmp.log',
             'socks.log', 'ssl.log', 'syslog.log', 'tunnel.log', 'files.log', 'pe.log', 'x509.log', 'intel.log',
             'notice.log', 'notice_alarm.log', 'signatures.log', 'traceroute.log', 'app_stats.log', 'known_certs.log',
             'known_devices.log', 'known_hosts.log', 'known_modbus.log', 'known_services.log', 'software.log',
             'barnyard2.log', 'dpd.log', 'unified2.log', 'weird.log', 'capture_loss.log', 'cluster.log',
             'communication.log', 'loaded_scripts.log', 'packet_filter.log', 'prof.log', 'reporter.log', 'stats.log',
             'stderr.log', 'stdout.log']

    # this list stores the valid log files in a directory

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(709, 489)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.analysis = QtWidgets.QTabWidget(self.centralWidget)
        self.analysis.setGeometry(QtCore.QRect(0, 30, 701, 391))
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
        self.label.setGeometry(QtCore.QRect(70, 260, 410, 17))
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
        self.graphicsView = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView.setGeometry(QtCore.QRect(65, 11, 521, 281))
        self.graphicsView.setStyleSheet("background-color: rgb(188, 188, 188);")
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(560, 320, 97, 27))
        self.pushButton_4.setObjectName("pushButton_4")
        self.analysis.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textEdit = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit.setGeometry(QtCore.QRect(30, 30, 371, 91))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 70, 141, 27))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tableView = QtWidgets.QTableView(self.tab_3)
        self.tableView.setGeometry(QtCore.QRect(30, 150, 591, 192))
        self.tableView.setAutoFillBackground(False)
        self.tableView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableView.setObjectName("tableView")
        self.analysis.addTab(self.tab_3, "")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 411, 17))
        self.label_2.setObjectName("label_2")
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

        self.message = QtWidgets.QMessageBox(MainWindow)
        self.__message2__ = QtWidgets.QMessageBox(MainWindow)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuBRO_visualizer.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.retranslateUi(MainWindow)
        self.analysis.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.__message2__.setText("error connecting to database")
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
        self.pushButton_5.setText(_translate("MainWindow", "Execute Command"))
        self.analysis.setTabText(self.analysis.indexOf(self.tab_3), _translate("MainWindow", "SQL commands "))
        self.actionAbout.setText(_translate("MainWindow", "about"))
        self.label_2.setStyleSheet("color : green")
        self.pushButton_4.setText(_translate("MainWindow", "draw timeline"))
        self.label_2.setVisible(False)
        self.analysis.setTabEnabled(1, False)
        # self.analysis.setTabEnabled(2,False)
        self.radioButton.clicked.connect(self.switch1)  # connect event click to function switch1
        self.radioButton_2.clicked.connect(self.switch2)  # connect event click to function switch2)
        self.pushButton_2.clicked.connect(self.openFileDialog)  # connect event click to function openfile dialog
        self.actionAbout.triggered.connect(self.about)  # connect event triggered to function about
        self.lineEdit.textChanged.connect(self.openFile)  # connect event text-changed to function openFile
        self.pushButton_3.clicked.connect(self.openDirDialog)  # connect event click to function openDirDialog
        self.pushButton.clicked.connect(self.load)  # # connect event click to function load
        self.textEdit.textChanged.connect(self.uMan)
        self.pushButton_5.clicked.connect(self.executeSQL)
        self.radioButton.click()

    def uMan(self):
        self.label_2.setVisible(False)

    def executeSQL(self):
        command = self.textEdit.toPlainText()
        try:
            con.execute(command)
            # select statments and insertion queried results into the table view
            # handle tables that doesnt exist -> show text boxes that show the suitbale hint
            # handle SQLITE syntax errors
            self.label_2.setText("command executed successfully")
            self.label_2.setStyleSheet("color:green")
            self.label_2.setVisible(True)
        except sqlite3.OperationalError as err:
            print(str(err))
            self.message.setText("make sure you have entered a valid SQLite3 command  ")
            self.message.setDetailedText(str(err))
            self.label_2.setText("error executing SQL command")
            self.label_2.setStyleSheet("color : red")
            self.label_2.setVisible(True)
            self.message.show()

    def load(self):  # this function loads the content of the log files into the DB
        # this function should use regex to find and match patterns from log files
        timeIndex = uidIndex = sipIndex = spIndex = dipIndex = dpIndex = protoIndex = serviceIndex = durationIndex = countOriginBytesIndex = countResponseBytesIndex = 0
        connStateIndex = localOrig = localResp = missedBytes = history = origPkts = origIPBytes = respPkts = respIPBytes = tunnelParents = 0
        if self.loaded:
            reply = QMessageBox.question(self.message, 'Message', "are you sure you want to load files",
                                         QMessageBox.Yes,
                                         QMessageBox.No)  # shows a message box to user to  make sure of reloading files
            if reply == QMessageBox.Yes:
                self.reset()
            else:
                return

        if self.radioButton.isChecked() and self.lineEdit.text() != "":
            f = open(self.lineEdit.text(), 'r')
            i = 0
            # print(self.linesCount)
            for each in f:
                print(each)
                inpu = each.split()
                if inpu[0] == "#fields":

                    print("true")
                    indecies = each.split()
                    timeIndex = indecies.index('ts')-1  # time index
                    uidIndex = indecies.index("uid")-1 # user Id
                    sipIndex = indecies.index("id.orig_h")-1  # source IP
                    spIndex = indecies.index('id.orig_p') -1 # source Port
                    dipIndex = indecies.index("id.resp_h") -1 # Destination IP
                    dpIndex = indecies.index("id.resp_p")-1  # Destination Port
                    protoIndex = indecies.index("proto")-1  # Protocol type index
                    serviceIndex = indecies.index("service")-1  # stores the type of service
                    durationIndex = indecies.index("duration") -1 # stores the duration of service
                    countOriginBytesIndex = indecies.index("orig_bytes")-1  # count of bytes sent by client
                    countResponseBytesIndex = indecies.index("resp_bytes")-1  # count of bytes sent by server
                    connStateIndex = indecies.index("conn_state")-1
                    localOrig = indecies.index("conn_state")-1
                    localResp = indecies.index("local_resp")-1
                    missedBytes = indecies.index("missed_bytes")-1
                    history = indecies.index("history")-1
                    origPkts = indecies.index("orig_pkts")-1
                    origIPBytes = indecies.index("orig_ip_bytes")-1
                    respPkts = indecies.index("resp_pkts")-1
                    respIPBytes = indecies.index("resp_ip_bytes")-1
                    tunnelParents = indecies.index("tunnel_parents")-1

                    print("wtf is this shit ?")

                elif inpu[0][0] != "#":
                    print("dfgh")
                    print(inpu,'\n', each)
                    con.execute(
                        """insert into analysis values (\'{0}\',\'{1}\',\'{2}\',\'{3}\',\'{4}\',\'{5}\',\'{6}\',\'{7}\',
                        \'{8}\',\'{9}\',\'{10}\',\'{11}\',\'{12}\',\'{13}\',\'{14}\',\'{15}\',
                        \'{16}\',\'{17}\',\'{18}\',\'{19}\',\'{20}\'""".format(
                            inpu[timeIndex], inpu[uidIndex], inpu[sipIndex], inpu[spIndex], inpu[dipIndex],
                            inpu[dpIndex], inpu[protoIndex], inpu[serviceIndex], inpu[durationIndex],
                            inpu[countOriginBytesIndex], inpu[countResponseBytesIndex], inpu[connStateIndex],
                            inpu[localOrig], inpu[localResp], inpu[missedBytes],
                            inpu[history], inpu[origPkts], inpu[origIPBytes], inpu[respPkts], inpu[respIPBytes],str(inpu[tunnelParents])))
                else:  # lines that begin with # denote comment lines

                    try:

                        # brace yourself for the longest sql line ever
                        print("dfgh")
                        # con.execute("insert into analysis values("+str(inpu[timeIndex])+","+str(inpu[uidIndex])+","+str(inpu[sipIndex])+","+str(inpu[spIndex])+","+str(inpu[dipIndex])+","+str(inpu[dpIndex])+","+str(inpu[protoIndex])+","+str(inpu[serviceIndex])+","+str(inpu[durationIndex])+","+str(inpu[countOriginBytesIndex])+","+str(inpu[countResponseBytesIndex])+")")
                    except:
                        self.message.setText("make sure you have previliges to execute command over data base \n")
                        # insert into data base for further analysis
                        # do some operations to the input line
                        # do pattern matching

                self.progressBar.setValue((i / self.linesCount) * 100)

            f.close()
        elif self.radioButton_2.isChecked() and self.lineEdit_2.text() != "":
            v = 100 / len(self.validFiles)
            for each in self.validFiles:
                f = open(each, 'r')
                for i in f:
                    f.readline()
                    # do some operations to the input line
                    # do pattern matching
                    # insert into data base for further analysis
                f.close()
                self.progressBar.setValue(self.progressBar.value() + v)
            self.analysis.setTabEnabled(1, True)
            self.analysis.setTabEnabled(2, True)
            self.loaded = True
        else:
            self.message.setText("please specifiy a file to load or a directory")
            self.message.show()

    def switch1(self):  # functions switch1 and switch 2 disables the objects of GUI accoridng to radiobuttons
        self.lineEdit_2.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.lineEdit.setDisabled(False)
        self.pushButton_2.setDisabled(False)

    def switch2(self):
        self.lineEdit.setDisabled(True)
        self.pushButton_2.setDisabled(True)
        self.lineEdit_2.setDisabled(False)
        self.pushButton_3.setDisabled(False)

    def about(self):  # displays the about message if the user selected it from main menu
        self.message.setText(
            "this is a graduation project as a requirment for PSUT \n for more info visit the github link below")
        self.message.setDetailedText("https://github.com/ahmadjd94/BRO-IDS-Log-files-visualizer-and-analyzer")
        self.message.show()

    def openFile(self):  # function used to open files (single files and files inside working directory )
        self.label.setVisible(False)
        try:

            path = self.lineEdit.text().split('/')
            name = path[len(path) - 1]
            if name in self.valid or ".log" in name:
                file = open(self.lineEdit.text())
                print(file)
                self.count = 0
                for i in file:
                    self.linesCount += 1
                self.label.setText("the selected file has " + str(self.count) + " lines")
                self.label.setVisible(True)
                file.close()
            else:
                self.message.setText("make sure you selected a valid file")
                self.message.show()
                self.lineEdit.clear()
        except FileNotFoundError:  # handling incorrect file directories / paths
            self.label.show()

    def openFileDialog(self):  # displays open file dialog for user to select the required log file

        fname = QFileDialog.getOpenFileName(None, 'Open file', '/home', '*.log')  # error in params
        print(fname)
        self.lineEdit.setText(fname[0])
        try:
            file = open(fname[0])
            count = 0
            for i in file:
                count += 1
            self.label.setText("the selected file has " + str(count) + " lines")
            self.label.setVisible(True)
            self.lineEdit.setText(fname[0])
        except FileNotFoundError:
            self.label.show()

    def openDirDialog(self):
        try:
            di = QFileDialog.getExistingDirectory(None, 'open dir of log files', '/home',
                                                  QFileDialog.ShowDirsOnly)  # error in params
            print(di)
            os.chdir(di)  # change current working directory
            files = (os.listdir())  # make a list of files inside current working dir
            for each in files:
                if fnmatch.fnmatch(each, "*.log") or each in self.valid:
                    print(each)
                    self.validFiles.append(each)
            self.label.setText(
                "the directory you have selected have " + str(len(self.validFiles)) + " files seem to be valid ")
            self.lineEdit_2.setText(di)
        except NotADirectoryError:  # exception raised if the selection was not a dir
            self.label.setText("make sure you are entering a dir")
        except:
            self.label.setText("make sure you have selected a directory")
        finally:
            self.label.show()

    def reset(self):  # this function resets gui components if user tried to reload files
        self.progressBar.setValue(0)
        self.analysis.setTabEnabled(1, False)
        # reset timeline


if __name__ == "__main__":  # main module
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    try:
        con = sqlite3.connect('analyze.db')  # initializing connection to DB // should be in UI init ??
        try:
            con.execute("drop table analysis")
        except:
            raise Exception
            print("table doest exist")

        finally:
            con.execute("""create table analysis ( time text, UID text,SIP text, SP text,DIP text,
                                    DP text,protype text,service text,duration text, origin text, response text,connState text ,localOrig text ,localResp text,
                                    missedBytes text,history text ,origPkts text ,origIPBytes text ,respPkts text ,
                                    respIPBytes text,tunnelParents)""")

        """create a table for analysizing the log file : time , source IP ,source Port,Destination IP , Destination port , protocol in use,count of packets use"""

        ##############################IMPORT DATABASE DATATYPES NEED FURTHER CHECKING ##############################################################
    except:
        ui.__message2__.show()

    sys.exit(app.exec_())
