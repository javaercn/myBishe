import pymysql
'''
获取管理姐main要显示的数据
'''

class ManagerMsg(object):
    def __init__(self):
        self.__conn = pymysql.connect(host='localhost', user='root', passwd='123', db='dataset', port=3306,
                                      charset='utf8')
        self.__cur = self.__conn.cursor()

    def __getAllTables(self):
        count = self.__cur.execute("show tables from dataset")
        tables_lists = []
        for i in self.__cur.fetchall():
            tables_lists.append(i[0])
        tables_lists.remove("allsqls")
        return tables_lists

    def getAllTablesNames(self):
        table_list = self.__getAllTables()
        tables_names = {}
        for i in table_list:
            tables_names[i] = self.__getNames(i)
        return tables_names

    def __getNames(self, table):
        names = []
        sql = "select * from " + table
        self.__cur.execute(sql)
        desc = self.__cur.description
        for info in desc:
            names.append(info[0])
        return names


if __name__ == '__main__':
    msg = ManagerMsg()
    print(msg.getAllTablesNames())
