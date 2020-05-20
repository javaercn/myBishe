import DealData.getMyUseData as myData
'''
登陆的逻辑
'''

class service(object):
    def __init__(self):
        self.myDataObject=myData.getMyData()

    # 用户登陆的判断
    def LoginUser(self,username, password):
        return self.myDataObject.getUserLoginMsg(username,password)

    # 管理员登陆的判断
    def LoginManager(self,username, password):
        return self.myDataObject.getManagerMsg(username,password)


