from PyQt5.QtWidgets import QPushButton, QGridLayout
from displayer import Displayer


class GridLayout(QGridLayout):
    def __init__(self):
        super().__init__()
        self.widgets()
        self.displayCalculus()
        self.widgetsPosition()
        self.setSpacing(3)

    def widgets(self):
        self.clear = self.createButton("C")
        self.clear_entry = self.createButton("CE")
        self.percentage = self.createButton("%")

        self.b1 = self.createButton("1")
        self.b1 = self.createButton("1")
        self.b2 = self.createButton("2")
        self.b3 = self.createButton("3")
        self.b4 = self.createButton("4")
        self.b5 = self.createButton("5")
        self.b6 = self.createButton("6")
        self.b7 = self.createButton("7")
        self.b8 = self.createButton("8")
        self.b9 = self.createButton("9")

        self.division = self.createButton("÷")
        self.multiply = self.createButton("x")
        self.subtract = self.createButton("-")
        self.add = self.createButton("+")

        self.division.setStyleSheet(self.cssOperation())
        self.multiply.setStyleSheet(self.cssOperation())
        self.subtract.setStyleSheet(self.cssOperation())
        self.add.setStyleSheet(self.cssOperation())
        self.clear.setStyleSheet(self.cssOperation())
        self.clear_entry.setStyleSheet(self.cssOperation())
        self.percentage.setStyleSheet(self.cssOperation())

        self.negative = self.createButton("+/-")
        self.b0 = self.createButton("0")
        self.point = self.createButton(".")
        self.result = self.createButton("=")
        self.result.setStyleSheet(self.cssResult())

    def widgetsPosition(self):
        self.addWidget(self.display, 0, 0, 1, 4)
        self.addWidget(self.clear, 1, 0, 1, 1)
        self.addWidget(self.clear_entry, 1, 1, 1, 1)
        self.addWidget(self.percentage, 1, 2, 1, 1)

        self.addWidget(self.b1, 2, 0, 1, 1)
        self.addWidget(self.b2, 2, 1, 1, 1)
        self.addWidget(self.b3, 2, 2, 1, 1)
        self.addWidget(self.b4, 3, 0, 1, 1)
        self.addWidget(self.b5, 3, 1, 1, 1)
        self.addWidget(self.b6, 3, 2, 1, 1)
        self.addWidget(self.b7, 4, 0, 1, 1)
        self.addWidget(self.b8, 4, 1, 1, 1)
        self.addWidget(self.b9, 4, 2, 1, 1)

        self.addWidget(self.division, 1, 3, 1, 1)
        self.addWidget(self.multiply, 2, 3, 1, 1)
        self.addWidget(self.subtract, 3, 3, 1, 1)
        self.addWidget(self.add, 4, 3, 1, 1)

        self.addWidget(self.negative, 5, 0, 1, 1)
        self.addWidget(self.b0, 5, 1, 1, 1)
        self.addWidget(self.point, 5, 2, 1, 1)
        self.addWidget(self.result, 5, 3, 1, 1)

    def displayCalculus(self):
        self.display = Displayer()

    def createButton(self, text=""):
        button = QPushButton()
        button.setText(str(text))
        button.setMinimumHeight(80)
        button.setMinimumWidth(100)
        button.setMaximumHeight(150)
        button.setStyleSheet(self.cssNumbers())
        return button

    def cssNumbers(self):
        css = """
        QWidget {background: white;}
        
        QPushButton {
        background: #F7F7F7;
        font-size: 27px;
        border-style: none;}
        
        QPushButton:hover {
        background: #D3D3D3;}
        
        QPushButton:pressed {
        background: #C3C3C3;}
        
        """
        return css

    def cssOperation(self):
        css = """
        QPushButton {
        background: #E6E6E6;
        font-size: 25px;
        border-style: none;
        color: #3A3A3A}
        
        QPushButton:hover {
        background: #D3D3D3;}
        
        QPushButton:pressed {
        background: #C3C3C3;}
        
        """
        return css

    def cssResult(self):
        css = """
        QPushButton {
        background: #83B789;
        border-style: none;
        font-size: 25px;}
        
        QPushButton:hover{
        background: #679B6D;}
        
        QPushButton:pressed {
        background: #4C7951;}
        """
        return css
