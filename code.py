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
import json


class Ui_MainWindow(object):  # Qt and PYUIC creator generated functions and classes
    ################################  defining global variable ###################################
    global con  # connection to DB
    linesCount = 0  # count of lines
    loaded = False  # this variable stores if there is a file loaded into program or not
    validFiles = []
    valid = ['conn', 'dhcp', 'dns', 'ftp', 'http', 'irc',
             'smtp','ssl', 'files','signatures','weird']

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
    def traverse(self,fname):

        f=open(fname+'.log','r')
        for i in f:
            if i[0]=="#":
                if i[:7]=="#fields" or "Fields" :
                    fields=(i[7:].split())
                    for field in fields:
                        validFields[fname][field]=fields.index(field)
                else:
                    continue
            else:
                line = i.split()

                if fname == 'http' or fname=="HTTP":  #no hardcoded indecies of fields  / PYTHON HAS NO SWITCH SYNTAX SO ....
                    con.execute("insert into main (%s)"%line[validFields['http']['uid']])
                    con.execute("insert into main (%s)" % line[validFields['http']['ts']])
                    con.execute("""insert into http (%s,%d,%d,%s,%s,%s,%s,%s,%d,%d,%s,%d,%s,%s,%s,
                                            %s,%s,%s,%s,%s,
                                            %s)"""
                                %(line [validFields['http']['UID']]
                                , int(line[validFields["http"]['ID']])
                                , int(line[validFields["http"]["TRANS_DEPTH"]])
                                , line[validFields['http']['METHOD']]
                                , line[validFields["http"]['HOST']]
                                , line[validFields['http']['URI']]
                                , line[validFields["http"]["REFERRER"]]
                                , line[validFields['http']['USER_AGENT']]
                                , int(line[validFields["http"]["REQUEST_BODY_LEN"]])
                                , int (validFields["HTTP"]["STATUS_CODE"])
                                , line[validFields["http"]["STATUS_MSG"]]
                                , int(line[validFields["http"]["INFO_CODE"]])
                                , line[validFields['http']['INFO_MSG']]
                                , line[validFields["http"]["TAGS"]]
                                , line[validFields['http']['USERNAME']]
                                , line[validFields["http"]["PASSWORD"]]
                                , line[validFields["http"]['PROXIED']]
                                , line[validFields['http']["ORIG_FUIDS"]]
                                , line[validFields["http"]['ORIG_MEME_TYPES']]
                                , line[validFields["http"]['ORIG_FUID']]
                                , line[validFields["http"]['RESP_MEME_TY']]
                                ))

                if fname == 'ftp' or fname=="FTP":  # no hardcoded indecies of fields
                    con.execute("insert into main (%s)" % line[validFields['ftp']['uid']])
                    con.execute("insert into main (%s)" % line[validFields['ftp']['ts']])
                    con.execute("""insert into ftp (%s,%s,%s,%s,%s,%d,%d,%s,%s,%s)"""
                                % ( line[validFields['ftp']['user']]
                                   , line[validFields["ftp"]['PASSWORD']]
                                   , line[validFields["ftp"]["COMMAND"]]
                                   , line[validFields['ftp']['ARG']]
                                   , line[validFields["ftp"]['MIME_TYPE']]
                                   , int(line[validFields['ftp']['FILE_SIZE']])
                                   , int(line[validFields["ftp"]["REPLY_CODE"]])
                                   , line[validFields['ftp']['REPLY_MSG']]
                                   , line[validFields["ftp"]["DATA_CHANNEL"]]
                                   , line[validFields["ftp"]["FUID"]]
                                   ))

                if fname == 'irc'or fname=="IRC":   # no hardcoded indecies of fields
                    con.execute("insert into main (%s)" % line[validFields['irc']['uid']])
                    con.execute("insert into main (%s)" % line[validFields['irc']['ts']])
                    con.execute("""insert into irc (%d,%s,%s,%s,%s,%s,%s,%d,%s,%s)"""
                                    % (int(line[validFields['irc']['ID']])
                                       , line[validFields["irc"]['NICK']]
                                       , line[validFields["irc"]["USER"]]
                                       , line[validFields['irc']['COMMAND']]
                                       , line[validFields["irc"]['VALUE']]
                                       , (line[validFields['irc']['ADDI']])
                                       , line[validFields["irc"]["DCC_FILE_NAME"]]
                                       , int(line[validFields['irc']['DCC_FILE_SIZE']])
                                       ,line[validFields['irs']['DCC_FILE_TYPE']]
                                       , line[validFields["irc"]["FUID"]]
                                       )
                                    )

                if fname == 'conn'or fname=="CONN":  # no hardcoded indecies of fields
                    con.execute("insert into main (%s)" % line[validFields['conn']['uid']])
                    con.execute("insert into main (%s)" % line[validFields['conn']['ts']])
                    con.execute("""insert into conn (%s,%s,%d,%s,%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d,%d,%d,%s,%s,%s)"""
                                    % ((line[validFields['CONN']['uid']])
                                       , line[validFields["CONN"]['ID_ORIG_H']]
                                       , int(line[validFields["CONN"]["ID_ORIG_P"]])
                                       , line[validFields['CONN']['ID_RESP_H']]
                                       , int(line[validFields["CONN"]['RESP_P']])
                                       , (line[validFields['CONN']['PROTO']])
                                       , line[validFields["CONN"]["SERVICE"]]
                                       , (line[validFields['CONN']['DURATION']])
                                       , line[validFields['CONN']['ORIG_BYTES']]
                                       , line[validFields["CONN"]["RESP_BYTES"]]
                                       ,line[validFields["CONN"]["CONN_STATE"]]
                                       ,line[validFields["CONN"]["LOCAL_ORIG"]]
                                       ,line[validFields["CONN"]["MISSED_BYTES"]]
                                       ,line[validFields["CONN"]["HISTORY"]]
                                       ,line[validFields["CONN"]["ORIG_PKTS"]]
                                       ,int(line[validFields["CONN"]["ORIG_IP_BYTES"]])
                                       ,int(line[validFields["CONN"]["RESP_PKTS"]])
                                       ,int(line[validFields["CONN"]["RESP_IP_BYTES"]])
                                       ,line[validFields["CONN"]["TUNNEL_PARENTS"]]
                                       ,line[validFields["CONN"]["ORIG_CC"]]
                                       ,line[validFields["CONN"]["RESP_CC"]]
                                       )
                                    )

                if fname == 'signature' or fname=="SIGNATURE":  # no hardcoded indecies of fields
                    con.execute("insert into main (%s)" % line[validFields['irc']['uid']])
                    con.execute("insert into main (%s)" % line[validFields['irc']['ts']])
                    con.execute("""insert into signature (%s,%s,%d,%s,%d,%s,%s,%s,%s,%d,%d)"""
                                % (int(line[validFields['signature']['ts']])
                                   , line[validFields["signature"]['SRC_ADDR']]
                                   , int(line[validFields["signature"]["SRC_PORT"]])
                                   , line[validFields['signature']['DST_ADDR']]
                                   , int(line[validFields["signature"]['DST_PORT']])
                                   , (line[validFields['signature']['NOTE']])
                                   , line[validFields["signature"]["SIG_ID"]]
                                   , (line[validFields['signature']['EVENT_MSG']])
                                   , line[validFields['signature']['SUB_MSG']]
                                   , int(line[validFields["signature"]["SIG_COUNT"]])
                                   , int(line[validFields["signature"]["host_COUNT"]])
                                   )
                                )

                if fname == 'dns' or fname== "DNS":  # no hardcoded indecies of fields
                    con.execute("insert into main (%s)" % line[validFields['dns']['uid']])
                    con.execute("insert into main (%s)" % line[validFields['dns']['ts']])
                    con.execute(
                            """insert into dns (%s,%s,%s,%d,%s,%d,%s,%d,%s,%d,%s,%d,%d,%d,%d,%d,%d,%s,%s,%d)"""
                            % ((line[validFields['DNS']['UID']])
                               , line[validFields["DNS"]['ID']]
                               , (line[validFields["DNS"]["PROTO"]])
                               , int(line[validFields['DNS']['TRANS_ID']])
                               , (line[validFields["DNS"]['QUERY']])
                               , int((line[validFields['DNS']['QCLASS']]))
                               , line[validFields["DNS"]["QCLASS_NAME"]]
                               , int(line[validFields["DNS"]["QTYPE"]])
                               , line[validFields["DNS"]["QTYPE_NAME"]]
                               , int((line[validFields['DNS']['RCODE']]))
                               , line[validFields['DNS']['RCODE_NAME']]
                               , int(line[validFields["DNS"]["QR"]])
                               , int(line[validFields["DNS"]["AA"]])
                               , int(line[validFields["DNS"]["TC"]])
                               , int(line[validFields["DNS"]["RD"]])
                               , int(line[validFields["DNS"]["RA"]])
                               , int(line[validFields["DNS"]["Z"]])
                               , (line[validFields["DNS"]["ANSWERS"]])
                               , (line[validFields["DNS"]["TTLS"]])
                               , int(line[validFields["DNS"]["REJECTED"]])
                               )
                            )

                if fname == 'SSH' or fname=="ssh":  # no hardcoded indecies of fields
                    con.execute("insert into main (%s)" % line[validFields['SSH']['uid']])
                    con.execute("insert into main (%s)" % line[validFields['SSH']['ts']])
                    con.execute(
                        """insert into dns (%s,%s,%s,%s,%s,%s,%d)"""
                        % ((line[validFields['SSH']['UID']])
                           , line[validFields["SSH"]['ID']]
                           , (line[validFields["SSH"]["STATUS"]])
                           , (line[validFields['SSH']['DIRECTION']])
                           , (line[validFields["SSH"]['CLIENT']])
                           , line[validFields['SSH']['SERVER']]
                           , int(line[validFields["SSH"]["RESP_SIZE"]])
                           )
                    )

                if fname == 'SSL' or fname=="ssl":  # no hardcoded indecies of fields
                    con.execute("insert into main (%s)" % line[validFields['SSL']['uid']])
                    con.execute("insert into main (%s)" % line[validFields['SSL']['ts']])
                    con.execute(
                            """insert into SSL (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                            % ((line[validFields['SSL']['UID']])
                               , line[validFields["SSL"]['ID']]
                               , (line[validFields["SSL"]["VERSION"]])
                               , (line[validFields['SSL']['CIPHER']])
                               , (line[validFields["SSL"]['SERVER_NAME']])
                               , line[validFields['SSL']['SESSIONS_ID']]
                               , (line[validFields["SSL"]["SUBJECT"]])
                               ,(line[validFields["SSL"]["ISSUER_SUBJECT"]])
                               ,(line[validFields["SSL"]["NOT_VALID_BEFORE"]])
                               ,(line[validFields["SSL"]["NOT_VALID_AFTER"]])
                               ,(line[validFields["SSL"]["LAST_ALERT"]])
                               ,(line[validFields["SSL"]["CLEINT_SUBJECT"]])
                               ,(line[validFields["SSL"]["CLNT_ISSUER_SUBJECT"]])
                               ,(line[validFields["SSL"]["CERT_HASH"]])
                               ,(line[validFields["SSL"]["VALIDATION_STATUS"]])

                               )
                        )
                if fname == 'SMTP' or fname=="smtp":  # no hardcoded indecies of fields
                    con.execute("insert into main (%s)" % line[validFields['SSL']['uid']])
                    con.execute("insert into main (%s)" % line[validFields['SSL']['ts']])
                    con.execute(
                        """insert into SMTP (%s,%s,%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                        % ((line[validFields['SMTP']['UID']]
                           , line[validFields["SMTP"]['ID']]
                           , line[validFields["SMTP"]["TRANS_DEPTH"]]
                           , line[validFields['SMTP']['HELO']]
                           , line[validFields["SMTP"]['MAILFROM']]
                           , line[validFields['SMTP']['RCPTTO']]
                           , line[validFields["SMTP"]["DATE"]]
                           , line[validFields["SMTP"]["FROM"]]
                           , line[validFields["SMTP"]["TO"]]
                           , line[validFields["SMTP"]["REPLY_TP"]]
                           , line[validFields["SMTP"]["MSG_ID"]]
                           , line[validFields["SMTP"]["IN_REPLY_TO"]]
                           , line[validFields["SMTP"]["SUBJECT"]]
                           , line[validFields["SMTP"]["X_ORIGINATING_IP"]]
                           , line[validFields["SMTP"]["FIRST_RECEIVED"]]
                           ,line[validFields["SMTP"]["SECOND_RECEIVED"]]
                           ,line[validFields["SMTP"]["LAST_REPLY"]]
                           ,line[validFields["SMTP"]["PATH"]]
                           ,line[validFields["SMTP"]["USER_AGENT"]]
                           ,line[validFields["SMTP"]["TLS"]]
                           ,line[validFields["SMTP"]["FUID"]]
                           ,line[validFields["SMTP"]["IS_WEBMAIL"]]

                           )
                    )

    def executeSQL(self):
        command = self.textEdit.toPlainText().lower()
        s = False
        try:
            if "select" in command:
                s = True
                result = con.execute(command).fetchall()
                for i in result:
                    for each in i:
                        pass
                        # this lines should insert the result of select statments into the tableview

            if "insert" in command:

                con.execute(command)
            else:
                con.execute(command)
                self.label_2.setStyleSheet("color: green")
                self.label_2.setText("operation succeded")
                self.label_2.show()

        except sqlite3.OperationalError as err:
            print(str(err))

            if s:
                self.message.setText("error selecting rows from data base")

            else:
                self.message.setText("error inserting rows into database")

            self.message.setDetailedText(str(err))
            self.label_2.setText("error executing SQL command")
            self.label_2.setStyleSheet("color : red")
            self.label_2.setVisible(True)
            self.message.show()

        except:

            self.message.show()

    def load(self):  # this function loads the content of the log files into the DB

        # this function should use regex to find and match patterns from log files
        timeIndex = uidIndex = sipIndex = spIndex = dipIndex = dpIndex = protoIndex = serviceIndex = durationIndex = countOriginBytesIndex = countResponseBytesIndex = 0
        connStateIndex = localOrig = localResp = missedBytes = history = origPkts = origIPBytes = respPkts = respIPBytes = tunnelParents = 0

        if self.loaded:
            reply = QMessageBox.question(self.message, 'Message',
                                         "there is files already loaded into databse ,are you sure you want to load files",
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
                    #enable files discovery and fields detections

            """ elif inpu[0][0] != "#":
                    print("dfgh")
                    print(inpu,'\n', each)
                    con.execute("")

                else:  # lines that begin with # denote comment lines

                    try:

                        # brace yourself for the longest sql line ever
                        #sql code that insert records in
                        # con.execute("insert into analysis values("+str(inpu[timeIndex])+","+str(inpu[uidIndex])+","+str(inpu[sipIndex])+","+str(inpu[spIndex])+","+str(inpu[dipIndex])+","+str(inpu[dpIndex])+","+str(inpu[protoIndex])+","+str(inpu[serviceIndex])+","+str(inpu[durationIndex])+","+str(inpu[countOriginBytesIndex])+","+str(inpu[countResponseBytesIndex])+")")
                    except:
                        self.message.setText("make sure you have previliges to execute command over data base \n")
                        # insert into data base for further analysis
                        # do some operations to the input line
                        # do pattern matching

                self.progressBar.setValue((i / self.linesCount) * 100)
"""
            f.close()

        elif self.radioButton_2.isChecked() and self.lineEdit_2.text() != "":  # creating db tables will be moved here
            v = 100 / len(self.validFiles)
            for each in self.validFiles:
                eachIgnorecase= each
                if each == "ftp" or each == "FTP":   #DONE
                    con.execute("""CREATE TABLE FTP(UID TEXT,ID INT,USER TEXT,PASSWORD TEXT,COMMAND TEXT,ARG TEXT,
                    MIME_TYPE TEXT,FILE_SIZE INT,REPLY_CODE INT,REPLY_MSG TEXT,
                    DATA_CHANNEL BLOB,FUID TEXT,FOREIGN KEY (UID)REFERENCES MAIN(UID))""")
                    print("step3")

                if each == "dhcp" or each == "DCHP":
                    con.execute("""CREATE TABLE DHCP(UID TEXT ,ID INTEGER ,MAC TEXT, ASSIGNED_IP TEXT,LEASE_TIME TEXT
                    , TRANS_ID INT,FOREIGN KEY(UID) REFERENCES MAIN(UID) )""")
                    print("step2")

                if each == "irc" or each == "IRC": #DONE
                    con.execute("""CREATE TABLE IRC (UID TEXT,ID INT, NICK TEXT,USER TEXT,COMMAND TEXT,VALUE TEXT,ADDI TEXT,
                    DCC_FILE_NAME TEXT,DCC_FILE_SIZE INT,DCC_MIME_TYPE TEXT,FUID TEXT,FOREIGN KEY (UID) REFERENCES MAIN(UID))""")
                    print("step4")

                if each == "weird.log" or each == "WEIRD.log":
                    con.execute("""CREATE TABLE WEIRD(UID TEXT,ID INT ,NAME TEXT,
                    ADDI TEXT,NOTICE BOOL,PEER TEXT,FOREIGN KEY (UID) REFERENCES MAIN(UID))""")
                    print("step5")

                if each == "ssh.log" or each == "SSH.log": #DONE
                    con.execute("""CREATE TABLE SSH( UID TEXT,STATUS TEXT,
                    DIRECTION TEXT,CLIENT TEXT, SERVER TEXT,RESP_SIZE INT,FOREIGN KEY (UID) REFERENCES MAIN(UID))""")
                    print("step6")

                if each == "conn.log" or each == "CONN.log": #DONE
                    con.execute("""CREATE TABLE CONN(UID TEXT,ID_ORIG_H TEXT,ID_ORIG_P INT,ID_RESP_H TEXT,ID_RESP_P INT,PROTO TEXT,SERVICE TEXT,DURATION TIME,ORIG_BYTES INT,
                    RESP_BYTES INT,CONN_STATE TEXT,LOCAL_ORIG BOOL,MISSED_BYTES COUNT,HISTORY TEXT,ORIG_PKTS INT,ORIG_IP_BYTES INT,
                    RESP_PKTS INT,RESP_IP_BYTES INT,TUNNEL_PARENTS BLOB,ORIG_CC TEXT,RESP_CC TEXT,FOREIGN KEY (UID) REFERENCES MAIN(UID))""")
                    print("step7")

                if each == "http.log" or each == "HTTP.log":  #DONE
                    con.execute("""CREATE TABLE  HTTP (UID TEXT,
                                            ID INT,TRANS_DEPTH INT,METHOD TEXT,HOST TEXT,URI TEXT,REFERRER TEXT,
                                            USER_AGENT TEXT,REQUEST_BODY_LEN INT,
                                            STATUS_CODE INT,STATUS_MSG TEXT,INFO_CODE INT,INFO_MSG TEXT,TAGS TEXT,USERNAME TEXT,
                                            PASSWORD TEXT,PROXIED TEXT,
                                            ORIG_FUIDS TEXT,ORIG_MEME_TYPES TEXT,ORIG_FUID TEXT,
                                            RESP_MEME_TY BLOB,FOREIGN KEY  (UID) REFERENCES MAIN (UID))""")
                    print("step8")

                if each == "DNS.log" or each == "dns.log":   #DONE
                    con.execute("""CREATE TABLE DNS (UID TEXT,ID INT,PROTO TEXT,TRAN_ID INT,
                                            QUERY TEXT,QCLASS INT,QCLASS_NAME TEXT,QTYPE INT,QTYPE_NAME TEXT,RCODE INT,RCODE_NAME TEXT,QR BLOB,AA BOOL,TC BOOL,
                                            RD BOOL,RA BOOL,Z INT,ANSWERS BLOB,TTLS BLOB,REJECTED BOOL,FOREIGN KEY (UID) REFERENCES MAIN(UID))""")
                    print("step9")

                if each == "signatrue.log" or each == "SIGNATURE.log":  #DONE
                    con.execute("""CREATE TABLE SIGNATURE(TIMESTAMP TIME ,SRC_ADDR TEXT ,
                                SRC_PORT INT ,DST_ADR TEXT ,DST_PORT INT ,NOTE TEXT ,SIG_ID TEXT
                                EVENT_MSG TEXT ,SUB_MSG TEXT ,SIG_COUNT INT ,HOST_COUNT INT )""")
                    print("step10")

                if each == "SSL.log" or each == "ssl.log":  #DONE
                    con.execute("""CREATE TABLE SSL(UID TEXT,VERSION TEXT ,CIPHER TEXT ,
                    SERVER_NAME TEXT ,SESSION_ID TEXT ,SUBJECT TEXT ,
                    ISSUER_SUBJECT TEXT ,NOT_VALID_BEFORE TIME ,
                    LAST_ALERT TEXT ,CLIENT_SUBJECT TEXT ,CLNT_ISSUER_SUBJECT TEXT ,CERT_HASH TEXT ,VALIDATION_STATUS BLOB ,
                    FOREIGN KEY (UID)REFERENCES MAIN(UID))""")
                print("step11")

                if each == "FILES.log" or each == "files.log":
                    con.execute(
                        """CREATE TABLE FILES (TS TIME , FUID TEXT,tx_hosts TEXT,rx_hosts TEXT,CONN_UIDS,SOURCE TEXT ,DEPTH INT,
                            ANALYZERS TEXT,MIME_TYPE TEXT,
                            FILENAME TEXT,DURATION TIME,LOCAL_ORIG BOOL,IS_ORIG BOOL,SEEN_BYTES INT,TOTAL_BYTES INT ,
                            MISSING_BYTES INT,OVERFLOW_BYTES INT,TIMEDOUT INT,PARENT_FUID STRING,
                            MD5A_SHA1_SHA256 TEXT,EXTRACTED BOOL)""")

                if each == "smtp.log" or each == "SMTP.log":
                    con.execute("""CREATE TABLE SMTP (uid TEXT ,id INT,trans_depth INT ,helo TEXT,mailfrom STRING,rcptto BLOB
              ,date TEXT ,from TEXT ,to BLOB,reply_to TEXT,msg_id TEXT ,in_reply_to TEXT ,subject TEXT
              ,x_originating_ip TEXT,first_received TEXT ,
            second_received TEXT ,last_reply TEXT ,path BLOB,user_agent TEXT ,
            tls BOOL,fuids BLOB,is_webmail BOOL , FOREIGN KEY (UID) REFERENCES  MAIN(UID))""")

               #function moved to top#
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
        self.message.setDetailedText(
            "https://bitbucket.org/Psut/bro-ids-log-files-visualizer-and-analyzer")  ####################3333
        self.message.show()

    def openFile(self):  # function used to open files (single files and files inside working directory )
        self.label.setVisible(False)
        try:

            path = self.lineEdit.text().split('/')
            name = path[len(path) - 1]
            if name in self.valid:
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
        except:  # handling incorrect file directories / paths
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
            dire = QFileDialog.getExistingDirectory(None, 'open dir of log files', '/home',
                                                    QFileDialog.ShowDirsOnly)  # error in params
            print(dire)
            os.chdir(dire)  # change current working directory
            files = (os.listdir())  # make a list of files inside current working dir
            for each in files:
                if each in self.valid:
                    print(each)
                    self.validFiles.append(each)  # appends BRO valid log files names to the discovered logs

            self.label.setText(
                "the directory you have selected have " + str(len(self.validFiles)) + " valid files")
            self.lineEdit_2.setText(dire)
        except  NotADirectoryError as e:  # exception raised if the selection was not a dir
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

    UnsupportedFiles=['x509.log','packet_filter.log','app_stats.log','capture_loss.log','dnp3.log','intel.log',
                      'known_certs.log','radius.log','modbus.log','notice.log','reporter.log',
                      'notice.log','software.log','snmp.log','socks.log',
                      'syslog.log','traceroute.log','known_hosts.log']
    validFields = {
    "http" :{'UID': -1,'TS':-1, "ID": -1, "TRANS_DEPTH": -1, "METHOD": -1, "HOST":-1, "URI": -1, "REFERRER": -1,
            "USER_AGENT": -1, "REQUEST_BODY_LEN": -1,"STATUS_CODE":-1, "STATUS_MSG":-1, "INFO_CODE":-1, "INFO_MSG":-1,
             "TAGS": -1, "USERNAME":-1,"PASSWORD":-1, "PROXIED":-1,"ORIG_FUIDS":-1, "ORIG_MEME_TYPES":-1, "ORIG_FUID":-1,
            "RESP_MEME_TY":-1},  # this dictionary will store the indecies of lof fileds for each file

    'ftp' :{"UID": 0, "TS": 0, "ID": 0, "USER": 0, "PASSWORD": 0, "COMMAND": 0, "ARG": 0,
           "MIME_TYPE": 0, "FILE_SIZE": 0, "REPLY_CODE": 0, "REPLY_MSG": 0,
           "DATA_CHANNEL": 0, "FUID": 0},

    "files": {"TS": 0, "FUID": 0, "tx_hosts": 0, "rx_hosts": 0, "CONN_UIDS": 0, "SOURCE": 0, "DEPTH": 0,
             "ANALYZERS": 0, "MIME_TYPE": 0,
             "FILENAME": 0, "DURATION": 0, "LOCAL_ORIG": 0, "IS_ORIG": 0, "SEEN_BYTES": 0, "TOTAL_BYTES": 0,
             "MISSING_BYTES": 0, "OVERFLOW_BYTES": 0, "TIMEDOUT": 0, "PARENT_FUID": 0,
             "MD5A/SHA1/SHA256": 0, "EXTRACTED": 0} , # CHECK THIS AGAIN

    'irc' : {"UID": -1,'TS':-1, "ID": -1, "NICK": -1, "USER": -1, "COMMAND": -1, "VALUE": -1, "ADDI": -1,
           "DCC_FILE_NAME": -1, "DCC_FILE_SIZE": -1, "DCC_MIME_TYPE": -1, "FUID": 1},

    'smtp' : {'ts': 0, 'uid': 0, 'id': 0, 'trans_depth': 0, "helo": 0, "mailfrom": -1, "rcptto": 0
        , "date": 0, "from": 0, "to": 0, "reply_to": 0, "msg_id": 0, "in_reply_to": 0, "subject": 0
        , "x_originating_ip": 0, "first_received": 0,
            "second_received": 0, "last_reply": 0, "path": 0, "user_agent": 0,
            "tls": 0, "fuids": 0, "is_webmail": 0},

    'ssh' : {"UID": 0, "STATUS": 0, "DIRECTION": 0, "CLIENT": 0, "SERVER": 0, "RESP_SIZE": 0},

    'ssl' : {"UID": 0, "VERSION": 0, "CIPHER": 0,
           "SERVER_NAME": 0, "SESSION_ID": 0, "SUBJECT": 0,
           "ISSUER_SUBJECT": 0, "NOT_VALID_BEFORE": 0,
           "LAST_ALERT": 0, "CLIENT_SUBJECT": 0, "CLNT_ISSUER_SUBJECT": 0, "CERT_HASH": 0, "VALIDATION_STATUS": 0},

    'weird' :{"UID": 0, "ID": 0, "NAME": 0, "ADDI": 0, "NOTICE": 0, "PEER": 0},

    'signatures':{"sss":0},

    'conn':{"UID": 0, "ID_ORIG_H": 0, "ID_ORIG_P": 0, "ID_RESP_H": 0, "ID_RESP_P": 0, "PROTO": 0, "SERVICE": 0,
            "DURATION": 0, "ORIG_BYTES": 0,
            "RESP_BYTES": 0, "CONN_STATE": 0, "LOCAL_ORIG": 0, "MISSED_BYTES": 0, "HISTORY": 0, "ORIG_PKTS": 0,
            "ORIG_IP_BYTES": 0,"RESP_PKTS": 0, "RESP_IP_BYTES": 0, "TUNNEL_PARENTS": 0, "ORIG_CC": 0, "RESP_CC": 0},

    'dhcp':{"UID": 0, "ID": 0, "MAC": 0, "ASSIGNED_IP": 0, "LEASE_TIME ": 0, "TRANS_ID": 0},

    'dns':{"UID": 0, 'ts': 0, "ID": 0, "PROTO": 0, "TRAN_ID": 0,
           "QUERY": 0, "QCLASS": 0, "QCLASS_NAME": 0, "QTYPE": 0, "QTYPE_NAME": 0, "RCODE": 0, "RCODE_NAME": 0, "QR": 0,
           "AA": 0,"TC": 0, "RD": 0, "RA": 0, "Z": 0, "ANSWERS": 0, "TTLS": 0, "REJECTED BOOL": 0}
    }

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    try:

        con = sqlite3.connect('analyze2.db')  # initializing connection to DB // should be in UI init ??
        print("connected")

        try:
            con.execute("DROP TABLE main")  # 1
            con.execute("DROP TABLE DHCP")  # 2
            con.execute("DROP TABLE SMTP")  # 3
            con.execute("DROP TABLE irc")  # 4
            con.execute("DROP TABLE weird")  # 5
            con.execute("DROP TABLE ssh")  # 6
            con.execute("DROP TABLE conn")  # 7
            con.execute("DROP TABLE http")  # 8
            con.execute("DROP TABLE dns")  # 9
            con.execute("DROP TABLE signature")  # 10
            con.execute("DROP TABLE ssl")  # 11
            con.execute("DROP TABLE IDS")  # 12
            con.execute("DROP TABLE files")  # 13

        except:
            print("table doest exist")

        finally:
            print("final")
            con.execute("""CREATE TABLE MAIN( UID TEXT PRIMARY KEY, TIMESTAMP TIME )""")
            # con.execute("CREATE TABLE IDS ()")
            print("step1")

        """create a table for analysizing the log file : time , source IP ,source Port,Destination IP , Destination port , protocol in use,count of packets use"""

        ##############################IMPORT DATABASE DATATYPES NEED FURTHER CHECKING ##############################################################
    except sqlite3.Error as e:
        print(e)
        print("error")

        ui.__message2__.show()

    sys.exit(app.exec_())
