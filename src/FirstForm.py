from functools import partial
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from EGEaudioRec.src.OGEForm import OGEForm

class FirstForm(QWidget):
    x = 6000

    def clearLayout(self, layout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().deleteLater()

    def ogeHandler(self):
        #self.clearLayout(self.grid)
        oge = OGEForm()
        self.grid.addWidget(oge)

    def egeHandler(self):
        print()

    def __init__(self):
        super().__init__()
        self.grid = QGridLayout(self)
        label = QLabel()
        label.setText('Варианты экзамена')
        label.setAlignment(Qt.AlignCenter)
        pix = QPixmap("../images/exam.jpg")
        print(pix.isNull())
        pix = pix.scaled(QSize(100, 100), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label.setPixmap(pix)
        label.setScaledContents(True)

        button1 = QPushButton('ОГЭ')
        button1.setMinimumHeight(500)
        button1.setToolTip('Начать тест ОГЭ')
        button1.clicked.connect(partial(self.ogeHandler))

        button2 = QPushButton('ЕГЭ')
        button2.setToolTip('Начать тест ЕГЭ')
        button2.setMinimumHeight(500)
        button2.clicked.connect(self.egeHandler)
        self.grid.setRowStretch(0, 0)
        self.grid.setRowStretch(2, 0)
        self.grid.setRowStretch(1, 0)
        self.grid.setColumnStretch(0, 0)
        self.grid.setColumnStretch(1, 0)

        self.grid.addWidget(label,1,0,1,0)
        self.grid.addWidget(button1,3,0)
        self.grid.setRowStretch(3,0)
        self.grid.addWidget(button2,3,1)

    def startTimer(self, duration):
        timer = QTimer()
        timer.setInterval(1000)
        timer.timeout.connect(lambda: self.tick(timer))
        timer.start()

    def tick(self, timer):
        print(self.x)
        # timer.stop()

    def handler(self):
        print('Button pushed!')
        self.startTimer(1000)
