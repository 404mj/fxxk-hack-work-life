import os
from itertools import groupby
# 处理六楼测试照片
import openpyxl

inxls=openpyxl.load_workbook("6Lceshi.xlsx")
insht=inxls.worksheets[0]
start_row=6

# https://juejin.im/post/5c57afb1f265da2dda6924a1
# 处理用户名-分割数字和其他。
nowdir = os.walk("./")
for path,dir_list,file_list in nowdir:
    for file_name in file_list:
        if not file_name.endswith(".xlsx"):
            ss = [''.join(list(g)) for k, g in groupby(file_name, key=lambda x: x.isdigit())]
            if ss[2].startswith("眼镜"):
                picext="."+ss[2].split(".")[1]
            else:
                picext=ss[2]
            insht.cell(start_row,1).value=ss[0]
            insht.cell(start_row,5).value=ss[1]
            os.rename(file_name,ss[1]+picext)
            start_row+=1
# 必须空一行xiongdei
inxls.save("6Lpics.xlsx")


# 处理图片大小
from glob import glob
from PIL import Image

threshold=300*1024
for _,_,imgfile_list in nowdir:
    for imgname in imgfile_list:
        if os.path.getsize(imgname) >= threshold:
            img=Image.open(imgname)
            img=img.resize((585,760),Image.ANTIALIAS)
            img.save(imgname,quality=100)

files=os.listdir(".")
for file in files:
    portion=os.path.splitext(file)
    if portion[1]==".JPG":
        os.rename(file,portion[0]+".jpg")

