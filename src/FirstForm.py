from functools import partial
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from EGEaudioRec.src.OGEForm import OGEForm

class FirstForm(QWidget):
    x = 6000

    def clearLayout(self, layout):
        item = layout.takeAt(0)
        while item:
            w = item.widget()
            if w:
                w.deleteLater()
            lay = item.layout()
            if lay:
                self.clearLayout(item.layout())
            item = layout.takeAt(0)

    def ogeHandler(self):
        self.clearLayout(self.hbox)
        oge = OGEForm()
        self.hbox.addWidget(oge)
        self.startTimer(self.x)

    def egeHandler(self):
        print()

    def __init__(self):
        super().__init__()
        self.hbox = QHBoxLayout(self)
        self.upperHbox = QHBoxLayout(self)
        label = QLabel()
        label.setText('Варианты экзамена')
        # label.move(0,0)
        button1 = QPushButton('ОГЭ')
        button1.setToolTip('Начать тест ОГЭ')
        # button1.move(10,10)
        button1.clicked.connect(partial(self.ogeHandler))

        button2 = QPushButton('ЕГЭ')
        button2.setToolTip('Начать тест ЕГЭ')
        # button2.move(150,10)
        button2.clicked.connect(self.egeHandler)

        self.upperHbox.addWidget(label)
        self.hbox.addWidget(button1)
        self.hbox.addWidget(button2)

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
