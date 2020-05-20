import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mainWindow.MySignal as mySignal
import Service.showPics.dealMain as dealMain
import Service.showMsg as myMsg



class FangWeidget(QWidget):
    def __init__(self, parent=None):
        super(FangWeidget, self).__init__(parent)
        self.path = ""
        self.dataObj = myMsg.getMsgs()
        self.picData = dealMain.dealMainPics()
        self.setFixedSize(1100, 700)
        self.pasteLable()
        self.setWindowTitle("防火墙")


    def paintEvent(self, QPaintEvent):
        qp = QPainter()
        # 椭圆
        qp.begin(self)
        qp.setFont(QFont('Arial', 15))
        qp.setPen(QColor(Qt.black))
        # logol
        #qp.drawEllipse(0, 0, 100, 50)

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

        # 最底下
        qp.drawRect(100, 600, 900, 100)

        # 最上边搜索栏
        qp.drawRect(100, 5, 900, 40)

        # 搜索按钮
        qp.drawRect(1005, 5, 80, 40)

        # 接下来画里边，长900，宽550
        # 画左上的表格
        # qp.drawRect(150,60,200,50)
        qp.fillRect(150, 60, 200, 50, QBrush(QColor("#E6E6FA")))
        qp.drawText(152, 90, "      防护类型")
        qp.drawRect(100, 120, 290, 200)

        # 中上
        # qp.drawRect(450,60,200,50)
        qp.fillRect(450, 60, 200, 50, QBrush(QColor("#E6E6FA")))
        qp.drawText(452, 90, "     受攻击类型")
        qp.drawRect(405, 120, 290, 200)

        # 左上
        # qp.drawRect(750,60,200,50)
        qp.fillRect(750, 60, 200, 50, QBrush(QColor("#E6E6FA")))
        qp.drawText(775, 90, "被攻击的方法")
        qp.drawRect(710, 120, 290, 200)

        # 画左下的表格###########
        # qp.drawRect(150, 340, 200, 50)
        qp.fillRect(150, 340, 200, 50, QBrush(QColor("#E6E6FA")))
        qp.drawText(170, 370, "被攻击严重程度")
        qp.drawRect(100, 400, 290, 200)

        # 中下
        # qp.drawRect(450, 340, 200, 50)
        qp.fillRect(450, 340, 200, 50, QBrush(QColor("#E6E6FA")))
        qp.drawText(475, 370, "攻击源分析")
        qp.drawRect(405, 400, 290, 200)

        # 中右
        # qp.drawRect(750, 340, 200, 50)
        qp.fillRect(750, 340, 200, 50, QBrush(QColor("#E6E6FA")))
        qp.drawText(765, 370, "防火墙处理动作")
        qp.drawRect(710, 400, 290, 200)
        qp.end()

    def pasteLable(self):
        # 显示防护器防护类型
        #  qp.drawEllipse(0, 0, 100, 50)
        mylabel2=QLabel(self)
        mylabel2.resize(100,50)
        mylabel2.move(0,0)
        mylabel2.setAutoFillBackground(True)
        mylabel2.setPixmap(QPixmap("../resources/logo/logo.png"))
        mylabel2.setScaledContents(True)




        # 这个label可以显示被攻击排
        self.TextEdit_BeiGongJi = QPlainTextEdit(self)
        self.TextEdit_BeiGongJi.resize(100, 450)
        self.TextEdit_BeiGongJi.move(0, 150)
        self.TextEdit_BeiGongJi.setFocusPolicy(QtCore.Qt.NoFocus)  # 不可编辑
        self.TextEdit_BeiGongJi.setWordWrapMode(False)  # 禁止换行
        self.getTextFangMsg1()



        '''
        显示风险报警
        '''
        self.TextEdit_FengXian = QPlainTextEdit(self)
        self.TextEdit_FengXian.resize(100, 130)
        self.TextEdit_FengXian.move(1000, 100)
        self.TextEdit_FengXian.setFocusPolicy(QtCore.Qt.NoFocus)  # 不可编辑
        self.TextEdit_FengXian.setWordWrapMode(False)  # 禁止换行
        self.getTextFangMsg2()


        '''
        显示攻击源排行
        '''
        self.TextEdit_GongJiYuan = QPlainTextEdit(self)
        self.TextEdit_GongJiYuan.resize(100, 320)
        self.TextEdit_GongJiYuan.move(1000, 280)
        self.TextEdit_GongJiYuan.setFocusPolicy(QtCore.Qt.NoFocus)  # 不可编辑
        self.TextEdit_GongJiYuan.setWordWrapMode(False)  # 禁止换行
        self.getTextFangMsg3()

        '''
        设备防护状态统计
        100,120,290,200
        '''
        self.path="../resources/secondPic/pic2/pic1.png"
        self.label_P_FangHu = mySignal.myLabel(self)
        self.label_P_FangHu.resize(280, 190)
        self.label_P_FangHu.move(105, 130)
        self.label_P_FangHu.setPixmap(QPixmap(self.path))
        self.label_P_FangHu.setScaledContents(True)  # 使图片自适应标签大小
        self.label_P_FangHu.setAutoFillBackground(True)
       # self.label_P_FangHu.clicked.connect(lambda :self.changPic1(int(filter(str.isdigit, self.path.split("/").pop().split(".")[0]).__next__()) - 1))




        '''
        风险及风险投资
         '''
        self.path="../resources/secondPic/pic2/pic1.png"
        self.label_P_FengXian = mySignal.myLabel(self)
        self.label_P_FengXian.resize(280, 190)
        self.label_P_FengXian.move(410, 130)
        self.label_P_FengXian.setPixmap(QPixmap(self.path))
        self.label_P_FengXian.setScaledContents(True)  # 使图片自适应标签大小
        self.label_P_FengXian.setAutoFillBackground(True)
        self.label_P_FengXian.clicked.connect(lambda :self.changPic2(int(list(filter(str.isdigit, self.path.split("/").pop().split(".")[0]))[0])-1))

        '''
        高危漏洞统计
        '''
        self.path = "../resources/secondPic/pic3/pic1.png"
        self.label_P_LouDong = mySignal.myLabel(self)
        self.label_P_LouDong.resize(280, 190)
        self.label_P_LouDong.move(715, 130)
        self.label_P_LouDong.setPixmap(QPixmap(self.path))
        self.label_P_LouDong.setScaledContents(True)  # 使图片自适应标签大小
        self.label_P_LouDong.setAutoFillBackground(True)
        self.label_P_LouDong.clicked.connect(lambda: self.changPic3(int(filter(str.isdigit, self.path.split("/").pop().split(".")[0]).__next__()) - 1))

        '''
        攻击次数分析
        '''
        self.path = "../resources/secondPic/pic4/pic1.png"
        self.label_P_CiShu = mySignal.myLabel(self)
        self.label_P_CiShu.resize(280, 190)
        self.label_P_CiShu.move(105, 410)
        self.label_P_CiShu.setPixmap(QPixmap(self.path))
        self.label_P_CiShu.setScaledContents(True)  # 使图片自适应标签大小
        self.label_P_CiShu.setAutoFillBackground(True)
        self.label_P_CiShu.clicked.connect(lambda: self.changPic4(int(filter(str.isdigit, self.path.split("/").pop().split(".")[0]).__next__()) - 1))

        '''
            攻击源分析
            '''
        self.path="../resources/secondPic/pic5/pic1.png"
        self.label_P_Yuan =mySignal.myLabel(self)
        self.label_P_Yuan.resize(280, 190)
        self.label_P_Yuan.move(410, 410)
        self.label_P_Yuan.setPixmap(QPixmap(self.path))
        self.label_P_Yuan.setScaledContents(True)  # 使图片自适应标签大小
        self.label_P_Yuan.setAutoFillBackground(True)
        self.label_P_Yuan.clicked.connect(lambda: self.changPic5(int(filter(str.isdigit, self.path.split("/").pop().split(".")[0]).__next__()) - 1))

        '''
               攻击类型
               '''
        self.path="../resources/secondPic/pic6/pic1.png"
        self.label_P_LeiXing = mySignal.myLabel(self)
        self.label_P_LeiXing.resize(280, 190)
        self.label_P_LeiXing.move(715, 410)
        self.label_P_LeiXing.setPixmap(QPixmap(self.path))
        self.label_P_LeiXing.setScaledContents(True)  # 使图片自适应标签大小
        self.label_P_LeiXing.setAutoFillBackground(True)
        self.label_P_LeiXing.clicked.connect(lambda: self.changPic6(int(filter(str.isdigit, self.path.split("/").pop().split(".")[0]).__next__()) - 1))



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
        label_RuQinJIanCe = mySignal.myLabel(self)
        label_RuQinJIanCe.resize(200, 80)
        label_RuQinJIanCe.move(340, 610)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#D2691E"))
        label_RuQinJIanCe.setPalette(palette)
        label_RuQinJIanCe.setFont(QFont('Arial', 15))
        label_RuQinJIanCe.setText("        web安全")
        label_RuQinJIanCe.setAutoFillBackground(True)
        label_RuQinJIanCe.clicked.connect(self.WebSafeSlot)

        # 入侵防护110,610,115,80
        label_RuQinFangHu = mySignal.myLabel(self)
        label_RuQinFangHu.resize(200, 80)
        label_RuQinFangHu.move(560, 610)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#D2691E"))
        label_RuQinFangHu.setPalette(palette)
        label_RuQinFangHu.setFont(QFont('Arial', 15))
        label_RuQinFangHu.setText("      数据库审计")
        label_RuQinFangHu.setAutoFillBackground(True)
        label_RuQinFangHu.clicked.connect(self.dataBase)
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
        dialog = search.SearchDialog()
        if dialog.exec_() == QDialog.Accepted:
            pass

    def MainSlot(self):
        import mainWindow.mainWeidget as mainWeidget
        self.hide()
        self.s = mainWeidget.firstWeidget()
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

    def Login(self):
        import mainWindow.login2 as login2
        dialog = login2.Login()
        if dialog.exec_() == QDialog.Accepted:
            pass

    def changPic1(self, n):
        paths = self.picData.getFangPic2()
        index = (n + 1) % paths.__len__()
        self.path = paths[index]
        self.label_P_FangHusetPixmap(QPixmap(self.path))
        self.label_P_FangHu.setScaledContents(True)  # 使图片自适应标签大小

    def changPic2(self, n):
        paths = self.picData.getFangPic2()
        index = (n + 1) % paths.__len__()
        self.path = paths[index]
        self.label_P_FengXian.setPixmap(QPixmap(self.path))
        self.label_P_FengXian.setScaledContents(True)  # 使图片自适应标签大小

    def changPic3(self, n):
        paths = self.picData.getFangPic3()
        index = (n + 1) % paths.__len__()
        self.path = paths[index]
        self.label_P_LouDong.setPixmap(QPixmap(self.path))
        self.label_P_LouDong.setScaledContents(True)  # 使图片自适应标签大小

    def changPic4(self, n):
        paths = self.picData.getFangPic4()
        index = (n + 1) % paths.__len__()
        self.path = paths[index]
        self.label_P_CiShu.setPixmap(QPixmap(self.path))
        self.label_P_CiShu.setScaledContents(True)  # 使图片自适应标签大小

    def changPic5(self, n):
        paths = self.picData.getFangPic5()
        index = (n + 1) % paths.__len__()
        self.path = paths[index]
        self.label_P_Yuan.setPixmap(QPixmap(self.path))
        self.label_P_Yuan.setScaledContents(True)  # 使图片自适应标签大小

    def changPic6(self, n):
        paths = self.picData.getFangPic6()
        index = (n + 1) % paths.__len__()
        self.path = paths[index]
        self.label_P_LeiXing.setPixmap(QPixmap(self.path))
        self.label_P_LeiXing.setScaledContents(True)  # 使图片自适应标签大小

    def getTextFangMsg1(self):
        data = self.dataObj.getTextFangMsg1()
        for i in data:
            self.TextEdit_BeiGongJi.appendPlainText(i)

    def getTextFangMsg2(self):
        data = self.dataObj.getTextFangMsg2()
        for i in data:
            self.TextEdit_FengXian.appendPlainText(i)

    def getTextFangMsg3(self):
        data = self.dataObj.getTextFangMsg3()
        for i in data:
            self.TextEdit_GongJiYuan.appendPlainText(i)


if __name__=='__main__':
    app = QApplication(sys.argv)
    mainindow = FangWeidget()
    mainindow.show()
    sys.exit(app.exec_())
