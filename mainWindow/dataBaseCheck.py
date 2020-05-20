import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mainWindow.MySignal as mySignal
import Service.showSqls as showSql

class dataBase(QWidget):
    def __init__(self, parent=None):
        super(dataBase, self).__init__(parent)
        self.__sqls = showSql.getSqls().getMySqls()
        self.button = QPushButton(self)
        self.index_page = 1
        self.end_page=int(self.__sqls.__len__()/10)
        self.buttonDown = QPushButton(self)
        self.setFixedSize(1100, 700)
        self.pasteLable()
        self.setWindowTitle("数据库审计")



    def paintEvent(self, QPaintEvent):
        qp = QPainter()
        # 椭圆
        qp.begin(self)
        qp.setFont(QFont('Arial', 15))
        qp.setPen(QColor(Qt.black))
        # logol


        # 矩形1
        # qp.drawRect(0,50,100,550)
        qp.fillRect(0, 50, 100, 550, QBrush(QColor("#B9D3EE")))

        # 矩形2  我的安全设备
        # qp.drawRect(0,600,100,100)
        qp.fillRect(0, 600, 100, 100, QBrush(QColor("#4F94CD")))
        qp.drawText(10, 640, "我的安")
        qp.drawText(10, 670, "全设备")

        # 矩形3  防火墙防护类型
        # qp.drawRect(0, 50, 100, 100)
        qp.fillRect(0, 50, 100, 100, QBrush(QColor("#9FB6CD")))
        # 写字
        qp.drawText(10, 90, "防火墙")
        qp.drawText(10, 115, "防护类")
        qp.drawText(10, 140, "型")

        # 画右边
        qp.drawRect(1000, 50, 100, 650)

        # 右边 风险预报
        # qp.drawRect(1000,50,100,50)
        qp.setFont(QFont('Arial', 10))
        qp.fillRect(1000, 50, 100, 50, QBrush(QColor("#B22222")))
        qp.drawText(1001, 80, "攻击方法排名")

        # 右边 显示风险预报
        # qp.drawRect(1000,100,100,130)
        qp.fillRect(1000, 100, 100, 130, QBrush(QColor("#B9D3EE")))

        # 右边 攻击源排行
        # qp.drawRect(1000,230,100,50)
        qp.setFont(QFont('Arial', 12))
        qp.fillRect(1000, 230, 100, 50, QBrush(QColor("#B22222")))
        qp.drawText(1000, 260, "攻击源排行")

        # 右边显示  攻击源
        # qp.drawRect(1000,280,100,130)
        qp.fillRect(1000, 280, 100, 130, QBrush(QColor("#B9D3EE")))

        # 右边显示  攻击源次数
        # qp.drawRect(1000, 460, 100, 140)
        qp.fillRect(1000, 460, 100, 140, QBrush(QColor("#B9D3EE")))

        # 我的安全威胁
        qp.setFont(QFont('Arial', 15))
        qp.fillRect(1000, 600, 100, 100, QBrush(QColor("#EE2C2C")))
        qp.drawText(1010, 640, "我的安")
        qp.drawText(1010, 670, "全威胁")
    ##########################################################################
        qp.drawRect(120,60,860,460)

        qp.drawRect(200,535,100,50)

        qp.drawRect(800,535,100,50)


    #########################################################################

        # 最底下
        qp.drawRect(100, 600, 900, 100)

        # 最上边搜索栏
        qp.drawRect(100, 5, 900, 40)

        # 搜索按钮
        qp.drawRect(1005, 5, 80, 40)


    def pasteLable(self):
        # 显示防护器防护类型
        mylabel2 = QLabel(self)
        mylabel2.resize(100, 50)
        mylabel2.move(0, 0)
        mylabel2.setAutoFillBackground(True)
        mylabel2.setPixmap(QPixmap("../resources/logo/logo.png"))
        mylabel2.setScaledContents(True)

        # 这个label可以显示被攻击排
        label_BeiGongJi = QLabel(self)
        label_BeiGongJi.resize(100, 450)
        label_BeiGongJi.move(0, 150)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#B9D3EE"))
        label_BeiGongJi.setPalette(palette)
        label_BeiGongJi.setAutoFillBackground(True)

        '''
        显示风险报警
        '''
        label_FengXian = QLabel(self)
        label_FengXian.resize(100, 130)
        label_FengXian.move(1000, 100)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#B9D3EE"))
        label_FengXian.setPalette(palette)
        label_FengXian.setAutoFillBackground(True)

        '''
        显示攻击源排行
        '''
        label_GongJiYuan = QLabel(self)
        label_GongJiYuan.resize(100, 320)
        label_GongJiYuan.move(1000, 280)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#B9D3EE"))
        label_GongJiYuan.setPalette(palette)
        label_GongJiYuan.setAutoFillBackground(True)
