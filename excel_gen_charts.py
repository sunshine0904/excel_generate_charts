import xlrd
import matplotlib.pyplot as plt

from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
font_size =11 # 字体大小
fig_size = (8, 6) # 图表大小
# 更新字体大小
mpl.rcParams['font.size'] = font_size
# 更新图表大小
mpl.rcParams['figure.figsize'] = fig_size

f = xlrd.open_workbook("K:2020年7月份男士内裤.xlsx")

def get_data(file, sheet_name):
	return file.sheets()
	
sheet0 = get_data(f, "test")
print(sheet0[0].col_values(0))



'''
data = get_data(f, "test")
for i in range(0, len(data)):
	print(data[i].col_values(0))
'''



参考连接：https://blog.csdn.net/u013421629/article/details/72645301?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param



'''
col_0 = get_data(f,"test").col_values(0)
print(col_0[0])
for i in range(0, len(col_0)):
	print(col_0[i])
'''