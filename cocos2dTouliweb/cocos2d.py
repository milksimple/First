#coding:utf-8
import re
import requests
i = 0
for j in range(5,101):
	# print "page in ++++++++++++++++++++++++++++++++++++++++++",j
	url = "http://www.cocoachina.com/bbs/thread.php?fid=41&page=%s"%j
	ret = requests.get(url)
	# print ret.content
	all1 = re.findall('<tr align="center".*?<td class="tal".*?<a.href="read.*?tid=(\d+).*?</a>.*?</td>\
	.*?<td class="tal y-style f10 gray"><span class="s3">(\d+)</span>/(\d+)</td>.*?</tr>',ret.content,re.S)
	# print len(all1)
	if __name__ == '__main__':
		for a in all1:
			if int(a[1]) > 5 and int(a[2]) > 1000:
				i += 1
				print a[0],a[1],a[2]
#print i

