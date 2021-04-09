# -*- coding: utf8 -*-
import requests
import os
import logging
import time
import distance
import string
import re
import jieba

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
TOKEN='8b3b69dbb20d4450adba074998d684d5'

'''
#event hooks , hooks={'response':presp}
def presp(res, *args, **kwargs):
    logger.info('HOOK!---'+res.text)
'''
mp3_list=[]
for root,dirs,files in os.walk('./'):
    for file in files:
        ext=os.path.splitext(file)[-1]
        name=os.path.splitext(file)[0]
        if(ext=='.mp3'):
            mp3_list.append(file)

post_line='http://nls-gateway.cn-shanghai.aliyuncs.com/stream/v1/FlashRecognizer?appkey=IqbobRnd8whta8vw&token='+TOKEN+'&format=mp3&sample_rate=16000&enable_inverse_text_normalization=true'
header={'Content-type': 'application/octet-stream','Host': 'nls-gateway.cn-shanghai.aliyuncs.com'}

ress=dict()#{city:[time_cost,sentence]}
for mp3 in mp3_list:
    payload=open(mp3,'rb')
    start=time.perf_counter()
    resp=requests.post(post_line, timeout=30, headers=header, data=payload)
    finish=time.perf_counter()
    name=os.path.splitext(mp3)[0].split('_')[1]
    sentences= ''.join(texts['text'] for texts in resp.json()['flash_result']['sentences'])
    ress[name]=[finish-start,sentences]

'''
# labeled text procress,earse all text to a line
for _,_,files in os.walk('./'):
    for file in files:
        if(os.path.splitext(file)[-1]=='.txt'):
            fo=open(file,'r+')
            newtxt=''.join(line.strip()+' ' for line in fo.readlines())
            fo.seek(0,0)
            fo.write(newtxt)
            fo.close()
'''
#clear stopwords and puncatuation
def clear_text(linestr):
    ch_p='，。？！《》、——  '
    en_p=string.punctuation
    stopw=[line.strip() for line in open('./baidu_stopwords.txt', encoding="utf-8").readlines()]
    seged_line=jieba.lcut(re.sub('[%s]+' %(ch_p+en_p),'',linestr))
    newtxt=''
    for w in seged_line:
        if w not in stopw and w!='\t':
            newtxt+=w+' '
    return newtxt

for _,_,files in os.walk('./'):
    for file in files:
        if(os.path.splitext(file)[-1]=='.txt' and os.path.splitext(file)[0] != 'baidu_stopwords'):
            print(os.path.basename(file))
            fo=open(file,'r+',encoding='UTF-8-sig')
            newtxt=clear_text(fo.readline())
            fo=open(file,'w',encoding='utf-8')
            fo.write(newtxt)
            fo.close()





#compare,logging and write text 
data=dict()
for city,res in ress.items():
    tfname='t_{}{}'.format(city,'.txt')
    label_t=open(tfname,'r',encoding='UTF-8').readline()
    clean_res = clear_text(res[1])
    edit_dis=distance.levenshtein(label_t,clean_res)
    report='<{}>: edit_dis:{}, label total:{}, similarity:{}, time_cost:{}'.format(city,edit_dis,len(label_t),1-edit_dis/len(label_t),res[0])
    logger.info(report)
    
    city_pure=''.join(i for i in city if i.isalpha())
    if city_pure in data:
        data[city_pure]=(data.get(city_pure) + 1-edit_dis/len(label_t))/2
    else:
        data[city_pure]=1-edit_dis/len(label_t)
        
    fo=open('c_{}{}'.format(city,'.txt'),'w')
    fo.write(report+'\n')
    fo.write(clean_res)
    fo.close()

# total and every city statistic 
total_similarity=sum(v for v in data.values())/len(data)
logger.info('total_similarity:%s',total_similarity)
logger.info(data)



'''
# the same as above
os.system('sh test.sh')
'''
