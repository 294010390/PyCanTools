# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PCANBasic import *  ## PCAN-Basic library import
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def __init__(self):
        # Parent's configuration
        self.m_objPCANBasic = PCANBasic()
        self.m_PcanHandle = PCAN_NONEBUS
        self.m_CHANNELS = {'PCAN_DNGBUS1': PCAN_DNGBUS1, 'PCAN_USBBUS1': PCAN_USBBUS1, 'PCAN_USBBUS2': PCAN_USBBUS2, }
        self.m_BAUDRATES = {'1 MBit/sec': PCAN_BAUD_1M, '800 kBit/sec': PCAN_BAUD_800K, '500 kBit/sec': PCAN_BAUD_500K,
                            '250 kBit/sec': PCAN_BAUD_250K,
                            '125 kBit/sec': PCAN_BAUD_125K}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(526, 436)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 501, 111))
        self.groupBox.setObjectName("groupBox")
        self.label_canerr = QtWidgets.QLabel(self.groupBox)
        self.label_canerr.setGeometry(QtCore.QRect(410, 50, 31, 20))
        self.label_canerr.setStyleSheet("border-image: url(:/Source/ok.jpg);\n"
"border-image: url(:/Source/error.jpg);")
        self.label_canerr.setText("")
        self.label_canerr.setObjectName("label_canerr")
        self.label_canok = QtWidgets.QLabel(self.groupBox)
        self.label_canok.setGeometry(QtCore.QRect(410, 50, 31, 21))
        self.label_canok.setStyleSheet("border-image: url(:/Source/ok.jpg);")
        self.label_canok.setText("")
        self.label_canok.setObjectName("label_canok")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 17, 476, 80))
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 2, 1, 2)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_2, 0, 4, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 0, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 6, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 0, 7, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 0, 8, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 1, 1, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_4.addWidget(self.comboBox, 1, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(268, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 1, 5, 1, 4)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 2, 0, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 2, 2, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 2, 4, 1, 4)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_4.addWidget(self.pushButton_7, 2, 8, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 120, 191, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(210, 20, 60, 16))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.widget1 = QtWidgets.QWidget(self.groupBox_2)
        self.widget1.setGeometry(QtCore.QRect(10, 20, 165, 48))
        self.widget1.setObjectName("widget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_9 = QtWidgets.QLabel(self.widget1)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 1, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.widget1)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_5, 0, 2, 1, 2)
        self.radioButton = QtWidgets.QRadioButton(self.widget1)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_3.addWidget(self.radioButton, 1, 0, 1, 3)
        spacerItem6 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 1, 3, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 200, 491, 191))
        self.tabWidget.setObjectName("tabWidget")
        self.SWC = QtWidgets.QWidget()
        self.SWC.setObjectName("SWC")
        self.widget2 = QtWidgets.QWidget(self.SWC)
        self.widget2.setGeometry(QtCore.QRect(40, 20, 201, 131))
        self.widget2.setObjectName("widget2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_13 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 0, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 1, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 0, 2, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 1, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 1, 1, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 1, 2, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout.addWidget(self.pushButton_17, 2, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 2, 1, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout.addWidget(self.pushButton_18, 2, 2, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout.addWidget(self.pushButton_19, 3, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 3, 1, 1, 2)
        self.tabWidget.addTab(self.SWC, "")
        self.RVC = QtWidgets.QWidget()
        self.RVC.setObjectName("RVC")
        self.groupBox_4 = QtWidgets.QGroupBox(self.RVC)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 100, 231, 51))
        self.groupBox_4.setObjectName("groupBox_4")
        self.widget3 = QtWidgets.QWidget(self.groupBox_4)
        self.widget3.setGeometry(QtCore.QRect(10, 20, 220, 22))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem11 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.comboBox_3 = QtWidgets.QComboBox(self.widget3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_3)
        self.comboBox_4 = QtWidgets.QComboBox(self.widget3)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_4)
        self.comboBox_6 = QtWidgets.QComboBox(self.widget3)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_6)
        spacerItem12 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem12)
        self.groupBox_3 = QtWidgets.QGroupBox(self.RVC)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 10, 231, 80))
        self.groupBox_3.setObjectName("groupBox_3")
        self.widget4 = QtWidgets.QWidget(self.groupBox_3)
        self.widget4.setGeometry(QtCore.QRect(11, 21, 211, 51))
        self.widget4.setObjectName("widget4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget4)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 0, 0, 1, 2)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 0, 2, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.widget4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem13, 1, 1, 1, 2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget4)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 3, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.RVC)
        self.groupBox_7.setGeometry(QtCore.QRect(270, 10, 201, 141))
        self.groupBox_7.setObjectName("groupBox_7")
        self.widget5 = QtWidgets.QWidget(self.groupBox_7)
        self.widget5.setGeometry(QtCore.QRect(20, 20, 163, 111))
        self.widget5.setObjectName("widget5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget5)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem14 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem14)
        self.checkBox = QtWidgets.QCheckBox(self.widget5)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget5)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget5)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget5)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        spacerItem15 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem15)
        self.tabWidget.addTab(self.RVC, "")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(220, 120, 291, 80))
        self.groupBox_5.setObjectName("groupBox_5")
        self.widget6 = QtWidgets.QWidget(self.groupBox_5)
        self.widget6.setGeometry(QtCore.QRect(10, 20, 271, 51))
        self.widget6.setObjectName("widget6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget6)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_8 = QtWidgets.QLabel(self.widget6)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget6)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_5.addWidget(self.lineEdit_5, 0, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem16, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget6)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 0, 3, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget6)
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_5.addWidget(self.lineEdit_6, 0, 4, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget6)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_5.addWidget(self.pushButton_6, 1, 0, 1, 2)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem17, 1, 2, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem18, 1, 3, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem19, 1, 4, 1, 1)
        # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 526, 23))
        self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(MainWindow.btnHwRefresh_Click)
        self.pushButton_2.clicked.connect(MainWindow.btnInit_Click)
        self.pushButton_3.clicked.connect(MainWindow.btnRelease_Click)
        self.pushButton_7.clicked.connect(MainWindow.chooseFile)
        self.comboBox_5.currentIndexChanged['int'].connect(MainWindow.Powerkeychanged)
        self.lineEdit_5.textChanged['QString'].connect(MainWindow.setVehicleSpeed)
        self.radioButton.clicked['bool'].connect(MainWindow.openDriverDoorchanged)
        self.pushButton_13.pressed.connect(MainWindow.SWC_Phonepress)
        self.pushButton_13.released.connect(MainWindow.SWC_Phonerelease)
        self.pushButton_15.pressed.connect(MainWindow.SWC_VolPluspress)
        self.pushButton_15.released.connect(MainWindow.SWC_VolPlusrelease)
        self.pushButton_17.pressed.connect(MainWindow.SWC_Previouspress)
        self.pushButton_17.released.connect(MainWindow.SWC_Previousrelease)
        self.pushButton_14.pressed.connect(MainWindow.SWC_Mutepress)
        self.pushButton_14.released.connect(MainWindow.SWC_Muterelease)
        self.pushButton_16.pressed.connect(MainWindow.SWC_VolMinuspress)
        self.pushButton_16.released.connect(MainWindow.SWC_VolMinusrelease)
        self.pushButton_18.pressed.connect(MainWindow.SWC_Nextpress)
        self.pushButton_18.released.connect(MainWindow.SWC_Nextrelease)
        self.pushButton_19.pressed.connect(MainWindow.SWC_SRCpress)
        self.pushButton_19.released.connect(MainWindow.SWC_SRCrelease)
        self.lineEdit_6.returnPressed.connect(MainWindow.sendTemp)
        self.pushButton_6.clicked.connect(MainWindow.sendChime)
        self.pushButton_4.clicked.connect(MainWindow.GL_left)
        self.pushButton_5.clicked.connect(MainWindow.GL_right)
        self.lineEdit_2.returnPressed.connect(MainWindow.set_GL_value)
        self.comboBox_3.currentIndexChanged['int'].connect(MainWindow.Rigion1Zoonechanged)
        self.comboBox_4.currentIndexChanged['int'].connect(MainWindow.Rigion2Zoonechanged)
        self.comboBox_6.currentIndexChanged['int'].connect(MainWindow.Rigion3Zoonechanged)
        self.checkBox.clicked['bool'].connect(MainWindow.RVCunavailable)
        self.checkBox_2.clicked['bool'].connect(MainWindow.GLunavailable)
        self.checkBox_3.clicked['bool'].connect(MainWindow.NoGuideline)
        self.checkBox_4.clicked['bool'].connect(MainWindow.parkSymbolunavailable)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setStatusTip(_translate("MainWindow", "CAN Status:Bus off"))
        self.groupBox.setTitle(_translate("MainWindow", "CAN State"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "PCAN_DNGBUS1"))
        self.pushButton.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_2.setText(_translate("MainWindow", "Initialize"))
        self.pushButton_3.setText(_translate("MainWindow", "Release"))
        self.label_2.setText(_translate("MainWindow", "Baudrate"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1 MBit/sec"))
        self.comboBox.setItemText(1, _translate("MainWindow", "800 kBit/sec"))
        self.comboBox.setItemText(2, _translate("MainWindow", "500 kBit/sec"))
        self.comboBox.setItemText(3, _translate("MainWindow", "250 kBit/sec"))
        self.comboBox.setItemText(4, _translate("MainWindow", "125 kBit/sec"))
        self.comboBox.setItemText(5, _translate("MainWindow", "100 kBit/sec"))
        self.label_10.setText(_translate("MainWindow", "ConfigFile"))
        self.pushButton_7.setText(_translate("MainWindow", "ChooseFile"))
        self.label.setText(_translate("MainWindow", "HardWare"))
        self.groupBox_2.setTitle(_translate("MainWindow", "State Control"))
        self.label_9.setText(_translate("MainWindow", "PowerKey"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Off"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "Acc"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "Run"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "Crank"))
        self.radioButton.setText(_translate("MainWindow", "OpenDriverDoor"))
        self.pushButton_13.setText(_translate("MainWindow", "Phone"))
        self.pushButton_14.setText(_translate("MainWindow", "Mute"))
        self.pushButton_15.setText(_translate("MainWindow", "Vol +"))
        self.pushButton_16.setText(_translate("MainWindow", "Vol -"))
        self.pushButton_17.setText(_translate("MainWindow", "Previous"))
        self.pushButton_18.setText(_translate("MainWindow", "Next"))
        self.pushButton_19.setText(_translate("MainWindow", "SRC"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SWC), _translate("MainWindow", "Tab 2"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Set Warning icon"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Zone1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Zone2"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Zone3"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Zone4"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Zone1"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Zone2"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Zone3"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Zone4"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Zone1"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Zone2"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "Zone3"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "Zone4"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Set Guideline"))
        self.pushButton_4.setText(_translate("MainWindow", "GL_Left"))
        self.pushButton_5.setText(_translate("MainWindow", "GL_Right"))
        self.label_4.setText(_translate("MainWindow", "Set_GL_Val"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Set Text"))
        self.checkBox.setText(_translate("MainWindow", "RVC Unavailable"))
        self.checkBox_2.setText(_translate("MainWindow", "Guideline Unavailable"))
        self.checkBox_3.setText(_translate("MainWindow", "No Guideline"))
        self.checkBox_4.setText(_translate("MainWindow", "Park Symbol Unavailable"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RVC), _translate("MainWindow", "Tab 1"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Settings"))
        self.label_8.setText(_translate("MainWindow", "Speed"))
        self.label_5.setText(_translate("MainWindow", "Temp"))
        self.pushButton_6.setText(_translate("MainWindow", "Chime"))

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
        print(items)

        _translate = QtCore.QCoreApplication.translate
        i = 0
        for name in items:
            self.comboBox_2.setItemText(i, _translate("MainWindow", name))
            print(i)
            i += 1
            self.m_PcanHandle = self.m_CHANNELS[name]

    def btnInit_Click(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate

        baudrate = self.m_BAUDRATES['500 kBit/sec']

        print(self.m_PcanHandle)

        result = self.m_objPCANBasic.Initialize(self.m_PcanHandle, baudrate)

        if result != PCAN_ERROR_OK:
            try:
                MainWindow.setStatusTip(_translate("MainWindow", "CAN Status:Bus off"))
            except:
                print("No hardware")
            print("init failed")
        else:
            # Prepares the PCAN-Basic's PCAN-Trace file
            #
            self.ConfigureTraceFile()
            MainWindow.setStatusTip(_translate("MainWindow", "CAN Status:Bus OK"))
            print("init success")

    def btnRelease_Click(self):
        # Releases a current connected PCAN-Basic channel
        #
        self.m_objPCANBasic.Uninitialize(self.m_PcanHandle)

    def chooseFile(self):
        import json
        global configdata
        fileName, filetype = QtWidgets.QFileDialog.getOpenFileName(self,
                                                                   "选取文件",
                                                                   "C:/",
                                                                   "All Files (*);;json Files (*.json)")  # 设置文件扩展名过滤,注意用双分号间隔

        self.lineEdit.setText(fileName)

        with open(fileName, 'r', encoding='utf-8') as json_file:
            try:
                configdata = json.load(json_file)
                print(configdata["Power"])
                print(configdata['SWC_Mutepress'])

            except:
                print("error json file")

    def setVehicleSpeed(self):
        pass

    def Powerkeychanged(self):
        global configdata

        id = configdata["Power"]['signal']
        datalen = len(configdata["Power"]['data']["run"])
        data = configdata["Power"]['data']["run"]

        print(id)
        print(datalen)
        print(data)

        __class__.WriteFrame(self, id, datalen, data)

    def openDriverDoorchanged(self):
        pass

        # Setting

    def sendChime(self):
        pass

    def sendTemp(self):
        pass

        # Guideline

    def GL_left(self):
        pass

    def GL_right(self):
        pass

    def set_GL_value(self):
        pass

    def Rigion1Zoonechanged(self):
        pass

    def Rigion2Zoonechanged(self):
        pass

    def Rigion3Zoonechanged(self):
        pass

    def RVCunavailable(self):
        pass

    def GLunavailable(self):
        pass

    def NoGuideline(self):
        pass

    def parkSymbolunavailable(self):
        pass

    def SWC_Phonepress(self):
        pass

    def SWC_Phonerelease(self):
        pass

    def SWC_Mutepress(self):
        global configdata

        id = configdata["SWC_Mutepress"]['signal']
        datalen = len(configdata["SWC_Mutepress"]['data'])
        data = configdata["SWC_Mutepress"]['data']

        print(id)
        print(datalen)
        print(data)

        __class__.WriteFrame(self, id, datalen, data)
        print("SWC_Mutepress")

    def SWC_Muterelease(self):
        global configdata

        id = configdata["SWC_Muterelease"]['signal']
        datalen = len(configdata["SWC_Muterelease"]['data'])
        data = configdata["SWC_Muterelease"]['data']

        print(id)
        print(datalen)
        print(data)

        __class__.WriteFrame(self, id, datalen, data)
        print("SWC_Muterelease")

    def SWC_VolPluspress(self):
        pass

    def SWC_VolPlusrelease(self):
        pass

    def SWC_VolMinuspress(self):
        pass

    def SWC_VolMinusrelease(self):
        pass

    def SWC_Previouspress(self):
        pass

    def SWC_Previousrelease(self):
        pass

    def SWC_Nextpress(self):
        pass

    def SWC_Nextrelease(self):
        pass

    def SWC_SRCpress(self):
        pass

    def SWC_SRCrelease(self):
        pass

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

            print(CANMsg.DATA[i])

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
        print(strMsg)

