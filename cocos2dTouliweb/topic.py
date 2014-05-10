#coding:utf8
import re
import requests
import cocos2d as coco
for x in coco.all1:
	# print x[0]
	
	url = "http://www.cocoachina.com/bbs/read.php?tid=%s"%x[0]
	ret = requests.get(url)
	#print ret.content.decode('gbk').encode('utf8')
	topic = re.findall('<div class="tal m" style=".*?<span style=".*?">.*?:(.*?)</span>.*?</div>',ret.content,re.S)
	#print topic[0].decode('gbk').encode('utf8')
	top = topic[0].decode('gbk').encode('utf8')
	
	content = re.findall('<td height=".*?<div class="tpc_content"(.*?)</div>\W*?</td>',ret.content,re.S)
	#print content[0].decode('gbk').encode('utf8')
	cont = content[0].decode('gbk').encode('utf8')
	
	url = "http://uliweb.cpython.org/login"
	session = requests.Session()
	resp = session.get(url) #向服务器请求登录密钥
	csrf = resp.headers['set-cookie'].split(";")[0].split('=')[1] #通过拆分把密钥取出来
	body={'username':'mirk_sun','password':'gu257654','rememberme':"True"}
	body['csrf_token'] = csrf# 把密钥加入body
	resp = session.post(url,data=body)  #提交填写的内容  #以上7行功能是登录网站
	post_url = 'http://uliweb.cpython.org/forum/2/new_topic'
	resp = session.get(post_url)
	slug = re.findall("""<input class="field" id="field_slug" name="slug" placeholder="" type="hidden" value="(.*?)">""",\
	resp.content)  #这句据说要不要都行
	
	new_topic=  {"subject":top,'content':cont,'slug':slug} #把标题和内容写入字典
	new_topic['csrf_token'] = csrf #把密钥加入上面的字典
	resp = session.post(post_url,data=new_topic) #把标题内容提交到网站  实际上是提交到数据库
        # 把数据data提交到哪里 data是函数默认参数
	# session是把cookies中包括【csrf】 保存起来  用来发给访问过的网站 
