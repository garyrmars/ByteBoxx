'''
Created on 26 Oct 2013

@author: ByteBoxx
'''
#builtins
import sys, os
import xml.etree.ElementTree as ET
#3rd
from PyQt4 import QtCore, QtGui
#user
from ui import bbRenderBoxx_UI as uifile
from ui import bbRenderBoxx_queue_UI as queueuifile
from ui import bbRenderBoxx_info_UI as infouifile
from qt import popup
from smartshooter.session import MeshTake, TextureTake


#===============================================================================
# 
#===============================================================================
class DL_bbRenderBoxxQueue(QtGui.QDialog, queueuifile.Ui_Dialog_bbRenderBoxx_queue):
    '''
    classdocs
    '''
    def __init__(self,parent=None):
        super(DL_bbRenderBoxxQueue, self).__init__(parent)
        self.setupUi(self)
        self.mTakeList = []
        
        #connections
        
        
    def _main(self, pTakeList):
        self.mTakeList = pTakeList
        self.show()
        self._populate()
        
    def _populate(self):
        #what kind of data are we dealing with?
        '''
        if self.mTakeList[0].mType == self.mTakeList[0].cMESH_DATA:
            print 'mesh'
        elif self.mTakeList[0].mType == self.mTakeList[0].cTEX_DATA:
            print 'tex'
        '''

        i = len(self.mTakeList[0].mBatchJobs)
        lPlusBatchTk = self.mTakeList[0]
        for job in self.mTakeList[1:]:
            if len(job.mBatchJobs) > i:
                i = len(job.mBatchJobs)
                lPlusBatchTk = job
                
        self.tableWidget_queue.setRowCount(len(self.mTakeList))
        self.tableWidget_queue.setColumnCount(i)
        self.tableWidget_queue.setHorizontalHeaderLabels(lPlusBatchTk.mBatchJobs)
        
        for lTkRow in range(len(self.mTakeList)):
            item = QtGui.QTableWidgetItem()
            item.setText(self.mTakeList[lTkRow].mPath)
            self.tableWidget_queue.setItem(lTkRow,0, item)
            #set the batch widgets - get the current batch versions from the XML
            for index,value in enumerate(self.mTakeList[lTkRow].mBatchJobs):
                if value == 'tk': #default, ignore
                    continue
                lCheckNew = QtGui.QCheckBox()
                lFieldNew = QtGui.QLineEdit()
                lCheckNew.setText(self.mTakeList[lTkRow].mBatchVersions[value][0]) #pull the current version from the take's dictionary
                self.tableWidget_queue.setCellWidget(lTkRow,index,lCheckNew)
                self.tableWidget_queue.setCellWidget(lTkRow,index,lFieldNew)
        
        
        
    def _addCmd(self, pCmdStr):
        pass

#===============================================================================
# 
#===============================================================================
class DL_bbRenderBoxxInfo(QtGui.QDialog, infouifile.Ui_Dialog_bbRenderBoxx_info):
    '''
    classdocs
    '''
    def __init__(self, pXML, parent=None):
        super(DL_bbRenderBoxxInfo, self).__init__(parent)
        self.setupUi(self)
        self.mXML = pXML
        
    def _main(self):
        lTree = ET.parse(self.mXML)
        root = lTree.getroot()
        lHeaders = [gchild.tag for child in root for gchild in child]
        lText = [gchild.text for child in root for gchild in child]
        
        if len(lHeaders) != len(lText):
            #malformed xml
            self.close()
        
        #read the xml data structures
        self.tableWidget_info.setRowCount(len(lHeaders))
        self.tableWidget_info.setColumnCount(1)
        for row in range(len(lHeaders)):
            item = QtGui.QTableWidgetItem()
            item.setText(lText[row])
            self.tableWidget_info.setItem(row,0, item)
            
        self.tableWidget_info.setVerticalHeaderLabels(lHeaders)
        self.tableWidget_info.setHorizontalHeaderLabels(['Data'])
        
        
        self.show()


