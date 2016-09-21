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

# module used for changing Current working directory of the program
import fnmatch  # module used for matching files names
# import pyqtgraph as pg
import hashlib, codecs, operator, sqlite3, os,time
#hashlib used to use MD5 , codecs , converting strings to bytes , sqlite3 to use db , os to use DIRs ,

class Ui_MainWindow(object):  # Qt and PYUIC creator generated functions and classes

    ################################  defining global variable ###################################
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #self.__message2__.setText("error connecting to database")
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
#        self.mainToolBar.setWindowTitle(_translate("MainWindow", "BRO Log file analyzer and visualizer"))
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


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(759, 518)
        MainWindow.setStyleSheet("background-color: rgb(51, 51, 51);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.message=QtWidgets.QMessageBox()
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
        #self.pushButton_2.setGeometry(QtCore.QRect(240, 120, 29, 27))
        self.pushButton_2.setGeometry(QtCore.QRect(616, 99, 29, 27))
        self.pushButton_2.setStyleSheet("background-color: rgb(186, 186, 186);\n"
                                        "color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        #self.pushButton_2.setGeometry(QtCore.QRect(240, 120, 29, 27))
        #self.pushButton_2.setStyleSheet("background-color: rgb(186, 186, 186);\n"
        #                                "color: rgb(0, 0, 0);")
        #self.pushButton_2.setObjectName("pushButton_2")
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


    def uMan(self):
        self.label_2.setVisible(False)

    def tableCreator(self, fname):  # this function creates tables based on the fname argument
        print ('fname passes to function',fname)
        print (dropped)
        if fname in ["ids","IDS"]:
            try:
                con.execute("""CREATE TABLE ids (uid text,ts int ,ORIG_H TEXT,
                                ORIG_P INT,RESP_H TEXT,RESP_P INT,FOREIGN KEY (`UID`) REFERENCES MAIN(`UID`),foreign key (`ts`) references  main (`ts`))""")
                table_created['IDS']=True
                print ("success creating ids  table ")
            except :
                table_created['IDS'] = False
                print ("error creating ids table ")

        elif fname == "ftp.log":  # DONE # create FTP table //THIS TABLE HAS RELATION WITH IDS TABLE
            try:
                con.execute("""CREATE TABLE FTP(UID TEXT
                ,USER TEXT,PASSWORD TEXT,COMMAND TEXT,ARG TEXT,
                MIME_TYPE TEXT,FILE_SIZE INT,REPLY_CODE INT,REPLY_MSG TEXT,
                FUID TEXT,FOREIGN KEY (UID)REFERENCES MAIN(UID))""")
                print("step3")
                table_created['FTP'] = True
                return True
            except:
                return False

        elif fname == "dhcp.log":  # create DHCP table //THIS TABLE HAS RELATION WITH IDS TABLE
            try:
                #if list(dropped)[tables.index("IDS")] == 0:  # indicates if the IDS exists or not
                self.tableCreator('ids')  # call the table creator function to create the ids table

                con.execute("""CREATE TABLE DHCP(UID TEXT,TS int
                ,MAC TEXT, ASSIGNED_IP TEXT,LEASE_TIME TEXT
                , TRANS_ID INT,FOREIGN KEY(UID) REFERENCES MAIN(UID),FOREIGN KEY(ts) REFERENCES MAIN(ts) )""")
                print("step2")
                table_created['DHCP'] = True
                return True
            except:
                return False

        elif fname == "irc.log":  # DONE  create IRC table //THIS TABLE HAS RELATION WITH IDS TABLE
            try:
                if list(dropped)[tables.index("IDS")] == 0:  # indicates if the IDS exists or not
                    self.tableCreator('ids')  # call the table creator function to create the ids table

                con.execute("""CREATE TABLE IRC (UID TEXT
                , NICK TEXT,USER TEXT,COMMAND TEXT,VALUE TEXT,ADDI TEXT,
                DCC_FILE_NAME TEXT,DCC_FILE_SIZE INT,DCC_MIME_TYPE TEXT,FUID TEXT,FOREIGN KEY (UID,TS) REFERENCES MAIN(UID,TS))""")
                print("step4")
                table_created['IRC'] = True
                return True
            except:
                return False

        elif fname == "weird.log":  # DONE  create weird table
            try:
                #if list(dropped)[tables.index("IDS")] == 0: # indicates if the IDS exists or not
                self.tableCreator('ids')      # call the table creator function to create the ids table

                con.execute("CREATE TABLE WEIRD(UID TEXT,ts int, NAME TEXT,"
                            "ADDI TEXT,NOTICE BOOL,PEER TEXT,FOREIGN KEY (UID,TS) REFERENCES MAIN(UID,TS))")
                table_created['WEIRD'] = True
                print("step5")
            except:
                return False

        elif fname == "ssh.log":  # DONE create SSH table
            try:
                if list(dropped)[tables.index("IDS")] == 0:  # indicates if the IDS exists or not
                    self.tableCreator('ids')  # call the table creator function to create the ids table

                con.execute("""CREATE TABLE SSH( UID TEXT,TS INT,STATUS TEXT,
                DIRECTION TEXT,CLIENT TEXT, SERVER TEXT,RESP_SIZE INT,FOREIGN KEY (UID,TS) REFERENCES MAIN(UID,TS))""")
                table_created['SSH'] = True
                print("step6")
                return True
            except:
                return False

        elif fname == "conn.log":  # DONE  create CONN table
            try:
                # if list(dropped)[tables.index("IDS")] == 0:  # indicates if the IDS exists or not
                self.tableCreator('ids')  # call the table creator function to create the ids table

                con.execute("""CREATE TABLE CONN(UID TEXT,TS INT,PROTO TEXT,SERVICE TEXT,DURATION TIME,ORIG_BYTES INT,
                RESP_BYTES INT,CONN_STATE TEXT,LOCAL_ORIG BOOL,MISSED_BYTES COUNT,HISTORY TEXT,ORIG_PKTS INT,ORIG_IP_BYTES INT,
                RESP_PKTS INT,RESP_IP_BYTES INT,TUNNEL_PARENTS BLOB,ORIG_CC TEXT,RESP_CC TEXT,
                FOREIGN KEY (UID)REFERENCES MAIN(UID),FOREIGN KEY (ts)REFERENCES MAIN(ts))""")

                con.execute ("""CREATE TABLE CONN_TUNNEL_PARENTS (UID TEXT , TS INT , PARENT TEXT ,FOREIGN KEY (UID) REFERENCES conn (UID),
                             FOREIGN KEY (TS) REFERENCES conn (TS))""")
                table_created['CONN'] = True
                print("step7")
                return True
            except:
                return False

        elif fname == "http.log":  # DONE  create HTTP table and related normalized tables

            try:
                # if dropped['IDS'] == 0:  # indicates if the IDS exists or not

                self.tableCreator("ids")  # call the table creator function to create the ids table

                con.execute("""CREATE TABLE  HTTP (
                                        UID TEXT,ts int 
                                        ,TRANS_DEPTH INT,METHOD TEXT,HOST TEXT,URI TEXT,REFERRER TEXT,
                                        USER_AGENT TEXT,REQUEST_BODY_LEN INT,
                                        STATUS_CODE INT,STATUS_MSG TEXT,INFO_CODE INT,INFO_MSG TEXT,filename text,USERNAME TEXT,
                                        PASSWORD TEXT,PROXIED TEXT,
                                        FOREIGN KEY  (UID) REFERENCES MAIN (UID),
                                        FOREIGN KEY  (ts) REFERENCES MAIN (ts))""")


                con.execute(
                    "CREATE TABLE HTTP_TAGS (UID TEXT , TS INT , TAG TEXT,FOREIGN KEY (UID) REFERENCES HTTP(UID),"
                    "FOREIGN KEY  (ts) REFERENCES http (ts))")


                con.execute("""CREATE TABLE HTTP_PROXIED_HEADERS (UID TEXT , TS INT ,
                              HEADER TEXT,FOREIGN KEY (UID) REFERENCES HTTP(UID),
                    FOREIGN KEY  (ts) REFERENCES http (ts))""")

                con.execute("""CREATE TABLE HTTP_ORIG_FUIDS (UID TEXT , TS INT
                          , ORIG_FUID TEXT,FOREIGN KEY (UID) REFERENCES HTTP(UID),
                    FOREIGN KEY  (ts) REFERENCES http (ts))""")

                con.execute("""CREATE TABLE HTTP_ORIG_MEME_TYPES (UID TEXT , TS INT
                    ,ORIG_MEME_TYPES TEXT,FOREIGN KEY (UID) REFERENCES HTTP(UID),
                    FOREIGN KEY  (ts) REFERENCES http (ts))""")

                con.execute(
                    """CREATE TABLE HTTP_RESP_FUIDS (UID TEXT , TS INT ,
                    RESP_FUIDS TEXT,FOREIGN KEY (UID) REFERENCES HTTP(UID),
                    FOREIGN KEY  (ts) REFERENCES http (ts))""")

                con.execute("""CREATE TABLE HTTP_RESP_MEME_TYPES (UID TEXT , TS INT
                            , RESP_MEME_TYPES TEXT,FOREIGN KEY (UID) REFERENCES HTTP(UID),
                    FOREIGN KEY  (ts) REFERENCES http (ts))""")

                table_created['HTTP'] = True
                table_created['HTTP_RESP_MEME_TYPES'] = True
                table_created['HTTP_RESP_FUIDS'] = True
                table_created['HTTP_ORIG_MEME_TYPES'] = True
                table_created['HTTP_ORIG_FUIDS'] = True
                table_created['HTTP_PROXIED_HEADERS'] = True
                table_created['HTTP_TAGS'] = True

                print("step8")
            except:
                return False
        elif fname == "dns.log":  # DONE # create DNS table
            try:
                if list(dropped)[tables.index("IDS")] == 0:  # indicates if the IDS exists or not
                    self.tableCreator('ids')  # call the table creator function to create the ids table

                con.execute("""CREATE TABLE DNS (
                                        UID TEXT,ts int,PROTO TEXT,TRAN_ID INT,
                                        `QUERY` TEXT,`QCLASS` INT,`QCLASS_NAME` TEXT,`QTYPE` INT,`QTYPE_NAME` TEXT,`RCODE` INT,
                                        `RCODE_NAME` TEXT,`QR` bool,`AA` BOOL,`TC` BOOL,
                                        `RD` BOOL,`RA` BOOL,`Z`INT,`REJECTED` BOOL,FOREIGN KEY (`UID`) REFERENCES MAIN(`UID`),
                                        FOREIGN KEY (`UID`) REFERENCES MAIN(`UID`))""")

                con.execute("CREATE TABLE DNS_ANSWERS (UID TEXT , TS INT ,ANSWER TEXT,"
                            "FOREIGN KEY (UID) REFERENCES DNS(UID),"
                            "FOREIGN KEY (ts) REFERENCES DNS(ts))")

                con.execute("CREATE TABLE DNS_TTLS (UID TEXT , TS INT ,TTL INT,"
                            "FOREIGN KEY (UID) REFERENCES DNS(UID),"
                            "FOREIGN KEY (ts) REFERENCES DNS(ts))")

                table_created['DNS_ANSWERS'] = True
                table_created['DNS_TTLS'] = True

                print("step9")
            except:
                return False

        elif fname == "signature.log":  # DONE # create SIGNATURES table
            try:
                con.execute("""CREATE TABLE SIGNATURE(TS INT ,SRC_ADDR TEXT ,
                            SRC_PORT INT ,DST_ADR TEXT ,DST_PORT INT ,NOTE TEXT ,SIG_ID TEXT,
                            EVENT_MSG TEXT ,SUB_MSG TEXT ,SIG_COUNT INT ,HOST_COUNT INT )""")
                table_created['SIGNATURE'] = True

                print("step10")
                return True
            except:
                return False

        elif fname == "ssl.log":  # DONE # create SSL table and it's realted tables
            try:
                if list(dropped)[tables.index("IDS")] == 0:  # indicates if the IDS exists or not
                    self.tableCreator('ids')  # call the table creator function to create the ids table

                con.execute("""CREATE TABLE SSL(UID TEXT,VERSION TEXT ,CIPHER TEXT ,
                SERVER_NAME TEXT ,SESSION_ID TEXT ,SUBJECT TEXT ,
                ISSUER_SUBJECT TEXT ,NOT_VALID_BEFORE TIME ,
                LAST_ALERT TEXT ,CLIENT_SUBJECT TEXT ,CLNT_ISSUER_SUBJECT TEXT ,CERT_HASH TEXT ,
                FOREIGN KEY (UID)REFERENCES MAIN(UID))""")
                table_created['SSL'] = True

                con.execute("CREATE TABLE SSL_VALIDATION_STATUS (UID TEXT , TS INT,"
                            "VALIDATION_STATUS TEXT,FOREIGN KEY (UID,TS) REFERENCES SSL(UID,TS))")
                table_created['SSL_VALIDATION_STATUS'] = True

                print("step11")
                return True
            except:
                return False

        elif fname == "files.log":  # DONE # create files table and it's related tables
            try:
                con.execute(
                    """CREATE TABLE FILES (TS INT , FUID TEXT,TX_HOSTS TEXT,RX_HOSTS TEXT,CONN_UIDS,SOURCE TEXT ,DEPTH INT,
                    ANALYZERS TEXT,MIME_TYPE TEXT,
                    FILENAME TEXT,DURATION TIME,LOCAL_ORIG BOOL,IS_ORIG BOOL,SEEN_BYTES INT,TOTAL_BYTES INT ,
                    MISSING_BYTES INT,OVERFLOW_BYTES INT,TIMEDOUT INT,PARENT_FUID STRING,
                    MD5A_SHA1_SHA256 TEXT,EXTRACTED BOOL)""")
                table_created['FILES'] = True

                con.execute ("CREATE TABLE FILES_TX_HOSTS(UID TEXT,TS INT,SOURCE"
                             ",FOREIGN KEY (UID,TS) REFERENCES FILE(UID,TS))")
                table_created['FILES_TX_HOSTS'] = True

                con.execute("CREATE TABLE FILES_RX_HOSTS(UID TEXT,TS INT,RECIEPENT TEXT"
                            ",FOREIGN KEY (UID,TS) REFERENCES FILE(UID,TS))")
                table_created['FILES_RX_HOSTS'] = True


                con.execute("CREATE TABLE FILES_CONN_UIDS(UID TEXT,TS INT,CONN_UID TEXT"
                            ",FOREIGN KEY (UID,TS) REFERENCES FILE(UID,TS))")
                table_created['FILES_CONN_UIDS'] = True

            except:
                return False

        elif fname == "smtp.log":  # DONE # create SMTP table and it's related tables
            try:
                if list(dropped)[tables.index("IDS")] == 0:  # indicates if the IDS exists or not
                    self.tableCreator('ids')  # call the table creator function to create the ids table

                con.execute("""CREATE TABLE SMTP (UID TEXT ,TS INT
                TRANS_DEPTH INT ,HELO TEXT,MAILFROM STRING,RCPTTO TEXT
                ,`DATE` TEXT ,`FROM` TEXT ,`TO` TEXT,`REPLY_TO` TEXT,`MSG_ID` TEXT ,`IN_REPLY_TO` TEXT ,`SUBJECT` TEXT
                ,`X_ORIGINATING_IP` TEXT,`FIRST_RECEIVED` TEXT ,
                `SECOND_RECEIVED` TEXT ,`LAST_REPLY` TEXT ,`USER_AGENT` TEXT ,
                `TLS` BOOL,`IS_WEBMAIL` BOOL , FOREIGN KEY (UID) REFERENCES  MAIN(UID))""")
                table_created['SMTP'] = True


                con.execute("""CREATE TABLE SMTP_ANALYZERS (UID TEXT , TS INT ,ANALYZER TEXT,
                FOREIGN KEY (UID,TS) REFERENCES SMTP(UID,TS))""")
                table_created['SMTP_ANALYZERS'] = True


                con.execute("""CREATE TABLE  SMTP_RCPTO (UID TEXT , TS INT ,HEADER TEXT,
                FOREIGN KEY (UID,TS) REFERENCES SMTP(UID,TS))""")
                table_created['SMTP_RCPTO'] = True


                con.execute("CREATE TABLE  SMTP_TO (UID TEXT , TS INT ,RECEIVER TEXT,"
                            "FOREIGN KEY (UID,TS) REFERENCES SMTP(UID,TS))")
                table_created['SMTP_TO'] = True


                con.execute("CREATE TABLE SMTP_PATHS (UID TEXT ,TS INT , PATH TEXT,"
                            "FOREIGN KEY (UID,TS) REFERENCES SMTP(UID,TS))")
                table_created['SMTP_PATHS'] = True


                con.execute("CREATE TABLE SMTP_FUIDS(UID TEXT ,TS INT,FUID TEXT ,"
                            "FOREIGN KEY (UID,TS) REFERENCES SMTP(UID,TS))")
                table_created['SMTP_FUIDS'] = True

                #`RCPTO` AND `TO` COLUMNS ARE ASSUMED TO BE SETS
                return True
            except:
                return False

    def valuefilter(self, num):
        if num != -1:
            return True
        else:
            return False

    def traverse(self, fname):  # this function will traverse the file that is based to it
        # if the field value is -1 , the field should be neglected )
        print('traversing')
        print(fname)
        progress = 0  # indicate the level of progress bar
        try:
            #fname = (fname.split('.')[0])  # this statment splits the fname and neglects the .log part of it
            print(fname)
            hashtemp = ""  # this variable stores the entire log file to calculate it's hash value
            print (os.getcwd())
            if fname in os.listdir():
                print('yes')
            f1 = open(fname , 'r')  # open the log file Read-Only mode
            print ('file is now opened')
            #IF FILED IN ID AND FNAME != 'CONN' : DO NOT EXECUTE SECOND INSERT STATMENT
            for i in f1:  # todo : modify function to increase the progress bar
                hashtemp += i  # concatenate the lines being read to the string

                if i[:7] == "#fields" or i[:7] == "Fields":  # field loading algorithm
                    # print(i)
                    fields = (i[7:].split())
                    print(fields)
                    fname=(fname.split('.')[0])
                    print(fname)
                    print(validFields[fname])
                    for field in fields:
                        if field in validFields[fname]:

                            try:
                                validFields[fname][field] = fields.index(field)  # this line stores the index of field in the dictionary
                            except :
                             print ('error')
                        print(fields.index(field), field)


                    try :
                        validFields[fname] = sorted(validFields[fname].items(), key=operator.itemgetter(1)) #
                        print ('sorted',validFields[fname])
                    except:
                        print ('already sorted ?')

                elif i[0] != "#":  # this line ignores the log lines that start with # , #indecates a commented line
                    line = i.split('\t')
                    # sort dictionary based on key values
                    try:
                        sql_commands=(self.SQLcreator(fname, line))
                        print ("PRINTING RECEIVED LIST",sql_commands)
                        for command in sql_commands:
                            try :
                                con.execute (command)
                                print ("executed correctly :\n",command)
                                con.commit()
                            except:
                                    print ('error executing',command)
                        # sql_command_ids=(self.SQLcreator2(line))  #this line stores command for other secondary normalized tables
                        # con.execute(sql_command,sql_command_ids)
                    except  :
                        # print (str(a))
                        print('error creating SQL')
                    print ('end')
                    #print(sql_command)
                    # no hardcoded indecies of
                    # fields  / PYTHON HAS NO SWITCH SYNTAX SO we used if statments
                    # todo : the algorithm is not handling undefined fields , sprint's extended to forever

                    #con.execute


                #else:
                 #   print(i + "neglected")
                #self.progressBar.setValue(int(self.progressBar.value() + (progress / self.count % 100 * 100)))
            f1.close()

            with open(historyLog, 'a') as csvfile:  # open log file to log the state of operation
                wr1 = csv.writer(csvfile, delimiter=',')
                digestive = hashlib.md5(codecs.encode(hashtemp))  # string must be converted to bytes to calculate hash
                # calculate the hash of the file
                # this block is only performed when no exceptions happen , all of data inserted into DB successfully
                try:
                    wr1.writerow(fname, digestive.hexdigest())   # write the file name , with it's hash value incase it was loaded successfully
                    #csvfile.write(fname, digestive.hexdigest())  # the digested value combined
                except :
                    print ('exception in writing')

        except Exception as e1:  # this block is executed in case of failure of instering
            print(str(e1))
            print ('exception occurd')
            with open(historyLog, 'a') as csvfile:
                wr1 = csv.writer(csvfile, delimiter=',')
                wr1.writerow((fname, "FAILED"))

    def SQLcreator(self, table, line): # this function creates SQL Queries based on table based to it
                                       # should use lambda expressions
                                        # should handle inserting to ids table also
        print (len (validFields[table]),len(line))

        # if len (line) < len(validFields[table]):
        #     print ("invalid line detected")
        #     return
        print (line)
        print(table)
        exist = {}       #stores the values of existing fields that can be extracted from the log file
        # THIS FUNCTION WILL RAISE AN EXCEPTION INCASE OF INVALID TABLE TYPE
        # HANDLED IN THE CALLER FUNCTION
        # use time.time to get the current time in epoch format
        # print('inside creator ', validFields[table])

        try:
            print (validFields[table])
            exist = dict(validFields[table])
        except:
            print('error making list')
        print(exist)
        # missing cast
        keys = list(exist.keys())
        print(type(keys))
        print(keys)
        print (exist.values())
        print ('prepare to cast ')
        try :
            print (type (exist))
            value =list( exist.values())
        except :
            print ("error getting values of dict")
            raise Exception

        print (value)
        #todo : check if the arrays are sorted already
        for i1 in range(len(value)):     # the following algorithm sorts the exist dictionary , python dictionary are not sorted
                                        # the algorithm is a modified version of bubble sort
            for i2 in range(len(value) -1):
                if value[i2] > value[i2 + 1]:
                    valuetemp = value[i2]
                    keytemp=keys[i2]
                    value[i2] = value[i2 + 1]
                    keys[i2]=keys[i2+1]
                    value[i2 + 1] = valuetemp
                    keys[i2+1]=keytemp
        try:
            keys = keys[value.index(0):]  #slice keys based based on the values array
            value = value[value.index(0):] # slice values array accoridng to the first 0 seen in the array
            print(value,keys)
        except Exception as E:
            print (str (E))

        try:
            # print(validFields['conn'])
            main_insert="insert into main (uid,ts) values ('%s',%s)"%(line[exist['uid']],line[exist['ts']])
            print(main_insert)
        except Exception as a:
            print ("WTF")
            print (str(a))
        inserts=[]

        ################################ DNS-SPECIFIC INSERTS AND STATMENTS######################
        dns_ttls_inserts=""
        dns_ANSWERS_inserts = ""

        ################################ http-SPECIFIC INSERTS AND STATMENTS######################
        http_tags_insert=conn_tunnel_parents_insert=http_proxied_insert=""
        http_orig_fuids_insert = ""# string will store the values if insert statments into http_fuids_table

        ################################ ids-SPECIFIC INSERTS AND STATMENTS######################
        ids_values = ""  # string will stores the values of insert statment for ids table
        ids_insert="insert into ids("
        ids_field=field = values_string = ""   # variable field stores the field name in table




        normal_table_insert = "insert into %s (" %table   # insert statment
        print (normal_table_insert)

        for i in keys:
            if i in dict(validFields[table]):
                # checking for ifelds of normalized table

                if i =="id.orig_h":                             #SPECIAL FIELDS OF IDS TABLE
                    ids_field += "orig_h" + ","
                elif i == "id.orig_p":
                    ids_field += "orig_p" + ","
                elif i == "id.resp_h":
                    ids_field += "resp_h" + ","
                elif i == "id.resp_p":
                    ids_field += "resp_p" + ","

                elif i=='tags':             #SPECIAL FIELDS FOR HTTP_TAGS TABLE
                    http_tags_insert = "insert into http_tags(ts,uid,tag)values("
                elif i=="proxied":   # SPECIAL FIELDS FOR HTTP_PROXIED TABLE
                    http_proxied_insert="insert into http_proxied_headers (ts,uid,header) values ("
                elif i=="orig_fuids":
                    http_orig_fuids_insert ="insert into http_orig_fuids (ts,uid,orig_fuid) values ("
                elif i=="tunnel_parents":
                    conn_tunnel_parents_insert="insert into conn_tunnel_parents (ts,uid,parent) values ("

                elif i=="TTLs":                                              #SPECIAL FIELDS FOR DNS
                    dns_ttls_inserts="insert into dns_ttl (uid,ts,ttl) values ("
                elif i == "answers":
                    dns_answers_inserts = "insert into dns_ttl (uid,ts,ttl) values ("

                else:
                    field += str(i) + ","
            else :
                pass # neglecting the invalid fields detected

        field = field[:len(field) - 1]  # this line will remove the colon at the end of fileds string
        # print (field)
        print (len (value))
        print ("312341231234214")
        print (line)
        print (keys)
        for key in keys:
            print (line[exist[key]])
            # print (validFields['ids'])
            if key in validFields['ids'].keys():
                if line[exist[key]] !='-':
                    if types[key] == str:
                        ids_values += "\'"+line[exist[key]] + '\','
                    else:
                        ids_values += line[exist[key]] + ","
                else :
                    ids_values += "\'" + "null" + '\','

            elif key=='tags' and http_tags_insert!='': # handle the inserting into tags normalized tables
                http_tags_insert+=line[exist['ts']]+",\'"+line[exist['uid']]+"\',\'"+line[exist[key]]+"\')"

            elif key=="proxied":   # handle insertin into procied normalized table
                http_proxied_insert+=line[exist["ts"]]+",\'"+line[exist['uid']]+"\',\'"+line[exist[key]]+"\')"

            elif key== "orig_fuids":  # handle inserting into orig_fuids normalized table
                http_orig_fuids_insert+=line[exist["ts"]]+",\'"+line[exist['uid']]+"\',\'"+line[exist[key]]+"\')"

            elif key =="tunnel_parents":
                conn_tunnel_parents_insert+=line[exist["ts"]]+",\'"+line[exist['uid']]+"\',\'"+line[exist[key]]+"\')"

            elif key=="TTLs":         #DNS TABLE
                print ("printing ttls",line[exist[key]])
                if line[exist[key]] != "" or line[exist[key]] != "-" or line[exist[i]] != "(empty)":
                    ttls_inserts=[]
                    ttls=line[exist[key]].split(',')
                    for ttl in ttls:
                        ttl_insert=dns_ttls_inserts+line[exist["uid"]]+","+line[exist["ts"]]+","+ttl+")"
                        ttls_inserts.append(ttl_insert)

            elif key=="answers" :   #DNS TABLE
                if line[exist[key]] != "" or line[exist[key]] != "-" or line[exist[key]]!= "(empty)":
                    answers_inserts = []
                    answers = line[exist[i]].split(',')
                    for answer in answers:
                        answer_insert = dns_answers_inserts+ line[exist["uid"]] + "," + line[exist["ts"]] + "," + answer + ")"
                        answers_inserts.append(answer_insert)

            elif line[exist[key]] != '-' or line[exist[key]] != "-":
                if types[key] == datetime: # checking for datetime type
                    a=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(line[exist[key]]))) # converting epoch to datetime
                    #print (a)
                    values_string +="\'"+str(a)+"\',"  # concatenating the value to the values string

                elif types[key] == int:
                    print(line[exist[key]], 'test1')
                    values_string += line[exist[key]] + ","
                elif types [key] == float :
                    values_string += line[exist[key]] + ","
                    # try:
                    #     a = int (line[exist[i]])# converting str to int
                    #     values_string += str(a) + ","  # concatenating the value to the values string

                    # except Exception as e:
                    #     print (i,exist[i])
                    #     print (str (e))
                    #     print ('error casting value%s' %line[exist[i]])
                    #
                    #     values_string += (line[exist[i]]) + ","
                else :
                    values_string += "\'"+str(line[exist[key]])+"\',"
            else :
                values_string += "null,"
                print (values_string)
        #print (values_string)

        ids_values = ids_values[:len(ids_values)-1]
        values_string = values_string[:len(values_string) - 1] # split the colons
        print (type(field))
        normal_table_insert += field + ") values (" + values_string + ")" #construct the final insert statment
        inserts.append(normal_table_insert)
        try:
            ids_insert=ids_insert+"ts"+",uid,"+ids_field[:len(ids_field)-1]+")values("+line[exist['ts']]+",\'"+line[exist['uid']]+"\',"+ids_values+")"
            inserts.append(ids_insert)
            print (ids_insert)
            # con.execute(ids_insert)

            if "insert into" in http_tags_insert:
                inserts.append(http_tags_insert)
                print (http_tags_insert)

            if "insert into" in http_proxied_insert:
                inserts.append(http_proxied_insert)
                print (http_proxied_insert)

            if "insert into " in http_orig_fuids_insert:
                inserts.append(http_orig_fuids_insert)
                print (http_orig_fuids_insert)

            if "insert into" in conn_tunnel_parents_insert:
                print ("fucking parent",conn_tunnel_parents_insert)
                inserts.append (conn_tunnel_parents_insert)

            if len (dns_answers_inserts) >0:
                    inserts.extend(dns_answers_inserts)

            if len(dns_ttls_inserts) > 0:
                    inserts.extend(dns_ttls_inserts)

        except Exception as a1:
            print (str(a1),'exception happend while appending')


        print(normal_table_insert)
        print ('returned tables')
        inserts.insert(0,main_insert)
        print (inserts)
        return inserts    # function will return a dictionary of insert statments
    #################################important segments of code ################################
    #a = con.execute('''insert into dates (d) values (?)''', (datetime.datetime.fromtimestamp(312312312.32112),))
    #  insert into db after normalizing epoch
    # SCREW QUOTATION MARKS RIGHT ?
    #con.execute("insert into time values('" + str(datetime.datetime.fromtimestamp(312312312.312312)) + "')")

    # con.execute('select * from dates where d <"2010-01-01 00:00:00"').fetchall() # selectbased on date and time and fetch from array
    # a=con.execute('select* from dates where d>"2000/00/00"' ) #select based on date only
    #################################important segments of code ################################

    # def SQLcreator2 (self,fname,line):  # this function creates insert statments for the IDs table
    #     command = "insert into ids (uid ,ts ,ID_ORIG_H, ID_ORIG_P, ID_RESP_H , ID_RESP_P ) VALUES ("
    #     values = line[validFields[fname]['uid']] +str(datetime.fromtimestamp(line[validFields[fname]['ts']])) +\
    #              line[validFields['ids']['id.orig_h']]+\
    #              int(line[validFields['ids']['id.orig_p']])+\
    #              line[validFields['ids']['id.resp_h']]+\
    #              int(line[validFields['ids']['id.resp_p']])+")"
    #     command = command + values
    #     return command


    def executeSQL(self):  # this function performs the SQL queries in the SQL panel
        command = self.textEdit.toPlainText().lower()
        select =insert =False  # indicates if the text area contains a select statment
        try:
            if "select" in command:
                select = True
                result = con.execute(command).fetchall()
                for i in result:
                    for each in i:
                        pass
                        # this lines should insert the result of select statments into the tableview

            if "insert" in command:  # THE PROGRAM SHOULD DISBLAY A WARNING IN CASE USER TRIED TO insert data into db
                self.message.setText("are you trying to insert data into DB ? \n "
                                     "the program prohibits the user from inserting data into db")
                insert=True
                raise sqlite3.OperationalError  # todo : define our own exception class
            else:
                con.execute(command)
                self.label_2.setStyleSheet("color: green")
                self.label_2.setText("operation succeded")
                self.label_2.show()

        except sqlite3.OperationalError as err:
            print(str(err))
            if select:
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
        if self.loaded:    #check if the program is already loaded with log files
            reply = QMessageBox.question(self.message, 'Message',
                                         "there is files already loaded into database ,are you sure you want to load files",
                                         QMessageBox.Yes,
                                         QMessageBox.No)  # shows a message box to user to  make sure of reloading files
            if reply == QMessageBox.Yes:
                self.reset()            # reset the GUI , clear line edit , clear database all tables
                map(droptables, tables) # dropping tables   # drop tables , function will return 0 incase of failure / exceptions were raised
            else:
                return
        if self.radioButton.isChecked() and self.lineEdit.text() != "":  # user choosed to load a single file
            fPath = self.lineEdit.text().split('/')  # split the DIR path to get file name
            fName = fPath[len(fPath) - 1]            # get file name
            path = '/'.join(fPath[:len(fPath) - 1])  # -1 since the right slicing operator is excluded
            print("123456",fName)
            print(fPath, path)
            os.chdir(path)             # change crwdir

            if  self.tableCreator(fName)==False:
                self.message.setText("error creating table " + str(fName))

            self.traverse(fName)

            # print(self.linesCount)


        elif self.radioButton_2.isChecked() and self.lineEdit_2.text() != "":   # user choosed to load multiple files

            progress = 100 / len(
                self.validFiles)  # not so accurate, progress bar will be filled according to progress in file , not according to line numbers
            for each in self.validFiles:
                each = str.lower(each)
                print(each)
                self.tableCreator(each)
                self.traverse(each)   # load every file in the dir
                self.progressBar.setValue(self.progressBar.value() + progress)
            self.analysis.setTabEnabled(1, True)   #enable plotting tab after loading
            self.analysis.setTabEnabled(2, True)  #enable query tab after loading
            self.loaded = True                      # this flag indicates the program and database are loaded with data
        else:
            self.message.setText("please specifiy a file to load or a directory")
            self.message.show()

    def switch1(self):  # functions switch1 and switch 2 disables the objects of GUI accoridng to radiobuttons
                        # disables the GUI components that allow user to load DIRs
        self.lineEdit_2.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.lineEdit.setDisabled(False)
        self.pushButton_2.setDisabled(False)

    def switch2(self):  # disables GUI components that allow loading single files
        self.lineEdit.setDisabled(True)
        self.pushButton_2.setDisabled(True)
        self.lineEdit_2.setDisabled(False)
        self.pushButton_3.setDisabled(False)

    def about(self):  # displays the about message if the user selected it from main menu
        self.message.setText(
            "this is a graduation project as a requirment for PSUT \n for more info visit the BitBucket link below")
        self.message.setDetailedText(
            "https://bitbucket.org/Psut/bro-ids-log-files-visualizer-and-analyzer\n"
            "https://tree.taiga.io/project/ahmadjd94-bila")
        self.message.show()
                    #todo : continue documentation
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

    def openDirDialog(self): # the following function provides the ability to open DIRs through dialog box
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
                    ui.linesCount += 1  # stores the total lines count of the DIR
                file.close()
            self.label.setText(
                "the directory you have selected have %s valid files with %s lines" % (
            str(len(self.validFiles)), str(ui.linesCount)))
            self.lineEdit_2.setText(dire)

        except  NotADirectoryError as e:  # exception raised if the selection was not a dir
            self.label.setText("make sure you are selecting a dir")
        #todo should raise an exception if the DIR has no valid logs
        except:
            self.label.setText("make sure you have selected a directory")

        finally:
            self.label.show()

    def reset(self):  # this function resets gui components if user tried to reload files
        self.progressBar.setValue(0)
        self.analysis.setTabEnabled(1, False)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
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
            else :
                return 0



    import sys
    import csv
    from datetime import datetime

    OriDir = os.getcwd()  # this variable will store the original
    historyLog = os.getcwd() + '/history.csv'

    types = {  # the foloowing dictionary denotes every field in log files with their data types

        # the following lines denote the types that require a set
        #################sets##############
        "tags": str,"proxied": str , "analyzers": str,
        "orig_fuid": str,"resp_meme_ty": str,"orig_meme_type": str,
        "conn_uids": str,"data_channel":str, "rcptto": str,
        "rx_hosts": str,"path": str, "tx_hosts": str,"validation_status": str,
         "name": str,"tunnel_parents": str, "TTLs": -1, "answers": str, "fuids": str,
        #################end of sets##############
        "uid": str, "ts":float, "id": str, "trans_depth": int, "method": str, "host": str, "uri": str,
        "referrer": str, "user_agent": str, "request_body_len": int, "status_code": int, "status_msg": str, "info_code": int,
         "info_msg": str, "username": str, "password": str, "command": str, "arg": str
        , "mime_type": str, "file_size": int, "reply_code": int, "reply_msg": str
        , "fuid": str, "source": str, "depth": int
        , "filename": str, "duration": str, "local_orig": bool, "is_orig": bool, "seen_bytes": int,
             "total_bytes": int
        , "missing_bytes": int, "overflow_bytes": int, "timedout": bool, "parent_fuid": str
        , "md5": str, "sha1": str, "sha256": str, "extracted": str
        , "nick": str, "user": str, "value": str, 'addi': str
        , "dcc_file_name": str, "dcc_file_size": int, "dcc_mime_type": str
        , 'trans_depth': int, "helo": str, "mailfrom": str
        , "from": str, "to": str, "reply_to": str, "msg_id": str, "in_reply_to": str, "subject": str
        , "x_originating_ip": str, "first_received": str
        , "second_received": str, "last_reply": str
        , "tls": bool, "is_webmail": bool
        , "status": str, "direction": str, "client": str, "server": str, "resp_size": int
        , "id.orig_h": str, "id.orig_p": int, "id.resp_h": str, "id.resp_p": int, "version": str, "cipher": str,
        "server_name": str, "session_id": str, "issuer_subject": str, "not_valid_before": str,
        "last_alert": str, "client_subject": str, "clnt_issuer_subject": str, "cert_hash": str
        , "notice": bool, "peer": str
        , "src_addr": str, "src_port": int, "dst_adr": str, "dst_port": int, "note": str, "sig_id": str
        , "event_msg": str, "sub_msg": str, "sig_count": int, "host_count": int
        , "id_resp_h": str, "id_resp_p": int, "proto": str, "service": str
        , "orig_bytes": int, "resp_bytes": int, "conn_state": str, "missed_bytes": int, "history": str, "orig_pkts": int
        , "orig_ip_bytes": int, "resp_pkts": int, "resp_ip_bytes": int, "orig_cc": str,
             "resp_cc": str
        , "mac": str, "assigned_ip": str, "lease_time ": str
        , "query": str, "qclass": int, "qclass_name": str, "qtype": int, "qtype_name": str, "rcode": int,
             "rcode_name": str
        , "QR": bool, "AA": bool, "TC": bool, "RD": bool, "RA": bool, "Z": int,
             "rejected bool": bool
             }  # end of types dictionary declaration

    validFields = {  #this line stores the indecies of the fields at each line for every log file type

        "http": {'uid': -1, 'ts': -1, "id.orig_h": -1, "id.orig_p": -1,
                 "id.resp_h": -1, "id.resp_p": -1, "trans_depth": -1,
                 "method": -1, "host": -1, "uri": -1, "referrer": -1,
                 "user_agent": -1, "request_body_len": -1, "status_code": -1,
                 "status_msg": -1, "info_code": -1,"info_msg": -1,
                 "filename":-1,"tags": -1, "username": -1,
                 "password": -1, "proxied": -1,
                 "orig_fuids": -1, "orig_meme_type": -1,
                 "orig_fuid": -1,"resp_meme_ty": -1},

        'ftp': {"uid": -1, "ts": -1, "id.orig_h": -1, "id.orig_p": .1, "id.resp_h": -1, "id.resp_p": -1,  "user": -1, "password": -1, "command": -1, "arg": -1,
                "mime_type": -1, "file_size": -1, "reply_code": -1, "reply_msg": -1,
                "data_channel": -1, "fuid": -1},

        "files": {"ts": -1, "fuid": -1, "tx_hosts": -1, "rx_hosts": -1, "conn_uids": -1, "source": -1, "depth": -1,
                  "analyzers": -1, "mime_type": -1,
                  "filename": -1, "duration": -1, "local_orig": -1, "is_orig": -1, "seen_bytes": -1, "total_bytes": -1,
                  "missing_bytes": -1, "overflow_bytes": -1, "timedout": -1, "parent_fuid": -1,
                  "md5": -1, "sha1": -1, "sha256": -1, "extracted": -1},  # check this again

        'irc': {"uid": -1, 'ts': -1, "id.orig_h": -1, "id.orig_p": -1, "id.resp_h": -1, "id.resp_p": -1,  "nick": -1, "user": -1, "command": -1, "value": -1, "addi": -1,
                "dcc_file_name": -1, "dcc_file_size": -1, "dcc_mime_type": -1, "fuid": 1},

        'smtp': {'ts': -1, 'uid': -1, "id.orig_h": -1, "id.orig_p": -1, "id.resp_h": -1, "id.resp_p": -1, 'trans_depth': -1, "helo": -1, "mailfrom": -1, "rcptto": -1
            , "date": -1, "from": -1, "to": -1, "reply_to": -1, "msg_id": -1, "in_reply_to": -1, "subject": -1
            , "x_originating_ip": -1, "first_received": -1
            , "second_received": -1, "last_reply": -1, "path": -1, "user_agent": -1
            , "tls": -1, "fuids": -1, "is_webmail": -1},

        'ssh': {"uid": -1,"id.orig_h": -1, "id.orig_p": -1, "id.resp_h": -1, "id.resp_p": -1,"status": -1, "direction": -1, "client": -1, "server": -1, "resp_size": -1},

        'ssl': {"uid": -1, "id.orig_h": -1, "id_orig_p": -1, "id.resp_h": -1, "id.resp_p": -1, "version": -1,
                "cipher": -1,
                "server_name": -1, "session_id": -1, "subject": -1,
                "issuer_subject": -1, "not_valid_before": -1,
                "last_alert": -1, "client_subject": -1, "clnt_issuer_subject": -1, "cert_hash": -1,
                "validation_status": -1},

        'weird': {"uid": -1,'ts':-1 ,"id.orig_h": -1, "id.orig_p": -1, "id.resp_h": -1, "id.resp_p": -1 , "name": -1, "addi": -1, "notice": -1, "peer": -1},

        'signatures': {"ts": -1, 'src_addr': -1,"id.orig_h": -1, "id.orig_p": -1, "id.resp_h": -1, "id.resp_p": -1,
                       'src_port': -1, 'dst_adr': -1, 'dst_port': -1, 'note': -1, 'sig_id': -1,
                       'event_msg': -1, 'sub_msg': -1, 'sig_count': -1, 'host_count': -1},
                    # THE FOLLOWING TABLES HAVE THE SUBSET OF CONN TABLE
                    #1 DHCP ,2 DNS,3 HTTP,4 IRC,5 FTP,6 SMTP,7 SSL,8 SSH,9 WEIRD
        'ids':{"id.orig_h": -1, "id.orig_p": -1, "id.resp_h": -1, "id.resp_p": -1},

        'conn': {'ts':-1,"uid": -1, "id.orig_h": -1, "id.orig_p": -1, "id.resp_h": -1, "id.resp_p": -1, "proto": -1,
                  "service": -1,
                  "duration": -1, "orig_bytes": -1,
                  "resp_bytes": -1, "conn_state": -1, "local_orig": -1, "missed_bytes": -1, "history": -1,
                  "orig_pkts": -1,
                  "orig_ip_bytes": -1, "resp_pkts": -1, "resp_ip_bytes": -1, "tunnel_parents": -1, "orig_cc": -1,
                  "resp_cc": -1},

        'dhcp': {"uid": -1, "id.orig_h": -1, "id.orig_p": -1, "id.resp_h": -1, "id.resp_p": -1, "mac": -1, "assigned_ip": -1, "lease_time ": -1, "trans_id": -1},

        'dns': {"uid": -1, 'ts': -1, "id.orig_h": -1, "id.orig_p": -1, "id.resp_h": -1, "id.resp_p": -1, "proto": -1, "trans_id": -1,
                "query": -1, "qclass": -1, "qclass_name": -1, "qtype": -1, "qtype_name": -1, "rcode": -1,
                "rcode_name": -1, "QR": -1,
                "AA": -1, "TC": -1, "RD": -1, "RA": -1, "Z": -1, "answers": -1, "TTLs": -1, "rejected": -1}
        # check tables strucutre !!! normalize conn_ID table
    }

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    tables = [ 'DHCP', "SMTP", "IRC", "WEIRD", "SSH", "CONN", "HTTP", "DNS", "SIGNATURE", "SSL", "IDS", "FILES"
                ,'SSH', 'SMTP_FUIDS','SMTP_PATHS','SMTP_TO','SMTP_RCPTO','SMTP_ANALYZERS'
                ,'FILES_CONN_UIDS','FILES_RX_HOSTS','FILES_TX_HOSTS',"CONN_TUNNEL_PARENTS"
                ,'SSL_VALIDATION_STATUS','MAIN','DNS_TTLS','DNS_ANSWERS'
                ,'HTTP_RESP_MEME_TYPES','HTTP_RESP_FUIDS','HTTP_ORIG_MEME_TYPES'
                ,'HTTP_ORIG_FUIDS','HTTP_PROXIED_HEADERS','HTTP_TAGS']  # this list declares every table in the database
    try:

        con = sqlite3.connect('analyze2.db')  # initializing connection to DB // should be in UI init ??
        print("connected")
        dropped = map(droptables, tables)  # fix ? dropping tables
        drop_result=list(dropped.__iter__())   # returns the results of the map

        dropped={}
        for i in range (len(drop_result)):
            dropped[tables[i]]=drop_result[i]

        for i in dropped :
            print (i,dropped[i])

        table_created ={ }
        for i in tables :
            table_created[i]=False
        print (table_created)
        print( "this is dropped tables ")  # fix ?

        # print(tables - dropped + "non dropped tables ") #fix ?
        try:
            con.execute("CREATE TABLE main (uid TEXT , ts int ) ")#PRIMARY KEY(uid,ts) )") #creating main table
            table_created['MAIN']=True
            print ("Success creating main table")

        except:
            print("error dropping main ?")

        if "history.csv" in os.listdir():  # creating a new history.csv if the program is executed for the first time
                                            # todo : logging into csv should add files paths
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