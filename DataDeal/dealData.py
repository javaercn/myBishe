import pandas as pd
from collections import Counter
import pickle

def Serialization(file,data):
    file.write(pickle.dumps(data))
    file.close()

def AntSerialization(file):
    data=pickle.loads(file.read())
    return data

file=open("AllUseData/MainPrc/Maipic1/p5.txt", "wb")



GongJi_type_data=pd.read_excel("AllData/data/data4_web.xlsx",skiprows=16,usecols=[17])
data=GongJi_type_data.values
data2=data.reshape(1,-1)
data_list=data2[0].tolist()
data_use=Counter(data_list)
print(data_use)


















'''
Serialization(file,data_use)
file=open("AllUseData/mainPrc/Maipic1/p5.txt", "rb")
data=AntSerialization(file)
print(data)
'''
