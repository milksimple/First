#coding:utf8
import re
import requests
import urllib
from lxml import etree
city = urllib.quote("北京")  #把utf8编码的\x改为适合网址的%
kw = "python"
url = """http://sou.zhaopin.com/jobs/searchresult.ashx?\
jl=%s&kw=%s&sm=0&sg=27ce606676a743128f9fbb1fa5dd09e7&p=1"""%(city,kw)
ret = requests.get(url)
#print ret.content
reg = '<td class="Jobname">.*?href="(.*?)".*?</span>.*?</td>'
urlAll = re.findall(reg,ret.content,re.S)
url1 = urlAll[0]

'''
#这里通过etree找所有链接地址
"/html/body/div[3]/div[5]/form/div[2]/div[2]/table[2]/tbody/tr[1]/td[1]/span/a"

a = etree.HTML(ret.content)
print a.xpath('//a')
print a.xpath('//a')[2].attrib
'''

for url1 in urlAll:
	ret1 = requests.get(url1)
	cont1 = ret1.content
	title = re.findall('<td colspan="2">.*?<h1>(.*?)</h1>.*?</td>',cont1,re.S)
	#print title[0]
	cmName = re.findall('<td colspan="2">.*?<h2>.*?<a target="_blank" href=".*?>(.*?)</a></h2>.*?</td>',cont1,re.S)
	#print cmName[0]
	money = re.findall('<tr>.*?职位月薪：</td>.*?<td valign="top">(.*?)</td>.*?</tr>',cont1,re.S)
	#print money[0]
	position = re.findall('td class=.*?>工作地点：</td>.*?<td.*?<a.*?>(.*?)</a>',cont1,re.S)
	#print position[0]
	print title[0],"+",cmName[0],"+月薪:",money[0],"+工作地点:",position[0]
'''
ret1 = requests.get(url1) #
cont1 = ret1.content      #
require = re.findall('<!-- SWSStringCutStart -->(.*?)<!-- SWSStringCutEnd -->',cont1,re.S)
#print require[0]
cmDepe = re.findall('(<div class="terminalpage-content clearfix">.*?</div>)\W*?<div class="terminalpage-content clearfix">',cont1,re.S)
#print cmDepe[0]
contact = re.findall('<div class="terminalpage-content clearfix">\W+?<h1>.*?(<h2>.*?</h2>)',cont1,re.S)
print contact[0]
'''


