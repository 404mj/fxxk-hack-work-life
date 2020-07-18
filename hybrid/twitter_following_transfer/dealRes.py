dt=dict()
abandon=list()

with open("./res.log",'r',encoding='UTF-8') as f:
	for line in f.readlines():
		if line.find("==>@") <= 0:
			abandon.append(line)
		else:
			nameid=line.strip().split("==>@")
			dt[nameid[0]]=nameid[1]


wf=open('./resDeald.log','w',encoding='UTF-8')
for k,v in dt.items():
	wf.write(k+'==> @'+v+'\n')
wf.close()	