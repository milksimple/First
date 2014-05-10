#coding:utf8
import re
import requests
import urllib
jl = urllib.quote("北京")
kw = "python"
salary = 0
count = 0
for page in range(1,10):
	url = """http://sou.zhaopin.com/jobs/searchresult.ashx?\
jl=%s&kw=%s&ssm=1&sf=0&sg=412bd9f74357402f95b1d4071db1a16d&p=%s"""%(jl,kw,page)
	ret = requests.get(url)
	cont = ret.content
	
	salaryAll = re.findall('<span>职位月薪：(\d+)-(\d+).*?</span>',cont,re.S)             #?????
	c = len(salaryAll)
	count += c
	#print count
	#print salaryAll
	for s in salaryAll:
		a = int(s[0]) + int(s[1])
		salary += a
per = salary / count / 2
print "平均工资：",per
