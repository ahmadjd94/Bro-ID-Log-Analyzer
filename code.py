# -*- coding: utf-8 -*-
#fewfew
# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!
"""project's backlog : https://tree.taiga.io/project/ahmadjd94-bila """
from BilaTypes import BilaTypes
import networkx as nx
import re
import pygraphviz as pgv
from DBconnection import *
from BilaFieldIndecies import validFields
from PyQt5 import QtCore, QtGui, QtWidgets,QtSql
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication, QMessageBox,QSizePolicy)
from networkx import draw_networkx_edge_labels as delnx
from Functions import SQLcreator,tableCreator
from Tables import table_created,WeirdFlags
from Queries import QueryStatment
from mmap import *
from PredefnedQueries import initQueries
from random import randint
import numpy
import Tables
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import patches
import random
from PyQt5.QtGui import QIcon

# module used for changing Current working directory of the program
import fnmatch  # module used for matching files names
# import pyqtgraph as pg
import hashlib, codecs, operator, sqlite3, os,time
#hashlib used to use MD5 , codecs , converting strings to bytes , sqlite3 to use db , os to use DIRs ,

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=8, dpi=100):
        fig = plt.figure(figsize=(height, width),facecolor='#333333',edgecolor='#ff9900')

        # ax = fig.gca()

        labels = list(linescount.keys())
        sizes = []
        colors = []
        indexes = list(linescount.keys())
        for i in linescount.keys():
            sizes.append(linescount[i] / ui.linesCount)
            color = indexes.index(i)
            colors.append(Tables.defaultColors[color])

            # explode = (0.1, 0, 0, 0)  # explode 1st slice

        # Plot, explode=explode

        self.pie = plt.pie(sizes, labels=labels, colors=colors,
                           autopct='%1.1f%%', shadow=True, startangle=140)
        print (self.pie)
        # self.pie.legendcolor
        # Set aspect ratio to be equal so that pie is drawn as a circle.
        plt.axis('equal')
        patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=140)
        plt.legend(patches, labels, loc=(0,0))
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent.tab_2)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        # [s.set_color("#333333") for s in self.pie.gca().get_xticklabels()]
        # self.axes.s
        # ax.set_xticks([0, 1])
        # ax.set_yticks([0, 1])

        # ax.set_xlim((-0.5, 1.5))
        # ax.set_ylim((-0.5, 1.5))

        # Set aspect ratio to be equal so that pie is drawn as a circle.
        # ax.set_aspect('equal')
        # plt.draw()

class PlotGraph(FigureCanvas):
    global connection
    def __init__(self, parent=None, width=5, height=8, dpi=100):
        fig = plt.figure(figsize=(width,height),facecolor='#333333',edgecolor='#ff9900')
        query='SELECT ORIG_H,RESP_H FROM ids'
        result=connection.DBquery.exec_(query)
        graph=nx.Graph()

        while connection.DBquery.next():
            print (connection.DBquery.value(0))
            graph.add_node(connection.DBquery.value(0))
            graph.add_node(connection.DBquery.value(1))
            graph.add_edge(connection.DBquery.value(0),connection.DBquery.value(1))
        nx.draw_networkx(graph)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent.container)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

class PlotBars(FigureCanvas):
    global connection
    def __init__(self, parent=None, width=5, height=7, dpi=100):
        fig = plt.figure(figsize=(width,height),facecolor='#333333',edgecolor='#ff9900')
        results={}
        for i in WeirdFlags :
            qu="select count  (name) from weird where name=\'"+i+"\'"
            print (qu)
            connection.DBquery.exec_(qu)
            while connection.DBquery.next():
                  print (connection.DBquery.value(0))
                  results[i]=connection.DBquery.value(0)
        self.barh = plt.bar(range(len(results)),results.values(),align='center')

        plt.xticks(range(len(results)), results.keys())
        print (results)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent.container)

        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        plt.tight_layout(1.0)

