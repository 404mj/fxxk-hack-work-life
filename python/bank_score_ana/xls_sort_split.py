'''
1-4 标兵榜
5-10 前有标兵后有追兵榜
11-16 追兵榜
'''
# https://www.cnblogs.com/Forever77/p/11135124.html
from xlrd import open_workbook
import xlwt
# from xlutils.copy as copy
FILE_PATH=r"C:\Users\zsx\Downloads\Documents"
wb=xlrd.open_workbook(FILE_PATH+r"ccc.xls")
sht=wb.sheet_by_index(0)
row_list=[]
for i in range(4,20):
    row_list.append(sht.row_values(i)[0:6:5])

row_list.sort(key=lambda x: x[1],reverse=True)

# wbwt=copy(wb)
# sht0=wbwt.get_sheet(0)
# sht0.write(22,14,row_list[0][0])
# wbwt.save(FILE_PATH)


wt=xlwt.Workbook()
shtwt=wt.add_sheet('Sheet1')
shtwt.write(0,0,row_list[0][0])
wt.save('test.xls')