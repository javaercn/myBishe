from matplotlib import pyplot as plt
#设置中文的问题
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']

bar_width=0.2


a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]



x_14=list(range(len(a)))
print(x_14)
x_15=[i+0.2 for i in x_14]
x_16=[i+0.2*2 for i in x_14]
plt.bar(x_14,b_14,width=bar_width,label="14日")
plt.bar(x_15,b_15,width=bar_width,label="15日")
plt.bar(x_16,b_16,width=bar_width,label="16日")

plt.xticks(x_15,a)

plt.legend()

plt.savefig("./tiaoxing.png")
plt.show()