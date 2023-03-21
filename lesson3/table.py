import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QTableWidgetItem, QFileDialog, \
    QInputDialog, QColorDialog, QDialog

from database import global_init, create_session, Student
from database import School
from ui_update_student import Ui_Dialog
from ui_table import Ui_MainWindow


from PyQt5.QtCore import Qt, QModelIndex


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
        self.tableWidget.doubleClicked.connect(self.update_student)
        # self.tableWidget.cellChanged.connect(self.cell_changed)
        # self.pushButton_open_file.clicked.connect(self.color_dialog)

    def update_student(self, index: QModelIndex):
        current_row = index.row()
        id_ = int(self.tableWidget.item(current_row, 0).text())
        self.student_updater = StudentUpdater(id_)
        self.student_updater.exec_()
        self.load_table()


    def open_file(self):
        file_name = QFileDialog.getOpenFileName(self, "Выберите файл", '', 'Текстовый файл (*.txt);;Все файлы (*)')[0]
        print(file_name)

    def input_dialog(self):
        var = QInputDialog.getText(self, 'Введите имя', 'Как вас зовут?')
        print(var)

    def item_dialog(self):
        var = QInputDialog.getItem(self, "Выберите страну",
                                   "Откуда ты?",
                                   ("Россия", "Германия", "США"), 1, False)
        print(var)

    def color_dialog(self):
        color = QColorDialog.getColor()
        print(color)

    def load_table(self):
        self.table_is_changeable = False
        students = self.session.query(Student).all()
        self.tableWidget.setRowCount(0)
        for student in students:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            tmp = QTableWidgetItem(str(student.id))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableWidget.setItem(row_position, 0, tmp)
            tmp = QTableWidgetItem(str(student.name))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableWidget.setItem(row_position, 1, tmp)
            tmp = QTableWidgetItem(str(student.bdate))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableWidget.setItem(row_position, 2, tmp)
            tmp = QTableWidgetItem(str(student.school.name))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableWidget.setItem(row_position, 3, tmp)
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


class StudentUpdater(QDialog, Ui_Dialog):
    def __init__(self, student_id):
        super().__init__()
        self.setupUi(self)

        self.session = create_session()
        self.student = self.session.query(Student).get(student_id)
        self.label_id_2.setText(str(self.student.id))
        self.lineEdit_name.setText(str(self.student.name))
        self.lineEdit_bdate.setText(str(self.student.bdate))
        schools = self.session.query(School).filter(School.id != self.student.school_id).all()
        self.comboBox.addItem(self.student.school.name, self.student.school.id)
        for school in schools:
            self.comboBox.addItem(school.name, school.id)

        self.pushButton.clicked.connect(self.save_data)

    def save_data(self):
        self.student.name = self.lineEdit_name.text()
        self.student.bdate = self.lineEdit_bdate.text()
        cb_ci = self.comboBox.currentIndex()
        school_id = self.comboBox.itemData(cb_ci)
        self.student.school_id = school_id
        self.session.commit()
        self.close()



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