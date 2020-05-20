
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mainWindow.MySignal as mySignal
import mainWindow.FangHuoQiangWeidget as secondWeidget
import Service.showPics.dealMain as dealMain
import Service.showMsg as myMsg



class firstWeidget(QWidget):
    def __init__(self, parent=None):
        super(firstWeidget, self).__init__(parent)
        self.path=""
        self.setWindowTitle("主界面")
        self.setFixedSize(1100, 700)
        self.dataObj = myMsg.getMsgs()
        self.picData = dealMain.dealMainPics()
        self.InitUI()


    def InitUI(self):
        self.pasteLable()



    def paintEvent(self, QPaintEvent):
        qp = QPainter()
        #椭圆
        qp.begin(self)
        qp.setFont(QFont('Arial', 15))
        qp.setPen(QColor(Qt.black))
        #logol


        #矩形1
        #qp.drawRect(0,50,100,550)
        qp.fillRect(0,50,100,550, QBrush(QColor("#B9D3EE")))


        #矩形2  我的安全设备
        #qp.drawRect(0,600,100,100)
        qp.fillRect(0,600,100,100, QBrush(QColor("#4F94CD")))
        qp.drawText(10, 640, "我的安")
        qp.drawText(10, 670, "全设备")

        #矩形3  我的网络资产
        #qp.drawRect(0, 50, 100, 100)
        qp.fillRect(0, 50, 100, 100, QBrush(QColor("#9FB6CD")))
        #写字
        qp.drawText(10, 90, "我的网")
        qp.drawText(10, 115, "络资产")

        #矩形4  485台
        #qp.drawRect(0,150,100,80)
        qp.fillRect(0,150,100,80, QBrush(QColor("#B9D3EE")))
        qp.drawText(15, 190, "485台")



        #矩形5,被攻击排名
        #qp.drawRect(0,230,100,50)
        qp.setFont(QFont('Arial', 12))
        qp.fillRect(0,230,100,50, QBrush(QColor("#B22222")))
        qp.drawText(0, 265, "被攻击排名")


        #画右边
        qp.drawRect(1000,50,100,650)

        #右边 风险预报
        #qp.drawRect(1000,50,100,50)
        qp.fillRect(1000,50,100,50, QBrush(QColor("#B22222")))
        qp.drawText(1010,80, "风险报警")

        #右边 显示风险预报
        #qp.drawRect(1000,100,100,130)
        qp.fillRect(1000,100,100,130, QBrush(QColor("#B9D3EE")))

        #右边 攻击源排行
        #qp.drawRect(1000,230,100,50)
        qp.setFont(QFont('Arial', 12))
        qp.fillRect(1000,230,100,50, QBrush(QColor("#B22222")))
        qp.drawText(1000, 260, "攻击源排行")

        #右边显示  攻击源
        #qp.drawRect(1000,280,100,130)
        #qp.fillRect(1000,280,100,130, QBrush(QColor("#B9D3EE")))


        # 右边 攻击源次数排行
        #qp.drawRect(1000, 410, 100, 50)
        qp.setFont(QFont('Arial', 10))
        qp.fillRect(1000, 410, 100, 50, QBrush(QColor("#B22222")))
        qp.drawText(1000, 440, "攻击次数排名")

        # 右边显示  攻击源次数
        #qp.drawRect(1000, 460, 100, 140)
        #qp.fillRect(1000, 460, 100, 140, QBrush(QColor("#B9D3EE")))



        #我的安全威胁
        qp.setFont(QFont('Arial', 15))
        qp.fillRect(1000, 600, 100, 100, QBrush(QColor("#EE2C2C")))
        qp.drawText(1010, 640, "我的安")
        qp.drawText(1010, 670, "全威胁")


        #最底下
        qp.drawRect(100,600,900,100)

        #最上边搜索栏
        qp.drawRect(100,5,900,40)

        #搜索按钮
        qp.drawRect(1005,5,80,40)



        #接下来画里边，长900，宽550
        #画左上的表格
        #qp.drawRect(150,60,200,50)
        qp.fillRect(150,60,200,50, QBrush(QColor("#E6E6FA")))
        qp.drawText(152, 90, "设备防护状态统计")
        qp.drawRect(100,120,290,200)

        #中上
        #qp.drawRect(450,60,200,50)
        qp.fillRect(450,60,200,50, QBrush(QColor("#E6E6FA")))
        qp.drawText(452, 90, "风险及风险资产")
        qp.drawRect(405,120,290,200)

        #左上
        #qp.drawRect(750,60,200,50)
        qp.fillRect(750,60,200,50, QBrush(QColor("#E6E6FA")))
        qp.drawText(775, 90, "高危漏洞统计")
        qp.drawRect(710,120,290,200)

        # 画左下的表格###########
        #qp.drawRect(150, 340, 200, 50)
        qp.fillRect(150, 340, 200, 50, QBrush(QColor("#E6E6FA")))
        qp.drawText(175, 370, "攻击次数分析")
        qp.drawRect(100, 400, 290, 200)

        # 中下
        #qp.drawRect(450, 340, 200, 50)
        qp.fillRect(450, 340, 200, 50, QBrush(QColor("#E6E6FA")))
        qp.drawText(475, 370, "攻击源分析")
        qp.drawRect(405, 400, 290, 200)

        # 中右
        #qp.drawRect(750, 340, 200, 50)
        qp.fillRect(750, 340, 200, 50, QBrush(QColor("#E6E6FA")))
        qp.drawText(775, 370, "攻击类型分析")
        qp.drawRect(710, 400, 290, 200)

        #最下边
        #qp.drawRect(110,610,115,80)
        qp.fillRect(110,610,115,80, QBrush(QColor("#D2691E")))
        qp.drawText(130, 660, "防火墙")
        #qp.drawRect(235,610,115,80)
        qp.fillRect(235,610,115,80, QBrush(QColor("#D2691E")))
        qp.drawText(245, 660, "入侵检测")
        #qp.drawRect(360,610,115,80)
        qp.fillRect(360,610,115,80, QBrush(QColor("#D2691E")))
        qp.drawText(370, 660, "入侵防护")
        #qp.drawRect(485,610,115,80)
        qp.fillRect(485,610,115,80, QBrush(QColor("#D2691E")))
        qp.drawText(505, 660, "堡垒机")
        #qp.drawRect(610,610,115,80)
        qp.fillRect(610,610,115,80, QBrush(QColor("#D2691E")))
        qp.drawText(630, 660, "洞扫描")
        #qp.drawRect(735,610,115,80)
        qp.fillRect(735,610,115,80, QBrush(QColor("#D2691E")))
        qp.drawText(748, 660, "web安全")
        #qp.drawRect(860,610,115,80)
        qp.fillRect(860,610,133,80, QBrush(QColor("#D2691E")))
        qp.drawText(870, 660, "数据库审计")
        qp.end()

    def pasteLable(self):
        #显示台数,这里可以设置显示台数
        mylabel2 = QLabel(self)
        mylabel2.resize(100, 50)
        mylabel2.move(0, 0)
        mylabel2.setAutoFillBackground(True)
        mylabel2.setPixmap(QPixmap("../resources/logo/logo.png"))
        mylabel2.setScaledContents(True)


        '''
        我的安设备，用于回到主界面
        :return:0,600,100,100
        '''
        label_FanHui = mySignal.myLabel(self)
        label_FanHui.resize(100,100)
        label_FanHui.move(0,600)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#4F94CD"))
        label_FanHui.setPalette(palette)
        label_FanHui.setFont(QFont('Arial', 15))
        label_FanHui.setText('''
  我的安
  全设备
        ''')
        label_FanHui.setAutoFillBackground(True)
        #label_FanHui.clicked.connect(self.GoBackMain)




        #这个label可以显示被攻击排名
        '''
        这里显示文字的位置需要调整
        :return:
        '''
        self.textEdit_BeiGongJi = QPlainTextEdit(self)
        self.textEdit_BeiGongJi.resize(100, 320)
        self.textEdit_BeiGongJi.move(0, 280)
        self.textEdit_BeiGongJi.setFocusPolicy(QtCore.Qt.NoFocus)#不可编辑
        self.textEdit_BeiGongJi.setWordWrapMode(False)#禁止换行
        self.showBeiGongJiMsg()

        '''
        显示风险报警
        '''
        self.textEdit_FengXian=QPlainTextEdit(self)
        self.textEdit_FengXian.resize(100,130)
        self.textEdit_FengXian.move(1000,100)
        self.textEdit_FengXian.setFocusPolicy(QtCore.Qt.NoFocus)  # 不可编辑
        self.textEdit_FengXian.setWordWrapMode(False)  # 禁止换行
        self.showFengXianMsg()


        '''
        显示攻击源排行
        '''
        self.textEdit_GongJiYuan = QPlainTextEdit(self)
        self.textEdit_GongJiYuan.resize(100, 130)
        self.textEdit_GongJiYuan.move(1000, 280)
        self.textEdit_GongJiYuan.setFocusPolicy(QtCore.Qt.NoFocus)  # 不可编辑
        self.textEdit_GongJiYuan.setWordWrapMode(False)  # 禁止换行
        self.showGongJiYuanMsg()


        '''
        显示攻击次数排行
        '''
        self.textEdit_GongJiCiShu = QPlainTextEdit(self)
        self.textEdit_GongJiCiShu.resize(100, 140)
        self.textEdit_GongJiCiShu.move(1000, 460)
        self.textEdit_GongJiCiShu.setFocusPolicy(QtCore.Qt.NoFocus)  # 不可编辑
        self.textEdit_GongJiCiShu.setWordWrapMode(False)  # 禁止换行
        self.showGongJiCiShuMsg()


        '''
        设备防护状态统计
        100,120,290,200
        '''
        self.path="../resources/mainPic/pic1/pic1.png"
        self.label_P_FangHu =mySignal.myLabel(self)
        self.label_P_FangHu.resize(280,190)
        self.label_P_FangHu.move(105,130)
        self.label_P_FangHu.setPixmap(QPixmap(self.path))
        self.label_P_FangHu.setScaledContents(True)  # 使图片自适应标签大小
        self.label_P_FangHu.setAutoFillBackground(True)


        '''
        风险及风险投资
         '''
        label_P_FengXian = mySignal.myLabel(self)
        label_P_FengXian.resize(280,190)
        label_P_FengXian.move(410,130)
        label_P_FengXian.setPixmap(QPixmap("../resources/mainPic/pic2/pic2.png"))
        label_P_FengXian.setScaledContents(True)  # 使图片自适应标签大小
        label_P_FengXian.setAutoFillBackground(True)

        '''
        高危漏洞统计
        '''
        self.path = "../resources/mainPic/pic3/pic1.png"
        self.label_P_LouDong = mySignal.myLabel(self)
        self.label_P_LouDong.resize(280, 190)
        self.label_P_LouDong.move(715,130)
        self.label_P_LouDong.setPixmap(QPixmap(self.path))
        self.label_P_LouDong.setScaledContents(True)  # 使图片自适应标签大小
        self.label_P_LouDong.setAutoFillBackground(True)
        self.label_P_LouDong.clicked.connect(lambda :self.changPic3(int(filter(str.isdigit, self.path.split("/").pop().split(".")[0]).__next__())-1))


        '''
                攻击次数分析
                '''
        self.path="../resources/mainPic/pic4/pic1.png"
        self.label_P_CiShu = mySignal.myLabel(self)
        self.label_P_CiShu.resize(280, 190)
        self.label_P_CiShu.move(105, 410)
        self.label_P_CiShu .setPixmap(QPixmap(self.path))
        self.label_P_CiShu .setScaledContents(True)  # 使图片自适应标签大小
        self.label_P_CiShu .setAutoFillBackground(True)
        self.label_P_CiShu.clicked.connect(lambda :self.changPic4(int(filter(str.isdigit, self.path.split("/").pop().split(".")[0]).__next__())-1))


        '''
        攻击源分析
        '''
        self.path = "../resources/mainPic/pic5/pic1.png"
        self.label_P_Yuan = mySignal.myLabel(self)
        self.label_P_Yuan.resize(280, 190)
        self.label_P_Yuan.move(410, 410)
        self.label_P_Yuan.setPixmap(QPixmap(self.path))
        self.label_P_Yuan.setScaledContents(True)  # 使图片自适应标签大小
        self.label_P_Yuan.setAutoFillBackground(True)
        self.label_P_Yuan.clicked.connect(lambda :self.changPic5(int(filter(str.isdigit, self.path.split("/").pop().split(".")[0]).__next__())-1))


        '''
        攻击类型
        '''
        self.path = "../resources/mainPic/pic6/pic1.png"
        self.label_P_LeiXing = mySignal.myLabel(self)
        self.label_P_LeiXing.resize(280, 190)
        self.label_P_LeiXing.move(715, 410)
        self.label_P_LeiXing.setPixmap(QPixmap(self.path))
        self.label_P_LeiXing.setScaledContents(True)  # 使图片自适应标签大小
        self.label_P_LeiXing.setAutoFillBackground(True)
        self.label_P_LeiXing.clicked.connect(lambda :self.changPic6(int(filter(str.isdigit, self.path.split("/").pop().split(".")[0]).__next__())-1))


        #####################################################################
        # 最下层
        # 防火墙110,610,115,80
        label_FangHuo = mySignal.myLabel(self)
        label_FangHuo.resize(115, 80)
        label_FangHuo.move(110, 610)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#D2691E"))
        label_FangHuo.setPalette(palette)
        label_FangHuo.setFont(QFont('Arial', 15))
        label_FangHuo.setText("   防火墙")
        label_FangHuo.setAutoFillBackground(True)
        label_FangHuo.clicked.connect(self.FangSlot)

        # 这里添加槽

        # 入侵检测110,610,115,80
        label_RuQinJIanCe = QLabel(self)
        label_RuQinJIanCe.resize(115, 80)
        label_RuQinJIanCe.move(235, 610)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#D2691E"))
        label_RuQinJIanCe.setPalette(palette)
        label_RuQinJIanCe.setFont(QFont('Arial', 15))
        label_RuQinJIanCe.setText(" 入侵检测")
        label_RuQinJIanCe.setAutoFillBackground(True)
        # 这里添加槽

        # 入侵防护110,610,115,80
        label_RuQinFangHu = QLabel(self)
        label_RuQinFangHu.resize(115, 80)
        label_RuQinFangHu.move(360, 610)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#D2691E"))
        label_RuQinFangHu.setPalette(palette)
        label_RuQinFangHu.setFont(QFont('Arial', 15))
        label_RuQinFangHu.setText(" 入侵防护")
        label_RuQinFangHu.setAutoFillBackground(True)
        # 这里添加槽

        # 堡垒机110,610,115,80
        label_BaoLeiJi = QLabel(self)
        label_BaoLeiJi.resize(115, 80)
        label_BaoLeiJi.move(485, 610)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#D2691E"))
        label_BaoLeiJi.setPalette(palette)
        label_BaoLeiJi.setFont(QFont('Arial', 15))
        label_BaoLeiJi.setText("   堡垒机")
        label_BaoLeiJi.setAutoFillBackground(True)
        # 这里添加槽

        # 洞扫描110,610,115,80
        label_DongSaoMiao = QLabel(self)
        label_DongSaoMiao.resize(115, 80)
        label_DongSaoMiao.move(610, 610)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#D2691E"))
        label_DongSaoMiao.setPalette(palette)
        label_DongSaoMiao.setFont(QFont('Arial', 15))
        label_DongSaoMiao.setText("   洞扫描")
        label_DongSaoMiao.setAutoFillBackground(True)
        # 这里添加槽

        # web安全110,610,115,80
        label_WebAnQuan = mySignal.myLabel(self)
        label_WebAnQuan.resize(115, 80)
        label_WebAnQuan.move(735, 610)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#D2691E"))
        label_WebAnQuan.setPalette(palette)
        label_WebAnQuan.setFont(QFont('Arial', 15))
        label_WebAnQuan.setText(" web安全")
        label_WebAnQuan.setAutoFillBackground(True)
        label_WebAnQuan.clicked.connect(self.WebSafeSlot)
        # 这里添加槽

        # 数据库审计110,610,115,80
        label_ShuJuku = mySignal.myLabel(self)
        label_ShuJuku.resize(133, 80)
        label_ShuJuku.move(860, 610)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#D2691E"))
        label_ShuJuku.setPalette(palette)
        label_ShuJuku.setFont(QFont('Arial', 15))
        label_ShuJuku.setText("数据库审计")
        label_ShuJuku.setAutoFillBackground(True)
        label_ShuJuku.clicked.connect(self.dataBase)
        # 这里添加槽

        # 添加按钮1005,5,80,40
        self.button = QPushButton(self)
        self.button.setText("搜索")
        self.button.resize(80, 40)
        self.button.move(1005, 5)
        self.button.clicked.connect(self.searchDialog)
        # 添加槽

        # 输入框100,5,900,40
        self.lineEdit = QLineEdit(self)
        self.lineEdit.resize(900, 40)
        self.lineEdit.move(100, 5)
        self.lineEdit.setPlaceholderText("智能查询(输入所要查询的基本信息)")

    def searchDialog(self):
        import mainWindow.SearchResult as search
        data = self.lineEdit.text()
        if data.__len__()==0:
          QMessageBox.information(self, "提示", "请输入查询信息", QMessageBox.Yes , QMessageBox.Yes)
        else:
            dialog = search.SearchDialog(data)
            if dialog.exec_() == QDialog.Accepted:
                pass


    def searchDoalog(self):
        import mainWindow.SearchResult as search
        dialog=search.SearchDialog()
        if dialog.exec_()==QDialog.Accepted:
            pass


    def FangSlot(self):
        self.hide()
        self.s=secondWeidget.FangWeidget()
        self.s.show()

    def WebSafeSlot(self):
        import mainWindow.WebSafe as webSafe
        self.hide()
        self.s = webSafe.webSafe()
        self.s.show()

    def dataBase(self):
        import mainWindow.dataBaseCheck as dataBase
        self.hide()
        self.s = dataBase.dataBase()
        self.s.show()

    def changPic3(self,n):

        paths=self.picData.getPic3()
        index=(n+1)%paths.__len__()
        self.path=paths[index]
        self.label_P_LouDong.setPixmap(QPixmap(self.path))
        self.label_P_LouDong.setScaledContents(True)  # 使图片自适应标签大小

    def changPic4(self,n):

        paths = self.picData.getPic4()
        index = (n + 1) % paths.__len__()
        self.path = paths[index]
        self.label_P_CiShu.setPixmap(QPixmap(self.path))
        self.label_P_CiShu.setScaledContents(True)  # 使图片自适应标签大小

    def changPic5(self,n):

        paths = self.picData.getPic5()
        index = (n + 1) % paths.__len__()
        self.path = paths[index]
        self.label_P_Yuan.setPixmap(QPixmap(self.path))
        self.label_P_Yuan.setScaledContents(True)  # 使图片自适应标签大小

    def changPic6(self,n):

        paths = self.picData.getPic6()
        index = (n + 1) % paths.__len__()
        self.path = paths[index]
        self.label_P_LeiXing.setPixmap(QPixmap(self.path))
        self.label_P_LeiXing.setScaledContents(True)  # 使图片自适应标签大小

    def showBeiGongJiMsg(self):
        data=self.dataObj.getMianBeiGongJiMsg()
        for i in data:
            self.textEdit_BeiGongJi.appendPlainText(i)

    def showFengXianMsg(self):
        data = self.dataObj.getTextEdit_FengXianMsg()
        for i in data:
            self.textEdit_FengXian.appendPlainText(i)

    def showGongJiYuanMsg(self):
        data = self.dataObj.getTextEdit_GongJiYuanMsg()
        for i in data:
            self.textEdit_GongJiYuan.appendPlainText(i)


    def showGongJiCiShuMsg(self):
        data = self.dataObj.getTextEdit_GongJiCiShuMsg()
        for i in data:
            self.textEdit_GongJiCiShu.appendPlainText(i)
























if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainindow = firstWeidget()
    mainindow.show()
    sys.exit(app.exec_())