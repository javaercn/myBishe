import threading
import Service.MainService as MainPic
import time


class updatePics(object):
    def __init__(self):
        self.key_words=['insert','update','delete']
        self.semphore = threading.Semaphore(1)
        self.key_sql_list=[]
        self.flag=True

    def writeLog(self):
        mytime=str(time.time())
        with open("../resources/log/updateLog.txt","a+") as f:
            f.write(mytime+"\n")

    def writeFlag(self):
        self.semphore.acquire()
        with open("../resources/isUPdateFlag/flag.txt", "w") as f:
            f.write("1")
        self.semphore.release()

    # 这个函数用于更新图片
    def updatePics(self):
        self.writeFlag() #写上是否需要更新的标志
        self.writeLog()#写日志
        MainPic.generatePic().updatePics()
        self.flag=True




    def updateStrategy(self,sql):
        a=sql.split(" ")[0]
        isExist=a in self.key_words #判断是不是要更新
        if self.flag and isExist:
            self.flag = False
            t = threading.Timer(1800, self.updatePics)#开启线程更新
            t.start()



if __name__ == '__main__':
    obj=updatePics()
    obj.updateStrategy("insert * from user")




