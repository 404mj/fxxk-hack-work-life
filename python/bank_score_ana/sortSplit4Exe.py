'''
1-4 标兵榜
5-10 前有标兵后有追兵榜
11-16 追兵榜
'''
# https://www.cnblogs.com/Forever77/p/11135124.html
import xlrd
import xlwt

FILE_PATH=input("输入文件路径：")
FILE_NAME=input("输入文件名：")
if len(FILE_PATH) == 0 or len(FILE_NAME) == 0 or FILE_PATH.find(':')==-1:
    print("参数输入错误，程序退出，重新运行输入:)")
    exit(1)

if FILE_PATH[-1] is not '\\':
    FILE_PATH=FILE_PATH+'\\'

wbrd=xlrd.open_workbook(FILE_PATH+FILE_NAME)
shtrd=wbrd.sheet_by_index(0)
row_list=[]
for i in range(4,20):
    row_list.append(shtrd.row_values(i)[0:6:5])

row_list.sort(key=lambda x: x[1],reverse=True)

wb=xlwt.Workbook()
sht=wb.add_sheet('Sheet1',cell_overwrite_ok=True)

# 写入格式设置-边框
borders=xlwt.Borders()
borders.top=1
borders.left=1
borders.right=1
borders.bottom=1

# 对齐方式
alignment=xlwt.Alignment()
alignment.horz=0x02
alignment.vert=0x01

# 普通单元格字体
cell_font=xlwt.Font()
cell_font.name=u'宋体'
cell_font.height=20*13

# 小标题字体
ltile_font=xlwt.Font()
ltile_font.bold=True
ltile_font.name=u'宋体'
ltile_font.height=20*13

head_font=xlwt.Font()
# head_font.bold=True
head_font.name=u"微软雅黑"
head_font.height=20*20

lhead_font=xlwt.Font()
# lhead_font.bold=True
lhead_font.name=u"微软雅黑"
lhead_font.height=20*12

# 第一梯队字体
tile_font=xlwt.Font()
tile_font.bold=True
tile_font.name=u"微软雅黑"
tile_font.height=20*18
tile_font.colour_index=10

# 第二梯队字体
tile_font1=xlwt.Font()
tile_font1.bold=True
tile_font.name=u"微软雅黑"
tile_font1.height=20*18
tile_font1.colour_index=49

# 第三梯队字体
tile_font2=xlwt.Font()
tile_font.name=u"微软雅黑"
tile_font2.bold=True
tile_font2.height=20*18
tile_font2.colour_index=17

# 第一梯队背景色
pat1=xlwt.Pattern()
pat1.pattern = xlwt.Pattern.SOLID_PATTERN
pat1.pattern_fore_colour=2

# 第二梯队背景色
pat2=xlwt.Pattern()
pat2.pattern = xlwt.Pattern.SOLID_PATTERN
pat2.pattern_fore_colour=40

# 第三梯队背景色
pat3=xlwt.Pattern()
pat3.pattern = xlwt.Pattern.SOLID_PATTERN
pat3.pattern_fore_colour=42

# 第一梯队单元格样式
cell_style1=xlwt.XFStyle()
cell_style1.alignment=alignment
cell_style1.borders=borders
cell_style1.pattern=pat1
cell_style1.font=cell_font
cell_style1.num_format_str='0.00%'

# 第二梯队单元格样式
cell_style2=xlwt.XFStyle()
cell_style2.alignment=alignment
cell_style2.borders=borders
cell_style2.pattern=pat2
cell_style2.font=cell_font
cell_style2.num_format_str='0.00%'

# 第三梯队单元格样式
cell_style3=xlwt.XFStyle()
cell_style3.alignment=alignment
cell_style3.borders=borders
cell_style3.pattern=pat3
cell_style3.font=cell_font
cell_style3.num_format_str='0.00%'

# 小标题单元格样式
little_style=xlwt.XFStyle()
little_style.alignment=alignment
little_style.borders=borders
little_style.font=ltile_font

# 元标题设置
head_title=xlwt.XFStyle()
head_title.font=head_font
head_title.alignment=alignment
head_title.borders=borders

lhead_title=xlwt.XFStyle()
lhead_title.font=lhead_font
lhead_title.alignment=alignment
lhead_title.borders=borders

# 第一梯队标题设置
big_title=xlwt.XFStyle()
big_title.font=tile_font
big_title.alignment=alignment
big_title.borders=borders

# 第二梯队标题设置
sec_title=xlwt.XFStyle()
sec_title.font=tile_font1
sec_title.alignment=alignment
sec_title.borders=borders

# 第三梯队标题设置
trd_title=xlwt.XFStyle()
trd_title.font=tile_font2
trd_title.alignment=alignment
trd_title.borders=borders

# 写入标题
sht.write_merge(0,0,0,3,"排行榜",head_title)
sht.write_merge(1,1,0,3,"日期",lhead_title)

sht.write_merge(2,2,0,3,"标兵榜",big_title)
sht.write(3,0,"支行",little_style)
sht.write(3,1,"完成率",little_style)
sht.write(3,2,"支行",little_style)
sht.write(3,3,"完成率",little_style)

sht.write_merge(6,6,0,3,"前有标兵后有追兵榜",sec_title)
sht.write(7,0,"支行",little_style)
sht.write(7,1,"完成率",little_style)
sht.write(7,2,"支行",little_style)
sht.write(7,3,"完成率",little_style)

sht.write_merge(11,11,0,3,"追兵榜",trd_title)
sht.write(12,0,"支行",little_style)
sht.write(12,1,"完成率",little_style)
sht.write(12,2,"支行",little_style)
sht.write(12,3,"完成率",little_style)


# 写入数据
for i,city in enumerate(row_list):
    if i<4:
        if i<2:
            j=0
            m=4
        else:
            m=2
            j=2
        sht.write((i+m),j,city[0],cell_style1)
        sht.write((i+m),j+1,city[1],cell_style1)
        continue
    if i<10:
        if i<7:
            m=4
            j=0
        else:
            m=1
            j=2
        sht.write((i+m),j,city[0],cell_style2)
        sht.write((i+m),j+1,city[1],cell_style2)
        continue
    if i<16:
        if i<13:
            j=0
            m=3
        else:
            m=0
            j=2
        sht.write((i+m),j,city[0],cell_style3)
        sht.write((i+m),j+1,city[1],cell_style3)
        continue
for  i in range(4):
    sht.col(i).width=256*15

wb.save(FILE_PATH+FILE_NAME.split('.')[0]+'_done.xls')
print("处理完毕done！")
