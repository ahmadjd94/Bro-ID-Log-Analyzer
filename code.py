# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!
"""project's backlog : https://tree.taiga.io/project/ahmadjd94-bila """

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication, QMessageBox)
from PyQt5.QtGui import QIcon
import sqlite3
import os  # module used for changing Current working directory of the program
import fnmatch  # module used for matching files names
# import pyqtgraph as pg
import hashlib
import codecs


class Ui_MainWindow(object):  # Qt and PYUIC creator generated functions and classes

    ################################  defining global variable ###################################
    global line  # this line will strore
    global con  # connection to DB
    single = False  # indicates if user is dealing with a signle file / DIR
    linesCount = 0  # count of lines
    loaded = False  # this variable stores if there is a file loaded into program or not
    validFiles = []  # this list stores the valid file found in a DIR

    valid = ['conn.log', 'dhcp.log', 'dns.log', 'ftp.log', 'http.log', 'irc.log',
             'smtp.log', 'ssl.log', 'files.log', 'signatures.log', 'weird.log',
             'ssh.log']  # this list stores the valid log files bila can deal with

    UnsupportedFiles = ['x509.log', 'packet_filter.log', 'app_stats.log', 'capture_loss.log', 'dnp3.log', 'intel.log',
                        'known_certs.log', 'radius.log', 'modbus.log', 'notice.log', 'reporter.log',
                        'notice.log', 'software.log', 'snmp.log', 'socks.log',
                        'syslog.log', 'traceroute.log',
                        'known_hosts.log']  # SHOW MESSAGE WHEN AN UNSUPPORTED FILE IS LOADED

    # END OF GLOVAL VARIABLES DEFENITION
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
        self.progressBar.setStyleSheet("background-color:#333333")
        self.analysis.setStyleSheet("background-color:#333333")
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
        self.tab_3.setStyleSheet("background-color:#333333")
        self.tab_2.setStyleSheet("background-color:#333333")
        self.tab.setStyleSheet("background-color:#333333")
        self.menuBar.setStyleSheet("background-color:#333333")
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

        # creating db tables will be moved here

    def tableCreator(self, fname):  # this function creates tables based on the fname argument

        if fname == "ftp.log":  # DONE
            try:
                con.execute("""CREATE TABLE FTP(UID TEXT,ID INT,USER TEXT,PASSWORD TEXT,COMMAND TEXT,ARG TEXT,
                MIME_TYPE TEXT,FILE_SIZE INT,REPLY_CODE INT,REPLY_MSG TEXT,
                DATA_CHANNEL BLOB,FUID TEXT,FOREIGN KEY (UID)REFERENCES MAIN(UID))""")
                print("step3")
                return True
            except:
                return False

        elif fname == "dhcp.log":  # DONE
            try:
                con.execute("""CREATE TABLE DHCP(UID TEXT ,ID INTEGER ,MAC TEXT, ASSIGNED_IP TEXT,LEASE_TIME TEXT
                , TRANS_ID INT,FOREIGN KEY(UID) REFERENCES MAIN(UID) )""")
                print("step2")
                return True
            except:
                return 0

        elif fname == "irc.log":  # DONE
            try:
                con.execute("""CREATE TABLE IRC (UID TEXT,ID INT, NICK TEXT,USER TEXT,COMMAND TEXT,VALUE TEXT,ADDI TEXT,
                DCC_FILE_NAME TEXT,DCC_FILE_SIZE INT,DCC_MIME_TYPE TEXT,FUID TEXT,FOREIGN KEY (UID) REFERENCES MAIN(UID))""")
                print("step4")
                return True
            except:
                return False

        elif fname == "weird.log":  # DONE
            try:
                con.execute("CREATE TABLE WEIRD(UID TEXT,ID INT ,NAME TEXT,"
                            "ADDI TEXT,NOTICE BOOL,PEER TEXT,FOREIGN KEY (UID) REFERENCES MAIN(UID))")
                print("step5")
            except:
                return False

        elif fname == "ssh.log":  # DONE
            try:
                con.execute("""CREATE TABLE SSH( UID TEXT,STATUS TEXT,
                DIRECTION TEXT,CLIENT TEXT, SERVER TEXT,RESP_SIZE INT,FOREIGN KEY (UID) REFERENCES MAIN(UID))""")
                print("step6")
                return True
            except:
                return False

        elif fname == "conn.log":  # DONE
            try:
                con.execute("""CREATE TABLE CONN(UID TEXT,id_orig_h TEXT,id_orig_p INT,ID_RESP_H TEXT,ID_RESP_P INT,PROTO TEXT,SERVICE TEXT,DURATION TIME,ORIG_BYTES INT,
                RESP_BYTES INT,CONN_STATE TEXT,LOCAL_ORIG BOOL,MISSED_BYTES COUNT,HISTORY TEXT,ORIG_PKTS INT,ORIG_IP_BYTES INT,
                RESP_PKTS INT,RESP_IP_BYTES INT,TUNNEL_PARENTS BLOB,ORIG_CC TEXT,RESP_CC TEXT,FOREIGN KEY (UID) REFERENCES MAIN(UID))""")
                print("step7")
                return True
            except:
                return False

        elif fname == "http.log":  # DONE
            try:
                con.execute("""CREATE TABLE  HTTP (UID TEXT,
                                        ID INT,TRANS_DEPTH INT,METHOD TEXT,HOST TEXT,URI TEXT,REFERRER TEXT,
                                        USER_AGENT TEXT,REQUEST_BODY_LEN INT,
                                        STATUS_CODE INT,STATUS_MSG TEXT,INFO_CODE INT,INFO_MSG TEXT,TAGS TEXT,USERNAME TEXT,
                                        PASSWORD TEXT,PROXIED TEXT,
                                        ORIG_FUIDS TEXT,ORIG_MEME_TYPES TEXT,ORIG_FUID TEXT,
                                        RESP_MEME_TY BLOB,FOREIGN KEY  (UID) REFERENCES MAIN (UID))""")
                print("step8")
            except:
                return False
        elif fname == "dns.log":  # DONE
            try:
                con.execute("""CREATE TABLE DNS (UID TEXT,ID INT,PROTO TEXT,TRAN_ID INT,
                                        QUERY TEXT,QCLASS INT,QCLASS_NAME TEXT,QTYPE INT,QTYPE_NAME TEXT,RCODE INT,RCODE_NAME TEXT,QR BLOB,AA BOOL,TC BOOL,
                                        RD BOOL,RA BOOL,Z INT,ANSWERS BLOB,TTLS BLOB,REJECTED BOOL,FOREIGN KEY (UID) REFERENCES MAIN(UID))""")
                print("step9")
            except:
                return False

        elif fname == "signature.log":  # DONE
            try:
                con.execute("""CREATE TABLE SIGNATURE(TIMESTAMP TIME ,SRC_ADDR TEXT ,
                            SRC_PORT INT ,DST_ADR TEXT ,DST_PORT INT ,NOTE TEXT ,SIG_ID TEXT
                            EVENT_MSG TEXT ,SUB_MSG TEXT ,SIG_COUNT INT ,HOST_COUNT INT )""")
                print("step10")
                return True
            except:
                return False

        elif fname == "ssl.log":  # DONE
            try:
                con.execute("""CREATE TABLE SSL(UID TEXT,VERSION TEXT ,CIPHER TEXT ,
                SERVER_NAME TEXT ,SESSION_ID TEXT ,SUBJECT TEXT ,
                ISSUER_SUBJECT TEXT ,NOT_VALID_BEFORE TIME ,
                LAST_ALERT TEXT ,CLIENT_SUBJECT TEXT ,CLNT_ISSUER_SUBJECT TEXT ,CERT_HASH TEXT ,VALIDATION_STATUS BLOB ,
                FOREIGN KEY (UID)REFERENCES MAIN(UID))""")
                print("step11")
                return True
            except:
                return False

        elif fname == "files.log":  # DONE
            try:
                con.execute(
                    """CREATE TABLE FILES (TS TIME , FUID TEXT,tx_hosts TEXT,rx_hosts TEXT,CONN_UIDS,SOURCE TEXT ,DEPTH INT,
                    ANALYZERS TEXT,MIME_TYPE TEXT,
                    FILENAME TEXT,DURATION TIME,LOCAL_ORIG BOOL,IS_ORIG BOOL,SEEN_BYTES INT,TOTAL_BYTES INT ,
                    MISSING_BYTES INT,OVERFLOW_BYTES INT,TIMEDOUT INT,PARENT_FUID STRING,
                    MD5A_SHA1_SHA256 TEXT,EXTRACTED BOOL)""")
            except:
                return False

        elif fname == "smtp.log":  # DONE
            try:
                con.execute("""CREATE TABLE SMTP (uid TEXT ,id INT,trans_depth INT ,helo TEXT,mailfrom STRING,rcptto BLOB
          ,date TEXT ,from TEXT ,to BLOB,reply_to TEXT,msg_id TEXT ,in_reply_to TEXT ,subject TEXT
          ,x_originating_ip TEXT,first_received TEXT ,
        second_received TEXT ,last_reply TEXT ,path BLOB,user_agent TEXT ,
        tls BOOL,fuids BLOB,is_webmail BOOL , FOREIGN KEY (UID) REFERENCES  MAIN(UID))""")
                return True
            except:
                return False

    def valuefilter(self, num):
        if num != -1:
            return True
        else:
            return False

    def SQLcreator(self, table):  # should use lambda expressions
        # THIS FUNCTION WILL RAISE AN EXCEPTION INCASE OF INVALID TABLE TYPE
        # HANDLED IN THE CALLER FUNCTION
        exist = list(filter(lambda x: validFields[table][x] > -1,
                            validFields[table]))  # problem : a UID of transaction may be used multiple time
        insert = "insert into %s (" % (table)
        fields = values = ""
        for i in exist:
            fields += i + ','
        fields = fields[:len(fields) - 1]  # this line will remove the colon at the end of fileds string
        for i in exist:
            values += line[validFields[table][i]]

    def traverse(self, fname):  # this function will traverse the file that is based to it
        # todo : major changes (inserting into DB should be dynamic , the function should insert fields according to their values
        # if the field value is -1 , the field should be neglected )
        print("traversing" + str(fname))
        print(type(fname))
        print(fname)
        progress = 0
        try:
            fname = (fname.split('.')[0])  # this statment splits the fname and neglects the .log part of it
            hashTemp = ""  # this variable stores the entire log file to calculate it's hash value
            f = open(fname + '.log', 'r')  # open the log file Read-Only mode

            for i in f:  # todo : modify function to increase the progress bar
                hashTemp += i  # concatenate the lines being read to the string

                if i[:7] == "#fields" or i[:7] == "Fields":  # field loading algorithm
                    print(i)
                    fields = (i[7:].split())
                    for field in fields:
                        if field in validFields[fname]:
                            validFields[fname][field] = fields.index(
                                field)  # this line stores the index of field in the dictionary
                        print(fields.index(field), field)

                    print("dfdsfds", validFields[fname])

                elif i[0] != "#":  # this line ignores the log lines that start with # , #indecates a commented line
                    line = i.split()
                    print(i)
                    # no hardcoded indecies of
                    # fields  / PYTHON HAS NO SWITCH SYNTAX SO we used if statments
                    # todo : the algorithm is not handling undefined fields , sprint's extended to thursday
                    if fname == 'http' or fname == "HTTP":  # this inserts the log data of http files into http table
                        try:
                            print(validFields["http"] + "printing fields")
                            con.execute("insert into main (%s)" % line[validFields['http']['uid']])
                            con.execute("insert into main (%s)" % line[validFields['http']['ts']])
                            con.execute("""insert into http (%s,%d,%d,%s,%s,%s,%s,%s,%d,%d,%s,%d,%s,%s,%s,
                                                        %s,%s,%s,%s,%s,
                                                        %s)"""
                                        % (line[validFields['http']['uid']]
                                           , int(line[validFields["http"]['id']])
                                           , int(line[validFields["http"]["trans_depth"]])
                                           , line[validFields['http']['method']]
                                           , line[validFields["http"]['host']]
                                           , line[validFields['http']['uri']]
                                           , line[validFields["http"]["referrer"]]
                                           , line[validFields['http']['user_agent']]
                                           , int(line[validFields["http"]["request_body_len"]])
                                           , int(validFields["http"]["status_code"])
                                           , line[validFields["http"]["status_msg"]]
                                           , int(line[validFields["http"]["info_code"]])
                                           , line[validFields['http']['info_msg']]
                                           , line[validFields["http"]["tags"]]
                                           , line[validFields['http']['username']]
                                           , line[validFields["http"]["password"]]
                                           , line[validFields["http"]['proxied']]
                                           , line[validFields['http']["orig_fuids"]]
                                           , line[validFields["http"]['orig_meme_types']]
                                           , line[validFields["http"]['orig_fuid']]
                                           , line[validFields["http"]['resp_meme_ty']]
                                           ))
                        except sqlite3.Error as http:  # exceptions renaming , cathcing sqlite3 exceptions
                            print(str(http))

                    if fname == 'ftp' or fname == "FTP":  # inserts data of ftp logs into ftp table
                        try:
                            con.execute("insert into main (%s)" % line[validFields['ftp']['uid']])
                            con.execute("insert into main (%s)" % line[validFields['ftp']['ts']])
                            con.execute("""insert into ftp (%s,%s,%s,%s,%s,%d,%d,%s,%s,%s)"""
                                        % (line[validFields['ftp']['user']]
                                           , line[validFields["ftp"]['password']]
                                           , line[validFields["ftp"]["command"]]
                                           , line[validFields['ftp']['arg']]
                                           , line[validFields["ftp"]['mime_type']]
                                           , int(line[validFields['ftp']['file_size']])
                                           , int(line[validFields["ftp"]["reply_code"]])
                                           , line[validFields['ftp']['reply_msg']]
                                           , line[validFields["ftp"]["data_channel"]]
                                           , line[validFields["ftp"]["fuid"]]
                                           ))
                        except sqlite3.Error as ftp:
                            print(str(ftp))

                    if fname == 'irc' or fname == "IRC":  # data into IRC table
                        try:
                            con.execute("insert into main (%s)" % line[validFields['irc']['uid']])
                            con.execute("insert into main (%s)" % line[validFields['irc']['ts']])
                            con.execute("""insert into irc (%d,%s,%s,%s,%s,%s,%s,%d,%s,%s)"""
                                        % (int(line[validFields['irc']['id']])
                                           , line[validFields["irc"]['nick']]
                                           , line[validFields["irc"]["user"]]
                                           , line[validFields['irc']['command']]
                                           , line[validFields["irc"]['value']]
                                           , (line[validFields['irc']['addi']])
                                           , line[validFields["irc"]["dcc_file_name"]]
                                           , int(line[validFields['irc']['dcc_file_size']])
                                           , line[validFields['irs']['dcc_file_type']]
                                           , line[validFields["irc"]["fuid"]]
                                           )
                                        )
                        except sqlite3.Error as irc:  # exception renaming
                            print(str(irc))

                    if fname == 'conn' or fname == "CONN":  # data into Conn table
                        try:
                            con.execute("insert into main (%s)" % line[validFields['conn']['uid']])
                            con.execute("insert into main (%s)" % line[validFields['conn']['ts']])
                            con.execute(
                                """insert into conn (%s,%s,%d,%s,%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d,%d,%d,%s,%s,%s)"""
                                % ((line[validFields['conn']['uid']])
                                   , line[validFields["conn"]['id_orig_h']]
                                   , int(line[validFields["conn"]["id_orig_p"]])
                                   , line[validFields['conn']['id_resp_h']]
                                   , int(line[validFields["conn"]['resp_p']])
                                   , (line[validFields['conn']['proto']])
                                   , line[validFields["conn"]["service"]]
                                   , (line[validFields['conn']['duration']])
                                   , line[validFields['conn']['orig_bytes']]
                                   , line[validFields["conn"]["resp_bytes"]]
                                   , line[validFields["conn"]["conn_state"]]
                                   , line[validFields["conn"]["local_orig"]]
                                   , line[validFields["conn"]["missed_bytes"]]
                                   , line[validFields["conn"]["history"]]
                                   , line[validFields["conn"]["orig_pkts"]]
                                   , int(line[validFields["conn"]["orig_ip_bytes"]])
                                   , int(line[validFields["conn"]["resp_pkts"]])
                                   , int(line[validFields["conn"]["resp_ip_bytes"]])
                                   , line[validFields["conn"]["tunnel_parents"]]
                                   , line[validFields["conn"]["orig_cc"]]
                                   , line[validFields["conn"]["resp_cc"]]
                                   )
                                )
                        except sqlite3.Error as conn:  # exception renaming
                            print(str(conn))

                    if fname == 'signature' or fname == "SIGNATURE":  # data into signatures table
                        try:
                            con.execute("insert into main (%s)" % line[validFields['irc']['uid']])
                            con.execute("insert into main (%s)" % line[validFields['irc']['ts']])
                            con.execute("""insert into signature (%s,%s,%d,%s,%d,%s,%s,%s,%s,%d,%d)"""
                                        % (int(line[validFields['signature']['ts']])
                                           , line[validFields["signature"]['src_addr']]
                                           , int(line[validFields["signature"]["src_port"]])
                                           , line[validFields['signature']['dst_addr']]
                                           , int(line[validFields["signature"]['dst_port']])
                                           , (line[validFields['signature']['note']])
                                           , line[validFields["signature"]["sig_id"]]
                                           , (line[validFields['signature']['event_msg']])
                                           , line[validFields['signature']['sub_msg']]
                                           , int(line[validFields["signature"]["sig_count"]])
                                           , int(line[validFields["signature"]["host_count"]])
                                           )
                                        )
                        except sqlite3.Error as sign:  # exception renaming
                            print(str(sign))

                    if fname == 'dns' or fname == "DNS":
                        try:
                            con.execute("INSERT INTO main (uid,ts) VALUES('test','test1')")
                            con.execute("insert into main(uid,ts) values(%s,%s)" % (
                            line[validFields['dns']['uid']], line[validFields['dns']['uid']]))
                            con.execute(
                                """insert into dns (%s,%s,%s,%d,%s,%d,%s,%d,%s,%d,%s,%d,%d,%d,%d,%d,%d,%s,%s,%d)"""
                                % ((line[validFields['dns']['uid']])
                                   , line[validFields["dns"]['id']]
                                   , (line[validFields["dns"]["proto"]])
                                   , int(line[validFields['dns']['trans_id']])
                                   , (line[validFields["dns"]['query']])
                                   , int((line[validFields['dns']['qclass']]))
                                   , line[validFields["dns"]["qclass_name"]]
                                   , int(line[validFields["dns"]["qtype"]])
                                   , line[validFields["dns"]["qtype_name"]]
                                   , int((line[validFields['dns']['rcode']]))
                                   , line[validFields['dns']['rcode_name']]
                                   , int(line[validFields["dns"]["qr"]])
                                   , int(line[validFields["dns"]["aa"]])
                                   , int(line[validFields["dns"]["tc"]])
                                   , int(line[validFields["dns"]["rd"]])
                                   , int(line[validFields["dns"]["ra"]])
                                   , int(line[validFields["dns"]["z"]])
                                   , (line[validFields["dns"]["answers"]])
                                   , (line[validFields["dns"]["ttls"]])
                                   , int(line[validFields["dns"]["rejected"]])
                                   )
                            )
                        except sqlite3.Error as dns:
                            print(str(dns))
                        except sqlite3.OperationalError as err:
                            print(str(err))
                    if fname == 'SSH' or fname == "ssh":  # data into ssh table
                        try:
                            con.execute("insert into main (%s)" % line[validFields['SSH']['uid']])
                            con.execute("insert into main (%s)" % line[validFields['SSH']['ts']])
                            con.execute(
                                """insert into dns (%s,%s,%s,%s,%s,%s,%d)"""
                                % ((line[validFields['ssh']['uid']])
                                   , line[validFields["ssh"]['id']]
                                   , (line[validFields["ssh"]["status"]])
                                   , (line[validFields['ssh']['direction']])
                                   , (line[validFields["ssh"]['client']])
                                   , line[validFields['ssh']['server']]
                                   , int(line[validFields["ssh"]["resp_size"]])
                                   )
                            )
                        except sqlite3.Error as ssh:
                            print(str(ssh))

                    if fname == 'SSL' or fname == "ssl":
                        try:
                            con.execute("insert into main (%s)" % line[validFields['ssl']['uid']])
                            con.execute("insert into main (%s)" % line[validFields['ssl']['ts']])
                            con.execute(
                                """insert into ssl (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                                % ((line[validFields['ssl']['uid']])
                                   , line[validFields["ssl"]['id']]
                                   , (line[validFields["ssl"]["version"]])
                                   , (line[validFields['ssl']['cipher']])
                                   , (line[validFields["ssl"]['server_name']])
                                   , line[validFields['ssl']['sessions_id']]
                                   , (line[validFields["ssl"]["subject"]])
                                   , (line[validFields["ssl"]["issuer_subject"]])
                                   , (line[validFields["ssl"]["not_valid_before"]])
                                   , (line[validFields["ssl"]["not_valid_after"]])
                                   , (line[validFields["ssl"]["last_alert"]])
                                   , (line[validFields["ssl"]["cleint_subject"]])
                                   , (line[validFields["ssl"]["clnt_issuer_subject"]])
                                   , (line[validFields["ssl"]["cert_hash"]])
                                   , (line[validFields["ssl"]["validation_status"]])

                                   )
                            )
                        except sqlite3.Error as ssl:
                            print(str(ssl))

                    if fname == 'SMTP' or fname == "smtp":
                        try:
                            con.execute("insert into main (%s)" % line[validFields['smtp']['uid']])
                            con.execute("insert into main (%s)" % line[validFields['smtp']['ts']])
                            con.execute(
                                """insert into SMTP (%s,%s,%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d,%s,%d)"""
                                % (line[validFields['smtp']['uid']]
                                   , line[validFields["smtp"]['id']]
                                   , int(line[validFields["smtp"]["trans_depth"]])
                                   , line[validFields['smtp']['helo']]
                                   , line[validFields["smtp"]['mailfrom']]
                                   , line[validFields['smtp']['rcptto']]
                                   , line[validFields["smtp"]["date"]]
                                   , line[validFields["smtp"]["from"]]
                                   , line[validFields["smtp"]["to"]]
                                   , line[validFields["smtp"]["reply_tp"]]
                                   , line[validFields["smtp"]["msg_id"]]
                                   , line[validFields["smtp"]["in_reply_to"]]
                                   , line[validFields["smtp"]["subject"]]
                                   , line[validFields["smtp"]["x_originating_ip"]]
                                   , line[validFields["smtp"]["first_received"]]
                                   , line[validFields["smtp"]["second_received"]]
                                   , line[validFields["smtp"]["last_reply"]]
                                   , line[validFields["smtp"]["path"]]
                                   , line[validFields["smtp"]["user_agent"]]
                                   , int(line[validFields["smtp"]["tls"]])
                                   , line[validFields["smtp"]["fuid"]]
                                   , int(line[validFields["smtp"]["is_webmail"]])
                                   )
                            )
                        except sqlite3.Error as s:
                            print(str(s))

                    if fname == 'dhcp' or fname == "DHCP":
                        try:
                            con.execute("insert into main (%s)" % line[validFields['dhcp']['uid']])
                            con.execute("insert into main (%s)" % line[validFields['dhcp']['ts']])
                            con.execute(
                                """insert into DHCP (%s,%s,%s,%s,%s,%s)"""
                                % ((line[validFields['dhcp']['uid']])
                                   , line[validFields["dhcp"]['id']]
                                   , (line[validFields["dhcp"]["mac"]])
                                   , (line[validFields['dhcp']['assigned_ip']])
                                   , (line[validFields["dhcp"]['lease_time']])
                                   , line[validFields['dhcp']['trans_id']]

                                   )
                            )
                        except sqlite3.Error as dhcp:
                            print(str(dhcp))
                        except sqlite3.OperationError as err:
                            print(str(err))

                    if fname == 'WEIRD' or fname == "weird":
                        try:
                            con.execute("insert into main (%s)" % line[validFields['WEIRD']['uid']])
                            con.execute("insert into main (%s)" % line[validFields['WEIRD']['ts']])
                            con.execute(
                                """insert into dhcp (%s,%s,%s,%s,%s,%d)"""
                                % ((line[validFields['weird']['uid']])
                                   , line[validFields["weird"]['id']]
                                   , (line[validFields["weird"]["name"]])
                                   , (line[validFields['weird']['addi']])
                                   , int(line[validFields["weird"]['notice']])
                                   , (line[validFields['weird']['peer']])

                                   )
                            )
                        except sqlite3.Error as weird:
                            print(str(weird))
                    if fname == 'FILES' or fname == "files":
                        try:
                            con.execute("insert into main (%s)" % line[validFields['FILES']['uid']])
                            con.execute("insert into main (%s)" % line[validFields['FILES']['ts']])
                            con.execute(
                                """insert into FILES (%s,%s,%s,%s,%s,%s,%d,%s,%s,%s,%s,%d,%d,%d,%d,%d,%d,%d,%s,%s,%s)"""
                                % (line[validFields['files']['ts']]
                                   , line[validFields["files"]['fuid']]
                                   , (line[validFields["files"]["tx_hosts"]])
                                   , line[validFields['files']['rx_hosts']]
                                   , line[validFields["files"]['conn_uids']]
                                   , line[validFields['files']['source']]
                                   , int(line[validFields["files"]["depth"]])
                                   , line[validFields["files"]["analyzers"]]
                                   , line[validFields["files"]["mime_type"]]
                                   , line[validFields["files"]["filename"]]
                                   , line[validFields["files"]["duration"]]
                                   , int(line[validFields["files"]["local_orig"]])
                                   , int(line[validFields["files"]["is_orig"]])
                                   , int(line[validFields["files"]["seen_bytes"]])
                                   , int(line[validFields["files"]["total_bytes"]])
                                   , int(line[validFields["files"]["missing_bytes"]])
                                   , int(line[validFields["files"]["overflow_bytes"]])
                                   , int(line[validFields["files"]["timedout"]])
                                   , (line[validFields["files"]["parent_fuid"]])
                                   , line[validFields["files"]["md5_sha1_sha256"]]
                                   , (line[validFields["files"]["extracted"]])
                                   ))
                        except sqlite3.Error as files:
                            print("error inserting into table" + str(f))
                else:
                    print(i + "neglected")
                self.progressBar.setValue(int(self.progressBar.value() + (progress / self.count % 100 * 100)))
            f.close()

            with open(historyLog, 'a') as csvfile:  # open log file to log the state of operation
                wr1 = csv.writer(csvfile, delimiter=',')
                digestive = hashlib.md5(codecs.encode(hashTemp))  # string must be converted to bytes to calculate hash
                # calculate the hash of the file
                # this block is only performed when no exceptions happen , all of data inserted into DB successfully
                csvfile.write(fname, digestive.hexdigest())  # the digested value combined

        except:  # this block is executed in case of failure of instering
            with open(historyLog, 'a') as csvfile:
                wr1 = csv.writer(csvfile, delimiter=',')
                wr1.writerow((fname, "FAILED"))

    def executeSQL(self):  # this function performs the SQL queries in the SQL panel
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

            if "insert" in command:  # THE PROGRAM SHOULD DISBLAY A WARNING IN CASE USER TRIED TO insert data into db
                self.message.setText("are you trying to insert data into DB ? \n "
                                     "the program prohibits the user from inserting data into db")
                self.message.show()
            else:
                con.execute(command)
                self.label_2.setStyleSheet("color: green")
                self.label_2.setText("operation succeded")
                self.label_2.show()

        except sqlite3.OperationalError as err:
            print(str(err))

            if s:
                self.message.setText("error selecting rows from data base")
            self.message.setDetailedText(str(err))
            self.label_2.setText("error executing SQL command")
            self.label_2.setStyleSheet("color : red")
            self.label_2.setVisible(True)
            self.message.show()

        except:
            self.message.show()

    def load(self):  # this function loads the content of the log files into the DB
        # todo : progress bar check
        if self.loaded:
            reply = QMessageBox.question(self.message, 'Message',
                                         "there is files already loaded into database ,are you sure you want to load files",
                                         QMessageBox.Yes,
                                         QMessageBox.No)  # shows a message box to user to  make sure of reloading files
            if reply == QMessageBox.Yes:
                self.reset()
            else:
                return
        if self.radioButton.isChecked() and self.lineEdit.text() != "":
            fPath = self.lineEdit.text().split('/')
            fName = fPath[len(fPath) - 1]
            path = '/'.join(fPath[:len(fPath) - 1])  # -1 since the right slicing operator is excluded
            print(fName)
            print(fPath, path)
            os.chdir(path)

            if not self.tableCreator(fName):
                self.message.setText("error creating table " + str(fName))

            self.traverse(fName)

            # print(self.linesCount)



        elif self.radioButton_2.isChecked() and self.lineEdit_2.text() != "":

            progress = 100 / len(
                self.validFiles)  # not so accurate, progress bar will be filled according to progress in file , not according to line numbers
            for each in self.validFiles:
                each = str.lower(each)
                print(each)
                self.tableCreator(each)
                self.traverse(each)
                self.progressBar.setValue(self.progressBar.value() + progress)
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
            "https://bitbucket.org/Psut/bro-ids-log-files-visualizer-and-analyzer\n"
            "https: // tree.taiga.io / project / ahmadjd94 - bila")
        self.message.show()

    def openFile(self):  # function used to open files (single files and files inside working directory )
        self.label.setVisible(False)
        single = True
        try:
            path = self.lineEdit.text().split('/')
            name = path[len(path) - 1]
            print(name + "this")
            if name in self.valid:
                print(name)
                file = open(self.lineEdit.text())
                self.count = 0
                for i in file:
                    self.linesCount += 1
                self.label.setText("the selected file has " + str(self.count) + " lines")
                self.label.setVisible(True)
                file.close()
            elif name in self.UnsupportedFiles:
                print("here")
                self.message.setText("BILA does not currently support the file you are trying to use")
                self.message.show()
                self.lineEdit.clear()
            else:
                self.message.setText("make sure you are trying to load a valid log files")
                self.message.show()
                self.lineEdit.clear()

        except:  # handling incorrect file directories / paths
            print("exception raised")
            self.label.show()

    def openFileDialog(self):  # displays open file dialog for user to select the required log file
        single = False
        fname = QFileDialog.getOpenFileName(None, 'Open file', '/home', '*.log')  # error in params
        print(fname)
        self.lineEdit.setText(fname[0])
        try:
            file = open(fname[0])
            ui.linesCount = 0
            for i in file:
                ui.linesCount += 1
            self.label.setText("the selected file has " + str(ui.linesCount) + " lines")
            self.label.setVisible(True)
            file.close()
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
                    self.validFiles.append(each)  # appends BRO valid log files names to the discovered logs
                    print(self.validFiles)
            for each in self.validFiles:
                file = open(each, 'r')
                for i in file:
                    ui.linesCount += 1
                file.close()
            self.label.setText(
                "the directory you have selected have %s valid files with %s lines" % (
            str(len(self.validFiles)), str(ui.linesCount)))
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
        # todo : drop tables
        # todo  reset timeline


if __name__ == "__main__":  # main module

    def droptables(table):  # a map function drops tables , return 1 on success
        try:
            con.execute("drop table %s" % table)
            return 1
        except sqlite3.OperationalError as a:
            if "no such table" in str(a):
                return 0


    import sys
    import csv
    from datetime import datetime

    OriDir = os.getcwd()  # this variable will store the original
    historyLog = os.getcwd() + '/history.csv'

    types = {"uid": int, "ts": float, "id": -1, "trans_depth": int, "method": str, "host": str, "uri": str,
             "referrer": str
        , "user_agent": str, "request_body_len": int, "status_code": int, "status_msg": str, "info_code": int,
             "info_msg": str
        , "tags": -1, "username": str, "password": str, "proxied": -1, "orig_fuids": -1, "orig_meme_type": -1,
             "orig_fuid": -1
        , "resp_meme_ty": -1, "command": str, "arg": str
        , "mime_type": str, "file_size": int, "reply_code": int, "reply_msg": str
        , "data_channel": -1, "fuid": str
        , "tx_hosts": -1, "rx_hosts": -1, "conn_uids": -1, "source": str, "depth": int
        , "analyzers": -1, "filename": str, "duration": -1, "local_orig": bool, "is_orig": bool, "seen_bytes": int,
             "total_bytes": int
        , "missing_bytes": int, "overflow_bytes": int, "timedout": bool, "parent_fuid": str
        , "md5": str, "sha1": str, "sha256": str, "extracted": str
        , "nick": str, "user": str, "value": str, 'addi': str
        , "dcc_file_name": str, "dcc_file_size": int, "dcc_mime_type": str
        , 'trans_depth': int, "helo": str, "mailfrom": str, "rcptto": -1
        , "date": -1, "from": str, "to": str, "reply_to": str, "msg_id": str, "in_reply_to": str, "subject": str
        , "x_originating_ip": str, "first_received": str
        , "second_received": str, "last_reply": str, "path": -1
        , "tls": bool, "fuids": -1, "is_webmail": bool
        , "status": str, "direction": str, "client": str, "server": str, "resp_size": int
        , "id_orig_h": str, "id_orig_p": int, "id.resp_h": int, "id.resp_p": int, "version": str, "cipher": str,
             "server_name": str, "session_id": str, "issuer_subject": str, "not_valid_before": str,
             "last_alert": str, "client_subject": str, "clnt_issuer_subject": str, "cert_hash": str,
             "validation_status": -1  # todo :resolve vectors issues
        , "name": -1, "notice": -1, "peer": -1
        , "src_addr": str, "src_port": int, "dst_adr": str, "dst_port": int, "note": str, "sig_id": str
        , "event_msg": str, "sub_msg": str, "sig_count": int, "host_count": int
        , "id_resp_h": str, "id_resp_p": int, "proto": str, "service": str
        , "orig_bytes": int, "resp_bytes": int, "conn_state": str, "missed_bytes": int, "history": str, "orig_pkts": int
        , "orig_ip_bytes": int, "resp_pkts": int, "resp_ip_bytes": int, "tunnel_parents": -1, "orig_cc": str,
             "resp_cc": str
        , "mac": str, "assigned_ip": str, "lease_time ": str
        , "query": str, "qclass": int, "qclass_name": str, "qtype": int, "qtype_name": str, "rcode": int,
             "rcode_name": str
        , "QR": bool, "AA": bool, "TC": bool, "RD": bool, "RA": bool, "Z": int, "answers": -1, "TTLs": -1,
             "rejected bool": bool

             }
    # this dictionary will declare the datatypes for each field in the database

    validFields = {  # todo : check fields of every log file (DNS done,
        "http": {'uid': -1, 'ts': -1, "id": -1, "trans_depth": -1, "method": -1, "host": -1, "uri": -1, "referrer": -1,
                 "user_agent": -1, "request_body_len": -1, "status_code": -1, "status_msg": -1, "info_code": -1,
                 "info_msg": -1,
                 "tags": -1, "username": -1, "password": -1, "proxied": -1, "orig_fuids": -1, "orig_meme_type": -1,
                 "orig_fuid": -1,
                 "resp_meme_ty": -1,},  # this dictionary will store the indecies of lof fileds for each file

        'ftp': {"uid": -1, "ts": -1, "id": -1, "user": -1, "password": -1, "command": -1, "arg": -1,
                "mime_type": -1, "file_size": -1, "reply_code": -1, "reply_msg": -1,
                "data_channel": -1, "fuid": -1},

        "files": {"ts": -1, "fuid": -1, "tx_hosts": -1, "rx_hosts": -1, "conn_uids": -1, "source": -1, "depth": -1,
                  "analyzers": -1, "mime_type": -1,
                  "filename": -1, "duration": -1, "local_orig": -1, "is_orig": -1, "seen_bytes": -1, "total_bytes": -1,
                  "missing_bytes": -1, "overflow_bytes": -1, "timedout": -1, "parent_fuid": -1,
                  "md5": -1, "sha1": -1, "sha256": -1, "extracted": -1},  # check this again

        'irc': {"uid": -1, 'ts': -1, "id": -1, "nick": -1, "user": -1, "command": -1, "value": -1, "addi": -1,
                "dcc_file_name": -1, "dcc_file_size": -1, "dcc_mime_type": -1, "fuid": 1},

        'smtp': {'ts': -1, 'uid': -1, 'id': -1, 'trans_depth': -1, "helo": -1, "mailfrom": -1, "rcptto": -1
            , "date": -1, "from": -1, "to": -1, "reply_to": -1, "msg_id": -1, "in_reply_to": -1, "subject": -1
            , "x_originating_ip": -1, "first_received": -1
            , "second_received": -1, "last_reply": -1, "path": -1, "user_agent": -1
            , "tls": -1, "fuids": -1, "is_webmail": -1},

        'ssh': {"uid": -1, "status": -1, "direction": -1, "client": -1, "server": -1, "resp_size": -1},

        'ssl': {"uid": -1, "id_orig_h": -1, "id_orig_p": -1, "id.resp_h": -1, "id.resp_p": -1, "version": -1,
                "cipher": -1,
                "server_name": -1, "session_id": -1, "subject": -1,
                "issuer_subject": -1, "not_valid_before": -1,
                "last_alert": -1, "client_subject": -1, "clnt_issuer_subject": -1, "cert_hash": -1,
                "validation_status": -1},

        'weird': {"uid": -1, "id": -1, "name": -1, "addi": -1, "notice": -1, "peer": -1},

        'signatures': {"ts": -1, 'src_addr': -1,
                       'src_port': -1, 'dst_adr': -1, 'dst_port': -1, 'note': -1, 'sig_id': -1,
                       'event_msg': -1, 'sub_msg': -1, 'sig_count': -1, 'host_count': -1},

        'conn': {"uid": -1, "id_orig_h": -1, "id_orig_p": -1, "id_resp_h": -1, "id_resp_p": -1, "proto": -1,
                 "service": -1,
                 "duration": -1, "orig_bytes": -1,
                 "resp_bytes": -1, "conn_state": -1, "local_orig": -1, "missed_bytes": -1, "history": -1,
                 "orig_pkts": -1,
                 "orig_ip_bytes": -1, "resp_pkts": -1, "resp_ip_bytes": -1, "tunnel_parents": -1, "orig_cc": -1,
                 "resp_cc": -1},

        'dhcp': {"uid": -1, "id": -1, "mac": -1, "assigned_ip": -1, "lease_time ": -1, "trans_id": -1},

        'dns': {"uid": -1, 'ts': -1, "id": -1, "proto": -1, "trans_id": -1,
                "query": -1, "qclass": -1, "qclass_name": -1, "qtype": -1, "qtype_name": -1, "rcode": -1,
                "rcode_name": -1, "QR": -1,
                "AA": -1, "TC": -1, "RD": -1, "RA": -1, "Z": -1, "answers": -1, "TTLs": -1, "rejected bool": -1}
        # todo : check tables strucutre !!! normalize conn_ID table
    }

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    tables = ["main", "dhcp", "smtp", "irc", "weird", "ssh", "conn", "http", "dns", "signature", "ssl", "ids", "files",
              'ssh']
    try:

        con = sqlite3.connect('analyze2.db')  # initializing connection to DB // should be in UI init ??
        print("connected")
        dropped = map(droptables, tables)  # fix ?
        print(list(dropped))
        print(str(list(dropped)) + "this is dropped tables ")  # fix ?
        # print(tables - dropped + "non dropped tables ") #fix ?
        try:
            con.execute("CREATE TABLE main (uid TEXT PRIMARY KEY , ts string)")
            con.execute("CREATE TABLE IDs(uid INT ,id_orig_h TEXT, id_orig_p INT, ID_RESP_H TEXT"
                        ", ID_RESP_P INT,FOREIGN KEY(uid) REFERENCES main (uid))")
        except:
            print("error dropping main ?")

        if "history.csv" in os.listdir():
            with open(historyLog, 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["new session", str(datetime.now())[:19]])
        else:

            print(historyLog)
            f = open(historyLog, "w")
            f.close()
            with open(historyLog, 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["new session", str(datetime.now())[:19]])

        """create a table for analysizing the log file : time , source IP ,source Port,Destination IP , Destination port , protocol in use,count of packets use"""

        ##############################IMPORT DATABASE DATATYPES NEED FURTHER CHECKING ##############################################################
    except sqlite3.Error as e:
        print(e)
        print("error")

        ui.__message2__.show()

    sys.exit(app.exec_())
