# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bbTriggerBoxx_UI.ui'
#
# Created: Sun May 11 16:51:06 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow_bbTriggerBoxx(object):
    def setupUi(self, MainWindow_bbTriggerBoxx):
        MainWindow_bbTriggerBoxx.setObjectName(_fromUtf8("MainWindow_bbTriggerBoxx"))
        MainWindow_bbTriggerBoxx.resize(738, 435)
        self.centralwidget = QtGui.QWidget(MainWindow_bbTriggerBoxx)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.tabWidget_master = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget_master.setObjectName(_fromUtf8("tabWidget_master"))
        self.tab_project = QtGui.QWidget()
        self.tab_project.setObjectName(_fromUtf8("tab_project"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_project)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.radioButton_mesh = QtGui.QRadioButton(self.tab_project)
        self.radioButton_mesh.setObjectName(_fromUtf8("radioButton_mesh"))
        self.horizontalLayout_3.addWidget(self.radioButton_mesh)
        self.radioButton_texture = QtGui.QRadioButton(self.tab_project)
        self.radioButton_texture.setObjectName(_fromUtf8("radioButton_texture"))
        self.horizontalLayout_3.addWidget(self.radioButton_texture)
        spacerItem = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.tab_project)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_projectRoot = QtGui.QLineEdit(self.tab_project)
        self.lineEdit_projectRoot.setMinimumSize(QtCore.QSize(81, 0))
        self.lineEdit_projectRoot.setObjectName(_fromUtf8("lineEdit_projectRoot"))
        self.horizontalLayout_3.addWidget(self.lineEdit_projectRoot)
        self.label_6 = QtGui.QLabel(self.tab_project)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.lineEdit_photoDownload = QtGui.QLineEdit(self.tab_project)
        self.lineEdit_photoDownload.setMinimumSize(QtCore.QSize(160, 0))
        self.lineEdit_photoDownload.setObjectName(_fromUtf8("lineEdit_photoDownload"))
        self.horizontalLayout_3.addWidget(self.lineEdit_photoDownload)
        spacerItem1 = QtGui.QSpacerItem(48, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.treeView_diskMap = QtGui.QTreeView(self.tab_project)
        self.treeView_diskMap.setEnabled(True)
        self.treeView_diskMap.setObjectName(_fromUtf8("treeView_diskMap"))
        self.verticalLayout.addWidget(self.treeView_diskMap)
        self.tabWidget_master.addTab(self.tab_project, _fromUtf8(""))
        self.tab_capture = QtGui.QWidget()
        self.tab_capture.setObjectName(_fromUtf8("tab_capture"))
        self.gridLayout = QtGui.QGridLayout(self.tab_capture)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_structure = QtGui.QGroupBox(self.tab_capture)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_structure.setFont(font)
        self.groupBox_structure.setCheckable(False)
        self.groupBox_structure.setObjectName(_fromUtf8("groupBox_structure"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_structure)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_11 = QtGui.QLabel(self.groupBox_structure)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_4.addWidget(self.label_11)
        self.lineEdit_shootday = QtGui.QLineEdit(self.groupBox_structure)
        self.lineEdit_shootday.setReadOnly(True)
        self.lineEdit_shootday.setObjectName(_fromUtf8("lineEdit_shootday"))
        self.horizontalLayout_4.addWidget(self.lineEdit_shootday)
        self.label_10 = QtGui.QLabel(self.groupBox_structure)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_4.addWidget(self.label_10)
        self.lineEdit_bucket = QtGui.QLineEdit(self.groupBox_structure)
        self.lineEdit_bucket.setObjectName(_fromUtf8("lineEdit_bucket"))
        self.horizontalLayout_4.addWidget(self.lineEdit_bucket)
        self.gridLayout.addWidget(self.groupBox_structure, 0, 0, 1, 1)
        self.groupBox_take = QtGui.QGroupBox(self.tab_capture)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_take.setFont(font)
        self.groupBox_take.setObjectName(_fromUtf8("groupBox_take"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_take)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_5 = QtGui.QLabel(self.groupBox_take)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.spinBox_take = QtGui.QSpinBox(self.groupBox_take)
        self.spinBox_take.setFrame(True)
        self.spinBox_take.setMinimum(1)
        self.spinBox_take.setObjectName(_fromUtf8("spinBox_take"))
        self.horizontalLayout_2.addWidget(self.spinBox_take)
        self.checkBox_inc = QtGui.QCheckBox(self.groupBox_take)
        self.checkBox_inc.setChecked(True)
        self.checkBox_inc.setObjectName(_fromUtf8("checkBox_inc"))
        self.horizontalLayout_2.addWidget(self.checkBox_inc)
        spacerItem2 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_9 = QtGui.QLabel(self.groupBox_take)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_2.addWidget(self.label_9)
        self.lineEdit_comment = QtGui.QLineEdit(self.groupBox_take)
        self.lineEdit_comment.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_comment.setText(_fromUtf8(""))
        self.lineEdit_comment.setReadOnly(False)
        self.lineEdit_comment.setObjectName(_fromUtf8("lineEdit_comment"))
        self.horizontalLayout_2.addWidget(self.lineEdit_comment)
        self.gridLayout.addWidget(self.groupBox_take, 0, 1, 1, 1)
        self.groupBox_logging = QtGui.QGroupBox(self.tab_capture)
        self.groupBox_logging.setObjectName(_fromUtf8("groupBox_logging"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_logging)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.textEdit_logging = QtGui.QTextEdit(self.groupBox_logging)
        self.textEdit_logging.setObjectName(_fromUtf8("textEdit_logging"))
        self.verticalLayout_2.addWidget(self.textEdit_logging)
        self.gridLayout.addWidget(self.groupBox_logging, 2, 0, 1, 1)
        self.groupBox_control = QtGui.QGroupBox(self.tab_capture)
        self.groupBox_control.setObjectName(_fromUtf8("groupBox_control"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_control)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.groupBox_control)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.spinBox_cams = QtGui.QSpinBox(self.groupBox_control)
        self.spinBox_cams.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_cams.setMinimum(1)
        self.spinBox_cams.setMaximum(250)
        self.spinBox_cams.setProperty("value", 100)
        self.spinBox_cams.setObjectName(_fromUtf8("spinBox_cams"))
        self.gridLayout_2.addWidget(self.spinBox_cams, 0, 1, 1, 1)
        self.pushButton_prime = QtGui.QPushButton(self.groupBox_control)
        self.pushButton_prime.setMinimumSize(QtCore.QSize(0, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_prime.setFont(font)
        self.pushButton_prime.setObjectName(_fromUtf8("pushButton_prime"))
        self.gridLayout_2.addWidget(self.pushButton_prime, 1, 0, 1, 2)
        self.pushButton_fire = QtGui.QPushButton(self.groupBox_control)
        self.pushButton_fire.setMinimumSize(QtCore.QSize(0, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton_fire.setFont(font)
        self.pushButton_fire.setObjectName(_fromUtf8("pushButton_fire"))
        self.gridLayout_2.addWidget(self.pushButton_fire, 2, 0, 1, 2)
        self.lcdNumber_countdown = QtGui.QLCDNumber(self.groupBox_control)
        self.lcdNumber_countdown.setSmallDecimalPoint(False)
        self.lcdNumber_countdown.setNumDigits(1)
        self.lcdNumber_countdown.setDigitCount(1)
        self.lcdNumber_countdown.setMode(QtGui.QLCDNumber.Dec)
        self.lcdNumber_countdown.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdNumber_countdown.setObjectName(_fromUtf8("lcdNumber_countdown"))
        self.gridLayout_2.addWidget(self.lcdNumber_countdown, 3, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox_control, 1, 1, 2, 1)
        self.tabWidget_master.addTab(self.tab_capture, _fromUtf8(""))
        self.verticalLayout_4.addWidget(self.tabWidget_master)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_logo = QtGui.QLabel(self.centralwidget)
        self.label_logo.setText(_fromUtf8(""))
        self.label_logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/bbTriggerBoxx_logo.jpg")))
        self.label_logo.setObjectName(_fromUtf8("label_logo"))
        self.horizontalLayout.addWidget(self.label_logo)
        spacerItem3 = QtGui.QSpacerItem(208, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        MainWindow_bbTriggerBoxx.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow_bbTriggerBoxx)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 738, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuNew_Project = QtGui.QMenu(self.menuFile)
        self.menuNew_Project.setObjectName(_fromUtf8("menuNew_Project"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuShootday = QtGui.QMenu(self.menubar)
        self.menuShootday.setObjectName(_fromUtf8("menuShootday"))
        MainWindow_bbTriggerBoxx.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow_bbTriggerBoxx)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow_bbTriggerBoxx.setStatusBar(self.statusbar)
        self.actionMesh = QtGui.QAction(MainWindow_bbTriggerBoxx)
        self.actionMesh.setObjectName(_fromUtf8("actionMesh"))
        self.actionTexture = QtGui.QAction(MainWindow_bbTriggerBoxx)
        self.actionTexture.setObjectName(_fromUtf8("actionTexture"))
        self.actionConfigure = QtGui.QAction(MainWindow_bbTriggerBoxx)
        self.actionConfigure.setObjectName(_fromUtf8("actionConfigure"))
        self.actionOpen_COM1 = QtGui.QAction(MainWindow_bbTriggerBoxx)
        self.actionOpen_COM1.setObjectName(_fromUtf8("actionOpen_COM1"))
        self.actionCreate = QtGui.QAction(MainWindow_bbTriggerBoxx)
        self.actionCreate.setObjectName(_fromUtf8("actionCreate"))
        self.actionLoad = QtGui.QAction(MainWindow_bbTriggerBoxx)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionTriggerBoxx = QtGui.QAction(MainWindow_bbTriggerBoxx)
        self.actionTriggerBoxx.setObjectName(_fromUtf8("actionTriggerBoxx"))
        self.actionOpen_COM3 = QtGui.QAction(MainWindow_bbTriggerBoxx)
        self.actionOpen_COM3.setObjectName(_fromUtf8("actionOpen_COM3"))
        self.actionOpen_COM4 = QtGui.QAction(MainWindow_bbTriggerBoxx)
        self.actionOpen_COM4.setObjectName(_fromUtf8("actionOpen_COM4"))
        self.actionNew_Subject = QtGui.QAction(MainWindow_bbTriggerBoxx)
        self.actionNew_Subject.setObjectName(_fromUtf8("actionNew_Subject"))
        self.actionNew_Character = QtGui.QAction(MainWindow_bbTriggerBoxx)
        self.actionNew_Character.setObjectName(_fromUtf8("actionNew_Character"))
        self.actionNew_Definition = QtGui.QAction(MainWindow_bbTriggerBoxx)
        self.actionNew_Definition.setObjectName(_fromUtf8("actionNew_Definition"))
        self.actionEdit_Prefs = QtGui.QAction(MainWindow_bbTriggerBoxx)
        self.actionEdit_Prefs.setObjectName(_fromUtf8("actionEdit_Prefs"))
        self.actionStart_Monitor = QtGui.QAction(MainWindow_bbTriggerBoxx)
        self.actionStart_Monitor.setObjectName(_fromUtf8("actionStart_Monitor"))
        self.actionCopyNow = QtGui.QAction(MainWindow_bbTriggerBoxx)
        self.actionCopyNow.setObjectName(_fromUtf8("actionCopyNow"))
        self.actionLoad_Project = QtGui.QAction(MainWindow_bbTriggerBoxx)
        self.actionLoad_Project.setObjectName(_fromUtf8("actionLoad_Project"))
        self.actionHelp_on_TriggerBoxx = QtGui.QAction(MainWindow_bbTriggerBoxx)
        self.actionHelp_on_TriggerBoxx.setObjectName(_fromUtf8("actionHelp_on_TriggerBoxx"))
        self.actionSave_Project = QtGui.QAction(MainWindow_bbTriggerBoxx)
        self.actionSave_Project.setObjectName(_fromUtf8("actionSave_Project"))
        self.actionNewShootday = QtGui.QAction(MainWindow_bbTriggerBoxx)
        self.actionNewShootday.setObjectName(_fromUtf8("actionNewShootday"))
        self.menuNew_Project.addAction(self.actionMesh)
        self.menuNew_Project.addAction(self.actionTexture)
        self.menuFile.addAction(self.menuNew_Project.menuAction())
        self.menuFile.addAction(self.actionLoad_Project)
        self.menuFile.addAction(self.actionSave_Project)
        self.menuAbout.addAction(self.actionTriggerBoxx)
        self.menuShootday.addAction(self.actionNewShootday)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuShootday.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.label_2.setBuddy(self.lineEdit_projectRoot)
        self.label_6.setBuddy(self.lineEdit_photoDownload)
        self.label_11.setBuddy(self.lineEdit_shootday)
        self.label_10.setBuddy(self.lineEdit_bucket)
        self.label_5.setBuddy(self.spinBox_take)
        self.label_9.setBuddy(self.lineEdit_comment)

        self.retranslateUi(MainWindow_bbTriggerBoxx)
        self.tabWidget_master.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_bbTriggerBoxx)

    def retranslateUi(self, MainWindow_bbTriggerBoxx):
        MainWindow_bbTriggerBoxx.setWindowTitle(_translate("MainWindow_bbTriggerBoxx", "ByteBoxx::TRIGGERBOXX control v2.5 20140511", None))
        self.radioButton_mesh.setText(_translate("MainWindow_bbTriggerBoxx", "Mesh Project", None))
        self.radioButton_texture.setText(_translate("MainWindow_bbTriggerBoxx", "Texture Project", None))
        self.label_2.setText(_translate("MainWindow_bbTriggerBoxx", "Project:", None))
        self.label_6.setText(_translate("MainWindow_bbTriggerBoxx", "Smart Shooter Download:", None))
        self.tabWidget_master.setTabText(self.tabWidget_master.indexOf(self.tab_project), _translate("MainWindow_bbTriggerBoxx", "Project View", None))
        self.groupBox_structure.setTitle(_translate("MainWindow_bbTriggerBoxx", "Structure", None))
        self.label_11.setText(_translate("MainWindow_bbTriggerBoxx", "ShootDay:", None))
        self.label_10.setText(_translate("MainWindow_bbTriggerBoxx", "Bucket:", None))
        self.groupBox_take.setTitle(_translate("MainWindow_bbTriggerBoxx", "Take Info", None))
        self.label_5.setText(_translate("MainWindow_bbTriggerBoxx", "Current:", None))
        self.checkBox_inc.setText(_translate("MainWindow_bbTriggerBoxx", "Inc", None))
        self.label_9.setText(_translate("MainWindow_bbTriggerBoxx", "Comment:", None))
        self.groupBox_logging.setTitle(_translate("MainWindow_bbTriggerBoxx", "Logging", None))
        self.groupBox_control.setTitle(_translate("MainWindow_bbTriggerBoxx", "Rig Control", None))
        self.label.setText(_translate("MainWindow_bbTriggerBoxx", "Cameras Connected This Setup:", None))
        self.pushButton_prime.setText(_translate("MainWindow_bbTriggerBoxx", "Prime Array (Auto Focus)", None))
        self.pushButton_fire.setText(_translate("MainWindow_bbTriggerBoxx", "&Fire Array", None))
        self.tabWidget_master.setTabText(self.tabWidget_master.indexOf(self.tab_capture), _translate("MainWindow_bbTriggerBoxx", "Capture View", None))
        self.menuFile.setTitle(_translate("MainWindow_bbTriggerBoxx", "File", None))
        self.menuNew_Project.setTitle(_translate("MainWindow_bbTriggerBoxx", "New Project", None))
        self.menuAbout.setTitle(_translate("MainWindow_bbTriggerBoxx", "About", None))
        self.menuShootday.setTitle(_translate("MainWindow_bbTriggerBoxx", "Shootday", None))
        self.actionMesh.setText(_translate("MainWindow_bbTriggerBoxx", "Mesh", None))
        self.actionTexture.setText(_translate("MainWindow_bbTriggerBoxx", "Texture", None))
        self.actionConfigure.setText(_translate("MainWindow_bbTriggerBoxx", "Configure", None))
        self.actionOpen_COM1.setText(_translate("MainWindow_bbTriggerBoxx", "Open COM1", None))
        self.actionCreate.setText(_translate("MainWindow_bbTriggerBoxx", "Create", None))
        self.actionLoad.setText(_translate("MainWindow_bbTriggerBoxx", "Load", None))
        self.actionTriggerBoxx.setText(_translate("MainWindow_bbTriggerBoxx", "TriggerBoxx", None))
        self.actionOpen_COM3.setText(_translate("MainWindow_bbTriggerBoxx", "Open COM3", None))
        self.actionOpen_COM4.setText(_translate("MainWindow_bbTriggerBoxx", "Open COM4", None))
        self.actionNew_Subject.setText(_translate("MainWindow_bbTriggerBoxx", "New Subject", None))
        self.actionNew_Character.setText(_translate("MainWindow_bbTriggerBoxx", "New Character", None))
        self.actionNew_Definition.setText(_translate("MainWindow_bbTriggerBoxx", "New Definition", None))
        self.actionEdit_Prefs.setText(_translate("MainWindow_bbTriggerBoxx", "Edit Prefs", None))
        self.actionStart_Monitor.setText(_translate("MainWindow_bbTriggerBoxx", "Start Monitor", None))
        self.actionCopyNow.setText(_translate("MainWindow_bbTriggerBoxx", "CopyNow", None))
        self.actionLoad_Project.setText(_translate("MainWindow_bbTriggerBoxx", "Load Project", None))
        self.actionHelp_on_TriggerBoxx.setText(_translate("MainWindow_bbTriggerBoxx", "Help on TriggerBoxx", None))
        self.actionSave_Project.setText(_translate("MainWindow_bbTriggerBoxx", "Save Project", None))
        self.actionNewShootday.setText(_translate("MainWindow_bbTriggerBoxx", "New", None))

import bbTriggerBoxx_QRC_rc