class DirectedPlotGraph(FigureCanvas):
    global connection
    from networkx import draw_networkx_edge_labels as delnx
    def onpick (self,*args):
        print ("hovering")

    def __init__(self, parent=None, width=5, height=8, dpi=100,file_output=False):
        print (file_output)
        fig = plt.figure(figsize=(width,height),facecolor='#333333',edgecolor='#ff9900')
        query='SELECT ORIG_H,RESP_H FROM ids'

        result=connection.DBquery.exec_(query)
        graph=nx.DiGraph()

        # edge_labels=[];i=0
        # pos = nx.spring_layout(graph)
        if result :
            while connection.DBquery.next():
                # i+=1
                print (connection.DBquery.value(0))
                graph.add_node(connection.DBquery.value(0))
                graph.add_node(connection.DBquery.value(1))
                if graph.has_edge(connection.DBquery.value(0),connection.DBquery.value(1)):
                    graph[connection.DBquery.value(0)][connection.DBquery.value(1)]['weight']+=1
                    print("has edge")
                else:
                    graph.add_edge(connection.DBquery.value(0), connection.DBquery.value(1), weight=1)
                    print ("has no edge")
                # edge_labels.append(i)
        sever_response="select resp_h ,orig_h from ids"

        result = connection.DBquery.exec_(sever_response)
        if result :
            while connection.DBquery.next():
                print(connection.DBquery.value(0))
                # graph.add_node(connection.DBquery.value(0))
                # graph.add_node(connection.DBquery.value(1))
                graph.add_edge(connection.DBquery.value(0), connection.DBquery.value(1),color="r")
        pos = nx.circular_layout(graph)
        nx.draw_networkx(graph,pos)
        labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph,pos,labels)
        print ((graph.out_degree([0,1])))
        if file_output:
            filegraph=nx.nx_agraph.to_agraph(graph)
            filegraph.layout(prog="circo")
            filegraph.draw('dns.png')
        FigureCanvas.__init__(self, fig)
        self.setParent(parent.container)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        fig.canvas.mpl_connect("button_press_event" , self.onpick)


