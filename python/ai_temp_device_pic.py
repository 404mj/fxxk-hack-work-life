import os
from itertools import groupby

# https://juejin.im/post/5c57afb1f265da2dda6924a1
# 处理用户名-分割数字和其他。
nowdir = os.walk("./")
for path,dir_list,file_list in nowdir:
    for file_name in file_list:
        ss = [''.join(list(g)) for k, g in groupby(file_name, key=lambda x: x.isdigit())] 
        os.rename(file_name,ss[1]+ss[2])


# 处理图片大小
from glob import glob
from PIL import Image

for _,_,imgs in nowdir:
for imgname in imgs:
	img=Image.open(imgname)
	if img.width > 800:
		img=img.resize((685,860),Image.ANTIALIAS)
		img.save(imgname,quality=100)

files=os.listdir(".")
for file in files:
    portion=os.path.splitext(file)
    if portion[1]==".JPG":
        os.rename(file,portion[0]+".jpg")
