import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QTableWidgetItem

from database import global_init, create_session, Student
from ui_table import Ui_MainWindow

from PyQt5.QtCore import Qt

class TableViewer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.table_is_changeable = True

    def initUI(self):
        global_init("database/db.db")
        self.session = create_session()
        self.pushButton.clicked.connect(self.load_table)
        self.tableWidget.cellChanged.connect(self.cell_changed)

    def load_table(self):
        self.table_is_changeable = False
        students = self.session.query(Student).all()
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        for student in students:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            tmp = QTableWidgetItem(str(student.id))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableWidget.setItem(row_position, 0, tmp)
            self.tableWidget.setItem(row_position, 1, QTableWidgetItem(student.name))
            self.tableWidget.setItem(row_position, 2, QTableWidgetItem(student.bdate))
            self.tableWidget.setItem(row_position, 3, QTableWidgetItem(student.school.name))
        self.table_is_changeable = True

    def cell_changed(self, row, col):
        if self.table_is_changeable:
            id_ = int(self.tableWidget.item(row, 0).text())
            student = self.session.query(Student).\
                filter(Student.id == id_).first()
            if col == 1:
                student.name = self.tableWidget.item(row, col).text()
                self.session.commit()
            elif col == 2:
                student.bdate = self.tableWidget.item(row, col).text()
                self.session.commit()



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
    ex = TableViewer()
    ex.show()
    sys.exit(app.exec())