# Author    : Zhang Jiankai
# Version   : v1.0
#
import sys
from test_home import Ui_MainWindow  # 这里的first是.ui文件生成的.py文件名
from PyQt5 import QtWidgets


# 这个类继承界面UI类
class mywindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.BTNstate()


#调用show
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())

