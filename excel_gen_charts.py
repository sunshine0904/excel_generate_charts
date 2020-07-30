#-*- coding:utf-8 -*-
import xlrd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from pylab import *
import os

#这里是要生成图片的excel的文件名
file_name="K:2020年7月份男士内裤.xlsx"

#这里是生成的柱状图图片的名字
save_fig_name="K:test.jpg"


#f = xlrd.open_workbook(file_name)

def get_all_excel_file(path):
	excel_files=[]
	for files in os.walk(path):
		print(type(files))
		print(files[len(files) - 4 : len(files)])
		if files[len(files) - 4 : len(files)] == "xlsx":
			excel_files.append(files)
	return excel_files

def fig_setting():
	mpl.rcParams['font.sans-serif'] = ['SimHei']
	font_size =10 # 字体大小
	fig_size = (8, 6) # 图表大小
	# 更新字体大小
	mpl.rcParams['font.size'] = font_size
	# 更新图表大小
	mpl.rcParams['figure.figsize'] = fig_size

def get_data(file, sheet_name):
	return file.sheets()
	
def gen_figure():
	fig_setting()
	#x y轴数据获取
	sheet0 = get_data(f, "test")
	x_data=sheet0[0].col_values(0)
	x_axis=x_data[4:len(x_data)-1]
	y_data1=sheet0[0].col_values(3)
	y_axis1=y_data1[4:len(y_data1)-1]
	y_data2=sheet0[0].col_values(6)
	y_axis2=y_data2[4:len(y_data2)-1]
	z_data=sheet0[0].col_values(9)
	z_axis=z_data[4:len(z_data)-1]

	#画柱状图
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
	
	#图例
	plt.legend( labels = ['2020年', '2019年'], loc = 'best')

	'''
	柱形图标注（暂不需要）
	max_saler_20 = max(y_axis1)
	for x,y in zip(index, y_axis1):
		plt.text(x, y + max_saler_20 * 0.02, round(y,1), ha='center', va='center', fontsize=13)

	max_saler_19 = max(y_axis2)
	for x,y in zip(index, y_axis2):
		plt.text(x, y + max_saler_19 * 0.02, round(y,1), ha='center', va='center', fontsize=13)
	'''


	#折线图
	plt.twinx()
	plt.plot(index + bar_width * 1.5, z_axis,color='r',marker='o',markersize='5',markeredgecolor='g')
	plt.ylabel(u"同比增长")
	saler_compare = max(z_axis)
	for x,y in zip(index, z_axis):
		#plt.text(x, y + saler_compare * 0.02, ('%.1f%%'%(y*100)), ha='center', va='center', fontsize=13)
		plt.text(x, y + saler_compare * 0.02, ('  %d%%'%((y*100))), ha='center', va='center', fontsize=13)

	#图例
	plt.legend(labels = ['同比销额增长'], loc='upper right', bbox_to_anchor=(1.0,0.9), ncol=3, fancybox=True,shadow=True)

	#保存图
	plt.savefig(save_fig_name)
	
	#出图
	#plt.show()

#gen_figure()
print(get_all_excel_file(os.getcwd()+"\excel"))