#===============================================================================
# 
#===============================================================================
class MW_bbRenderBoxx(QtGui.QMainWindow, uifile.Ui_MainWindow_bbRenderBoxx):
    '''
    classdocs
    '''
    def __init__(self, parent=None):
        super(MW_bbRenderBoxx, self).__init__(parent)
        self.setupUi(self)
        
        styleFile=os.path.join(os.path.dirname(os.path.split(__file__)[0]),"common//qt", "DarkOrangeQStyleTemplate.txt")
        with open(styleFile,"r") as fh:
            self.setStyleSheet(fh.read())
                       
        #connections
        self.connect(self.pushButton_browse, QtCore.SIGNAL("clicked()"), self.GetSessionRoot)
        self.connect(self.pushButton_genBatch, QtCore.SIGNAL("clicked()"), self.GenerateBatch)
        self.connect(self.pushButton_addQueue, QtCore.SIGNAL("clicked()"), self.AddQueue)
        self.connect(self.pushButton_remQueue, QtCore.SIGNAL("clicked()"), self.RemQueue)
        self.connect(self.pushButton_info, QtCore.SIGNAL("clicked()"), self.MoreInfo)
        
        #attrs
        self.mRootPath = ""
        self.mQueueDialog = DL_bbRenderBoxxQueue(self) #dlg for render queue
        self.mProcessQueue = {} #dict to hold the take objects to process
        
    def _main(self):
        self.show()
        
    def GetSessionRoot(self):
        lSessionFolder = popup.FileDialog.getDirectory(self, "Pick Dataset Session Root")
        if lSessionFolder:
            self.mRootPath = os.path.abspath(str(lSessionFolder))
            self.lineEdit_session.setText(lSessionFolder)
            
        self.PopulateTreeView()
        
    def PopulateTreeView(self):
        self.model = QtGui.QFileSystemModel(self.treeView_dataSets)
        self.model.setReadOnly(True)
        root = self.model.setRootPath(self.mRootPath)
        self.treeView_dataSets.setModel(self.model)
        self.treeView_dataSets.setRootIndex(root)
        
    def CheckForModel(self):
        #have they even populated the treeview at this point?
        try:
            assert 'model' in self.__dict__
        except AssertionError:
            popup.Popup.warning(self, "Pick a session root directory first!")
            return False
        return True
        
    def AddQueue(self):
        if self.CheckForModel():
            #get the path from the tree view and ensure they are only trying to add take objects
            lPath = self.ResolveTreeIndex()
            if not os.path.basename(str(lPath)).startswith('tk'):
                popup.Popup.warning(self, "Only take objects can be added to the process queue!")
                return
                
            #what take type are we dealing with
            if self.mRootPath.endswith('_Mesh'):
                lProcTake = MeshTake(lPath)
            elif self.mRootPath.endswith('_Texture'):
                lProcTake = TextureTake(lPath)
            lProcTake.BindXML() #check for XML and bind it
            lProcTake.updateBatchVersions()
            #save the take in the dict, reference it by path name
            if not lPath in self.mProcessQueue.keys():
                lProcTake.popBatchJobs()
                self.mProcessQueue[lPath] = lProcTake
                self.listWidget_queue.addItem(lPath)
            else:
                popup.Popup.info(self, "This take is already in your queue!")
                del(lProcTake)
            
    def RemQueue(self):
        if self.CheckForModel():
            #grab the text of the current selection in the queue list and pop it from the dict
            lPath = self.listWidget_queue.currentItem().text()
            if lPath:
                self.mProcessQueue.pop(lPath)
                self.listWidget_queue.takeItem(self.listWidget_queue.currentRow())

    def ResolveTreeIndex(self):
        indexItem = self.treeView_dataSets.currentIndex()
        return self.model.filePath(indexItem)
    
    def MoreInfo(self):
        if self.CheckForModel():
            #parse the associated take XML to glean more info about the take
            lPath = self.listWidget_queue.currentItem().text()
            lXML = self.mProcessQueue[lPath].mXML
            if not lXML:
                popup.Popup.info(self, "This take has no bound XML info!")
                return
            
            lInfoDlg = DL_bbRenderBoxxInfo(lXML, self)
            lInfoDlg._main()
        
    def GenerateBatch(self):
        if not self.mProcessQueue:
            popup.Popup.warning(self, "There's nothing in your queue to process!")
            return
        #extract the list of session/data takes and pass to the queue
        self.mQueueDialog._main([x for x in self.mProcessQueue.values()])
        
#------------------------------------------------------------------------------ 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win = MW_bbRenderBoxx()
    win._main()
    app.exec_()