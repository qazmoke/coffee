import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.con = sqlite3.connect("coffee.db")
        cur = self.con.cursor()
        coffee = cur.execute("SELECT * FROM coffee").fetchall()
        self.tableWidget.setRowCount(len(coffee))
        self.tableWidget.setColumnCount(len(coffee[0]))
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Название сорта", "Степень обжарки", "Молотый/в зернах",
                                                    "Описание вкуса", "Цена"])

        [[self.tableWidget.setItem(i, k, QTableWidgetItem(str(m)))
          for k, m in enumerate(j)] for i, j in enumerate(coffee)]


app = QApplication(sys.argv)
ex = Coffee()
ex.show()
app.exec()
