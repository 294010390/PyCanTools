from PCANBasic import *        ## PCAN-Basic library import
from PyQt5 import QtCore, QtGui, QtWidgets

def __init__(self):
    self.m_objPCANBasic = PCANBasic()
    self.m_PcanHandle = PCAN_NONEBUS
    self.m_CHANNELS = {'PCAN_DNGBUS1': PCAN_DNGBUS1, 'PCAN_USBBUS1': PCAN_USBBUS1, 'PCAN_USBBUS2': PCAN_USBBUS2, }
    self.m_BAUDRATES = {'1 MBit/sec': PCAN_BAUD_1M, '800 kBit/sec': PCAN_BAUD_800K, '500 kBit/sec': PCAN_BAUD_500K,
                        '250 kBit/sec': PCAN_BAUD_250K,
                        '125 kBit/sec': PCAN_BAUD_125K}

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

        # def confirmMessage(self, event, message):  # 关闭窗口触发以下事件
        #     reply = QtWidgets.QMessageBox.question(self, '消息框标题', message, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        #     if reply == QtWidgets.QMessageBox.Yes:
        #         event.accept()  # 接受关闭事件
        #     else:
        #         event.ignore()  # 忽略关闭事件

        ## Button btnInit handler

        ##


def btnInit_Click(self):
    # gets the connection values
    #
    baudrate = self.m_BAUDRATES['500 kBit/sec']

    print(self.m_PcanHandle)

    result = self.m_objPCANBasic.Initialize(self.m_PcanHandle, baudrate)

    if result != PCAN_ERROR_OK:
        print("init failed")
    else:
        # Prepares the PCAN-Basic's PCAN-Trace file
        #
        self.ConfigureTraceFile()
        print("init success")


## Button btnRelease handler
##
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
    print(fileName)

    with open(fileName, 'r', encoding='utf-8') as json_file:
        try:
            configdata = json.load(json_file)
            print(configdata["Power"])
            print(configdata['SWC_Mutepress'])

        except:
            print("error json file")


def setpower(self):
    global configdata

    id = configdata["Power"]['signal']
    datalen = len(configdata["Power"]['data']["run"])
    data = configdata["Power"]['data']["run"]

    print(id)
    print(datalen)
    print(data)

    __class__.WriteFrame(self, id, datalen, data)


def SWC_Phonepress(self):
    global configdata

    id = configdata["SWC_Mutepress"]['signal']
    datalen = len(configdata["SWC_Mutepress"]['data'])
    data = configdata["SWC_Mutepress"]['data']

    print(id)
    print(datalen)
    print(data)

    __class__.WriteFrame(self, id, datalen, data)
    print("press")


def SWC_Phonerelease(self):
    global configdata

    id = configdata["SWC_Muterelease"]['signal']
    datalen = len(configdata["SWC_Muterelease"]['data'])
    data = configdata["SWC_Muterelease"]['data']

    print(id)
    print(datalen)
    print(data)

    __class__.WriteFrame(self, id, datalen, data)
    print("release")


def OpenDD(self):
    print("open Driver door")


def SetVehiclespeed(self):
    print("Set Vehicle speed")


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