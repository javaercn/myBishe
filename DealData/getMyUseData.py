import Dao.getData as Data
import threading




class getMyData(object):
    def __init__(self):
        super(getMyData,self).__init__()
        self.semphore = threading.Semaphore(1)

        self.__data=Data.getData()


    #############第一个界面##############

     #返回主界面第一幅图的数据
    def getMainPic1(self):
        data=self.__data.getMainPic1()
        myData = {}
        data_Fang = []
        data_Fang.append(data[0][6])
        data_Fang.append(data[0][1])
        data_Fang.append(data[0][2])
        myData["防火墙"] = data_Fang
        data_IDS = []
        data_IDS.append(data[1][6])
        data_IDS.append(data[1][1])
        data_IDS.append(data[1][2])
        myData["IDS"] = data_IDS
        data_WAF = []
        data_WAF.append(data[2][6])
        data_WAF.append(data[2][1])
        data_WAF.append(data[2][2])
        myData["WAF"] = data_WAF
        data_IPS = []
        data_IPS.append(data[3][6])
        data_IPS.append(data[3][1])
        data_IPS.append(data[3][2])
        myData["IPS"] = data_IPS
        return myData

        #返回主界面第二幅图的数据

    # 返回主界面第一幅图的数据
    def getMainPic2(self):
        data=self.__data.getMainPic2()
        mydata2={}
        type1=[]
        type1.append(data[0][1])
        type1.append(data[0][2])
        type1.append(data[0][3])
        mydata2["类型1"]=type1

        type2 = []
        type2.append(data[1][1])
        type2.append(data[1][2])
        type2.append(data[1][3])
        mydata2["类型2"] = type2

        type3 = []
        type3.append(data[2][1])
        type3.append(data[2][2])
        type3.append(data[2][3])
        mydata2["类型3"] = type3

        type4 = []
        type4.append(data[3][1])
        type4.append(data[3][2])
        type4.append(data[3][3])
        mydata2["类型4"] = type4
        return mydata2

     #三幅图片轮播
    def getMainPic3(self):
        data=self.__data.getMainPic3()
        mydata3=[]
        mydata3_1={}
        mydata3_1["WEBSHELL上传"]=data[0][3]
        mydata3_1["网站扫描"]=data[0][1]
        mydata3_1["信息泄露攻击"]=data[0][2]
        mydata3_1["SQL注入"]=data[0][7]

        mydata3_2 = {}
        mydata3_2["WEBSHELL上传"] = data[1][3]
        mydata3_2["网站扫描"] = data[1][1]
        mydata3_2["信息泄露攻击"] = data[1][2]
        mydata3_2["SQL注入"] = data[1][7]

        mydata3_3 = {}
        mydata3_3["WEBSHELL上传"] = data[2][3]
        mydata3_3["网站扫描"] = data[2][1]
        mydata3_3["信息泄露攻击"] = data[2][2]
        mydata3_3["SQL注入"] = data[2][7]

        mydata3.append(mydata3_1)
        mydata3.append(mydata3_2)
        mydata3.append(mydata3_3)
        return mydata3

    def getMainPic4(self):
        data=self.__data.getMainPic4()
        mydata4=[]
        mydata4_1={}
        mydata4_1["信息泄露"]=data[0][2]
        mydata4_1["网站扫描"]=data[0][1]
        mydata4_1["弱口令"]=data[0][6]
        mydata4_1["目录遍历"]=data[0][8]
        mydata4_1["WEBSHELL"]=data[0][3]
        mydata4.append(mydata4_1)

        mydata4_2 = {}
        mydata4_2["信息泄露"] = data[1][2]
        mydata4_2["网站扫描"] = data[1][1]
        mydata4_2["弱口令"] = data[1][6]
        mydata4_2["目录遍历"] = data[1][8]
        mydata4_2["WEBSHELL"] = data[1][3]

        mydata4_3 = {}
        mydata4_3["信息泄露"] = data[2][2]
        mydata4_3["网站扫描"] = data[2][1]
        mydata4_3["弱口令"] = data[2][6]
        mydata4_3["目录遍历"] = data[2][8]
        mydata4_3["WEBSHELL"] = data[2][3]
        mydata4.append(mydata4_1)
        mydata4.append(mydata4_2)
        mydata4.append(mydata4_3)

        return mydata4

    #获取攻击源，两个数据，做两幅图片
    def getMainPic5(self):
        data=self.__data.getMainPic5()
        mydata5 = []
        data1=sorted(data[0][0].items(),key=lambda x:x[1],reverse=True)[0:8]
        data_dict=dict(data1)
        data_dict["其他"]=300
        mydata5.append(data_dict)

        data2 = sorted(data[0][1].items(), key=lambda x: x[1], reverse=True)[0:8]
        data_dict = dict(data2)
        data_dict["其他"] = 200
        mydata5.append(data_dict)
        return mydata5

    #主界面的第六幅图
    def getMainPic6(self):
        data = self.__data.getFangPic3()
        for i in data:
            i.pop('id')
        return data

    ##############第二个界面################
    def getFangPic1(self):
        pass

    def getFangPic2(self):
        data=self.__data.getFangPic2()
        for i in data:
            i.pop('id')
        return data

    def getFangPic3(self):
        data=self.__data.getFangPic3()
        for i in data:
            i.pop('id')
        return data

    def getFangPic4(self):
        data=self.__data.getFangPic4()
        for i in data:
            i.pop('id')
        return data

    #防火墙页面第五幅图
    def getFangPic5(self):
        data = self.__data.getFangPic5()
        for i in data:
            i.pop('id')
        data1 = sorted(data[0].items(), key=lambda x: x[1], reverse=True)[0:8]
        data2=sorted(data[1].items(), key=lambda x: x[1], reverse=True)[0:8]
        mydata=[]
        mydata.append(dict(data1))
        mydata.append(dict(data2))
        return mydata

    #防火墙第六幅图
    def getFangPic6(self):
        data=self.__data.getFangPic6()
        for i in data:
            i.pop('id')
        return data

    ####################web安全########################
    #做一个饼状图
    def getWebPic1(self):
        data=self.__data.getWebPic1()
        data.pop('id')
        return data

    #生成多符图
    def getWebPic2(self):
        data=self.__data.getWebPic2()
        for i in data:
            i.pop('id')
        return data

    #用饼状图,两幅图
    def getWebPic3(self):
        data=self.__data.getWebPic3()
        data2 = sorted(data[0].items(), key=lambda x: x[1], reverse=True)[0:8]
        data3=sorted(data[1].items(), key=lambda x: x[1], reverse=True)[0:8]
        mydata=[]
        mydata.append(dict(data2))
        mydata.append(dict(data3))
        return mydata

    #做一个饼状图
    def getWebPic4(self):
        data=self.__data.getWebPic4()
        data.pop('id')
        return data
    ############################显示信息#####################################

    def getMainLabelShow1(self):
        data=self.__data.getMainLabelShow1()
        for i in data:
            i.pop('id')
        return self.__dictSum(data)

    #待处理，缺数据
    def getMainLabelShow2(self):
        data=self.__data.getMainLabelShow2()
        for i in data:
            i.pop('id')
        return self.__dictSum(data)

    def getMainLabelShow3(self):
        data=self.__data.getMainLabelShow3()
        for i in data:
            i.pop('id')
        return self.__dictSum(data)

    def getMainLabelShow4(self):
        data=self.__data.getMainLabelShow4()
        for i in data:
            i.pop('id')
        return self.__dictSum(data)

    def getFangLabelShow1(self):
        data=self.__data.getFangLabelShow1()
        for i in data:
            i.pop('id')
        return self.__dictSum(data)

    def getFangLabelShow2(self):
        data=self.__data.getFangLabelShow2()
        for i in data:
            i.pop('id')
        return self.__dictSum(data)

    def getFangLabelShow3(self):
        data = self.__data.getFangLabelShow3()
        for i in data:
            i.pop('id')
        return self.__dictSum(data)
    def getWebLabelShow1(self):
        return self.getFangLabelShow1()

    def getWebLabelShow2(self):
        return self.getFangLabelShow1()

    def getWebLabelShow3(self):
        return self.getFangLabelShow1()

    def getSqls(self):
        return self.__data.getSqls()





    ################登陆#################################################
    #用户是否可以登录
    def getUserLoginMsg(self,username,password):
        count=self.__data.LoginUser(username,password)
        if count==0:
            return False
        else:
            self.aboutUpadePics()
            return True

    #是否更新图片的逻辑
    def aboutUpadePics(self):
        import Service.MainService as MainPic
        self.semphore.acquire()
        with open("../resources/isUPdateFlag/flag.txt", "r") as f:
            data = int(f.read())
        self.semphore.release()
        if data == 0:
            pass
        else:
            MainPic.generatePic().updatePics()









    #管理员登陆
    def getManagerMsg(self,username,password):
        count=self.__data.LoginManager(username,password)
        if count==0:
            return False
        else:
            with open("../resources/manager/manager.txt", 'w+') as f:
                f.write(username)
            return True
    ##################################其他工具函数###########################
    def __dictSum(self,data):
        data_use = data[0]
        del (data[0])
        for i in data:
            for k, value in i.items():
                data_use[k] = data_use[k] + value
        return data_use





if __name__ == '__main__':
    mydata=getMyData()
    data = mydata.aboutUpadePics()



