import threading

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from EGEaudioRec.src.Recording import Recording
import time


class OGEForm(QWidget):

    seconds = 0
    minutes = 0

    def record(self):
        recording = Recording()
        recording.run()

    def invertedTick(self, invertedTimer):
        self.timeLabel.setText(str(self.minutes) + ":" + str(self.seconds))
        self.timeLabel.setMinimumWidth(100)
        if self.seconds == 0:
            if self.minutes == 0:
                self.invertedTimer.stop()
            else:
                self.minutes -= 1
                self.seconds = 60
        if self.seconds == 0 and self.minutes == 0:
            self.invertedTimer.stop()
            self.timeLabel.setText("Время вышло. Включена запись.")
            self.timeLabel.setMinimumWidth(100)
            self.repaint()
            thread = threading.Thread(target=self.record())
            thread.start()
            self.timeLabel.setText("Recording is stopped. Next stage for...")
            return
        self.seconds -= 1


    def invertedTimer1M(self):
        self.seconds = 2
        self.minutes = 0

        label = QLabel()
        label.setText('Варианты экзамена')
        self.invertedTimer.setInterval(1000)
        self.invertedTimer.timeout.connect(lambda: self.invertedTick(self.invertedTimer))
        self.invertedTimer.start()

    def tick(self, timer):
        if self.seconds == 60:
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
        self.grid = QGridLayout(self)
        self.label = QLabel()
        pix = QPixmap("../images/1.png")
        #print(pix.isNull())
        self.label.setPixmap(pix)

        self.timeLabel = QLabel()
        self.timeLabel.setFont(QFont('Arial',30,QFont.Bold))
        #self.timeLabel.setFixedSize(30)

        """self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(lambda: self.tick(self.timer))
        self.timer.start()"""
        self.grid.addWidget(self.label)
        self.grid.addWidget(self.timeLabel)
        self.invertedTimer = QTimer()
        self.invertedTimer1M()



