import DealData.getMyUseData as getUseData

'''
这个类生成要显示的数据
'''
class getMsgs(object):
    def __init__(self):
        self.__myData=getUseData.getMyData()

    def __dealData(self,data):
        msgs = []
        index = 1
        for k, values in data.items():
            msg = str(str(index) + " " + k + " " + str(values))
            msgs.append(msg)
            msgs.append("---------------------------")
            index += 1
        return msgs

    def getMianBeiGongJiMsg(self):
        return self.__dealData(self.__myData.getMainLabelShow1())
    #待处理
    def getTextEdit_FengXianMsg(self):
        msg=[]
        msg.append("1.web漏洞")
        msg.append("---------------------------")
        msg.append("2.弱口令")
        msg.append("---------------------------")
        msg.append("3.网站扫描")
        msg.append("---------------------------")
        return msg


    def getTextEdit_GongJiYuanMsg(self):
        return self.__dealData(self.__myData.getMainLabelShow3())
    def getTextEdit_GongJiCiShuMsg(self):
        return self.__dealData(self.__myData.getMainLabelShow4())

    def getTextFangMsg1(self):
        return self.__dealData(self.__myData.getFangLabelShow1())

    def getTextFangMsg2(self):
        return self.__dealData(self.__myData.getFangLabelShow2())

    def getTextFangMsg3(self):
        return self.__dealData(self.__myData.getFangLabelShow3())

    def getWebMsg1(self):
        return self.getTextFangMsg1()
    def getWebMsg2(self):
        return self.getTextFangMsg2()
    def getWebMsg3(self):
        return self.getTextFangMsg3()



if __name__ == '__main__':
    obj=getMsgs()
    print(obj.getTextFangMsg3())
