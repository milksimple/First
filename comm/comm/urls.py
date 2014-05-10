from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'comm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$','comm.views.home'),
	url(r'^classt/$','comm.views.classt'),
	url(r'^message$','comm.views.message'),
	url(r'^manage$','comm.views.manage'),
	url(r'^register$','comm.views.register'),
	url(r'^login$','django.contrib.auth.views.login',{'template_name':'login.html'}),
	# url(r'^logout$','django.contrib.auth.views.logout'),
	url(r'logout$','comm.views.logout_view'),
	# url(r'^accounts/profile/$','comm.views.profiles'),
	url(r'^create_classt$','comm.views.create_classt'),
	url(r'^manage_classt$','comm.views.manage_classt'),
	url(r'^manage_member/(.+)','comm.views.manage_member'),
	url(r'^delete_classt/(.+)','comm.views.delete_classt'),
	url(r'^on_classt/(\d+)$','comm.views.on_classt'),
	url(r'^publish_article/(\d+)','comm.views.publish_article'),
	url(r'^classt/(\d+)/article/(\d+)$','comm.views.view_article'),
	url(r'^classt/(\d+)/message$','comm.views.view_message'),
	url(r'^send_message$','comm.views.send_message'),
	url(r'^classt/(\d+)/create_event$','comm.views.create_event'),
	url(r'^classt/(\d+)/event$','comm.views.view_event'),
	url(r'^classt/(\d+)/event/(\d+)/upload','comm.views.upload_image'),
	url(r'^media/(?P<path>.*)$','django.views.static.serve',\
		{'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
)
