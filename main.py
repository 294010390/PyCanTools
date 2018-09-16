import sys
from test import Ui_Dialog  # 这里的first是.ui文件生成的.py文件名
from PyQt5 import QtWidgets
from PCANBasic import *  # PCAN-Basic library import
import time  ## Time-related library
import threading  ## Threading-based Timer library

import platform  ## Underlying platform’s info library

# data from PCAN Basic example
TCL_DONT_WAIT = 1 << 1
TCL_WINDOW_EVENTS = 1 << 2
TCL_FILE_EVENTS = 1 << 3
TCL_TIMER_EVENTS = 1 << 4
TCL_IDLE_EVENTS = 1 << 5
TCL_ALL_EVENTS = 0

COL_TYPE = 0
COL_ID = 1
COL_LENGTH = 2
COL_COUNT = 3
COL_TIME = 4
COL_DATA = 5

IS_WINDOWS = platform.system() == 'Windows'
DISPLAY_UPDATE_MS = 100



# 这个类继承界面UI类
class mywindow(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

def PCANMain(root):

    def __init__():
        pass

    def InitializeBasicComponents(self):

        self.exit = -1
        self.m_objPCANBasic = PCANBasic()
        self.m_PcanHandle = PCAN_NONEBUS
        self.m_LastMsgsList = []


#调用show
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())