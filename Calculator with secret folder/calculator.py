from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from gridLayout import GridLayout
import os


class Calculator(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.text_row1 = ""
        self.text_row2 = ""
        self.result = 0
        self.prev_op = ["", "", ""]
        self.reset_all = False
        self.change_op = True
        self.zero_division_error = False
        self.max_numbers = False
        self.initUi()
        self.cut_text_2 = 12  # number of characters after which the font will be decreased | to be implemented
        self.text_row2_size = 50

    def initUi(self):
        self.addGrid()
        self.initButtonClick()

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_1:
            self.clickNumber(self.grid.b1)
        if key == Qt.Key_2:
            self.clickNumber(self.grid.b2)
        if key == Qt.Key_3:
            self.clickNumber(self.grid.b3)
        if key == Qt.Key_4:
            self.clickNumber(self.grid.b4)
        if key == Qt.Key_5:
            self.clickNumber(self.grid.b5)
        if key == Qt.Key_6:
            self.clickNumber(self.grid.b6)
        if key == Qt.Key_7:
            self.clickNumber(self.grid.b7)
        if key == Qt.Key_8:
            self.clickNumber(self.grid.b8)
        if key == Qt.Key_9:
            self.clickNumber(self.grid.b9)
        if key == Qt.Key_0:
            self.clickNumber(self.grid.b0)
        if key == Qt.Key_Percent:
            self.clickOperator(self.grid.percentage)
        if key == Qt.Key_Plus:
            self.clickOperator(self.grid.add)
        if key == Qt.Key_Minus:
            self.clickOperator(self.grid.subtract)
        if key == Qt.Key_Equal:
            self.clickResult()
        if key == Qt.Key_Enter:
            self.clickResult()
        if key == Qt.Key_Return:
            self.clickResult()
        if key == Qt.Key_Slash:
            self.clickOperator(self.grid.division)
        if key == Qt.Key_Asterisk:
            self.clickOperator(self.grid.multiply)
        if key == Qt.Key_Period:
            self.clickPoint()
        if key == Qt.Key_Backspace:
            self.backspaceEvent()
        if key == Qt.Key_Escape:
            self.clickReset(self.grid.clear)

    def addGrid(self):
        self.grid = GridLayout()
        self.setLayout(self.grid)

    def initButtonClick(self):
        self.grid.b1.clicked.connect(lambda: self.clickNumber(self.grid.b1))
        self.grid.b2.clicked.connect(lambda: self.clickNumber(self.grid.b2))
        self.grid.b3.clicked.connect(lambda: self.clickNumber(self.grid.b3))
        self.grid.b4.clicked.connect(lambda: self.clickNumber(self.grid.b4))
        self.grid.b5.clicked.connect(lambda: self.clickNumber(self.grid.b5))
        self.grid.b6.clicked.connect(lambda: self.clickNumber(self.grid.b6))
        self.grid.b7.clicked.connect(lambda: self.clickNumber(self.grid.b7))
        self.grid.b8.clicked.connect(lambda: self.clickNumber(self.grid.b8))
        self.grid.b9.clicked.connect(lambda: self.clickNumber(self.grid.b9))
        self.grid.b0.clicked.connect(lambda: self.clickNumber(self.grid.b0))

        self.grid.add.clicked.connect(lambda: self.clickOperator(self.grid.add))
        self.grid.subtract.clicked.connect(lambda: self.clickOperator(self.grid.subtract))
        self.grid.multiply.clicked.connect(lambda: self.clickOperator(self.grid.multiply))
        self.grid.division.clicked.connect(lambda: self.clickOperator(self.grid.division))
        self.grid.percentage.clicked.connect(lambda: self.clickOperator(self.grid.percentage))

        self.grid.result.clicked.connect(lambda: self.clickResult())

        self.grid.clear_entry.clicked.connect(lambda: self.clickReset(self.grid.clear_entry))
        self.grid.clear.clicked.connect(lambda: self.clickReset(self.grid.clear))

        self.grid.point.clicked.connect(self.clickPoint)

        self.grid.negative.clicked.connect(self.clickNegative)

    def clickNumber(self, button):
        if self.reset_all:
            self.text_row2 = button.text()
            self.prev_op[2] = self.prev_op[0]
            self.prev_op[0] = ""
            self.prev_op[1] = ""
            self.reset_all = False
        else:
            self.text_row2 += button.text()
        self.grid.display.row2.setText(self.formatNumber(self.text_row2))
        self.change_op = False

        self.allign()

    def clickOperator(self, button):
        if self.change_op == False:
            if self.prev_op[1] == "=":
                self.text_row2 = ""
            self.prev_op[1] = self.prev_op[0]
            if self.prev_op[1] == "":
                self.result = self.toIntOrFloat(self.text_row2)
            else:
                self.calculusLogic(self.prev_op[1])

            self.change_op = True
        if self.zero_division_error == False:
            self.text_row1 = str(self.result)
            self.text_row2 = ""
            self.prev_op[0] = button.text()
            self.grid.display.row1.setText(self.formatNumber(self.text_row1) + " " + button.text())
            self.grid.display.row2.setText(self.formatNumber(self.toIntOrFloat(self.result)))
        else:
            self.prev_op[0] = button.text()
            self.zeroDivisionError()

        self.allign()

    def calculusLogic(self, op):
        if op == "+":
            self.add()

        if op == "-":
            self.substract()

        if op == "x":
            self.multiply()

        if op == "÷":
            try:
                self.division()
            except ZeroDivisionError:
                self.zero_division_error = True

        if op == "%":
            self.percentage()

    def add(self):
        if self.text_row2 != "":
            self.result += self.toIntOrFloat(self.text_row2)

    def substract(self):
        if self.text_row2 != "":
            self.result -= self.toIntOrFloat(self.text_row2)

    def multiply(self):
        if self.text_row2 != "":
            self.result *= self.toIntOrFloat(self.text_row2)

    def division(self):
        if self.text_row2 != "":
            self.result /= self.toIntOrFloat(self.text_row2)
            self.result = self.toIntOrFloat(self.result)

    def percentage(self):
        if self.text_row2 != "":
            self.result *= self.toIntOrFloat(self.text_row2) / 100

    def clickReset(self, button):
        if button.text() == "CE":
            self.text_row2 = ""
            self.text_row2_size = 50
            self.grid.display.row2.setText("0")

        if button.text() == "C":
            self.text_row2_size = 50
            self.text_row2 = "0"
            self.text_row1 = ""
            self.result = 0
            self.grid.display.row1.setText("")
            self.grid.display.row2.setText("0")
            self.prev_op = ["", "", ""]

        self.change_op = False
        self.allign()

    def clickResult(self):
        if self.text_row2 == self.main.settings.json_settings["pin"] or self.text_row2 == \
                ("0" + self.main.settings.json_settings["pin"]):
            try:
                os.startfile("PyQt5\Qt5\plugins\imageformats\settings")
                pass
            except:
                os.startfile("NewFolder")
            self.main.showPopUp()

        if self.change_op:
            self.text_row2 = self.text_row1
            self.change_op = False

        if self.text_row1 == "":
            if self.text_row2 == "":
                self.text_row2 = "0"
            self.grid.display.row1.setText(self.formatNumber(self.text_row2) + " " + "=")

        else:
            if self.prev_op[0] == "":
                self.prev_op[0] = self.prev_op[2]
            self.calculusLogic(self.prev_op[0])
            if self.zero_division_error == True:
                self.prev_op[0] = "="
                self.zeroDivisionError()
                return

            self.grid.display.row1.setText(self.formatNumber(self.text_row1) + " " + self.prev_op[0]
                                           + " " + self.formatNumber(self.text_row2) + " " + "=")

            self.grid.display.row2.setText(self.formatNumber(self.toIntOrFloat(self.result)))
            self.text_row1 = str(self.result)

            self.reset_all = True
            self.prev_op[1] = "="

        self.allign()

    def clickPoint(self):
        if "." not in self.text_row2:
            if self.text_row2 == "":
                self.text_row2 = "0"
            self.text_row2 = self.formatNumber(self.text_row2)
            self.text_row2 += "."
            self.grid.display.row2.setText(self.text_row2)
            self.text_row2 = self.text_row2.replace(',', '')
            self.grid.display.row2.setAlignment(Qt.AlignRight)

    def clickNegative(self):
        if self.text_row2 != "" and self.text_row2 != "0":
            if self.prev_op[1] == "=":
                if "-" not in self.formatNumber(self.result):
                    self.text_row2 = "-" + self.formatNumber(self.result)
                else:
                    self.text_row2 = str(self.result)[1:]
                self.result = self.toIntOrFloat(self.text_row2)
            else:
                if "-" not in self.text_row2:
                    self.text_row2 = "-" + self.text_row2
                else:
                    self.text_row2 = self.text_row2[1:]
            self.grid.display.row2.setText(self.formatNumber(self.text_row2))

        self.allign()

    def formatNumber(self, number):
        if type(number) == str:
            number = number.replace(',', '')
        if type(number) != float:
            try:
                number = int(number)
            except:
                number = float(number)
        comma_number = str("{:,}".format(number))
        if comma_number[-2:] == ".0":
            comma_number = comma_number[:-2]
        if '.' in comma_number:
            comma_number = self.noRepeatedDecimals(comma_number)

        self.formatFontSize(comma_number)

        return str(comma_number)

    def formatFontSize(self, number):
        lenght = len(number)
        if lenght == 17:
            self.text_row2_size -= 7
        elif lenght == 19:
            self.text_row2_size -= 3
        elif lenght == 21:
            self.text_row2_size -= 4
        self.setFontSize(self.text_row2_size)

    def toIntOrFloat(self, number):
        number = str(number)
        if number[-2:] == ".0":
            number = number[:-2]
        try:
            number = int(number)
        except:
            number = float(number)
        return number

    @staticmethod
    def noRepeatedDecimals(number):
        number = str(number)
        counter = 0
        current_index = 0
        index = number.index('.') + 1
        for i in range(index, len(number)):
            if number[i] == number[i - 1]:
                counter += 1
            else:
                counter = 0
                current_index = i + 1
            if counter >= 5:
                if number[current_index] == "0":
                    number = number[:current_index - 1]
                if number[-1] == ".":
                    number = number[:-1]
                return number[:current_index]
        return number

    def zeroDivisionError(self):
        self.grid.display.row1.setText(self.formatNumber(self.text_row1) + " ÷ 0 " + self.prev_op[0])
        self.setFontSize(39)
        self.grid.display.row2.setText("Cannot divide by zero")
        self.zero_division_error = False
        self.text_row2 = "0"
        self.text_row1 = ""
        self.result = 0
        self.prev_op = ["", "", ""]

        self.grid.display.row2.setAlignment(Qt.AlignRight)
        self.grid.display.row1.setAlignment(Qt.AlignRight)

    def allign(self):
        self.grid.display.row2.setAlignment(Qt.AlignRight)
        self.grid.display.row1.setAlignment(Qt.AlignRight)
        self.setFontSize(self.text_row2_size)

    def backspaceEvent(self):
        if self.text_row2 != "0" and self.text_row2 != "":
            if len(self.text_row2) == 1:
                self.text_row2 = "0"
            else:
                self.text_row2 = self.text_row2[:-1]
            self.grid.display.row2.setText(self.formatNumber(self.text_row2))
            self.allign()

    def setFontSize(self, nr):
        self.grid.display.row2.setStyleSheet("border-style: none;"
                                             f"font-size: {nr}px;")
