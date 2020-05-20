import pymysql

#获取链接
conn=pymysql.connect(host='localhost',user='root',passwd='123',db='dataset',port=3306,charset='utf8')

#获取游标
cur=conn.cursor()
#count=cur.execute("show tables from dataset")
# tables_lists=[]
# for i in cur.fetchall():
#     tables_lists.append(i[0])


sql="select * from attack_type"
cur.execute(sql)
desc=cur.description
for info in desc:
    print(info[0])



