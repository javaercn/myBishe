import sys
import os

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Dao.getMangerMsg as ManagerMsg


class Manager(QDialog):
    def __init__(self):
        super(Manager, self).__init__()
        self.__getManager()
        self.setWindowTitle("数据库管理")
        self.textEdit = QTextEdit(self)
        self.textEdit.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.textEdit.customContextMenuRequested.connect(self.rightMenuShow)
        self.__msg = ManagerMsg.ManagerMsg().getAllTablesNames()
        self.setFixedSize(1100, 700)
        self.pasteLabel()

    def __getManager(self):
        with open("../resources/manager/manager.txt", 'r') as f:
            self.__manager = f.read()

    def paintEvent(self, QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        qp.drawRect(10, 10, 1080, 50)
        qp.drawRect(10, 65, 1080, 27)
        qp.drawRect(10, 100, 250, 620)
        qp.drawRect(270, 100, 820, 320)
        qp.drawRect(270, 430, 820, 260)

        qp.end()

    def pasteLabel(self):
        label_show = QLabel(self)
        label_show.resize(1079, 49)
        label_show.move(11, 11)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#B9D3EE"))
        label_show.setPalette(palette)
        label_show.setAutoFillBackground(True)

        label1 = QLabel(self)
        label1.resize(100, 50)
        label1.move(450, 10)
        label1.setText(self.__manager)

        label2 = QLabel(self)
        label2.resize(200, 50)
        label2.move(550, 10)
        label2.setText("欢迎您")

        # 10,70,200,620
        self.tree_model = QTreeWidget(self)
        self.tree_model.resize(249, 589)
        self.tree_model.move(11, 101)
        self.tree_model.setColumnCount(2)
        self.tree_model.setHeaderLabels(["表", "类型"])
        self.tree_model.setToolTip("hello")
        root = QTreeWidgetItem(self.tree_model)
        root.setText(0, 'dataset')
        root.setIcon(0, QIcon('../resources/icons/db.png'))
        # 设置宽度
        self.tree_model.setColumnWidth(0, 140)
        self.tree_model.clicked.connect(self.onClicked)
        QToolTip.setFont(QFont('SansSerif', 12))
        for key, value in self.__msg.items():
            child1 = QTreeWidgetItem()
            child1.setText(0, key)
            child1.setIcon(0, QIcon('../resources/icons/table.png'))
            root.addChild(child1)
            for i in value:
                child3 = QTreeWidgetItem(child1)
                child3.setText(0, i)
                child3.setText(1, "int")

        # 270,100,870,320
        self.textEdit.resize(819, 319)
        self.textEdit.move(271, 101)
        self.textEdit.setPlaceholderText("写出你的sql语句")

        # 显示结果的标签270,430,820,260
        self.showResult = QTextEdit(self)
        self.showResult.resize(819, 259)
        self.showResult.move(271, 431)
        self.showResult.setWordWrapMode(True)
        self.showResult.setFocusPolicy(QtCore.Qt.NoFocus)

        # 显示表名等
        self.showMsgEdit = QTextEdit(self)
        self.showMsgEdit.resize(1020, 26)
        self.showMsgEdit.move(11, 66)
        self.showMsgEdit.setPlaceholderText("显示点击的全部信息")

        # 刷新按钮
        self.button = QPushButton(self)
        self.button.resize(65, 26)
        self.button.move(1029, 66)
        self.button.setText("立即刷新")
        self.button.clicked.connect(self.myupdate)

        # 更新前段图片

    def myupdate(self):
        import Service.updatePics as update
        obj = update.updatePics()
        obj.updatePics()

    # 点击左边控件的响应函数
    def onClicked(self):
        item = self.tree_model.currentItem()
        key = item.text(0)
        value = item.text(1)
        if key == "dataset":
            showValue = ""
        else:
            if value.__len__() == 0:
                showValue = "表名是:" + key
            else:
                showValue = "字段名是:" + key + "      " + "字段类型是:" + value
        self.showMsgEdit.setText(showValue)

    def rightMenuShow(self):
        try:
            self.contextMenu = QMenu()
            self.actionA = self.contextMenu.addAction(QIcon("../resources/icons/execute.png"), u'| 执行')
            self.actionB = self.contextMenu.addAction(QIcon("../resources/icons/clear.png"), u'| 清除')
            self.contextMenu.popup(QCursor.pos())  # 2菜单显示的位置
            self.actionA.triggered.connect(self.actionExecute)
            self.actionB.triggered.connect(self.actionClear)
            self.contextMenu.show()
        except Exception as e:
            print(e)

    def actionExecute(self):
        import Service.updatePics as update
        obj = update.updatePics()
        import Service.executeSqls as executesql
        self.showResult.clear()
        info = self.textEdit.toPlainText()
        sqls = info.splitlines()
        if sqls.__len__() == 0:
            pass
        else:
            ex_sql = sqls[-1]
            obj.updateStrategy(ex_sql)  # 处理更新的逻辑
            value = executesql.executeSqls(ex_sql).executeCurrentSql()
            if value is None:
                self.showResult.append("执行错误")
            else:
                if value == 0:
                    self.showResult.append("执行成功")
                else:
                    for i in value:
                        self.showResult.append(i)

    def actionClear(self):
        self.textEdit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_mainwindow = Manager()
    the_mainwindow.show()
    sys.exit(app.exec_())
