import xlrd

f = xlrd.open_workbook("K:2020年7月份男士内裤.xlsx")

def get_data(file, sheet_name):
	return file.sheets()
	
data = get_data(f, "test")
print(type(data))


'''
data = get_data(f, "test")
for i in range(0, len(data)):
	print(data[i].col_values(0))





'''
col_0 = get_data(f,"test").col_values(0)
print(col_0[0])
for i in range(0, len(col_0)):
	print(col_0[i])
'''