class Ui_MainWindow(object):  # Qt and PYUIC creator generated functions and classes

    ################################  defining global variable ###################################
    global table_created  # connection to DB
    global AllowedQueries
    global connection

    linesCount = 0  # count of lines
    loaded = False  # this variable stores if there is a file loaded into program or not
    validFiles = []  # this list stores the valid file found in a DIR
    UnsupportedFiles=Tables.UnsupportedFiles
    valid=Tables.valid
    currentQuery=None

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(759, 518)
        self.single = False  # indicates if user is dealing with a signle file / DIR
        MainWindow.setStyleSheet("background-color: rgb(51, 51, 51);")
        self.progress = 0  # indicate the level of progress bar
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.message = QtWidgets.QMessageBox()
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
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
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
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit.setReadOnly(True)
        self.lineEdit_2.setReadOnly(True)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(140, 340, 430, 17))
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(616, 99, 29, 27))
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
        self.container =QtWidgets.QGraphicsView()
        self.container.setParent(self.tab_2)
        self.container.setGeometry(20,80,700,300)
        self.container.setStyleSheet("""
                                        border-color:rgb(255,153,0 );\n
                                        background - color:  # 333333;""")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(600, 390, 97, 27))
        self.pushButton_4.setStyleSheet("background-color: rgb(186, 186, 186);\n"
                                        "border-color: rgb(0, 0, 0);\n"
                                        "color: rgb(0, 0, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(0,0,400,20))
        self.label_4.setStyleSheet("color:red;\n"
                                   "border-color:rgb(255, 153, 0 );\n"
                                   "")
        self.analysis.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.model = QtWidgets.QTableWidget(self.tab_3)
        self.model.setGeometry(QtCore.QRect(60, 150, 641, 291))
        self.model.setStyleSheet("background-color: grey;\n"
                                 "border-color: rgb(0, 0, 0);")
        self.model.setObjectName("graphicsView")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(64, 136, 59, 14))
        self.label_3.setObjectName("label_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(500, 50, 141, 27))
        self.pushButton_5.setStyleSheet("background-color: rgb(186, 186, 186);\n"
                                        "color: rgb(0, 0, 0);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(480, 100, 191, 20))
        self.label_2.setStyleSheet("color: rgb(68, 206, 0);\n"
                                   "border-color:rgb(255, 153, 0 );\n"
                                   "")
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 390, 161, 22))
        self.comboBox.setGeometry(QtCore.QRect(60, 50, 351, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(480, 100, 191, 20))
        self.label_2.setStyleSheet("color: rgb(68, 206, 0);\n"
                                   "border-color:rgb(255, 153, 0 );\n"
                                   "")
        self.label_2.setObjectName("label_2")

        self.analysis.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
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
        self.menuBar.setNativeMenuBar(False)

        self.retranslateUi(MainWindow)
        self.analysis.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.SQLcreator = SQLcreator
        self.currentQuery
        # self.dbu=DB
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("small logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowTitle(_translate("MainWindow", "BILA"))
        self.radioButton.setText(_translate("MainWindow", "load single file"))
        self.radioButton_2.setText(_translate("MainWindow", "load directory of log files"))
        self.pushButton.setText(_translate("MainWindow", "Load"))
        self.label.setVisible(False)
        self.label.setText(_translate("MainWindow", "unable to load file , please check your file directory"))
        self.pushButton_2.setText(_translate("MainWindow", "..."))
        self.pushButton_3.setText(_translate("MainWindow", "..."))
        self.analysis.setTabText(self.analysis.indexOf(self.tab), _translate("MainWindow", "Load Files"))
        self.analysis.setTabText(self.analysis.indexOf(self.tab_2), _translate("MainWindow", "files statistics"))
        self.menuBRO_visualizer.setTitle(_translate("MainWindow", "BRO visualizer"))
        self.menuHelp.setTitle(_translate("MainWindow", "help"))
        #        self.mainToolBar.setWindowTitle(_translate("MainWindow", "BRO Log file analyzer and visualizer"))
        self.pushButton_5.setText(_translate("MainWindow", "Execute Command"))
        self.analysis.setTabText(self.analysis.indexOf(self.tab_3), _translate("MainWindow", "SQL commands "))
        self.actionAbout.setText(_translate("MainWindow", "about"))
        self.label_2.setStyleSheet("color : green")
        self.pushButton_4.setText(_translate("MainWindow", "draw timeline"))
        self.label_2.setVisible(False)
        self.label_4.setText("")
        self.label_4.setVisible(True)
        self.comboBox.setToolTip(
        _translate("MainWindow", "<html><head/><body><p>select a predefined query to execute</p></body></html>"))
        self.analysis.setTabEnabled(1, True)
        self.comboBox.setStyleSheet("QComboBox { combobox-popup: 0; }")
        # self.analysis.setTabEnabled(2,False)
        self.radioButton.clicked.connect(self.switch1)  # connect event click to function switch1
        self.radioButton_2.clicked.connect(self.switch2)  # connect event click to function switch2)
        self.pushButton_2.clicked.connect(self.openFileDialog)  # connect event click to function openfile dialog
        self.actionAbout.triggered.connect(self.about)  # connect event triggered to function about
        self.lineEdit.textChanged.connect(self.openFile)  # connect event text-changed to function openFile
        self.pushButton_3.clicked.connect(self.openDirDialog)  # connect event click to function openDirDialog
        self.pushButton.clicked.connect(self.load)  # # connect event click to function load
        self.pushButton_4.clicked.connect(self.pier)
        # self.textEdit.textChanged.connect(self.uMan)
        self.pushButton_5.clicked.connect(self.executeSQL)
        self.comboBox.currentIndexChanged.connect(self.selected_query)
        self.tab_2.setEnabled(True)
        self.tab_3.setEnabled(False)
        self.comboBox_2.addItem('--select a plot type--')
        self.comboBox_2.addItem('files statistics')
        self.comboBox_2.addItem('connections graph')
        self.comboBox_2.addItem('weird bars')
        self.comboBox_2.addItem('DNS Graph')
        self.radioButton.click()
        self.m = None

    def pier(self):

        if self.comboBox_2.currentText()=='--select a plot type--':
            self.label_4.setText('please select a valid option')
        elif self.comboBox_2.currentText()=='files statistics':
            if self.single==True:
                self.label_4.setText('files statistics not available in single files mode')
                self.label_4.show()
                return
            # Data to plot
            else :
                self.label_4.setVisible(False)
                self.m=PlotCanvas(self, width=9, height=3)

                self.m.show()
        elif self.comboBox_2.currentText() == 'connections graph':

            self.m = PlotGraph(self,width=9, height=4)
            toolbar=NavigationToolbar(canvas=self.m, parent=self.container)
            self.m.toolbar.show()
            print(self.m.get_width_height())
            self.m.show()
        elif self.comboBox_2.currentText() == 'weird bars':
            self.m = PlotBars(self, width=9, height=4)
            toolbar = NavigationToolbar(canvas=self.m, parent=self.container)
            self.m.toolbar.show()
            self.m.show()
        elif self.comboBox_2.currentText() == 'DNS Graph':
            reply = QMessageBox.question(self.message, 'Message',
                                         "due to NetworkX module limitation BILA can render the network in a "
                                         "clearer format as image file file\n"
                                         "would you like to render the result in a seperate file ?",
                                         QMessageBox.Yes,
                                         QMessageBox.No)  # shows a message box to user to  make sure of reloading files
            if reply == QMessageBox.Yes:
                self.m = DirectedPlotGraph(self, width=9, height=4,file_output=True)
            else:
                self.m = DirectedPlotGraph(self, width=9, height=4, file_output=False)
            toolbar = NavigationToolbar(canvas=self.m, parent=self.container)
            self.m.toolbar.show()
            self.m.show()


    def uMan(self):
        self.label_2.setVisible(False)

    def valuefilter(self, num):
        if num != -1:
            return True
        else:
            return False

    def traverse(self, fname):  # this function will traverse the file that is based to it
        global connection

        # if the field value is -1 , the field should be neglected )

        try:
            #fname = (fname.split('.')[0])  # this statment splits the fname and neglects the .log part of it

            hashtemp = ""  # this variable stores the entire log file to calculate it's hash value

            if fname in os.listdir():
                print('yes')
            fil = open(fname , 'r+')  # open the log file Read-Only mode
            #IF FILED IN ID AND FNAME != 'CONN' : DO NOT EXECUTE SECOND INSERT STATMENT
            f1=mmap(fil.fileno(),0,flags=MAP_PRIVATE,prot=PROT_WRITE)
            readline=f1.readline
            i =codecs.decode(readline(),'ascii')
            while i !='' or '' not in i:     # todo : modify function to increase the progress bar

                hashtemp += i  # concatenate the lines being read to the string

                if i[:7] == "#fields" or i[:7] == "Fields":  # field loading algorithm
                    # i = i.lower()  # ignore the case of the fields line
                    fields = (i[7:].split())
                    fname=(fname.split('.')[0])
                    for field in fields:
                        if field in validFields[fname]:

                            try:
                                validFields[fname][field] = fields.index(field)  # this line stores the index of field in the dictionary
                            except :
                             print ('error')
                        print(fields.index(field), field)


                    try :
                        validFields[fname] = sorted(validFields[fname].items(), key=operator.itemgetter(1)) # needs review , is this important ?
                    except:
                        print ('already sorted ?')

                elif i[0] != "#":  # this line ignores the log lines that start with # , #indecates a commented line
                    line=i.replace("\n",'')  # remove newlines escape character
                    line = line.split('\t')  #split file lines by tabs
                    # sort dictionary based on key values
                    try:
                        sql_commands=(self.SQLcreator(fname, line)) # call the SQL creator function which generates queries and return an array if queries
                        for command in sql_commands:                #execute each insert statment returned by the sqlcreator func
                            try :
                                connection.DBquery.exec_ (command)
                                connection.db_connection.commit()
                            except Exception as excc111:
                                print (excc111)

                        # sql_command_ids=(self.SQLcreator2(line))  #this line stores command for other secondary normalized tables
                        # DBquery.exec_(sql_command,sql_command_ids)
                    except Exception as exc1:
                        print('error creating SQL',str (exc1))
                i = codecs.decode(readline(), 'ascii')

                # i=fil.readline()
                    #print(sql_command)
                    # no hardcoded indecies of
                    # fields  / PYTHON HAS NO SWITCH SYNTAX SO we used if statments

                self.progress += 1
                self.progressBar.setValue((self.progress / self.linesCount) * 100)
            f1.close()


            with open(historyLog, 'a') as csvfile1:  # open log file to log the state of operation

                digestive = hashlib.md5(codecs.encode(hashtemp,'ascii'))  # string must be converted to bytes to calculate hash
                wr1 = csv.writer(csvfile1, delimiter=',')
                # calculate the hash of the file
                # this block is only performed when no exceptions happen , all of data inserted into DB successfully
                try:                                #TODO :  issue resolved to be ready for test once the master sprint starts
                    wr1.writerow((fname, digestive.hexdigest()))   # write the file name , with it's hash value incase it was loaded successfully

                except Exception as exc2:
                    print ('exception in writing the hash of the file',str(exc2))


        except Exception as exc3:  # this block is executed in case of failure of instering
            print(str(exc3))
            with open(historyLog, 'a') as csvfile:
                wr1 = csv.writer(csvfile, delimiter=',')
                wr1.writerow((fname, "FAILED"))

    def selected_query(self):
        self.clear_table()
        for i in AllowedQueries:
            for query in i:
                if query.Query == self.comboBox.currentText():
                    self.currentQuery = query
                    print(query.Headers[0])
                    self.model.setColumnCount(len(query.Headers[0]))
                    self.model.setHorizontalHeaderLabels(query.Headers[0])
                    self.model.show()

    def clear_table(self):
        while(self.model.rowCount()>0):
            self.model.removeRow(0)

    def setup_combobox(self):
        try:
            print (type(AllowedQueries))
            print (AllowedQueries)
            try :
                for obj in AllowedQueries:
                    for query in obj:
                        self.comboBox.addItem(query.Query)
                        print (query.Query)
                self.comboBox.setEnabled(True)
            except Exception as s1:
                print (s1)

        except Exception as A:
            print('eroro adding to combo box ', A)


    def executeSQL(self):  # this function performs the SQL queries in the SQL panel
        self.clear_table()
        command = self.comboBox.currentText()
        try:
            connection.DBquery.exec_(command)
            self.model.setRowCount(0)
            rowcount=0
            while connection.DBquery.next():
                    self.model.insertRow(rowcount)
                    result=''
                    for count in range (len(self.currentQuery.Headers[0])):
                        self.model.setItem(rowcount,count,QtWidgets.QTableWidgetItem(str(connection.DBquery.value(count))))
                        result+= str(connection.DBquery.value(count))
                    rowcount+=1

            self.label_2.setStyleSheet("color: green")
            self.label_2.setText("operation succeded")
            self.label_2.show()

        except sqlite3.OperationalError as err:
            self.message.setText("error selecting rows from data base")
            self.message.setDetailedText(str(err))
            self.label_2.setText("error executing SQL command")
            self.label_2.setStyleSheet("color : red")
            self.label_2.setVisible(True)
            self.message.show()

        except Exception as death:
            self.message.setDetailedText(str (death))
            self.message.show()

    def load(self):
        if self.loaded:    #check if the program is already loaded with log files
            reply = QMessageBox.question(self.message, 'Message',
                                         "there is files already loaded into database ,are you sure you want to load files",
                                         QMessageBox.Yes,
                                         QMessageBox.No)  # shows a message box to user to  make sure of reloading files
            if reply == QMessageBox.Yes:
                self.reset()            # reset the GUI , clear line edit , clear database all tables
                # map(droptables, tables) # dropping tables   # drop tables , function will return 0 incase of failure / exceptions were raised
                self.load_files(connection)

            else:
                return
        else :
            self.load_files(connection)

    def load_files(self,connection):  # this function loads the content of the log files into the DB

        self.tab_3.setEnabled(True)
        if self.radioButton.isChecked() and self.lineEdit.text() != "":  # user choosed to load a single file
            fPath = self.lineEdit.text().split('/')  # split the DIR path to get file name
            fName = fPath[len(fPath) - 1]            # get file name
            path = '/'.join(fPath[:len(fPath) - 1])  # -1 since the right slicing operator is excluded
            os.chdir(path)             # change crwdir

            if table_created[fName.split('.')[0]] == False:
                if fName.split('.')[0] in ['weird','dns','conn','http','dhcp','irc','ssl'] :
                    if table_created['ids']==False:
                        ids_creation_statment = tableCreator('ids')
                        try:
                            connection.DBquery.exec_(ids_creation_statment)
                            table_created['ids'] == True
                        except:
                            table_created['ids'] == False
                    queries =tableCreator(fName)
                    for key in list(queries.keys()):
                        connection.DBquery.exec_(queries[key])
                        table_created[key]=True

                else :
                    queries = tableCreator(fName)
                    for key in queries.keys():
                        connection.DBquery.exec_(queries[key])
                        table_created[key] = True
            AllowedQueries.append(initQueries(fName.split('.')[0]))
            self.traverse(fName)
            self.setup_combobox()

        elif self.radioButton_2.isChecked() and self.lineEdit_2.text() != "":   # user choosed to load multiple files
            for each in self.validFiles:
                each = str.lower(each)
                AllowedQueries.append(initQueries(each.split('.')[0]))
                if table_created[each.split('.')[0]] == False:
                    if each.split('.')[0] in ['weird', 'dns', 'conn', 'http', 'dhcp', 'irc', 'ssl'] and \
                                    table_created['ids'] == False:
                        ids_creation_statment = tableCreator('ids')
                        connection.DBquery.exec_(ids_creation_statment)
                        queries = tableCreator(each.split('.')[0])
                        for query in queries.keys():
                            connection.DBquery.exec_(queries[query])
                            table_created[query] = True

                    else:
                        queries = tableCreator(each.split('.')[0])
                        for query in queries.keys():
                            connection.DBquery.exec_(queries[query])
                            table_created[query] = True
                self.traverse(each)   # load every file in the dir
                print (each,"wtffffff")

            self.setup_combobox()
            self.analysis.setTabEnabled(1, True)   #enable plotting tab after loading
            self.loaded=True
            self.tab_2.setEnabled(True)
            self.analysis.setTabEnabled(2, True)  #enable query tab after loading
            # self.loaded = True                      # this flag indicates the program and database are loaded with data
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

    def openFile(self):  # function used to open files (single files and files inside working directory )
        global connection
        self.label.setVisible(False)
        self.single = True
        try:
            directory = self.lineEdit.text()[:len(self.lineEdit.text())-self.lineEdit.text()[::-1].index('/')]
            print (directory)
            os.chdir(directory)
            path = self.lineEdit.text().split('/')
            name = path[len(path) - 1]
            if name in self.valid:
                file = open(self.lineEdit.text())
                self.count = 0
                for line in file:
                    self.linesCount += 1
                file.close()
                self.label.setText("the selected file has " + str(self.count) + " lines")
                self.label.setVisible(True)
                try:
                    dir_files = (os.listdir())
                    for file in dir_files:
                        if re.match('BILA %s[\d]{4}-\d\d-\d\d\ \d\d\:\d\d\:\d\d\.db'%name, file):
                            self.message.setWindowTitle("DB file exists ! ")
                            self.message.setText(file+
                                " is A SQLITE database file was found.\nmake sure you rename the file or consider loading it through the files menu")
                            self.message.show()
                    print("current files in the dir")
                    connection = DbConnection('BILA '+name + datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S.db'))

                except PermissionError as DB1:
                    self.message = QMessageBox('error while creating database file')
                    self.message.show()
                    print(str(DB1) + 'database craetion error ')
                except Exception as DB:
                    print(str(DB) + 'wtf ')

            elif name in self.UnsupportedFiles:
                self.message.setText("BILA does not currently support the file you are trying to use")
                self.message.show()
                self.lineEdit.clear()
            else:
                self.message.setText("make sure you are trying to load a valid log files")
                self.message.show()
                self.lineEdit.clear()

        except:  # handling incorrect file directories / paths
            self.label.show()

    def openFileDialog(self):  # displays open file dialog for user to select the required log file
        global connection
        self.single = False
        fname = QFileDialog.getOpenFileName(None, 'Open file', '/home', '*.log')  # error in params
        print(fname)
        self.lineEdit.setText(fname[0])
        try:
            file = open(fname[0])
            ui.linesCount = 0
            for line in file:
                ui.linesCount += 1
            self.label.setText("the selected file has " + str(ui.linesCount) + " lines")
            self.label.setVisible(True)
            file.close()
            self.lineEdit.setText(fname[0])

        except FileNotFoundError:
            self.label.show()

    def openDirDialog(self): # the following function provides the ability to open DIRs through dialog box
        global connection
        ui.linesCount=0
        self.validFiles=[]
        self.single=False
        try:
            dire = QFileDialog.getExistingDirectory(None, 'open dir of log files', '/home',
                                                    QFileDialog.ShowDirsOnly)  # error in params
            os.chdir(dire)  # change current working directory


            files = (os.listdir())  # make a list of files inside current working dir
            for each in files:
                if each in self.valid:
                    self.validFiles.append(each)  # appends BRO valid log files names to the discovered logs
            for each in self.validFiles:
                file = open(each, 'r')
                linescount[each]=0
                line_sum = 0
                for line in file:
                    line_sum +=1
                    ui.linesCount += 1  # stores the total lines count of the DIR
                linescount[each]=line_sum
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
        try :
            dir_files= ( os.listdir())
            for file in dir_files:
                if re.match('BILA [\d]{4}-\d\d-\d\d \d\d:\d\d:\d\d\.db',file):
                    self.message.setWindowTitle("DB file exists ! ")
                    self.message.setText("A SQLITE database file was found.\nmake sure you rename the file or consider loading it through the files menu ")
                    self.message.show()
            print("current files in the dir")
            connection=DbConnection('BILA '+datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S.db'))

        except PermissionError as DB1:
            self.message1=QMessageBox('error while creating database file')
            self.message1.show()
            print(str(DB1) + 'database craetion error ')
        except Exception as DB:
            print (str (DB)+'wtf ')

    def reset(self):  # this function resets gui components if user tried to reload files
        self.progressBar.setValue(0)
        self.progress=0
        self.analysis.setTabEnabled(1, False)
        for key in  (table_created.keys()):
            table_created[key]=False
        connection.DBquery.exec_("CREATE TABLE main (uid TEXT , ts int ) ")  # PRIMARY KEY(uid,ts) )") #creating main table
        table_created['main'] = True
        # todo : drop tables
        # todo  reset timeline


# def droptables(table):  # a map function drops tables , return 1 on success
#     try:
#         DBquery.exec_("drop table %s" % table)
#         DBconnection.commit()
#         return 1
#     except sqlite3.OperationalError as a:
#         if "no such table" in str(a):
#             return 0
#         else:
#             return 0
if __name__ == "__main__":  # main module
    import sys
    import csv
    from datetime import datetime
    global connection
    linescount = {}
    tables=Tables.tables
    normalized_tables=Tables.normalized_tables
    AllowedQueries = []
    OriDir = os.getcwd()  # this variable will store the original
    historyLog = os.getcwd() + '/history.csv'
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    try:
        if "history.csv" in os.listdir():  # creating a new history.csv if the program is executed for the first time
                                            # todo : logging into csv should add files paths
            with open(historyLog, 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["new session", str(datetime.now())[:19]])
        else:
            f = open(historyLog, "w")
            f.close()
            with open(historyLog, 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["new session", str(datetime.now())[:19]])


    except sqlite3.Error as e:
        print(e)
        print("error")

        ui.__message2__.show()

    sys.exit(app.exec_())
