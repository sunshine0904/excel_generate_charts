import xlrd
import matplotlib.pyplot as plt

from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
font_size =10 # 字体大小
fig_size = (8, 6) # 图表大小
# 更新字体大小
mpl.rcParams['font.size'] = font_size
# 更新图表大小
mpl.rcParams['figure.figsize'] = fig_size
f = xlrd.open_workbook("K:2020年7月份男士内裤.xlsx")

def get_data(file, sheet_name):
	return file.sheets()
	
sheet0 = get_data(f, "test")
x_data=sheet0[0].col_values(0)
x_axis=x_data[4:len(x_data)-1]
y_data1=sheet0[0].col_values(3)
y_axis1=y_data1[4:len(y_data1)-1]
y_data2=sheet0[0].col_values(6)
y_axis2=y_data2[4:len(y_data2)-1]

z_data=sheet0[0].col_values(9)
z_axis=z_data[4:len(z_data)-1]

index = np.arange(len(y_axis1))
# 设置柱形图宽度
bar_width = 0.4

#颜色
#'cornflowerblue':       '#6495ED',  19年
#'salmon':               '#FA8072', 20年
plt.bar(index+bar_width, y_axis1, tick_label=x_axis, color='salmon',alpha=0.8, width=bar_width)
plt.bar(index+bar_width+bar_width, y_axis2, tick_label=x_axis, color='cornflowerblue',alpha=0.8, width=bar_width)
plt.xticks(np.arange(len(x_axis))+ bar_width * 1.5, x_axis)
plt.xticks(rotation=60)
plt.ylabel(u"销量")
plt.title(u"2020年7月份男裤销售量")
#plt.xlabel('Numbers',fontsize=4)
plt.legend( labels = ['2020年', '2019年'], loc = 'best')

#折线图
plt.plot(z_axis,color='b')



plt.show()







'''
data = get_data(f, "test")
for i in range(0, len(data)):
	print(data[i].col_values(0))
'''

'''
col_0 = get_data(f,"test").col_values(0)
print(col_0[0])
for i in range(0, len(col_0)):
	print(col_0[i])
参考连接：https://blog.csdn.net/u013421629/article/details/72645301?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param
'''