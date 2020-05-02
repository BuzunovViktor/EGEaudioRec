import threading

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from EGEaudioRec.src.Recording import Recording


class EGEForm(QWidget):

    seconds = 0
    minutes = 0

    def __init__(self):
        super().__init__()
        self.grid = QGridLayout(self)
        self.showTask1()

    def record(self):
        recording = Recording(self)
        return recording.start(5)

    def update(self, text):
        self.timeLabel.setText("Time is over. Recording is started " + str(5 - text))
        self.timeLabel.setMinimumWidth(100)
        self.repaint()

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
            self.timeLabel.setWordWrap(True)
            error = self.record()
            if error:
                self.timeLabel.setText(error)
            else:
                self.timeLabel.setText("Recording is stopped. Next stage for...")
            return
        self.seconds -= 1

    def invertedTimer1M(self):
        self.seconds = 2
        self.minutes = 0

        self.invertedTimer = QTimer()
        self.invertedTimer.setInterval(1000)
        self.invertedTimer.timeout.connect(lambda: self.invertedTick(self.invertedTimer))
        self.invertedTimer.start()

    def prepareTick(self):
        self.timeLabel.setText("Time to prepare your answer: " + str(self.seconds))
        self.timeLabel.setMinimumWidth(100)
        self.repaint()
        self.timeLabel.setWordWrap(True)
        if self.seconds == 0:
            self.prepareTimer.stop()
            error = self.record()
            if error:
                self.timeLabel.setText(error)
            else:
                self.endTimer()
            return
        self.seconds -= 1

    def endTick(self):
        self.timeLabel.setText("Recording is stopped. Next stage for " + str(self.seconds))
        if self.seconds == 0:
            self.endTimer.stop()
            self.showTask2()
            return
        self.seconds -= 1

    def endTimer(self):
        self.seconds = 5
        self.endTimer = QTimer()
        self.endTimer.setInterval(1000)
        self.endTimer.timeout.connect(lambda: self.endTick())
        self.endTimer.start()

    def prepareTimer(self):
        self.seconds = 5
        self.prepareTimer = QTimer()
        self.prepareTimer.setInterval(1000)
        self.prepareTimer.timeout.connect(lambda: self.prepareTick())
        self.prepareTimer.start()

    def secTick(self):
        self.timeLabel.setText("Task will start in " + str(self.seconds))
        self.timeLabel.setMinimumWidth(100)
        if self.seconds == 0:
            self.invertedTimer.stop()
            self.prepareTimer()
            return
        self.seconds -= 1

    def fiveSecTimer(self):
        self.seconds = 5
        self.invertedTimer = QTimer()
        self.invertedTimer.setInterval(1000)
        self.invertedTimer.timeout.connect(lambda: self.secTick())
        self.invertedTimer.start()

    def showTask1(self):
        self.label = QLabel()
        self.pix = QPixmap("../images/21.png")
        self.label.setPixmap(self.pix)

        self.timeLabel = QLabel()
        self.timeLabel.setFont(QFont('Arial', 30, QFont.Bold))

        self.grid.addWidget(self.label)
        self.grid.addWidget(self.timeLabel)

        self.fiveSecTimer()

    def showTask2(self):
        self.pix = QPixmap("../images/22.png")
        self.label.setPixmap(self.pix)

        self.fiveSecTimer()


