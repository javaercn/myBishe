import Dao.executeManagerSql as executeSql
'''
这个类处理管理员的sql语句
'''
class executeSqls(object):
    def __init__(self,sql):
        self.__sql=sql

    def executeCurrentSql(self):
        data=executeSql.execueManagersql(self.__sql).executeSql()
        mydata=[]
        if data!=None:
            if data.__len__()==0:
                return 0
            else:
                for i in data:
                    for k, v in i.items():
                        mydata.append(str(k) + "----------------------" + str(v))
                return mydata

        else:
            return None



if __name__ == '__main__':
   execute=executeSqls("aa")
   a=execute.executeCurrentSql("select * from user")
   print(a)

