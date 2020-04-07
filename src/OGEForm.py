from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class OGEForm(QWidget):
    def __init__(self):
        super().__init__()
        label = QLabel(self)
        pix = QPixmap("../images/1.png")
        print(pix.isNull())
        label.setPixmap(pix)
