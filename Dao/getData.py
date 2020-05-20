import pymysql
import time

'''
这个类生成图片所需要的数据
'''


class getData(object):
    def __init__(self):
        super(getData, self).__init__()
        self.__conn = pymysql.connect(host='localhost', user='root', passwd='123', db='dataset', port=3306,
                                      charset='utf8')
        # 获取游标
        self.__cur = self.__conn.cursor()
        self.__cur_key = self.__conn.cursor(cursor=pymysql.cursors.DictCursor)
        self.time = time.strftime("%Y-%m-%d %H:%M:%S")

    def __release(self):
        self.__cur.close()
        self.__cur_key.close()
        self.__conn.close()

    ###############################界面1###########################3
    def getMainPic1(self):
        self.__cur.execute("select * from attack")
        data = self.__cur.fetchall()

        return data

    def getMainPic2(self):
        self.__cur.execute("select * from risk_assets")

        data = self.__cur.fetchall()
        return data

    def getMainPic3(self):
        self.__cur.execute("select * from attack")
        data = self.__cur.fetchall()

        return data

    def getMainPic4(self):
        return self.getMainPic3()

    def getMainPic5(self):
        data = []
        self.__cur_key.execute("select * from inner_atack_source")
        data1 = self.__cur_key.fetchall()
        data.append(data1)

        return data

    def getMainPic6(self):
        self.__cur_key.execute("select * from illegal_web")
        data = self.__cur_key.fetchall()

        return data

    ####################界面2##########################
    def getFangPic1(self):
        pass

    def getFangPic2(self):
        self.__cur_key.execute("select * from attack_type")
        data = self.__cur_key.fetchall()

        return data

    def getFangPic3(self):
        self.__cur_key.execute("select * from attack_method")
        data = self.__cur_key.fetchall()

        return data

    def getFangPic4(self):
        self.__cur_key.execute("select * from attack_degree")
        data = self.__cur_key.fetchall()

        return data

    def getFangPic5(self):
        self.__cur_key.execute("select * from outer_attack_source")
        data = self.__cur_key.fetchall()
        return data

    def getFangPic6(self):
        self.__cur_key.execute("select * from deal_method")
        data = self.__cur_key.fetchall()

        return data

    ############web安全#####################################
    def getWebPic1(self):
        self.__cur_key.execute("select * from attack")
        data = self.__cur_key.fetchall()

        return data[0]

    def getWebPic2(self):
        self.__cur_key.execute("select * from attack_method")
        data = self.__cur_key.fetchall()

        return data

    def getWebPic3(self):
        self.__cur_key.execute("select * from inner_atack_source")
        data = self.__cur_key.fetchall()

        return data

    def getWebPic4(self):
        self.__cur_key.execute("select * from attack_degree ")
        data = self.__cur_key.fetchall()

        return data[0]

    #########################################################################
    def getMainLabelShow1(self):
        self.__cur_key.execute("select * from attack")
        data = self.__cur_key.fetchall()

        return data

    def getMainLabelShow2(self):
        # 编数据
        pass

    def getMainLabelShow3(self):
        self.__cur_key.execute("select * from outer_attack_source")
        data = self.__cur_key.fetchall()

        return data

    def getMainLabelShow4(self):
        self.__cur_key.execute("select * from attack_type")
        data = self.__cur_key.fetchall()
        return data

    def getFangLabelShow1(self):
        data = self.getMainLabelShow4()
        return data

    def getFangLabelShow2(self):
        self.__cur_key.execute("select * from attack_method")
        data = self.__cur_key.fetchall()
        return data

    def getFangLabelShow3(self):
        self.__cur_key.execute("select * from  inner_atack_source")
        data = self.__cur_key.fetchall()
        return data

    def getWebLabelShow1(self):
        pass

    def getWebLabelShow2(self):
        pass

    def getWebLabelShow3(self):
        pass

    ########################################################################

    # 用户登录
    def LoginUser(self, username, password):
        sql = "select * from user where userName='{0}' and password='{1}'".format(username, password)
        count = self.__cur.execute(sql)
        return count

    # 管理员登陆
    def LoginManager(self, username, password):
        sql = "select * from manager where userName='{0}' and password='{1}'".format(username, password)
        count = self.__cur.execute(sql)
        return count

    #######################################################################################

    def getSqls(self):
        sql = []
        sql.append(self.__utils("select * from  inner_atack_source"))
        sql.append(self.__utils("select * from attack_method"))
        sql.append(self.__utils("select * from attack_type"))
        sql.append(self.__utils("select * from attack"))
        sql.append(self.__utils("select * from risk_assets"))
        sql.append(self.__utils("select * from attack"))
        sql.append(self.__utils("select * from inner_atack_source"))
        sql.append(self.__utils("select * from illegal_web"))
        sql.append(self.__utils("select * from attack_type"))
        sql.append(self.__utils("select * from attack_method"))
        sql.append(self.__utils("select * from attack_degree"))
        sql.append(self.__utils("select * from outer_attack_sourc"))
        sql.append(self.__utils("select * from deal_method"))
        sql.append(self.__utils("select * from attack"))
        sql.append(self.__utils("select * from attack_method"))
        sql.append(self.__utils("select * from inner_atack_sourceb"))
        sql.append(self.__utils("select * from attack_degree"))
        sql.append(self.__utils("select * from attack"))
        sql.append(self.__utils("select * from outer_attack_source"))
        self.DealManagerSqls(sql)
        return sql

    def __utils(self, sql):
        msg = []
        msg.append(sql)
        msg.append("system")
        msg.append(self.time)
        msg.append("safe")
        return msg

    # 获取管理员运行的sql语句
    def getManagerSqls(self):
        self.__cur_key.execute("select * from allsqls")
        data = self.__cur_key.fetchall()
        return getData.get_Search_Result2(data)

    # 处理管理员的sql语句
    def DealManagerSqls(self, sql_list):
        datas = self.getManagerSqls()
        for i in datas:
            msg = []
            for k, v in i.items():
                msg.append(v)
            sql = i["sqls"]
            issafe = "unsafe" if sql.split(" ")[0] in ["insert", "update", "delete"] else "safe"
            msg.append(issafe)
            sql_list.append(msg)

    # 查询的代码，不要动，我动过一次，重新写的,千万不要动！！！！！！！！！！！！！！
    def get_Search_Result(self, sql_list):
        result=[]
        for i in sql_list:
            self.__cur_key.execute(i)
            data=self.__cur_key.fetchall()
            for i in data:
                i.pop("id")
            result.append(data)
        return result


    # 处理查询的结果
    @staticmethod
    def get_Search_Result2(sqls_list):
        for i in sqls_list:
            i.pop("id")
        return sqls_list


if __name__ == '__main__':
    myData = getData()
    data=myData.getMainPic5()
    print(data)
