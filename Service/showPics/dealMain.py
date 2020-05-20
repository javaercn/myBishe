import os
'''
这个类为前端提供图片的路径
'''
class dealMainPics(object):
    def __init__(self):
        self.pathMain="../resources/mainPic/"
        self.pathSec="../resources/secondPic/"
        self.thirdPic="../resources/thirdPic/"

    def getPic1(self):
        pathMain=self.pathMain+"pic1"
        path_list = os.listdir(pathMain)
        path_list_use = ["../resources/mainPic/pic1/" + i for i in path_list]
        return path_list_use


    def getPic2(self):
        pathMain = self.pathMain + "pic2"
        path_list = os.listdir(pathMain)
        path_list_use = ["../resources/mainPic/pic2/" + i for i in path_list]
        return path_list_use

    def getPic3(self):
        pathMain = self.pathMain + "pic3"
        path_list = os.listdir(pathMain)
        path_list_use = ["../resources/mainPic/pic3/" + i for i in path_list]
        return path_list_use

    def getPic4(self):
        pathMain = self.pathMain + "pic4"
        path_list = os.listdir(pathMain)
        path_list_use = ["../resources/mainPic/pic4/" + i for i in path_list]
        return path_list_use

    def getPic5(self):
        pathMain = self.pathMain + "pic5"
        path_list = os.listdir(pathMain)
        path_list_use = ["../resources/mainPic/pic5/" + i for i in path_list]
        return path_list_use

    def getPic6(self):
        pathMain = self.pathMain + "pic6"
        path_list = os.listdir(pathMain)
        path_list_use = ["../resources/mainPic/pic6/" + i for i in path_list]
        return path_list_use

    ###############################################################################
    def getFangPic1(self):
        pathSec = self.pathSec + "pic1"
        path_list = os.listdir(pathSec)
        path_list_use = ["../resources/secondPic/pic1/" + i for i in path_list]
        return path_list_use


    def getFangPic2(self):
        pathSec = self.pathSec + "pic2"
        path_list = os.listdir(pathSec)
        path_list_use = ["../resources/secondPic/pic2/" + i for i in path_list]
        return path_list_use


    def getFangPic3(self):
        pathSec = self.pathSec + "pic3"
        path_list = os.listdir(pathSec)
        path_list_use = ["../resources/secondPic/pic3/" + i for i in path_list]
        return path_list_use


    def getFangPic4(self):
        pathSec = self.pathSec + "pic4"
        path_list = os.listdir(pathSec)
        path_list_use = ["../resources/secondPic/pic4/" + i for i in path_list]
        return path_list_use


    def getFangPic5(self):
        pathSec = self.pathSec + "pic5"
        path_list = os.listdir(pathSec)
        path_list_use = ["../resources/secondPic/pic5/" + i for i in path_list]
        return path_list_use

    def getFangPic6(self):
        pathSec = self.pathSec + "pic6"
        path_list = os.listdir(pathSec)
        path_list_use = ["../resources/secondPic/pic6/" + i for i in path_list]
        return path_list_use
    ######################################################################################

    def getWebPic2(self):
        pathSec = self.thirdPic + "pic2"
        path_list = os.listdir(pathSec)
        path_list_use = ["../resources/thirdPic/pic2/" + i for i in path_list]
        return path_list_use

    def getWebPic3(self):
        pathSec = self.thirdPic + "pic3"
        path_list = os.listdir(pathSec)
        path_list_use = ["../resources/thirdPic/pic3/" + i for i in path_list]
        return path_list_use

    def getWebPic4(self):
        pathSec = self.thirdPic + "pic4"
        path_list = os.listdir(pathSec)
        path_list_use = ["../resources/thirdPic/pic4/" + i for i in path_list]
        return path_list_use


















if __name__ == '__main__':
    dealMainPics=dealMainPics()
    print(dealMainPics.getPic1())

