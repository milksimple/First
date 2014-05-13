#coding:utf8
from django.db import models
from django.contrib.auth.models import *

class Article(models.Model):
	title   = models.CharField(max_length=70)
	content = models.TextField()
	group = models.ForeignKey('auth.Group')

class Reply(models.Model):
	content  = models.TextField()
	article  = models.ForeignKey('Article')

class Message(models.Model):
	title   = models.CharField(max_length=70)
	content = models.TextField()
	group = models.ForeignKey('auth.Group')

class Event(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    group = models.ForeignKey('auth.Group')

class EventImage(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos')
    event = models.ForeignKey('Event')



