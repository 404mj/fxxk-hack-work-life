# -*- coding: utf-8 -*-
import requests
from lxml import etree
import re

def get_answer(input_s):
	user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
	headers = {'User-Agent':user_agent}
	url = 'http://zhannei.baidu.com/cse/search'
	params = {'q':input_s,'click':1,'entry':1,'s':'10823138076610196716'}
	r = requests.get(url, headers = headers, params=params)
	r.encoding = 'utf-8'
	selector=etree.HTML(r.text)
	a1 = selector.xpath('//*[@id="results"]/div[1]/h3/a')[0]
	ref_url = a1.get('href')
	headers['referer']=r.url
	r2 = requests.get(ref_url,headers=headers)
	r2.encoding='GB2312'
	p=re.compile(r"(\u6b63\u786e\u7b54\u6848)(.{2})")
	res = p.search(r2.text)
	print(res.group(2))

if __name__ == '__main__':
	while True:
		input_s = input("enter your question: " )
		if input_s=='exit':
			exit()
		get_answer(input_s)
