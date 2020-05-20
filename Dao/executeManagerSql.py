import time
import pymysql
import datetime
'''
这个类执行管理员的sql语句
'''
class execueManagersql(object):
    def __init__(self,sql):
        super(execueManagersql, self).__init__()
        self.__getManager()
        self.__conn = pymysql.connect(host='localhost', user='root', passwd='123', db='dataset', port=3306,
                                      charset='utf8')
        # 获取游标
        self.__cur_key = self.__conn.cursor(cursor=pymysql.cursors.DictCursor)
        self.__sql=sql


    def __getManager(self):
        with open("../resources/manager/manager.txt", 'r') as f:
            self.__manager = f.read()

    def executeSql(self):
        try:
            if "select" in self.__sql:
                self.__cur_key.execute(self.__sql)
                data = self.__cur_key.fetchall()
                return data
            else:
                self.__cur_key.execute(self.__sql)
                data = self.__cur_key.fetchall()
                self.__conn.commit()
                #self.insertSqls()
                return data
        except(Exception):
            return None




    def insertSqls(self):
        if "insert" in self.__sql:
            self.__sql="insert"
        time1_str=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sqldata="insert into allsqls(sqls,writer,times) values('{0}','{1}','{2}')".format(self.__sql,self.__manager,time1_str)
        self.__cur_key.execute(sqldata)
        self.__conn.commit()

    def setSql(self, sql):
        self.__sql = sql


if __name__ == '__main__':
    execueManagersql = execueManagersql("aa")
    sql="select * from dnwji"
    execueManagersql.setSql(sql)
    data=execueManagersql.executeSql()
    print(data)
