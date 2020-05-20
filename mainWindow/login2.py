from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mainWindow.MySignal as mySignal
import Service.service as service
import sys
class Login(QDialog):
    def __init__(self,parent=None):
        super(Login, self).__init__(parent)
        self.setFixedSize(400, 280)
        self.setWindowTitle("登录")
        self.pasteLabel()

    def paintEvent(self, QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        qp.drawRect(10,20,80,50)
        qp.drawRect(100, 20, 250, 50)

        qp.drawRect(10, 100, 80, 50)
        qp.drawRect(100, 100, 250, 50)

        qp.drawRect(30,180,70,50)
        qp.drawRect(250, 180, 70, 50)
        qp.end()

    def pasteLabel(self):
        label_uaerName=QLabel(self)
        label_uaerName.resize(79,49)
        label_uaerName.move(11,21)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#B9D3EE"))
        label_uaerName.setPalette(palette)
        label_uaerName.setAutoFillBackground(True)
        label_uaerName.setFont(QFont('Arial', 12))
        label_uaerName.setText("  用户名")

        label_uaerName = QLabel(self)
        label_uaerName.resize(79, 49)
        label_uaerName.move(11, 101)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#B9D3EE"))
        label_uaerName.setPalette(palette)
        label_uaerName.setAutoFillBackground(True)
        label_uaerName.setFont(QFont('Arial', 12))
        label_uaerName.setText("   密码")
        #100, 20, 250, 50
        self.edit_userName=QLineEdit(self)
        self.edit_userName.resize(249, 49)
        self.edit_userName.move(101, 21)
        self.edit_userName.setPlaceholderText("用户名")

        #100, 100, 250, 50
        self.edit_password=QLineEdit(self)
        self.edit_password.resize(249,49)
        self.edit_password.move(101,101)
        self.edit_password.setPlaceholderText("密码")

        #确定按钮30,190,70,50
        ok_button=QPushButton(self)
        ok_button.resize(69,49)
        ok_button.move(31,181)
        ok_button.setFont(QFont('Arial', 12))
        ok_button.setText("确定")
        ok_button.clicked.connect(self.loginothers)
        #槽

        # 250, 190, 70, 50
        cancel_button = QPushButton(self)
        cancel_button.resize(69, 49)
        cancel_button.move(251, 181)
        cancel_button.setFont(QFont('Arial', 12))
        cancel_button.setText("取消")
        cancel_button.clicked.connect(self.close)

    def loginothers(self):
        import  mainWindow.mainWeidget as mainWidget
        import  mainWindow.ManagerDialog as manager
        serviceobj=service.service()
        username=self.edit_userName.text()
        password=self.edit_password.text()
        if serviceobj.LoginManager(username, password):
            dialog = manager.Manager()
            self.close()
            if dialog.exec_() == QDialog.Accepted:
                pass

        else:
            reply = QMessageBox.information(self, "提示", "用户名或密码错误", QMessageBox.Yes | QMessageBox.No,
                                            QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainindow = Login()
    mainindow.show()
    sys.exit(app.exec_())