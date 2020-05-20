
'''

获取要显示的sql语句
'''
import Dao.getData as data
class getSqls():
    def __init__(self):
        self.__mydata=data.getData()

    def getMySqls(self):
        sql=self.__mydata.getSqls()
        return sql




if __name__ == '__main__':
    obj=getSqls()
    obj.getMySqls()