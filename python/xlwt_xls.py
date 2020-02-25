import xlwt

wb=xlwt.Workbook()
sht=wb.add_sheet('Sheet1',cell_overwrite_ok=True)

borders=xlwt.Borders()
borders.top=1
borders.left=1
borders.right=1
borders.bottom=1

alignment=xlwt.Alignment()
alignment.horz=0x02
alignment.vert=0x01

tile_font=xlwt.Font()
tile_font.bold=True
tile_font.height=350
tile_font.colour_index=10

ltile_font=xlwt.Font()
ltile_font.bold=True

tile_font1=xlwt.Font()
tile_font1.bold=True
tile_font1.height=350
tile_font1.colour_index=49

tile_font2=xlwt.Font()
tile_font2.bold=True
tile_font2.height=350
tile_font2.colour_index=17


cell_style=xlwt.XFStyle()
cell_style.alignment=alignment
cell_style.borders=borders

little_style=xlwt.XFStyle()
little_style.alignment=alignment
little_style.borders=borders
little_style.font=ltile_font

big_title=xlwt.XFStyle()
big_title.font=tile_font
big_title.alignment=alignment
big_title.borders=borders

sec_title=xlwt.XFStyle()
sec_title.font=tile_font1
sec_title.alignment=alignment
sec_title.borders=borders

trd_title=xlwt.XFStyle()
trd_title.font=tile_font2
trd_title.alignment=alignment
trd_title.borders=borders


sht.write_merge(0,0,0,3,"标兵榜",big_title)
sht.write(1,0,"支行",little_style)
sht.write(1,1,"完成率",little_style)
sht.write(1,2,"支行",little_style)
sht.write(1,3,"完成率",little_style)

sht.write_merge(4,4,0,3,"前有标兵后有追兵榜",sec_title)
sht.write(5,0,"支行",little_style)
sht.write(5,1,"完成率",little_style)
sht.write(5,2,"支行",little_style)
sht.write(5,3,"完成率",little_style)

sht.write_merge(9,9,0,3,"追兵榜",trd_title)
sht.write(10,0,"支行",little_style)
sht.write(10,1,"完成率",little_style)
sht.write(10,2,"支行",little_style)
sht.write(10,3,"完成率",little_style)
row_list=[['先行区', 0.12452830188679245], ['历城', 0.07045454545454545], ['济阳', 0.060909090909090906], ['平阴', 0.03495145631067961], ['开发区', 0.034375], ['商河', 0.03428571428571429], ['章丘', 0.01869918699186992], ['营业部', 0.01818181818181818], ['和平', 0.01598173515981735], ['银河', 0.014634146341463415], ['槐荫', 0.013488372093023256], ['天桥', 0.009583333333333333], ['长清', 0.009285714285714286], ['泺源', 0.008556149732620321], ['市中', 0.0084], ['历下', 0.004285714285714286]]

for i,city in enumerate(row_list):
	if i<4:
		if i<2:
			j=0
		else:
			j=2
		sht.write((2+i%2),j,city[0],cell_style)
		sht.write((2+i%2),j+1,city[1],cell_style)
		continue
	if i<10:
		if i<7:
			m=2
			j=0
		else:
			m=-1
			j=2
		sht.write((i+m),j,city[0],cell_style)
		sht.write((i+m),j+1,city[1],cell_style)
		continue
	if i<16:
		if i<13:
			j=0
			m=1
		else:
			m=-2
			j=2
		sht.write((i+m),j,city[0],cell_style)
		sht.write((i+m),j+1,city[1],cell_style)
		continue



wb.save('a.xls')


