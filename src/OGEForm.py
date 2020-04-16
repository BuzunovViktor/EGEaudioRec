from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class OGEForm(QWidget):

    seconds = 0
    minutes = 0

    def tick(self, timer):
        if self.seconds == 59:
            self.seconds = 0
            self.minutes += 1
        else:
            self.seconds += 1
        print(self.seconds)
        self.timeLabel.setText(str(self.minutes) + ":" + str(self.seconds))
        self.timeLabel.setMinimumWidth(100)
        # timer.stop()

    def __init__(self):
        super().__init__()
        """self.label = QLabel(self)
        pix = QPixmap("../images/1.png")
        #print(pix.isNull())
        self.label.setPixmap(pix)
"""
        self.timeLabel = QLabel(self)
        self.timeLabel.setFont(QFont('Arial',30,QFont.Bold))
        #self.timeLabel.setFixedSize(30)

        print("Hello")
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(lambda: self.tick(self.timer))
        self.timer.start()



