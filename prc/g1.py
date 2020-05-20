from matplotlib import pyplot as plt

#设置中文的问题
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']




x=range(2,26,2)
y=[15,13,14,5,17,20,25,26,26,27,22,18]
y2=[15,10,13,12,10,10,25,26,22,1,11,12]

#设置图拍大小
plt.figure(figsize=(20,8),dpi=80)


#绘图,label添加标识
plt.plot(x,y,label="我",color="orange",linestyle=":",linewidth=5)
#绘制第二
plt.plot(x,y2,label="p2",color="cyan",linestyle="--")




#设置x轴的刻度
#plt.xticks(x)




#设置横坐标字符串
x_labels=["你好,{}".format(i) for i in x]
plt.xticks(x,x_labels,rotation=90)#rotation是旋转90度




#添加描述信息
plt.xlabel("时间")
plt.ylabel("温度，单位（C）")
plt.title("一天的气温变化 ")





#设置网格
plt.grid(alpha=0.8,linestyle=":")#alpha设置透明度

#让plot()中的label标签显示出来
plt.legend()






#保存
plt.savefig("./t1.png")

#显示
plt.show()