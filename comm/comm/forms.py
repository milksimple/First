#coding:utf8
from django import forms
from django.forms import ModelForm 
from comm.models import *
from django.contrib.auth.models import *
from django.contrib.auth.forms import *
class UserForm(UserCreationForm):
    error_messages = {
        'duplicate_username': ("用户已经存在。"),
        'password_mismatch': ("密码不匹配"),
    }
    username = forms.RegexField(label=("用户名"), max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text=("小于30个字符,含字符和数字"
                      "@/./+/-/_ "),
        error_messages={
            'invalid': ("用户名不符合规范"
                         "@/./+/-/_ ")})
    password1 = forms.CharField(label=("密码"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=("确认密码"),
        widget=forms.PasswordInput,
        help_text=("确认使用相同的密码"))
    class Meta(UserCreationForm.Meta):
        fields = ("username",'email',)  #为什么这个就行

class ArticleForm(ModelForm):
	class Meta:
		model = Article

class ReplyForm(ModelForm):
	class Meta:
		model = Reply

class MessageForm(ModelForm):
	class Meta:
		model = Message
class GroupForm(ModelForm):
	class Meta:
		model = Group

class EventForm(ModelForm):
	class Meta:
		model = Event
		# exclude = ('group',)
'''
class EventImageForm(ModelForm):
	class Meta:
		mdoel = EventImage
'''


