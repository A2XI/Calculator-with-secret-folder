from PyQt5.QtWidgets import QGridLayout, QWidget, QTextBrowser
from PyQt5.QtCore import Qt


class Displayer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setMinimumHeight(150)
        self.setMaximumHeight(200)

        self.addLabels()
        self.gridLayout()

    def gridLayout(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.grid.addWidget(self.row1, 0, 0, 1, 4)
        self.grid.addWidget(self.row2, 1, 0, 1, 4)

    def addLabels(self):
        self.row1 = QTextBrowser()
        self.row1.setStyleSheet("border-style: none;"
                                "font-size: 18px;"
                                "word-spacing: 3px;"
                                "color: #555555;")
        self.row1.setMaximumHeight(40)
        self.row1.setAlignment(Qt.AlignRight)

        self.row2 = QTextBrowser()
        self.row2.setText("0")
        self.row2.setStyleSheet("border-style: none;"
                                "font-size: 50px;")
        self.row2.setMaximumHeight(70)
        self.row2.setAlignment(Qt.AlignRight)
