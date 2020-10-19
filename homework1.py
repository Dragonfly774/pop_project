import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QListWidgetItem
from PyQt5.QtWidgets import QLabel, QLineEdit, QMainWindow, QListWidget
from bookname import Ui_MainWindow

class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # uic.loadUi('bookname.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        name = self.lineEdit.text()
        tel = self.lineEdit_2.text()
        item = (name, tel)
        self.listWidget.addItem(name + ' ' + tel)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
