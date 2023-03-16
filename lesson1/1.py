import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

from lesson1.prog1 import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        for btn in self.findChildren(QPushButton):
            btn.clicked.connect(self.action_digit)

    def action_digit(self):
        btn = self.sender()
        btn_text = btn.text()
        if btn_text.isdigit() or btn_text in "+/*-":
            current_text = self.lineEdit.text()
            self.lineEdit.setText(current_text + btn_text)
        elif btn_text == "=":
            equation = self.lineEdit.text()
            value = str(eval(equation))
            self.lineEdit.setText(value)
        elif btn_text == "C":
            self.lineEdit.clear()
        elif btn_text == "<":
            text = self.lineEdit.text()[:-1]
            self.lineEdit.setText(text)




def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)

# Back up the reference to the exceptionhook
sys._excepthook = sys.excepthook

# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())