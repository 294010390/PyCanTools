# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_home.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox
from PCANBasic import *  ## PCAN-Basic library import
from time import sleep
import os

class Ui_MainWindow(object):
    def __init__(self):
        # Parent's configuration
        self.LogTest = 1
        self.project = None
        self.curdir = os.getcwd()
        self.projectlist = ["None", 'K215', 'K221', 'K218', 'K256', "NGI2_0Low"]
        self.baudrate = PCAN_BAUD_500K
        self.flg = {"Canstate": 0, "initsuccess": 0, "Confsuccess": 0, "IGState": 0,
                    "RVCOn": 0, "Cancelalltimer": 0, 'SendNM': 0}
        self.timerflg = {"Powertimer": 0, "Positiontimer": 0, "tmptimer": 0, "speedtimer": 0, "ParkSysmboltimer": 0,
                         "Guidelinetimer": 0}
        # self.timerlist = [self.Powertimer, self.Positiontimer, self.tmptimer, self.speedtimer]
        self.m_objPCANBasic = PCANBasic()
        self.m_PcanHandle = PCAN_NONEBUS
        self.m_CHANNELS = {'PCAN_DNGBUS1': PCAN_DNGBUS1, 'PCAN_USBBUS1': PCAN_USBBUS1, 'PCAN_USBBUS2': PCAN_USBBUS2, }
        self.m_BAUDRATES = {'1 MBit/sec': PCAN_BAUD_1M, '500 kBit/sec': PCAN_BAUD_500K,
                            '250 kBit/sec': PCAN_BAUD_250K,
                            '125 kBit/sec': PCAN_BAUD_125K}
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(515, 391)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 491, 91))
        self.groupBox.setObjectName("groupBox")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(390, 58, 54, 16))
        self.label_6.setObjectName("label_6")
        # self.CANOK = QtWidgets.QLabel(self.groupBox)
        # self.CANOK.setGeometry(QtCore.QRect(450, 50, 31, 31))
        # self.CANOK.setStyleSheet("border-image: url(:/Source/ok.jpg);")
        # self.CANOK.setText("")
        # self.CANOK.setObjectName("CANOK")
        # self.CANErr = QtWidgets.QLabel(self.groupBox)
        # self.CANErr.setGeometry(QtCore.QRect(450, 60, 31, 21))
        # self.CANErr.setStyleSheet("border-image: url(:/Source/error.jpg);")
        # self.CANErr.setText("")
        # self.CANErr.setObjectName("CANErr")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 53, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 54, 61, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(180, 23, 75, 23))
        self.pushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 23, 161, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(12, 53, 148, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.comboBox_8 = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_8.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_8)
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(329, 25, 154, 22))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 110, 261, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboBox_7 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_7.setGeometry(QtCore.QRect(70, 51, 61, 20))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(11, 51, 48, 16))
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(11, 21, 48, 16))
        self.label_9.setObjectName("label_9")
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_5.setGeometry(QtCore.QRect(70, 20, 61, 20))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_5.setGeometry(QtCore.QRect(150, 20, 101, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 200, 501, 181))
        self.tabWidget.setObjectName("tabWidget")
        self.RVC = QtWidgets.QWidget()
        self.RVC.setObjectName("RVC")
        self.groupBox_4 = QtWidgets.QGroupBox(self.RVC)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 100, 231, 51))
        self.groupBox_4.setObjectName("groupBox_4")
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_4)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 20, 220, 22))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.comboBox_6 = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_6)

        self.comboBox_4 = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_4)

        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_3)

        spacerItem1 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.RVC)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 10, 231, 80))
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget4.setGeometry(QtCore.QRect(11, 21, 211, 51))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 0, 0, 1, 2)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 0, 2, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 1, 1, 2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 3, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.RVC)
        self.groupBox_7.setGeometry(QtCore.QRect(270, 10, 201, 141))
        self.groupBox_7.setObjectName("groupBox_7")
        self.layoutWidget5 = QtWidgets.QWidget(self.groupBox_7)
        self.layoutWidget5.setGeometry(QtCore.QRect(20, 20, 163, 111))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget5)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget5)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget5)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget5)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.tabWidget.addTab(self.RVC, "")
        self.SWC = QtWidgets.QWidget()
        self.SWC.setObjectName("SWC")
        self.layoutWidget6 = QtWidgets.QWidget(self.SWC)
        self.layoutWidget6.setGeometry(QtCore.QRect(40, 10, 241, 151))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_13 = QtWidgets.QPushButton(self.layoutWidget6)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 1, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.layoutWidget6)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 0, 2, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.layoutWidget6)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 1, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.layoutWidget6)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 1, 2, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.layoutWidget6)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout.addWidget(self.pushButton_17, 2, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 2, 1, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.layoutWidget6)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout.addWidget(self.pushButton_18, 2, 2, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.layoutWidget6)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout.addWidget(self.pushButton_19, 3, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 3, 1, 1, 2)
        self.tabWidget.addTab(self.SWC, "")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(290, 110, 221, 80))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(130, 21, 24, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_6.setGeometry(QtCore.QRect(160, 21, 51, 20))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 47, 81, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setGeometry(QtCore.QRect(14, 21, 30, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_5.setGeometry(QtCore.QRect(50, 21, 51, 20))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        # MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(MainWindow.btnHwRefresh_Click)
        self.pushButton_2.clicked.connect(MainWindow.btnInit_Click)
        self.pushButton_3.clicked.connect(MainWindow.btnRelease_Click)
        self.comboBox_5.currentIndexChanged['int'].connect(MainWindow.Powerkeychanged)
        self.lineEdit_5.returnPressed.connect(MainWindow.setVehicleSpeed)
        self.pushButton_13.pressed.connect(MainWindow.SWC_Phonepress)
        self.pushButton_13.released.connect(MainWindow.SWC_release)
        self.pushButton_15.pressed.connect(MainWindow.SWC_VolPluspress)
        self.pushButton_15.released.connect(MainWindow.SWC_release)
        self.pushButton_17.pressed.connect(MainWindow.SWC_Previouspress)
        self.pushButton_17.released.connect(MainWindow.SWC_release)
        self.pushButton_14.pressed.connect(MainWindow.SWC_Mutepress)
        self.pushButton_14.released.connect(MainWindow.SWC_release)
        self.pushButton_16.pressed.connect(MainWindow.SWC_VolMinuspress)
        self.pushButton_16.released.connect(MainWindow.SWC_release)
        self.pushButton_18.pressed.connect(MainWindow.SWC_Nextpress)
        self.pushButton_18.released.connect(MainWindow.SWC_release)
        self.pushButton_19.pressed.connect(MainWindow.SWC_SRCpress)
        self.pushButton_19.released.connect(MainWindow.SWC_release)
        self.lineEdit_6.returnPressed.connect(MainWindow.sendTemp)
        self.pushButton_6.clicked.connect(MainWindow.sendChime)
        self.pushButton_4.clicked.connect(MainWindow.GL_left)
        self.pushButton_5.clicked.connect(MainWindow.GL_right)
        self.lineEdit_2.returnPressed.connect(MainWindow.set_GL_value)
        self.comboBox_3.currentIndexChanged['int'].connect(MainWindow.RigionZoonechanged)
        self.comboBox_4.currentIndexChanged['int'].connect(MainWindow.RigionZoonechanged)
        self.comboBox_6.currentIndexChanged['int'].connect(MainWindow.RigionZoonechanged)
        self.checkBox.clicked['bool'].connect(MainWindow.RVCunavailable)
        self.checkBox_2.clicked['bool'].connect(MainWindow.GLunavailable)
        self.checkBox_3.clicked['bool'].connect(MainWindow.NoGuideline)
        self.checkBox_4.clicked['bool'].connect(MainWindow.parkSymbolunavailable)
        self.comboBox_8.currentTextChanged['QString'].connect(MainWindow.chooseProject)
        self.comboBox.currentIndexChanged['int'].connect(MainWindow.setbaudrate)
        self.comboBox_7.currentIndexChanged['int'].connect(MainWindow.setPosition)
        self.checkBox_5.clicked['bool'].connect(MainWindow.openDriverDoorchanged)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PCAN Tool"))
        MainWindow.setStatusTip(_translate("MainWindow", "CAN Status:Bus off"))
        self.groupBox.setTitle(_translate("MainWindow", "CAN State"))
        self.label_6.setText(_translate("MainWindow", "CAN State"))
        self.pushButton_2.setText(_translate("MainWindow", "Initialize"))
        self.pushButton_3.setText(_translate("MainWindow", "Release"))
        self.pushButton.setText(_translate("MainWindow", "Refresh"))
        self.label.setText(_translate("MainWindow", "HardWare"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "PCAN_DNGBUS1"))
        self.label_10.setText(_translate("MainWindow", "ConfigFile"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "K215"))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "K221"))
        self.comboBox_8.setItemText(3, _translate("MainWindow", "K256"))
        self.comboBox_8.setItemText(4, _translate("MainWindow", "K218"))
        self.comboBox_8.setItemText(5, _translate("MainWindow", "NGI2_0Low"))
        self.label_2.setText(_translate("MainWindow", "Baudrate"))
        self.comboBox.setItemText(0, _translate("MainWindow", "500 kBit/sec"))
        self.comboBox.setItemText(1, _translate("MainWindow", "1 MBit/sec"))
        self.comboBox.setItemText(2, _translate("MainWindow", "250 kBit/sec"))
        self.comboBox.setItemText(3, _translate("MainWindow", "100 kBit/sec"))
        self.groupBox_2.setTitle(_translate("MainWindow", "State Control"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "Park"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "Neutral"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "Drive"))
        self.comboBox_7.setItemText(3, _translate("MainWindow", "Reverse"))
        self.comboBox_7.setItemText(4, _translate("MainWindow", "Invalid"))
        self.label_3.setText(_translate("MainWindow", "Position"))
        self.label_9.setText(_translate("MainWindow", "PowerKey"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Off"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "Acc"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "Run"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "Crank"))
        self.checkBox_5.setText(_translate("MainWindow", "OpenDriverDoor"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Set Warning icon"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Zone1"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Zone2"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Zone3"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Zone4"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Zone1"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Zone2"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Zone3"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "Zone4"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Zone1"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "Zone2"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "Zone3"))
        self.comboBox_6.setItemText(4, _translate("MainWindow", "Zone4"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Set Guideline"))
        self.pushButton_4.setText(_translate("MainWindow", "GL_Left"))
        self.pushButton_5.setText(_translate("MainWindow", "GL_Right"))
        self.label_4.setText(_translate("MainWindow", "Set_GL_Val"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Set Text"))
        self.checkBox.setText(_translate("MainWindow", "RVC Unavailable"))
        self.checkBox_2.setText(_translate("MainWindow", "Guideline Unavailable"))
        self.checkBox_3.setText(_translate("MainWindow", "No Guideline"))
        self.checkBox_4.setText(_translate("MainWindow", "Park Symbol Unavailable"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RVC), _translate("MainWindow", "RVC"))
        self.pushButton_13.setText(_translate("MainWindow", "Phone"))
        self.pushButton_14.setText(_translate("MainWindow", "Mute"))
        self.pushButton_15.setText(_translate("MainWindow", "Vol +"))
        self.pushButton_16.setText(_translate("MainWindow", "Vol -"))
        self.pushButton_17.setText(_translate("MainWindow", "Previous"))
        self.pushButton_18.setText(_translate("MainWindow", "Next"))
        self.pushButton_19.setText(_translate("MainWindow", "SRC"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SWC), _translate("MainWindow", "SWC"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Others"))
        self.label_5.setText(_translate("MainWindow", "Temp"))
        self.pushButton_6.setText(_translate("MainWindow", "Chime"))
        self.label_8.setText(_translate("MainWindow", "Speed"))

# Can state
    def btnHwRefresh_Click(self):
        # Clears the Channel comboBox and fill it again with
        # the PCAN-Basic handles for no-Plug&Play hardware and
        # the detected Plug&Play hardware
        #
        items = []

        for name, value in self.m_CHANNELS.items():
            # Includes all no-Plug&Play Handles
            #
            if (value.value <= PCAN_DNGBUS1.value):
                # items.append(name)
                pass
            else:
                # Checks for a Plug&Play Handle and, according with the return value, includes it
                # into the list of available hardware channels.
                #
                result = self.m_objPCANBasic.GetValue(value, PCAN_CHANNEL_CONDITION)
                if (result[0] == PCAN_ERROR_OK) and (result[1] & PCAN_CHANNEL_AVAILABLE):
                    result = self.m_objPCANBasic.GetValue(value, PCAN_CHANNEL_FEATURES)
                    items.append(name)

        items.sort()

        _translate = QtCore.QCoreApplication.translate
        i = 0
        for name in items:
            self.comboBox_2.setItemText(i, _translate("MainWindow", name))
            if self.LogTest:
                print(i)
            i += 1
            self.m_PcanHandle = self.m_CHANNELS[name]

    def CANstate(self):

        pic1 = QtGui.QPixmap(self.curdir+"\\ok.jpg")
        pic2 = QtGui.QPixmap(self.curdir+"\\error.jpg")
        # Display can state icon
        self.CANErr = QtWidgets.QLabel(self.groupBox)
        self.CANErr.setGeometry(QtCore.QRect(450, 55, 31, 21))
        self.CANErr.setStyleSheet("")
        self.CANErr.setPixmap(pic2)
        self.CANErr.setObjectName("CANErr")
        self.CANErr.setScaledContents(True)
        self.CANOK = QtWidgets.QLabel(self.groupBox)
        self.CANOK.setGeometry(QtCore.QRect(450, 55, 31, 21))
        self.CANOK.setStyleSheet("")
        self.CANOK.setPixmap(pic1)
        self.CANOK.setObjectName("CANOK")
        self.CANOK.setScaledContents(True)

    def btnInit_Click(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        baudrate = self.baudrate
        if self.LogTest:
            print(self.m_PcanHandle)

        result = self.m_objPCANBasic.Initialize(self.m_PcanHandle, baudrate)
        self.CANstate()

        if result != PCAN_ERROR_OK:
            self.flg["initsuccess"] = 0
            self.BTNstate()

            if self.CANOK.isEnabled():
                self.CANOK.hide()
            self.CANErr.show()

            if self.LogTest:
                print("init failed")
        else:
            # Prepares the PCAN-Basic's PCAN-Trace file
            #
            self.ConfigureTraceFile()
            # MainWindow.setStatusTip(_translate("MainWindow", "CAN Status:Bus OK"))
            self.comboBox_8.setCurrentIndex(0)  # 设置Project为None
            self.flg["initsuccess"] = 1
            self.comboBox_5.setCurrentIndex(0)  # Set Powerkey to Off
            self.comboBox_7.setCurrentIndex(0)  # Set Position to Park
            self.lineEdit_5.clear()  # Clear Speed Value
            self.lineEdit_6.clear()  # Clear Temperature Value
            self.BTNstate()

            if self.CANErr.isEnabled():
                self.CANErr.hide()
            self.CANOK.show()

            if self.LogTest:
                print("init success")

    def btnRelease_Click(self):
        # Releases a current connected PCAN-Basic channel
        #
        self.timerflg["Cancelalltimer"] = 1
        self.cancelalltimer(state=self.timerflg["Cancelalltimer"])  # Cancel all timer
        try:
            self.m_objPCANBasic.Uninitialize(self.m_PcanHandle)
            self.comboBox_2.setCurrentIndex(0)

            self.flg["initsuccess"] = 0
            self.flg["Confsuccess"] = 0
            self.flg['SendNM'] = 0
            self.BTNstate()
            self.comboBox_8.setCurrentIndex(0)  # 设置Project为None

            if self.CANErr.isEnabled():
                self.CANErr.hide()
            if self.CANOK.isEnabled():
                self.CANOK.hide()
            if self.LogTest:
                print("release success")
        except:
            self.flg["initsuccess"] = 1
            self.BTNstate()
            if self.LogTest:
                print("release failed")

    def setbaudrate(self):
        self.baudrate = self.m_BAUDRATES[self.comboBox.currentText()]

    def BTNstate(self):
        if self.flg["initsuccess"]:
            stsConnected = True
            stsNotConnected = False
        else:
            stsConnected = False
            stsNotConnected = True

        if self.flg["Confsuccess"]:
            stsFile = True
            stsFilesuccess = False
        else:
            stsFile = False
            stsFilesuccess = True

        if self.flg["IGState"]:
            stsIG = True
        else:
            stsIG = False

        if self.flg["RVCOn"]:
            stsRVC = True
        else:
            stsRVC = False

        if self.flg['SendNM']:
            stsNM = True
        else:
            stsNM = False

        # Can state frame
        self.comboBox_2.setEnabled(stsNotConnected)  # HW Combobox
        self.pushButton.setEnabled(stsNotConnected)  # Refresh Button
        self.pushButton_2.setEnabled(stsNotConnected)  # Initialize Button
        self.pushButton_3.setEnabled(stsConnected)  # Release Button
        self.comboBox.setEnabled(stsNotConnected)  # Baudrate
        self.comboBox_8.setEnabled(stsConnected and stsFilesuccess)  # Config File
        # self.pushButton_7.setEnabled(stsConnected)  # ChooseFile Button

        # State Control
        self.comboBox_5.setEnabled(stsConnected and stsFile and stsNM)  # Power Combobox
        self.comboBox_7.setEnabled(stsConnected and stsFile and stsIG and stsNM)  # Position Combobox
        self.checkBox_5.setEnabled(stsConnected and stsFile)  # Opendriverdoor Button

        # Others
        self.lineEdit_5.setEnabled(stsConnected and stsFile and stsIG and stsNM)  # Speed Input box
        self.lineEdit_6.setEnabled(stsConnected and stsFile and stsIG and stsNM)  # Temperature input box
        self.pushButton_6.setEnabled(stsConnected and stsFile and stsNM)  # Chime Button

        # SWC
        self.pushButton_13.setEnabled(stsConnected and stsFile and stsNM)  # SWC Button
        self.pushButton_14.setEnabled(stsConnected and stsFile and stsNM)  # SWC Button
        self.pushButton_15.setEnabled(stsConnected and stsFile and stsNM)  # SWC Button
        self.pushButton_16.setEnabled(stsConnected and stsFile and stsNM)  # SWC Button
        self.pushButton_17.setEnabled(stsConnected and stsFile and stsNM)  # SWC Button
        self.pushButton_18.setEnabled(stsConnected and stsFile and stsNM)  # SWC Button
        self.pushButton_19.setEnabled(stsConnected and stsFile and stsNM)  # SWC Button

        # RVC
        self.pushButton_4.setEnabled(stsConnected and stsFile and stsRVC and stsNM)  # Guideline Button
        self.pushButton_5.setEnabled(stsConnected and stsFile and stsRVC and stsNM)  # Guideline Button
        self.lineEdit_2.setEnabled(stsConnected and stsFile and stsRVC and stsNM)  # Guideline input box
        self.comboBox_3.setEnabled(stsConnected and stsFile and stsRVC and stsNM)  # RVC warning symbol
        self.comboBox_4.setEnabled(stsConnected and stsFile and stsRVC and stsNM)  # RVC warning symbol
        self.comboBox_6.setEnabled(stsConnected and stsFile and stsRVC and stsNM)  # RVC warning symbol
        self.checkBox.setEnabled(stsConnected and stsFile and stsRVC and stsNM)  # RVC Text
        self.checkBox_2.setEnabled(stsConnected and stsFile and stsRVC and stsNM)  # RVC Text
        self.checkBox_3.setEnabled(stsConnected and stsFile and stsRVC and stsNM)  # RVC Text
        self.checkBox_4.setEnabled(stsConnected and stsFile and stsRVC and stsNM)  # RVC Text

    def chooseProject(self):
        import json
        import os
        global configdata
        curproject = self.comboBox_8.currentText()

        try:

            if curproject == 'K215':
                filename = "K215"
                self.project = self.projectlist[1]
            elif curproject == 'K221':
                filename = "K221"
                self.project = self.projectlist[2]
            elif curproject == 'K218':
                filename = "K218"
                self.project = self.projectlist[3]
            elif curproject == 'K256':
                filename = "K256"
                self.project = self.projectlist[4]

            elif curproject == 'NGI2_0Low':
                filename = "K215"
                self.project = self.projectlist[5]
            else:
                filename = "None"
                self.project = self.projectlist[0]

            if self.project != self.projectlist[0]:

                currentpath = os.getcwd() + '\\config.json'
                # fileName, filetype = QtWidgets.QFileDialog.getOpenFileName(self,
                #                                                            "选取文件",
                #                                                            currentpath,
                #                                                            "All Files (*);;json Files (*.json)")  # 设置文件扩展名过滤,注意用双分号间隔

                with open(currentpath, 'r', encoding='utf-8') as json_file:
                    try:
                        configdata0 = json.load(json_file)
                        configdata = configdata0[self.project]
                        self.flg["Confsuccess"] = 1
                        self.BTNstate()
                        if self.LogTest:
                            print("open success")

                    except:
                        self.flg["Confsuccess"] = 0
                        self.BTNstate()
                        self.show_criticalmessage("Error", "Enter Right Json file")
                        if self.LogTest:
                            print("error json file")
            else:
                pass
        except:
            self.show_criticalmessage("Error", "No Correct Config File!")

    def Poweroperate(self):
        global configdata
        currentPowerMode = self.comboBox_5.currentText()

        id = configdata["Power"]['signal']
        datalen = len(configdata["Power"]['data'][currentPowerMode])
        data = configdata["Power"]['data'][currentPowerMode]

        __class__.WriteFrame(self, id, datalen, data)
        if self.LogTest:
            print(id + " -> " + str(data))

            # if currentPowerMode != 'Off':
            #     __class__.WriteFrame(self, id, datalen, data)
            #
            # else:
            #     # self.Powertimer.stop()
            #     pass
            # self.Powertimer.killTimer(self.timer_id)

            # print("send powerstate " + time.ctime()+" "+str(data))

    def Powerkeychanged(self):
        global configdata

        currentPowerMode = self.comboBox_5.currentText()

        id = configdata["Power"]['signal']
        datalen = len(configdata["Power"]['data'][currentPowerMode])
        data = configdata["Power"]['data'][currentPowerMode]

        __class__.WriteFrame(self, id, datalen, data)

        if self.timerflg["Powertimer"]:
            pass
        else:
            self.Powertimer = QTimer(self)  # 初始化一个定时器
            self.Powertimer.timeout.connect(self.Poweroperate)  # 计时结束调用operate()方法
            self.Powertimer.start(100)  # 设置计时间100ms隔并启动

            # 发送挡位信号
            self.setPosition()

            self.timerflg["Powertimer"] = 1

        if currentPowerMode == "Run":
            self.flg["IGState"] = 1
            self.sendTemp()
            self.setVehicleSpeed()
        elif currentPowerMode == "Off":
            self.flg["IGState"] = 0
            # Cancel timer under Run mode
            self.timerflg["Cancelalltimer"] = 1
            self.cancelalltimer(state=self.timerflg["Cancelalltimer"])  # Cancel all timer
        else:
            self.flg["IGState"] = 0
            # Cancel timer under Run mode
            self.timerflg["Cancelalltimer"] = 0
            self.cancelalltimer(state=self.timerflg["Cancelalltimer"])  # Cancel all timer

        # Power == Run, Position == R, Change to RVC Mode
        if self.comboBox_7.currentText() == "Reverse" and currentPowerMode == "Run":
            self.flg["RVCOn"] = 1
            self.sendguideline()
        else:
            self.flg["RVCOn"] = 0
            if self.timerflg["Guidelinetimer"]:
                self.Guidelinetimer.stop()


        self.BTNstate()

    def setPositiontimer(self):
        global configdata
        currentPosition = self.comboBox_7.currentText()

        id = configdata["ParkPosition"]['signal']
        datalen = len(configdata["ParkPosition"]['data'][currentPosition])
        data = configdata["ParkPosition"]['data'][currentPosition]

        __class__.WriteFrame(self, id, datalen, self.Positiondata)
        if self.LogTest:
            print(id + "->" + str(self.Positiondata))

    def setPosition(self):
        global configdata

        currentPosition = self.comboBox_7.currentText()

        id = configdata["ParkPosition"]['signal']
        datalen = len(configdata["ParkPosition"]['data'][currentPosition])
        data = configdata["ParkPosition"]['data'][currentPosition]

        if self.project == self.projectlist[4]:  # Data For K256
            if self.checkBox_5.isChecked():  # OpenDriverDoor
                data[1] = "02"
            else:
                data[1] = "00"
        if self.project == self.projectlist[5]:  # Data For NGI2.0 Low
            if self.checkBox_5.isChecked():  # OpenDriverDoor
                data[0] = "80"
            else:
                data[0] = "00"

        # if self.comboBox_7.currentText() != "Invalid":
        #     self.checkBox.setChecked(False)

        if currentPosition == "Reverse" and self.comboBox_5.currentText() == "Run":
            self.flg["RVCOn"] = 1
            self.sendguideline()
            self.checkBox.setChecked(False)
        else:
            self.flg["RVCOn"] = 0
            if self.timerflg["Guidelinetimer"]:
                self.Guidelinetimer.stop()
        self.BTNstate()

        self.Positiondata = data

        __class__.WriteFrame(self, id, datalen, self.Positiondata)

        if self.timerflg["Positiontimer"]:
            pass
        elif self.comboBox_5.currentText() == 'Off':
            pass
        else:
            self.Positiontimer = QTimer(self)  # 初始化一个定时器
            self.Positiontimer.timeout.connect(self.setPositiontimer)  # 计时结束调用operate()方法
            self.Positiontimer.start(100)  # 设置计时间100ms隔并启动

            self.timerflg["Positiontimer"] = 1

    def setGuidelinetimer(self):
        global configdata

        id = configdata["Set_GL_Val"]['signal']
        datalen = len(configdata["Set_GL_Val"]['data'])
        data = configdata["Set_GL_Val"]['data']

        __class__.WriteFrame(self, id, datalen, self.Guidelinedata)
        if self.LogTest:
            print(id + "->" + str(self.Guidelinedata))

    def sendguideline(self):
        global configdata

        id = configdata["Set_GL_Val"]['signal']
        datalen = len(configdata["Set_GL_Val"]['data'])
        data = configdata["Set_GL_Val"]['data']

        if self.project == self.projectlist[5]:  # For NGI2.0Low
            if self.checkBox_2.isChecked():
                data[6] = "60"
            elif self.checkBox_3.isChecked():
                data[6] = "00"
            else:
                data[6] = "40"
        else:  # Not NGI2.0Low
            if self.checkBox_2.isChecked():
                data[0] = "A0"
            elif self.checkBox_3.isChecked():
                data[0] = "00"
            else:
                data[0] = "20"

        self.Guidelinedata = []
        newdata0 = []

        currentGLvaluephys = self.lineEdit_2.text()
        if currentGLvaluephys == "":
            newdata0 = []
            newdata0.append("00")
            newdata0.append("00")
        else:
            try:
                currentGLvalue = round(float(currentGLvaluephys), 2)

                try:

                    if 0 <= currentGLvalue <= 2047.9:
                        Hexvalue = hex(int(16 * currentGLvalue))
                    else:
                        ConstValue0xFFFF = 65535 + 1
                        Hexvalue = hex(int(16 * currentGLvalue + ConstValue0xFFFF))

                    if len(Hexvalue) == 3:
                        newdata0.append("00")
                        newdata0.append(Hexvalue[-1])
                    elif len(Hexvalue) == 4:
                        newdata0.append("00")
                        newdata0.append(Hexvalue[2:])
                    elif len(Hexvalue) == 5:
                        newdata0.append(Hexvalue[2])
                        newdata0.append(Hexvalue[3:])
                    elif len(Hexvalue) == 6:
                        newdata0.append(Hexvalue[2:4])
                        newdata0.append(Hexvalue[4:])
                except:
                    self.show_warningmessage("Warning", "Guideline angle value Range: -2048~2047.5")

            except:
                self.show_criticalmessage("Error", "Enter Right Guideline angle value")

        if self.LogTest:
            print("Changed Data is " + str(newdata0))

        for i in range(len(data)):
            if self.project == self.projectlist[5]:  # For NGI2.0Low
                if i == 4 or i == 5:
                    self.Guidelinedata.append(newdata0[i - 4])
                else:
                    self.Guidelinedata.append(data[i])
            else:  # For others
                if i == 1 or i == 2:
                    self.Guidelinedata.append(newdata0[i - 1])
                else:
                    self.Guidelinedata.append(data[i])

        __class__.WriteFrame(self, id, datalen, self.Guidelinedata)

        if self.timerflg["Guidelinetimer"]:
            pass
        else:
            self.Guidelinetimer = QTimer(self)  # 初始化一个定时器
            self.Guidelinetimer.timeout.connect(self.setGuidelinetimer)  # 计时结束调用operate()方法
            self.Guidelinetimer.start(100)  # 设置计时间100ms隔并启动

            self.timerflg["Guidelinetimer"] = 1

    def cancelalltimer(self, state):
        if state == True:
            if self.timerflg["Powertimer"]:
                self.Powertimer.stop()
                self.timerflg["Powertimer"] = 0
            if self.timerflg["Positiontimer"]:
                self.Positiontimer.stop()
                self.timerflg["Positiontimer"] = 0

            if self.timerflg["tmptimer"]:
                self.tmptimer.stop()
                self.timerflg["tmptimer"] = 0
            if self.timerflg["speedtimer"]:
                self.speedtimer.stop()
                self.timerflg["speedtimer"] = 0
            if self.timerflg["Guidelinetimer"]:
                self.Guidelinetimer.stop()
                self.timerflg["Guidelinetimer"] = 0
            if self.timerflg["ParkSysmboltimer"]:
                self.ParkSysmboltimer.stop()
                self.timerflg["ParkSysmboltimer"] = 0
        elif self.comboBox_5.currentText() != "Run":
            if self.timerflg["tmptimer"]:
                self.tmptimer.stop()
                self.timerflg["tmptimer"] = 0
            if self.timerflg["speedtimer"]:
                self.speedtimer.stop()
                self.timerflg["speedtimer"] = 0
            if self.timerflg["Guidelinetimer"]:
                self.Guidelinetimer.stop()
                self.timerflg["Guidelinetimer"] = 0
            if self.timerflg["ParkSysmboltimer"]:
                self.ParkSysmboltimer.stop()
                self.timerflg["ParkSysmboltimer"] = 0

    def openDriverDoorchanged(self):
        global configdata

        id = '621'
        datalen = 8
        data = ["01", "00", "00", "00", "00", "00", "00", "00"]
        result = self.m_objPCANBasic.Initialize(self.m_PcanHandle, self.baudrate)
        for i in range(10):
            __class__.WriteFrame(self, id, datalen, data)
            sleep(0.01)
            if self.LogTest:
                print("WakeUp")
        self.flg['SendNM'] = 1

        self.setPosition()

        if self.checkBox_5.isChecked():

            if self.project == self.projectlist[4]:  # Data for K256
                self.Positiondata[1] = "02"
            elif self.project == self.projectlist[5]:  # Data for NGI2.0Low
                self.Positiondata[0] = "80"
            else:
                pass
        else:
            if self.project == self.projectlist[4]:  # Data for K256
                self.Positiondata[1] = "00"
            elif self.project == self.projectlist[5]:  # Data for NGI2.0Low
                self.Positiondata[0] = "00"
            else:
                pass

        id = configdata["OpenDD"]['signal']
        datalen = len(configdata["OpenDD"]['data']['Open'])

        if self.LogTest:
            print(id + "->" + str(self.Positiondata))

        __class__.WriteFrame(self, id, datalen, self.Positiondata)

    # Others

    def sendChime(self):
        global configdata

        id = configdata["SendChime"]['signal']
        datalen = len(configdata["SendChime"]['data'])
        data = configdata["SendChime"]['data']
        if self.LogTest:
            print(data)

        __class__.WriteFrame(self, id, datalen, data)

    def tempchanged(self):
        global configdata

        self.tmpcounter += 1

        id = configdata["SetTemperature"][0]['signal']
        datalen = len(configdata["SetTemperature"][0]['data'])
        data = configdata["SetTemperature"][0]['data']

        __class__.WriteFrame(self, id, datalen, self.newdata)
        if self.LogTest:
            print(id + "->" + str(self.newdata))

        if self.tmpcounter % 10 == 0:
            id = configdata["SetTemperature"][1]['signal']
            datalen = len(configdata["SetTemperature"][1]['data'])
            data = configdata["SetTemperature"][1]['data']

            __class__.WriteFrame(self, id, datalen, data)
            if self.LogTest:
                print(id + "->" + str(data))

        if self.project != self.projectlist[5]:  # project for Need 0x62c
            if self.tmpcounter % 100 == 0:
                id = configdata["SetTemperature"][2]['signal']
                datalen = len(configdata["SetTemperature"][2]['data'])
                data = configdata["SetTemperature"][2]['data']

                __class__.WriteFrame(self, id, datalen, data)
                if self.LogTest:
                    print(id + "->" + str(data))

    def sendTemp(self):
        global configdata

        try:
            if self.lineEdit_6.text():
                curtmpdata = round(float(self.lineEdit_6.text()), 2)
            else:
                curtmpdata = 0

            if self.lineEdit_6.text() == "" and self.timerflg["tmptimer"]:
                self.tmptimer.stop()
            else:

                if -40 <= curtmpdata <= 87.5:
                    Hexvalue = hex(int(2 * (curtmpdata + 40)))

                    id = configdata["SetTemperature"][0]['signal']
                    datalen = len(configdata["SetTemperature"][0]['data'])
                    data = configdata["SetTemperature"][0]['data']

                    self.newdata = []
                    for i in data:
                        if i == "*":
                            d = Hexvalue[2:]
                            self.newdata.append(d)
                        else:
                            self.newdata.append(i)

                    __class__.WriteFrame(self, id, datalen, self.newdata)
                    if self.LogTest:
                        print(id + "->" + str(self.newdata))

                    id = configdata["SetTemperature"][1]['signal']
                    datalen = len(configdata["SetTemperature"][1]['data'])
                    data = configdata["SetTemperature"][1]['data']

                    __class__.WriteFrame(self, id, datalen, data)
                    if self.LogTest:
                        print(id + "->" + str(data))

                    if self.project != self.projectlist[5]:  # 0x62c not suitable for NGI2.0Low
                        id = configdata["SetTemperature"][2]['signal']
                        datalen = len(configdata["SetTemperature"][2]['data'])
                        data = configdata["SetTemperature"][2]['data']
                        if self.LogTest:
                            print(id + "->" + str(data))

                        __class__.WriteFrame(self, id, datalen, data)

                    if self.timerflg["tmptimer"]:
                        pass
                    else:
                        self.tmptimer = QTimer(self)  # 初始化一个定时器
                        self.tmpcounter = 0
                        self.tmptimer.timeout.connect(self.tempchanged)  # 计时结束调用operate()方法
                        self.tmptimer.start(10)  # 设置计时间100ms隔并启动

                        self.timerflg["tmptimer"] = 1
                else:
                    self.show_warningmessage("Warning", "Enter normal number: -40~87.5 ")
                    if self.LogTest:
                        print("Enter Right Value")
                    else:
                        pass

        except:
            self.show_criticalmessage("Error", "Temperature Value Range: -40~87.5 ")
            if self.LogTest:
                print("Enter normal Temperature Value")
            else:
                pass

    def speedchanged(self):
        id = configdata["SetSpeed"]['signal']
        datalen = len(configdata["SetSpeed"]['data'])
        data = configdata["SetSpeed"]['data']

        __class__.WriteFrame(self, id, datalen, self.newspeeddata)

        if self.LogTest:
            print(id + "->" + str(self.newspeeddata))

    def setVehicleSpeed(self):
        global configdata

        try:
            if self.lineEdit_5.text():
                curtmpdata = round(float(self.lineEdit_5.text()), 1)
            else:
                curtmpdata = 0

            if self.lineEdit_5.text() == "" and self.timerflg["speedtimer"]:
                self.tmptimer.stop()
            else:
                if self.project in [self.projectlist[1], self.projectlist[2]]:
                    if 0 <= curtmpdata <= 510:
                        Hexvalue = hex(int(64 * curtmpdata))

                        id = configdata["SetSpeed"]['signal']
                        datalen = len(configdata["SetSpeed"]['data'])
                        data = configdata["SetSpeed"]['data']

                        self.newspeeddata = []

                        newdata0 = []
                        if len(Hexvalue) == 3:
                            newdata0.append("00")
                            newdata0.append(Hexvalue[-1])
                        elif len(Hexvalue) == 4:
                            newdata0.append("00")
                            newdata0.append(Hexvalue[2:])
                        elif len(Hexvalue) == 5:
                            newdata0.append(Hexvalue[2])
                            newdata0.append(Hexvalue[3:])
                        elif len(Hexvalue) == 6:
                            newdata0.append(Hexvalue[2:4])
                            newdata0.append(Hexvalue[4:])

                        if self.LogTest:
                            print(newdata0)

                        j = 0
                        for i in data:
                            if i == "*":
                                self.newspeeddata.append(newdata0[j])
                                j += 1
                            else:
                                self.newspeeddata.append(i)

                        __class__.WriteFrame(self, id, datalen, self.newspeeddata)
                        if self.LogTest:
                            print(id + "->" + str(self.newspeeddata))

                        if self.timerflg["speedtimer"]:
                            pass
                        else:
                            self.speedtimer = QTimer(self)  # 初始化一个定时器
                            self.speedtimer.timeout.connect(self.speedchanged)  # 计时结束调用operate()方法
                            self.speedtimer.start(100)  # 设置计时间100ms隔并启动

                            self.timerflg["speedtimer"] = 1
                    else:
                        self.show_warningmessage("Warning", "Speed Value Range: 0~500")
                        if self.LogTest:
                            print("Enter Right Speed Value")

                if self.project == self.projectlist[3]:
                    if 0 <= curtmpdata <= 510:
                        Hexvalue = hex(int(64 * curtmpdata))

                        id = configdata["SetSpeed"]['signal']
                        datalen = len(configdata["SetSpeed"]['data'])
                        data = configdata["SetSpeed"]['data']

                        self.newspeeddata = []

                        newdata0 = []
                        if len(Hexvalue) == 3:
                            newdata0.append("00")
                            newdata0.append(Hexvalue[-1])
                        elif len(Hexvalue) == 4:
                            newdata0.append("00")
                            newdata0.append(Hexvalue[2:])
                        elif len(Hexvalue) == 5:
                            newdata0.append(Hexvalue[2])
                            newdata0.append(Hexvalue[3:])
                        elif len(Hexvalue) == 6:
                            newdata0.append(Hexvalue[2:4])
                            newdata0.append(Hexvalue[4:])

                        if self.LogTest:
                            print(newdata0)

                        j = 0
                        for i in data:
                            if i == "*":
                                self.newspeeddata.append(newdata0[j])
                                j += 1
                            else:
                                self.newspeeddata.append(i)

                        __class__.WriteFrame(self, id, datalen, self.newspeeddata)
                        if self.LogTest:
                            print(id + "->" + str(self.newspeeddata))

                        if self.timerflg["speedtimer"]:
                            pass
                        else:
                            self.speedtimer = QTimer(self)  # 初始化一个定时器
                            self.speedtimer.timeout.connect(self.speedchanged)  # 计时结束调用operate()方法
                            self.speedtimer.start(100)  # 设置计时间100ms隔并启动

                            self.timerflg["speedtimer"] = 1
                    else:
                        self.show_warningmessage("Warning", "Speed Value Range: 0~500")
                        if self.LogTest:
                            print("Enter Right Speed Value")

                if self.project == self.projectlist[4]:
                    if 0 <= curtmpdata <= 510:
                        Hexvalue = hex(int(64 * curtmpdata))

                        id = configdata["SetSpeed"]['signal']
                        datalen = len(configdata["SetSpeed"]['data'])
                        data = configdata["SetSpeed"]['data']

                        self.newspeeddata = []

                        newdata0 = []
                        if len(Hexvalue) == 3:
                            newdata0.append("00")
                            newdata0.append(Hexvalue[-1])
                        elif len(Hexvalue) == 4:
                            newdata0.append("00")
                            newdata0.append(Hexvalue[2:])
                        elif len(Hexvalue) == 5:
                            newdata0.append(Hexvalue[2])
                            newdata0.append(Hexvalue[3:])
                        elif len(Hexvalue) == 6:
                            newdata0.append(Hexvalue[2:4])
                            newdata0.append(Hexvalue[4:])

                        if self.LogTest:
                            print(newdata0)

                        j = 0
                        for i in data:
                            if i == "*":
                                self.newspeeddata.append(newdata0[j])
                                j += 1
                            else:
                                self.newspeeddata.append(i)

                        __class__.WriteFrame(self, id, datalen, self.newspeeddata)
                        if self.LogTest:
                            print(id + "->" + str(self.newspeeddata))

                        if self.timerflg["speedtimer"]:
                            pass
                        else:
                            self.speedtimer = QTimer(self)  # 初始化一个定时器
                            self.speedtimer.timeout.connect(self.speedchanged)  # 计时结束调用operate()方法
                            self.speedtimer.start(100)  # 设置计时间100ms隔并启动

                            self.timerflg["speedtimer"] = 1
                    else:
                        self.show_warningmessage("Warning", "Speed Value Range: 0~500")
                        if self.LogTest:
                            print("Enter Right Speed Value")

                if self.project == self.projectlist[5]:
                    if 0 <= curtmpdata <= 510:
                        Hexvalue = hex(int(bin(int(64 * curtmpdata)) + '0000000', 2))

                        if self.LogTest:
                            print("Hexvalue for Vehicle speed is ", str(Hexvalue))

                        id = configdata["SetSpeed"]['signal']
                        datalen = len(configdata["SetSpeed"]['data'])
                        data = configdata["SetSpeed"]['data']

                        self.newspeeddata = []

                        newdata0 = []

                        if len(Hexvalue) == 6:
                            newdata0.append("00")
                            newdata0.append(Hexvalue[2:4])
                            newdata0.append(Hexvalue[4:])
                        elif len(Hexvalue) == 7:
                            newdata0.append(Hexvalue[2])
                            newdata0.append(Hexvalue[3:5])
                            newdata0.append(Hexvalue[5:])
                        elif len(Hexvalue) == 8:
                            newdata0.append(Hexvalue[2:4])
                            newdata0.append(Hexvalue[4:6])
                            newdata0.append(Hexvalue[6:])
                        else:
                            newdata0.append("00")
                            newdata0.append("00")
                            newdata0.append("00")

                        if self.LogTest:
                            print(newdata0)

                        j = 0
                        for i in data:
                            if i == "*":
                                self.newspeeddata.append(newdata0[j])
                                j += 1
                            else:
                                self.newspeeddata.append(i)

                        __class__.WriteFrame(self, id, datalen, self.newspeeddata)
                        if self.LogTest:
                            print(id + "->" + str(self.newspeeddata))

                        if self.timerflg["speedtimer"]:
                            pass
                        else:
                            self.speedtimer = QTimer(self)  # 初始化一个定时器
                            self.speedtimer.timeout.connect(self.speedchanged)  # 计时结束调用operate()方法
                            self.speedtimer.start(100)  # 设置计时间100ms隔并启动

                            self.timerflg["speedtimer"] = 1
                    else:
                        self.show_warningmessage("Warning", "Speed Value Range: 0~500")
                        if self.LogTest:
                            print("Enter Right Speed Value")
        except:
            self.show_criticalmessage("Error", "Enter Right Speed Value")
            if self.LogTest:
                print("Enter normal number")
            else:
                pass

    # RVC & Guideline

    def GL_left(self):

        currentGLvaluephys = self.lineEdit_2.text()
        if currentGLvaluephys == "":
            self.lineEdit_2.setText("50")
        else:
            currentGLvaluephys = self.lineEdit_2.text()
            currentGLvaluephys = int(currentGLvaluephys) + 50
            self.lineEdit_2.setText(str(currentGLvaluephys))
        self.sendguideline()

    def GL_right(self):
        currentGLvaluephys = self.lineEdit_2.text()
        if currentGLvaluephys == "":
            self.lineEdit_2.setText("-50")
        else:
            currentGLvaluephys = self.lineEdit_2.text()
            currentGLvaluephys = int(currentGLvaluephys) - 50
            self.lineEdit_2.setText(str(currentGLvaluephys))
        self.sendguideline()

    def set_GL_value(self):
        self.sendguideline()

    def setParkSysmboltimer(self):
        id = configdata["Zone"]['signal']
        datalen = len(configdata["Zone"]['data'])
        data = configdata["Zone"]['data']

        __class__.WriteFrame(self, id, datalen, self.ParkSysmboldata)

        if self.LogTest:
            print(id + "->" + str(self.ParkSysmboldata))

    def RigionZoonechanged(self):
        global configdata

        currentZone1index = self.comboBox_3.currentIndex()
        currentZone2index = self.comboBox_4.currentIndex()
        currentZone3index = self.comboBox_6.currentIndex()

        if self.LogTest:
            print("current index is ", currentZone1index)
            print("current index is ", currentZone2index)
            print("current index is ", currentZone3index)

        id = configdata["Zone"]['signal']
        datalen = len(configdata["Zone"]['data'])
        data = configdata["Zone"]['data']

        if self.checkBox_4.isChecked():
            data[0] = "20"
        else:
            data[0] = "00"

        self.ParkSysmboldata = []
        for i in data:
            if i == "**":
                self.ParkSysmboldata.append(str(currentZone2index) + str(currentZone1index))
            elif i == "0*":
                self.ParkSysmboldata.append("0" + str(currentZone3index))
            else:
                self.ParkSysmboldata.append(i)

        if self.LogTest:
            print(self.ParkSysmboldata)

        __class__.WriteFrame(self, id, datalen, self.ParkSysmboldata)

        if self.timerflg["ParkSysmboltimer"]:
            pass
        else:
            self.ParkSysmboltimer = QTimer(self)  # 初始化一个定时器
            self.ParkSysmboltimer.timeout.connect(self.setParkSysmboltimer)  # 计时结束调用operate()方法
            self.ParkSysmboltimer.start(10)  # 设置计时间100ms隔并启动

            self.timerflg["ParkSysmboltimer"] = 1

    # def Rigion2Zoonechanged(self):
    #     global configdata
    #
    #     currentZone2index = self.comboBox_4.currentIndex()
    #
    #     if self.LogTest:
    #         print("current index is ", currentZone2index)
    #
    #     id = configdata["Zone1"]['signal']
    #     datalen = len(configdata["Zone1"]['data'])
    #     data = configdata["Zone1"]['data']
    #
    #     self.ParkSysmboldata = []
    #     for i in data:
    #         if "*" in i:
    #             self.ParkSysmboldata.append(str(currentZone2index)+i[1])
    #         else:
    #             self.ParkSysmboldata.append(i)
    #
    #     if self.LogTest:
    #         print(self.ParkSysmboldata)
    #
    #     __class__.WriteFrame(self, id, datalen, self.ParkSysmboldata)
    #
    #     if self.timerflg["ParkSysmboltimer"]:
    #         pass
    #     else:
    #         self.ParkSysmboltimer = QTimer(self)  # 初始化一个定时器
    #         self.ParkSysmboltimer.timeout.connect(self.setParkSysmboltimer)  # 计时结束调用operate()方法
    #         self.ParkSysmboltimer.start(10)  # 设置计时间100ms隔并启动
    #
    #         self.timerflg["ParkSysmboltimer"] = 1
    #
    # def Rigion3Zoonechanged(self):
    #     pass

    def RVCunavailable(self):
        global configdata

        if self.checkBox.isChecked():
            id = configdata["RVCUnavailable"][0]['signal']
            datalen = len(configdata["RVCUnavailable"][0]['data'])
            self.Positiondata = configdata["RVCUnavailable"][0]['data']

            self.comboBox_7.setCurrentIndex(4)

            if self.LogTest:
                print("current Combobox Position is ", str(self.comboBox_7.currentText()))
                print("current Position is ", str(self.Positiondata))
        else:
            id = configdata["RVCUnavailable"][1]['signal']
            datalen = len(configdata["RVCUnavailable"][1]['data'])
            self.Positiondata = configdata["RVCUnavailable"][1]['data']

            self.comboBox_7.setCurrentIndex(3)

            if self.LogTest:
                print("current Combobox Position is ", str(self.comboBox_7.currentText()))
                print("current Position is ", str(self.Positiondata))

        __class__.WriteFrame(self, id, datalen, self.Positiondata)

        if self.timerflg["Positiontimer"]:
            pass
        else:
            self.Positiontimer = QTimer(self)  # 初始化一个定时器
            self.Positiontimer.timeout.connect(self.setPositiontimer)  # 计时结束调用operate()方法
            self.Positiontimer.start(100)  # 设置计时间100ms隔并启动

            self.timerflg["Positiontimer"] = 1

    def GLunavailable(self):
        global configdata

        id = configdata["GLUnavailable"][0]['signal']
        datalen = len(configdata["GLUnavailable"][0]['data'])

        self.sendguideline()

        if self.checkBox_2.isChecked():
            self.Guidelinedata[0] = configdata["GLUnavailable"][0]['data'][0]
        elif self.checkBox_3.isChecked():
            self.Guidelinedata[0] = configdata["No_GL"][0]['data'][0]
        else:
            self.Guidelinedata[0] = configdata["GLUnavailable"][1]['data'][0]

        if self.LogTest:
            if self.Guidelinedata[0] == "A0":
                state = "Unavailable"
                print("current GLUnavailable is ", state)
            if self.Guidelinedata[0] == "20":
                state = "Available"
                print("current GLUnavailable is ", state)

        __class__.WriteFrame(self, id, datalen, self.Guidelinedata)

        if self.timerflg["Guidelinetimer"]:
            pass
        else:
            self.Guidelinetimer = QTimer(self)  # 初始化一个定时器
            self.Guidelinetimer.timeout.connect(self.setGuidelinetimer)  # 计时结束调用operate()方法
            self.Guidelinetimer.start(100)  # 设置计时间100ms隔并启动

            self.timerflg["Guidelinetimer"] = 1

    def NoGuideline(self):
        global configdata

        id = configdata["No_GL"][0]['signal']
        datalen = len(configdata["No_GL"][0]['data'])

        self.sendguideline()

        if self.checkBox_3.isChecked():
            self.Guidelinedata[0] = configdata["No_GL"][0]['data'][0]
        elif self.checkBox_2.isChecked():
            self.Guidelinedata[0] = configdata["GLUnavailable"][0]['data'][0]
        else:
            self.Guidelinedata[0] = configdata["No_GL"][1]['data'][0]

        if self.LogTest:
            if self.Guidelinedata[0] == "00":
                state = "No Guideline"
                print("current Guideline is ", state)
            if self.Guidelinedata[0] == "20":
                state = "Available"
                print("current Guideline is ", state)

        __class__.WriteFrame(self, id, datalen, self.Guidelinedata)

        if self.timerflg["Guidelinetimer"]:
            pass
        else:
            self.Guidelinetimer = QTimer(self)  # 初始化一个定时器
            self.Guidelinetimer.timeout.connect(self.setGuidelinetimer)  # 计时结束调用operate()方法
            self.Guidelinetimer.start(100)  # 设置计时间100ms隔并启动

            self.timerflg["Guidelinetimer"] = 1

    def parkSymbolunavailable(self):
        global configdata

        id = configdata["ParkUnavailable"][0]['signal']
        datalen = len(configdata["ParkUnavailable"][0]['data'])

        self.RigionZoonechanged()

        if self.checkBox_4.isChecked():
            self.ParkSysmboldata[0] = configdata["ParkUnavailable"][0]['data'][0]
        else:
            self.ParkSysmboldata[0] = configdata["ParkUnavailable"][1]['data'][0]

        if self.LogTest:
            if self.ParkSysmboldata[0] == "20":
                state = "unavailable"
                print("current park Symbol is ", state)
            if self.ParkSysmboldata[0] == "00":
                state = "Available"
                print("current park Symbol is ", state)

        __class__.WriteFrame(self, id, datalen, self.ParkSysmboldata)

        if self.timerflg["ParkSysmboltimer"]:
            pass
        else:
            self.ParkSysmboltimer = QTimer(self)  # 初始化一个定时器
            self.ParkSysmboltimer.timeout.connect(self.setParkSysmboltimer)  # 计时结束调用operate()方法
            self.ParkSysmboltimer.start(10)  # 设置计时间100ms隔并启动

            self.timerflg["ParkSysmboltimer"] = 1

    # SWC

    def SWC_Phonepress(self):
        global configdata

        id = configdata["SWC_Phonepress"]['signal']
        datalen = len(configdata["SWC_Phonepress"]['data'])
        data = configdata["SWC_Phonepress"]['data']

        __class__.WriteFrame(self, id, datalen, data)
        if self.LogTest:
            print("SWC_Phonepress")

    def SWC_Mutepress(self):
        global configdata

        id = configdata["SWC_Mutepress"]['signal']
        datalen = len(configdata["SWC_Mutepress"]['data'])
        data = configdata["SWC_Mutepress"]['data']

        __class__.WriteFrame(self, id, datalen, data)
        if self.LogTest:
            print("SWC_Mutepress")

    def SWC_release(self):
        global configdata

        id = configdata["SWC_release"]['signal']
        datalen = len(configdata["SWC_release"]['data'])
        data = configdata["SWC_release"]['data']
        if self.LogTest:
            print(id)
            print(datalen)
            print(data)

        __class__.WriteFrame(self, id, datalen, data)
        if self.LogTest:
            print("SWC_release")

    def SWC_VolPluspress(self):
        global configdata

        id = configdata["SWC_VolPluspress"]['signal']
        datalen = len(configdata["SWC_VolPluspress"]['data'])
        data = configdata["SWC_VolPluspress"]['data']

        __class__.WriteFrame(self, id, datalen, data)
        if self.LogTest:
            print("SWC_VolPluspress")

    def SWC_VolMinuspress(self):
        global configdata

        id = configdata["SWC_VolMinuspress"]['signal']
        datalen = len(configdata["SWC_VolMinuspress"]['data'])
        data = configdata["SWC_VolMinuspress"]['data']

        __class__.WriteFrame(self, id, datalen, data)
        if self.LogTest:
            print("SWC_VolMinuspress")

    def SWC_Previouspress(self):
        global configdata

        id = configdata["SWC_Previouspress"]['signal']
        datalen = len(configdata["SWC_Previouspress"]['data'])
        data = configdata["SWC_Previouspress"]['data']

        __class__.WriteFrame(self, id, datalen, data)
        if self.LogTest:
            print("SWC_Previouspress")

    def SWC_Nextpress(self):
        global configdata

        id = configdata["SWC_Nextpress"]['signal']
        datalen = len(configdata["SWC_Nextpress"]['data'])
        data = configdata["SWC_Nextpress"]['data']

        __class__.WriteFrame(self, id, datalen, data)
        if self.LogTest:
            print("SWC_Nextpress")

    def SWC_SRCpress(self):
        global configdata

        id = configdata["SWC_SRCpress"]['signal']
        datalen = len(configdata["SWC_SRCpress"]['data'])
        data = configdata["SWC_SRCpress"]['data']

        __class__.WriteFrame(self, id, datalen, data)
        if self.LogTest:
            print("SWC_SRCpress")

    # Called function
    def WriteFrame(self, id, datalen, data):
        global configdata
        # We create a TPCANMsg message structure
        #
        CANMsg = TPCANMsg()

        # We configurate the Message.  The ID,
        # Length of the Data, Message Type and the data
        #
        CANMsg.ID = int(id, 16)
        CANMsg.LEN = int(datalen)
        CANMsg.MSGTYPE = PCAN_MESSAGE_STANDARD

        for i in range(CANMsg.LEN):
            CANMsg.DATA[i] = int(data[i], 16)

        # The message is sent to the configured hardware
        #
        return self.m_objPCANBasic.Write(self.m_PcanHandle, CANMsg)

    ## Configures the PCAN-Trace file for a PCAN-Basic Channel
    ##
    def ConfigureTraceFile(self):
        # Configure the maximum size of a trace file to 5 megabytes
        #
        iBuffer = 5
        stsResult = self.m_objPCANBasic.SetValue(self.m_PcanHandle, PCAN_TRACE_SIZE, iBuffer)
        if stsResult != PCAN_ERROR_OK:
            self.IncludeTextMessage(self.GetFormatedError(stsResult))

        # Configure the way how trace files are created:
        # * Standard name is used
        # * Existing file is ovewritten,
        # * Only one file is created.
        # * Recording stopts when the file size reaches 5 megabytes.
        #
        iBuffer = TRACE_FILE_SINGLE | TRACE_FILE_OVERWRITE
        stsResult = self.m_objPCANBasic.SetValue(self.m_PcanHandle, PCAN_TRACE_CONFIGURE, iBuffer)
        if stsResult != PCAN_ERROR_OK:
            self.IncludeTextMessage(self.GetFormatedError(stsResult))

    ## Help Function used to get an error as text
    ##
    def GetFormatedError(self, error):
        # Gets the text using the GetErrorText API function
        # If the function success, the translated error is returned. If it fails,
        # a text describing the current error is returned.
        #
        stsReturn = self.m_objPCANBasic.GetErrorText(error, 0)
        if stsReturn[0] != PCAN_ERROR_OK:
            return "An error occurred. Error-code's text ({0:X}h) couldn't be retrieved".format(error)
        else:
            return stsReturn[1]

    ## Includes a new line of text into the information Listview
    ##
    def IncludeTextMessage(self, strMsg):
        if self.LogTest:
            print(strMsg)
        else:
            pass

    def show_criticalmessage(self, title, content):
        QMessageBox.critical(self, title, content)

    def show_warningmessage(self, title, content):
        QMessageBox.warning(self, title, content)
