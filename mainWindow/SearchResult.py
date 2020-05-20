import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import Service.dealSearch as SearchResult
class SearchDialog(QDialog):
    def  __init__(self,msg):
        super(SearchDialog, self).__init__()
        self.__sqls=SearchResult.Dealtxt(msg).changge_format()
        self.setWindowTitle("查询结果")
        self.index_page = 1
        self.end_page = int(self.__sqls.__len__() / 10)
        self.setFixedSize(700,500)
        self.setWindowFlags(Qt.Tool)
        self.pasteLable()

    def pasteLable(self):
        self.buttonUp = QPushButton(self)
        self.buttonUp.setText("上一页")
        self.buttonUp.move(80, 430)
        self.buttonUp.clicked.connect(self.pageUp)

        self.buttonDown = QPushButton(self)
        self.buttonDown.setText("下一页")
        self.buttonDown.move(530, 430)
        self.buttonDown.clicked.connect(self.pageDown)

        self.Text_showSql=QTableWidget(self)
        self.Text_showSql.setRowCount(10)
        self.Text_showSql.setColumnCount(1)
        self.Text_showSql.setColumnWidth(0, 600)
        self.Text_showSql.setHorizontalHeaderLabels(["查询结果"])
        self.Text_showSql.resize(600,403)
        self.Text_showSql.move(50,10)
        self.pageUp()



    def pageUp(self):
        self.index_page -= 1
        self.start = self.index_page * 10
        if self.index_page == self.end_page:
            self.end = self.__sqls.__len__()
        else:
            self.end = self.start + 10
        page_lists = range(self.start, self.end)
        for i in page_lists:
            self.Text_showSql.setItem(i - self.start, 0, QTableWidgetItem(self.__sqls[i]))
        shen_len = 10 - (self.end - self.start)
        for i in range(shen_len):
            self.Text_showSql.setItem(i + self.end - self.start, 0, QTableWidgetItem("  "))
        if self.index_page == 0:
            self.buttonUp.setEnabled(False)
        if self.index_page == self.end_page:
            self.buttonDown.setEnabled(False)
        else:
            self.buttonDown.setEnabled(True)

    def pageDown(self):
        self.index_page += 1
        self.start = self.index_page * 10
        if self.index_page == self.end_page:
            self.end = self.__sqls.__len__()
        else:
            self.end = self.start + 10
        page_lists = range(self.start, self.end)
        for i in page_lists:
            self.Text_showSql.setItem(i - self.start, 0, QTableWidgetItem(self.__sqls[i]))
        shen_len = 10 - (self.end - self.start)
        for i in range(shen_len):
            self.Text_showSql.setItem(i + self.end - self.start, 0, QTableWidgetItem("  "))
        if self.index_page == self.end_page:
            self.buttonDown.setEnabled(False)
        if self.index_page == 1:
            self.buttonUp.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_mainwindow = SearchDialog("攻击类型")
    the_mainwindow.show()
    sys.exit(app.exec_())