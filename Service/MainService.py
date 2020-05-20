import DealData.getMyUseData as getMyData
import threading

from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
'''
这个类生成图片
'''

#设置中文的问题


class generatePic(object):
    def __init__(self):
        self.__myData=getMyData.getMyData()
        self.semphore = threading.Semaphore(1)
        self.colors=["red","green","yellow","lightskyblue","blue","orange","cyan","purple","brown"]

    #主界面第一幅图
    def getMainPic1(self):
        plt.figure()
        bar_width = 0.2
        data=self.__myData.getMainPic1()
        label=list(data.keys())
        data1=[]
        data2=[]
        data3=[]
        for value in data.values():
            data1.append(value[0])
            data2.append(value[1])
            data3.append(value[2])
        x_1 = list(range(len(label)))
        x_2 = [i + 0.2 for i in x_1]
        x_3 = [i + 0.2 * 2 for i in x_1]
        plt.bar(x_1, data1, width=bar_width, label="网站扫描")
        plt.bar(x_2, data2, width=bar_width, label="若口令")
        plt.bar(x_3, data3, width=bar_width, label="信息泄露")
        plt.xticks(x_2, label)
        plt.grid()
        plt.legend()
        plt.savefig("../resources/mainPic/pic1/pic1.png")


    #主界面第二幅图
    def getMainPic2(self):
        plt.figure()
        data=self.__myData.getMainPic2()
        bar_width = 0.2
        label = list(data.keys())
        data1 = []
        data2 = []
        data3 = []
        for value in data.values():
            data1.append(value[0])
            data2.append(value[1])
            data3.append(value[2])
        x_1 = list(range(len(label)))
        x_2 = [i + 0.2 for i in x_1]
        x_3 = [i + 0.2 * 2 for i in x_1]
        plt.bar(x_1, data1, width=bar_width, label="系列1")
        plt.bar(x_2, data2, width=bar_width, label="系列2")
        plt.bar(x_3, data3, width=bar_width, label="系列3")
        plt.xticks(x_2, label)
        plt.grid()
        plt.legend()
        plt.savefig("../resources/mainPic/pic2/pic2.png")

    #有问题
    def getMainPic3(self):


        bar_width = 0.2
        data = self.__myData.getMainPic3()
        label = list(data[0].keys())
        # 这里有问题，生成三个图片的时候会出错
        for index, d in enumerate(data):
            plt.figure()
            data = list(d.values())
            x_1 = list(range(len(label)))
            plt.bar(x_1, data, width=bar_width)
            plt.xticks(x_1, label)
            plt.savefig("../resources/mainPic/pic3/pic%s.png" % (index+1))


    #饼状图
    def getMainPic4(self):
        plt.figure()
        data=self.__myData.getMainPic4()
        for index,i in enumerate(data):
            labels = list(i.keys())
            datause = list(i.values())
            plt.pie(datause, startangle=90, shadow=True)
            plt.axis('equal')
            plt.legend(labels, shadow=True, bbox_to_anchor=(0.85, 0.6))
            plt.title("攻击次数")
            plt.savefig("../resources/mainPic/pic4/pic%s.png" % (index+1))


    def getMainPic5(self):
        plt.figure()
        data=self.__myData.getMainPic5()
        for index, i in enumerate(data):
            labels = list(i.keys())
            datause = list(i.values())
            plt.pie(datause, startangle=90, shadow=True)
            plt.axis('equal')
            plt.legend(labels, shadow=True, bbox_to_anchor=(0.85, 0.6))
            plt.title("攻击源")
            plt.savefig("../resources/mainPic/pic5/pic%s.png" % (index + 1))

    def getMainPic6(self):

        data=self.__myData.getMainPic6()
        bar_width = 0.2
        label = list(data[0].keys())
        for index, d in enumerate(data):
            plt.figure()
            data1 = list(d.values())
            x_1 = list(range(len(label)))
            plt.bar(x_1, data1, width=bar_width)
            plt.xticks(x_1, label, rotation=12)
            plt.title("非法网站")
            plt.savefig("../resources/mainPic/pic6/pic%s.png" % (index + 1))

    #########################3第二个界面########################
    #没数据
    def getFangPic1(self):
        pass

    def getFangPic2(self):
        plt.figure()
        data=self.__myData.getFangPic2()
        bar_width = 0.2
        label = list(data[0].keys())
        for index, d in enumerate(data):
            data1 = list(d.values())
            x_1 = list(range(len(label)))
            plt.bar(x_1, data1, width=bar_width)
            plt.xticks(x_1, label,rotation=12)
            plt.savefig("../resources/secondPic/pic1/pic%s.png" % (index+1))

    def getFangPic3(self):
        plt.figure()
        import random
        data=self.__myData.getFangPic3()
        num = len(list(data[0].keys()))
        myColor = random.sample(self.colors, num)
        for index, i in enumerate(data):
            labels = list(i.keys())
            datause = list(i.values())
            plt.pie(datause, startangle=90, shadow=True,colors=myColor)
            plt.axis('equal')
            plt.legend(labels, shadow=True, bbox_to_anchor=(0.85, 0.6))
            plt.title("攻击源")
            plt.savefig("../resources/secondPic/pic3/pic%s.png" % (index + 1))

    def getFangPic4(self):
        plt.figure()
        import random
        data=self.__myData.getFangPic4()
        num=len(list(data[0].keys()))
        myColor=random.sample(self.colors,num)
        for index, i in enumerate(data):
            labels = list(i.keys())
            datause = list(i.values())
            plt.pie(datause, startangle=90, shadow=True,colors=myColor)
            plt.legend(labels, shadow=True, bbox_to_anchor=(0.85, 0.6))
            plt.axis('equal')
            plt.title("严重程度")
            plt.savefig("../resources/secondPic/pic4/pic%s.png" % (index + 1))


    def getFangPic5(self):
        plt.figure()
        import random
        data=self.__myData.getFangPic5()
        num = len(list(data[0].keys()))
        myColor = random.sample(self.colors, num)
        for index, i in enumerate(data):
            labels = list(i.keys())
            datause = list(i.values())
            plt.pie(datause, startangle=90, shadow=True, colors=myColor)
            plt.legend(labels, shadow=True, bbox_to_anchor=(0.85, 0.6))
            plt.axis('equal')
            plt.title("严重程度")
            plt.savefig("../resources/secondPic/pic5/pic%s.png" % (index + 1))

    def getFangPic6(self):
        plt.figure()
        import random
        data=self.__myData.getFangPic6()
        num = len(list(data[0].keys()))
        myColor = random.sample(self.colors, num)
        for index, i in enumerate(data):
            labels = list(i.keys())
            datause = list(i.values())
            plt.pie(datause, startangle=90, shadow=True, colors=myColor)
            plt.legend(labels, shadow=True, bbox_to_anchor=(0.85, 0.6))
            plt.axis('equal')
            plt.title("严重程度")
            plt.savefig("../resources/secondPic/pic6/pic%s.png" % (index + 1))
    #########################第三个界面##############################################
    def getWebPic1(self):
        plt.figure()
        bar_width=0.2
        data=self.__myData.getWebPic1()
        label=data.keys()
        datause = list(data.values())
        x_1 = list(range(len(label)))
        plt.bar(x_1, datause, width=bar_width)
        plt.xticks(x_1, label,rotation=25)
        plt.savefig("../resources/thirdPic/pic1/pic1.png" )

    def getWebPic2(self):
        plt.figure()
        import random
        data=self.__myData.getWebPic2()
        num = len(list(data[0].keys()))
        myColor = random.sample(self.colors, num)
        for index, i in enumerate(data):
            labels = list(i.keys())
            datause = list(i.values())
            plt.pie(datause, startangle=90, shadow=True, colors=myColor)
            plt.legend(labels, shadow=True, bbox_to_anchor=(0.85, 0.6))
            plt.axis('equal')
            plt.title("攻击方法")
            plt.savefig("../resources/thirdPic/pic2/pic%s.png" % (index + 1))



    def getWebPic3(self):
        plt.figure()
        import random
        data=self.__myData.getWebPic3()
        num = len(list(data[0].keys()))
        myColor = random.sample(self.colors, num)
        for index, i in enumerate(data):
            labels = list(i.keys())
            datause = list(i.values())
            plt.pie(datause, startangle=90, shadow=True, colors=myColor)
            plt.legend(labels, shadow=True, bbox_to_anchor=(0.85, 0.6))
            plt.axis('equal')
            plt.title("攻击源")
            plt.savefig("../resources/thirdPic/pic3/pic%s.png" % (index + 1))

    def getWebPic4(self):
        plt.figure()
        import random
        data=self.__myData.getWebPic4()
        label=list(data.keys())
        num = len(data)
        myColor = random.sample(self.colors, num)
        datause=list(data.values())
        plt.pie(datause, startangle=90, shadow=True, colors=myColor)
        plt.legend(label, shadow=True, bbox_to_anchor=(0.85, 0.6))
        plt.axis('equal')
        plt.title("严重程度")
        plt.savefig("../resources/thirdPic/pic4/pic1.png")

    def writeFlag(self):
        self.semphore.acquire()
        with open("../resources/isUPdateFlag/flag.txt", "w") as f:
            f.write("0")
        self.semphore.release()

    def updatePics(self):
        print("第1幅图片更新.....")
        self.getMainPic1()
        print("第2幅图片更新.....")
        self.getMainPic2()
        print("第3幅图片更新.....")
        self.getMainPic3()
        print("第4幅图片更新.....")
        self.getMainPic4()
        print("第5幅图片更新.....")
        self.getMainPic5()
        print("第6幅图片更新.....")
        self.getMainPic6()
        print("第7幅图片更新.....")
        self.getWebPic1()
        print("第8幅图片更新.....")
        self.getWebPic2()
        print("第9幅图片更新.....")
        self.getWebPic3()
        print("第10幅图片更新.....")
        self.getWebPic4()
        print("第11幅图片更新.....")
        self.getFangPic1()
        print("第12幅图片更新.....")
        self.getFangPic2()
        print("第13幅图片更新.....")
        self.getFangPic3()
        print("第14幅图片更新.....")
        self.getFangPic4()
        print("第15幅图片更新.....")
        self.getFangPic5()
        print("第16幅图片更新.....")
        self.getFangPic6()
        self.writeFlag()  #更改是否需要更新的标志


if __name__ == '__main__':
    generatePic=generatePic()
    generatePic.updatePics()
