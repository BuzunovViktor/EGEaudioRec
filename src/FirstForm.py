from functools import partial

from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from EGEaudioRec.src.EGEForm import EGEForm
from EGEaudioRec.src.OGEForm import OGEForm

class FirstForm(QWidget):

    def clearLayout(self, layout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().deleteLater()

    def ogeHandler(self):
        self.clearLayout(self.grid)
        oge = OGEForm()
        self.grid.addWidget(oge)

    def egeHandler(self):
        self.clearLayout(self.grid)
        ege = EGEForm()
        self.grid.addWidget(ege)

    def __init__(self):
        super().__init__()
        self.grid = QGridLayout(self)
        self.setStyleSheet("border: 1px solid #3873d9;")
        self.setMaximumWidth(1220)
        label = QLabel()
        label.setText('Варианты экзамена')
        label.setAlignment(Qt.AlignCenter)
        pix = QPixmap("../images/exam.jpg")
        pix = pix.scaled(QSize(1220, 450), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        label.setPixmap(pix)
        label.adjustSize()

        button1 = QPushButton('ОГЭ')
        button1.setFont(QtGui.QFont('Arial', 30, QtGui.QFont.Bold))
        button1.setMinimumHeight(500)
        button1.setToolTip('Начать тест ОГЭ')
        button1.clicked.connect(partial(self.ogeHandler))

        button2 = QPushButton('ЕГЭ')
        button2.setFont(QtGui.QFont('Arial', 30, QtGui.QFont.Bold))
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