#################################################################
        '''
              显示sql语句
        '''
        headerList=[]
        headerList.append("sql语句")
        headerList.append("操作者")
        headerList.append("时间")
        headerList.append("风险程度")
        self.Text_showSql = QTableWidget(self)
        self.Text_showSql.setRowCount(10)
        self.Text_showSql.setColumnCount(4)
        self.Text_showSql.setHorizontalHeaderLabels(headerList)
        self.Text_showSql.setColumnWidth(0,400)
        self.Text_showSql.setColumnWidth(1, 100)
        self.Text_showSql.setColumnWidth(2, 150)
        self.Text_showSql.setColumnWidth(3, 150)
        self.Text_showSql .resize(860, 460)
        self.Text_showSql .move(120,60)


        #200,535,100,50
        self.buttonUp=QPushButton(self)
        self.buttonUp.resize(100,50)
        self.buttonUp.move(200,535)
        self.buttonUp.setText("上一页")
        self.pageUp()
        self.buttonUp.clicked.connect(self.pageUp)

        # 800,535,100,50

        self.buttonDown.resize(100, 50)
        self.buttonDown.move(800,535)
        self.buttonDown.setText("下一页")
        self.buttonDown.clicked.connect(self.pageDown)



        #####################################################################
        # 最下层
        # 防火墙110,610,115,80
        label_FangHuo = mySignal.myLabel(self)
        label_FangHuo.resize(200, 80)
        label_FangHuo.move(120, 610)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#D2691E"))
        label_FangHuo.setPalette(palette)
        label_FangHuo.setFont(QFont('Arial', 15))
        label_FangHuo.setText("          主界面")
        label_FangHuo.setAutoFillBackground(True)
        label_FangHuo.clicked.connect(self.MainSlot)

        # 这里添加槽
        # 入侵检测110,610,115,80
        label_RuQinJIanCe = QLabel(self)
        label_RuQinJIanCe.resize(200, 80)
        label_RuQinJIanCe.move(340, 610)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#D2691E"))
        label_RuQinJIanCe.setPalette(palette)
        label_RuQinJIanCe.setFont(QFont('Arial', 15))
        label_RuQinJIanCe.setText("        web安全")
        label_RuQinJIanCe.setAutoFillBackground(True)
        # 这里添加槽

        # 入侵防护110,610,115,80
        label_RuQinFangHu = mySignal.myLabel(self)
        label_RuQinFangHu.resize(200, 80)
        label_RuQinFangHu.move(560, 610)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#D2691E"))
        label_RuQinFangHu.setPalette(palette)
        label_RuQinFangHu.setFont(QFont('Arial', 15))
        label_RuQinFangHu.setText("      防火墙")
        label_RuQinFangHu.setAutoFillBackground(True)
        label_RuQinFangHu.clicked.connect(self.FangSlot)
        # 这里添加槽

        # 堡垒机110,610,115,80
        label_BaoLeiJi = mySignal.myLabel(self)
        label_BaoLeiJi.resize(200, 80)
        label_BaoLeiJi.move(780, 610)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#D2691E"))
        label_BaoLeiJi.setPalette(palette)
        label_BaoLeiJi.setFont(QFont('Arial', 15))
        label_BaoLeiJi.setText("     管理员登陆")
        label_BaoLeiJi.setAutoFillBackground(True)
        label_BaoLeiJi.clicked.connect(self.Login)
        # 这里添加槽

        # 这里添加槽

        # 添加按钮1005,5,80,40

        self.button.setText("搜索")
        self.button.resize(80, 40)
        self.button.move(1005, 5)
        self.button.clicked.connect(self.searchDoalog)
        # 添加槽

        # 输入框100,5,900,40
        self.lineEdit = QLineEdit(self)
        self.lineEdit.resize(900, 40)
        self.lineEdit.move(100, 5)
        self.lineEdit.setPlaceholderText("智能查询(输入所要查询的基本信息)")

    def pageUp(self):
        self.index_page-=1
        self.start = self.index_page * 10
        if self.index_page == self.end_page:
            self.end = self.__sqls.__len__()
        else:
            self.end = self.start + 10
        page_lists = range(self.start, self.end)
        for i in page_lists:
            self.Text_showSql.setItem(i - self.start, 0, QTableWidgetItem(self.__sqls[i][0]))
            self.Text_showSql.setItem(i - self.start, 1, QTableWidgetItem(self.__sqls[i][1]))
            self.Text_showSql.setItem(i - self.start, 2, QTableWidgetItem(self.__sqls[i][2]))
            self.Text_showSql.setItem(i - self.start, 3, QTableWidgetItem(self.__sqls[i][3]))
        shen_len = 10 - (self.end - self.start)
        for i in range(shen_len):
            self.Text_showSql.setItem(i + self.end - self.start, 0, QTableWidgetItem("  "))
            self.Text_showSql.setItem(i + self.end - self.start, 1, QTableWidgetItem("  "))
            self.Text_showSql.setItem(i + self.end - self.start, 2, QTableWidgetItem("  "))
            self.Text_showSql.setItem(i + self.end - self.start, 3, QTableWidgetItem("  "))
        if self.index_page == 0:
            self.buttonUp.setEnabled(False)
        if self.index_page==self.end_page:
            self.buttonDown.setEnabled(False)
        else:
            self.buttonDown.setEnabled(True)

    def pageDown(self):
        self.index_page+=1
        self.start = self.index_page * 10
        if self.index_page == self.end_page:
            self.end = self.__sqls.__len__()
        else:
            self.end = self.start + 10
        page_lists = range(self.start, self.end)
        for i in page_lists:
            self.Text_showSql.setItem(i-self.start, 0, QTableWidgetItem(self.__sqls[i][0]))
            self.Text_showSql.setItem(i-self.start, 1, QTableWidgetItem(self.__sqls[i][1]))
            self.Text_showSql.setItem(i-self.start, 2, QTableWidgetItem(self.__sqls[i][2]))
            self.Text_showSql.setItem(i-self.start, 3, QTableWidgetItem(self.__sqls[i][3]))
        shen_len=10-(self.end-self.start)
        for i in range(shen_len):
            self.Text_showSql.setItem(i + self.end-self.start, 0, QTableWidgetItem("  "))
            self.Text_showSql.setItem(i + self.end-self.start, 1, QTableWidgetItem("  "))
            self.Text_showSql.setItem(i + self.end-self.start, 2, QTableWidgetItem("  "))
            self.Text_showSql.setItem(i + self.end-self.start, 3, QTableWidgetItem("  "))
        if self.index_page == self.end_page:
            self.buttonDown.setEnabled(False)
        if self.index_page==1:
            self.buttonUp.setEnabled(True)


    def searchDoalog(self):
        import mainWindow.SearchResult as search
        data = self.lineEdit.text()
        if data.__len__()==0:
          QMessageBox.information(self, "提示", "请输入查询信息", QMessageBox.Yes , QMessageBox.Yes)
        else:
            dialog = search.SearchDialog(data)
            if dialog.exec_() == QDialog.Accepted:
                pass


    def MainSlot(self):
        import mainWindow.mainWeidget as mainWeidget
        self.hide()
        self.s = mainWeidget.firstWeidget()
        self.s.show()

    def WebSafeSlot(self):
        import mainWindow.FangHuoQiangWeidget as Fang
        self.hide()
        self.s = Fang.FangWeidget()
        self.s.show()

    def FangSlot(self):
        import mainWindow.FangHuoQiangWeidget as secondWeidget
        self.hide()
        self.s = secondWeidget.FangWeidget()
        self.s.show()
    def Login(self):
        import mainWindow.login2 as login2
        dialog = login2.Login()
        if dialog.exec_() == QDialog.Accepted:
            pass

if __name__=='__main__':
    app = QApplication(sys.argv)
    mainindow = dataBase()
    mainindow.show()
    sys.exit(app.exec_())