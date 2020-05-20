import jieba
import Dao.getData as myData

'''
这个类处理搜索的字符串
'''
class Dealtxt(object):
    def __init__(self,dealStr):
        self.all_sqls = {}
        self.getAllSqls()
        self.key_words_set = {"攻击", "程度", "方法", "处理", "类型", "非法", "网站", "源", "国外", "国内"}
        self.dealStr=dealStr


    def getWords(self):
        result=set(jieba.lcut(self.dealStr,cut_all=True))
        sqls_list=list({"程度", "方法","源","国外", "国内"}&result)
        if sqls_list.__len__()>0:
            if result.__contains__("攻击"):
                result.remove("攻击")
        return  result&self.key_words_set



    def getAllSqls(self):
        self.all_sqls["攻击"]="select * from attack"
        self.all_sqls["程度"]="select * from attack_degree"
        self.all_sqls["方法"]="select * from attack_method"
        self.all_sqls["处理"]="select * from deal_method"
        self.all_sqls["类型"]="select * from attack_type"
        self.all_sqls["非法"]="select * from illegal_web"
        self.all_sqls["网站"]="select * from illegal_web"
        self.all_sqls["源"]="select * from inner_atack_source"
        self.all_sqls["国内"]="select * from inner_atack_source"
        self.all_sqls["国外"]="select * from outer_attack_source"

    #获取要使用的sql语句
    def get_use_sqls(self):
        other=set(["国外", "国内"])
        sql_list = []
        use_sets=self.getWords()
        if use_sets is None:
            return None
        elif  (other & use_sets).__len__() != 0:
            if use_sets.__contains__("源"):
                use_sets.remove("源")
                for i in use_sets:
                    sql_list.append(self.all_sqls[i])
        else:
            if use_sets.__contains__("源"):
                sql_list.append(self.all_sqls["国外"])
            else:
                for i in use_sets:
                    sql_list.append(self.all_sqls[i])


        Dao_level = myData.getData()
        result = Dao_level.get_Search_Result(sql_list)
        return result

    def changge_format(self):
        re=[]
        data=self.get_use_sqls()
        for i in data:
            if i is not None:
                for j in i:
                    for k, value in j.items():
                        re.append(k + "-------------------------------" + str(value))

        return re










if __name__ == '__main__':
    Dealtxt=Dealtxt("我想查询攻击源")
    re=Dealtxt.getWords()
    print(re)



