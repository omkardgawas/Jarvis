from JarvisUI import Ui_JarvisUI
from PyQt5.QtCore import Qt, QTime, QTimer, QDate
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import jarvis


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        jarvis.run()


startExe = MainThread()


class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_JarvisUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.label1 = QMovie("G.U.I Material/ExtraGui/initial.gif")
        self.ui.label_2.setMovie(self.ui.label1)
        self.ui.label1.start()
        self.ui.label2 = QMovie("G.U.I Material/VoiceReg/__1.gif")
        self.ui.label_3.setMovie(self.ui.label2)
        self.ui.label2.start()
        self.ui.label3 = QMovie("G.U.I Material/B.G/Iron_Template_1.gif")
        self.ui.label_4.setMovie(self.ui.label3)
        self.ui.label3.start()
        self.ui.label4 = QMovie("G.U.I Material/ExtraGui/Health_Template.gif")
        self.ui.label_5.setMovie(self.ui.label4)
        self.ui.label4.start()
        self.ui.label5 = QMovie("G.U.I Material/ExtraGui/B.G_Template_1.gif")
        self.ui.label_6.setMovie(self.ui.label5)
        self.ui.label5.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExe.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


GuiApp = QApplication(sys.argv)
jarvis_gui = Gui_Start()
jarvis_gui.show()
exit(GuiApp.exec_())
