from PyQt5.QtWidgets import QStackedWidget, QApplication
from PyQt5.QtCore import Qt
from calculator import Calculator
from settings import Settings
from popup import PopUp
from PyQt5.QtGui import QIcon, QPixmap
import sys


class MainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.settingsPage()
        self.computerPage()
        self.setWindowOpacity(0.96)
        self.initUi()

    def initUi(self):
        self.setStyleSheet("background: white;")
        self.setWindowTitle("Calculator")
        if self.settings.json_settings["show_settings"]:
            self.setCurrentWidget(self.settings)
        else:
            self.setCurrentWidget(self.calculator)
        pixmap = QPixmap(100, 100)
        pixmap.fill(Qt.transparent)
        self.setWindowIcon(QIcon(pixmap))

        self.settings.button.clicked.connect(self.saveClick)

    def computerPage(self):
        self.calculator = Calculator(self)
        self.addWidget(self.calculator)

    def settingsPage(self):
        self.settings = Settings()
        self.addWidget(self.settings)

    def saveClick(self):
        self.setCurrentWidget(self.calculator)
        self.settings.json_settings["pin"] = self.settings.pin.text()
        self.settings.json_settings["show_settings"] = False
        self.settings.jsonWrite()
        self.settings.pin.setText("")

    def showPopUp(self):
        self.popup = PopUp(self.calculator)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
