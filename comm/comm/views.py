#coding:utf8
import os
from django.shortcuts import render_to_response,render,redirect
from django.template import RequestContext
from comm.models import Article
from django.contrib.auth.forms import *
from django.contrib.auth.models import *
from django.contrib.contenttypes.models import ContentType
from comm.forms import *
from django.core.mail import send_mail
from django.contrib.auth import logout

def home(request):
	user = request.user
	return render_to_response('home.html',{'user':user},context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return redirect('/home')

def profiles(request):
	return redirect('/home')


def classt(request):
	classt = Group.objects.all()
	return render_to_response('classt.html',{'classt':classt},context_instance=RequestContext(request))

def message(request):
	allclasst = Group.objects.all()
	return render_to_response('message.html',{'allclasst':allclasst},\
	context_instance=RequestContext(request))


def create_event(request,classtId):
	form = EventForm()
	
	if request.method == 'POST':
		n = EventForm(request.POST,request.FILES)
		if n.is_valid():
			n.save()
			return redirect('/classt/'+classtId+'/event')
	return render_to_response('create_event.html',{'form':form},context_instance=RequestContext(request))


def view_event(request,classtId):
	classt = Group.objects.get(id=int(classtId))
	event = classt.event_set.all()
	
	return render_to_response('view_event.html',{'event':event,'classt':classt,},\
	context_instance=RequestContext(request))


def upload_image(request,classtId,eventId):
	event = Event.objects.get(id=int(eventId))
	if request.method == "POST":
		print request.FILES['image']
		n = EventImage.objects.create(title = request.POST['title'],image = request.FILES['image'],event=event)
		return redirect('/classt/'+classtId+'/event')
	return render_to_response('upload_image.html',{},context_instance=RequestContext(request))



def view_message(request,classtId):
	classt = Group.objects.get(id=int(classtId))
	allmessage = classt.message_set.all()
	return render_to_response('view_message.html',{'allmessage':allmessage},context_instance=RequestContext(request))

def send_message(request):
	form = MessageForm()

	if request.method == 'POST':
		n = MessageForm(request.POST)
		if n.is_valid():
			n.save()

			classtId = request.POST['group']
			classt = Group.objects.get(id=int(classtId))
			classmember = classt.user_set.all()
			# print classmember
			mailList = []
			for m in classmember:
				mailList.append(m.email)
			# print mailList
			send_mail(request.POST.get('title'),request.POST.get('content'),\
				'470042560@qq.com',mailList)
			
			return redirect('/message')
	return render_to_response('send_message.html',{'form':form},\
	context_instance=RequestContext(request))


def manage(request):
	user = request.user
	form = PasswordChangeForm(user)
	if request.method == 'POST':
		n = PasswordChangeForm(user,request.POST)
		if n.is_valid():
			n.save()
			sucess = '修改成功'
			return render_to_response('manage.html',{'sucess':sucess},context_instance=RequestContext(request))
	return render_to_response('manage.html',{'form':form},context_instance=RequestContext(request))

def register(request):
	form = UserForm()
	if request.method == "POST":
		n = UserForm(request.POST)
		if n.is_valid():
			n.save()
			return redirect('/home')
	return render_to_response('register.html',{'form':form},context_instance=RequestContext(request))

def create_classt(request):
	if request.method == 'POST':
		n = GroupForm(request.POST)
		if n.is_valid():
			n.save()
			return redirect('/classt')
	form = GroupForm()
	alluser = User.objects.all()
	return render_to_response('create_classt.html',{'form':form,'alluser':alluser},context_instance=RequestContext(request))


def manage_classt(request):
	# allclasst = Classt.objects.all()
	allclasst = Group.objects.all()
	return render_to_response('manage_classt.html',{'allclasst':allclasst},context_instance=RequestContext(request))


def manage_member(request,classtname):
	group = Group.objects.all()
	# alluser = group.user_set.all()
	return render_to_response('manage_member.html',{'group':group},context_instance=RequestContext(request))




def delete_classt(request,classtname):
	n = Group.objects.get(name=classtname)
	n.delete()
	return redirect('/manage_classt')


def on_classt(request,classtId):
	classt = Group.objects.get(id=int(classtId))
	messages = classt.message_set.all()
	user = classt.user_set.all()
	allarticle = classt.article_set.all()
	return render_to_response('on_classt.html',{'allarticle':allarticle,\
	'user':user,'classtId':classtId,'classt':classt,'messages':messages},\
	context_instance=RequestContext(request))

def publish_article(request,classtId):
	form = ArticleForm()
	if request.method == 'POST':
		n = ArticleForm(request.POST)
		if n.is_valid():
			n.save()
			return redirect('/on_classt/'+ classtId)
	return render_to_response('publish_article.html',{'form':form},\
	context_instance=RequestContext(request))

def view_article(request,classtId,articleId):
	user = request.user
	article = Article.objects.get(id=int(articleId))
	classt = Group.objects.get(id=int(classtId))
	classtUser = classt.user_set.all()
	print classtUser#####################
	print user##################
	alluser = []
	for u in classtUser:
		alluser.append(u.username)
	if request.method == 'POST':
		n = Reply.objects.create(content=request.POST.get('reply'),article=article)
	reply = article.reply_set.all()
	return render_to_response('one_article.html',{'alluser':alluser,'classtname':classt.name,\
	'user':user,'reply':reply,'article':article},\
	context_instance=RequestContext(request))


