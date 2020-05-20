import pandas as pd
from collections import Counter
import pickle



file=open("AllUseData/secondPrc/prc6/p.txt", "rb")
def AntSerialization(file):
    data=pickle.loads(file.read())
    return data

data=AntSerialization(file)
print(data)
