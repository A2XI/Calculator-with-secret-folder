from PyQt5.QtWidgets import QMessageBox


class PopUp(QMessageBox):
    def __init__(self, calculator):
        super().__init__()
        self.setGeometry(150, 170, 300, 150)
        self.setWindowOpacity(0.96)
        self.calculator = calculator
        self.setWindowTitle("Settings")
        self.setText("Do you want to change your PIN?       ")
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.buttonClicked.connect(self.clickPopup)
        self.calculator.main.move(40, 320)

        self.exec_()

    def clickPopup(self, button):
        if button.text() == "&Yes":
            self.calculator.main.setCurrentWidget(self.calculator.main.settings)
