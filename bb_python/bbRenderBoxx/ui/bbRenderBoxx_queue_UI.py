# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bbRenderBoxx_queue_UI.ui'
#
# Created: Sat Mar 15 21:08:22 2014
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

class Ui_Dialog_bbRenderBoxx_queue(object):
    def setupUi(self, Dialog_bbRenderBoxx_queue):
        Dialog_bbRenderBoxx_queue.setObjectName(_fromUtf8("Dialog_bbRenderBoxx_queue"))
        Dialog_bbRenderBoxx_queue.resize(652, 343)
        self.verticalLayout_6 = QtGui.QVBoxLayout(Dialog_bbRenderBoxx_queue)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.tabWidget = QtGui.QTabWidget(Dialog_bbRenderBoxx_queue)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_queue = QtGui.QWidget()
        self.tab_queue.setObjectName(_fromUtf8("tab_queue"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_queue)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.tab_queue)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableWidget_queue = QtGui.QTableWidget(self.groupBox)
        self.tableWidget_queue.setObjectName(_fromUtf8("tableWidget_queue"))
        self.tableWidget_queue.setColumnCount(0)
        self.tableWidget_queue.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget_queue)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab_queue, _fromUtf8(""))
        self.tab_mon = QtGui.QWidget()
        self.tab_mon.setObjectName(_fromUtf8("tab_mon"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_mon)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_mon)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.webView_monitor = QtWebKit.QWebView(self.groupBox_2)
        self.webView_monitor.setUrl(QtCore.QUrl(_fromUtf8("http://localhost:5555/")))
        self.webView_monitor.setObjectName(_fromUtf8("webView_monitor"))
        self.verticalLayout_4.addWidget(self.webView_monitor)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab_mon, _fromUtf8(""))
        self.verticalLayout_6.addWidget(self.tabWidget)
        self.frame = QtGui.QFrame(Dialog_bbRenderBoxx_queue)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_render = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_render.setFont(font)
        self.pushButton_render.setObjectName(_fromUtf8("pushButton_render"))
        self.horizontalLayout.addWidget(self.pushButton_render)
        self.checkBox_mail = QtGui.QCheckBox(self.frame)
        self.checkBox_mail.setChecked(True)
        self.checkBox_mail.setObjectName(_fromUtf8("checkBox_mail"))
        self.horizontalLayout.addWidget(self.checkBox_mail)
        spacerItem = QtGui.QSpacerItem(373, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_6.addWidget(self.frame)

        self.retranslateUi(Dialog_bbRenderBoxx_queue)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog_bbRenderBoxx_queue)

    def retranslateUi(self, Dialog_bbRenderBoxx_queue):
        Dialog_bbRenderBoxx_queue.setWindowTitle(_translate("Dialog_bbRenderBoxx_queue", "ByteBoxx:RENDERBOXX::queue v1.01", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_queue), _translate("Dialog_bbRenderBoxx_queue", "Queue", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mon), _translate("Dialog_bbRenderBoxx_queue", "Monitor", None))
        self.pushButton_render.setText(_translate("Dialog_bbRenderBoxx_queue", "Render Queue", None))
        self.checkBox_mail.setText(_translate("Dialog_bbRenderBoxx_queue", "Mail on Task Completion", None))

from PyQt4 import QtWebKit
