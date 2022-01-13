from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QWidget
from PyQt5.QtCore import Qt, QRegExp, QSize
from PyQt5.QtGui import QRegExpValidator, QIcon
import json


class Settings(QWidget):
    def __init__(self):
        super().__init__()
        self.show_pin = False
        self.jsonRead()
        self.initUi()

    def initUi(self):
        self.informativeText()
        self.saveButton()
        self.pinText()

    def informativeText(self):
        self.label_welcome = QLabel(self)
        self.label_welcome.setGeometry(50, 10, 350, 80)
        self.label_welcome.setText("Welcome!")
        self.label_welcome.setStyleSheet(self.labelCss(55))

        self.label1 = QLabel(self)
        self.label1.setGeometry(50, 95, 350, 70)
        self.label1.setText("Insert a PIN")
        self.label1.setStyleSheet(self.css())

        self.label2 = QLabel(self)
        self.label2.setGeometry(50, 150, 330, 50)
        self.label2.setText("The PIN should contain 5 to 7 numbers")
        self.label2.setStyleSheet(self.labelCss(20))

        self.label3 = QLabel(self)
        self.label3.setGeometry(50, 340, 330, 80)
        self.label3.setWordWrap(True)
        self.label3.setText('Info: to activate the secret folder, you have to insert your pin, followed by "=", '
                            'in the calculator application.')
        self.label3.setStyleSheet(self.labelCss(15))
        self.label3.setAlignment(Qt.AlignJustify)

        self.quote = QLabel(self)
        self.quote.setGeometry(50, 413, 330, 150)
        self.quote.setStyleSheet("background: yellow;")
        self.quote.setWordWrap(True)
        self.quote.setText('"If you reveal your secrets to the wind, you should not blame the wind for revealing them '
                           'to the trees."')
        self.quote.setStyleSheet(self.quoteCss())
        self.quote.setAlignment(Qt.AlignJustify)

    def pinText(self):
        self.pin = QLineEdit(self)
        self.pin.setGeometry(50, 220, 330, 100)
        self.pin.setStyleSheet(self.css())
        self.pin.setAlignment(Qt.AlignLeft)
        self.pinValidator()
        self.pin.textChanged.connect(self.showSaveButton)
        self.pin.setEchoMode(QLineEdit.Password)
        self.showPin()

    def showSaveButton(self):
        if len(self.pin.text()) >= 5:
            self.button.show()
            self.quote.hide()
        else:
            self.button.hide()
            self.quote.show()

    def saveButton(self):
        self.button = QPushButton(self)
        self.button.setGeometry(120, 455, 190, 60)
        self.button.setStyleSheet(self.css())
        self.button.setText("SAVE")
        self.button.hide()

    def showPin(self):
        self.show_pin_button = QPushButton(self)
        self.show_pin_button.setGeometry(323, 249, 40, 40)
        self.show_pin_button.setIcon(QIcon("img/display_true.png"))
        self.show_pin_button.setIconSize(QSize(40, 40))
        self.show_pin_button.setStyleSheet('border-style: none;')

        self.show_pin_button.clicked.connect(self.clickShowPin)

    def clickShowPin(self):
        if self.show_pin == False:
            self.show_pin_button.setIcon(QIcon("img/display_false.png"))
            self.pin.setEchoMode(QLineEdit.Normal)
            self.show_pin = True
        else:
            self.show_pin_button.setIcon(QIcon("img/display_true.png"))
            self.pin.setEchoMode(QLineEdit.Password)
            self.show_pin = False

    def jsonRead(self):
        try:
            with open("settings.json", "r") as fr:
                self.json_settings = json.load(fr)
        except:
            with open("PyQt5\Qt5\plugins\platforms\settings.json", "r") as fr:  # path to hide settings.json
                self.json_settings = json.load(fr)

    def jsonWrite(self):
        try:
            with open("settings.json", "w") as fw:
                json.dump(self.json_settings, fw)
        except:
            with open("PyQt5\Qt5\plugins\platforms\settings.json", "r") as fr:  # path to hide settings.json
                self.json_settings = json.load(fr)

    def pinValidator(self):
        self.regx = QRegExp("^\d{5,7}")
        self.input_validator = QRegExpValidator(self.regx, self.pin)
        self.pin.setValidator(self.input_validator)

    def css(self):
        css = """
        QLineEdit {
        border: 7px solid #826884;
        border-radius: 20px;
        font-size: 60px;}
        
        QLabel {
        font-size: 30px;
        font-family: Dubai;
        }
        
        QPushButton {
        font-family: Dubai;
        font-weight: bold;
        font-size: 40px;
        color: #826884;
        border: 5px solid #826884;
        border-radius: 30px;
        }
        
        QPushButton:hover{
        background: #826884;
        color: white;
        }
        """
        return css

    def labelCss(self, size):
        css = f"""
        font-size: {size}px;
        text-align: justify;
        font-family: Dubai;
        """
        return css

    def quoteCss(self):
        css = """
        font-size: 22px;
        text-align: justify;
        font-family: Dubai;
        font-weight: bold;
        font-style: italic;
        color: #826884;
        """
        return css
