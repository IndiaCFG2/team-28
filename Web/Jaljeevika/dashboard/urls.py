from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include,re_path
from . import views

urlpatterns = [
	url(r'^marketview/$',views.render_marketview,name='marketview'),
	url(r'^fpodashboard/$',views.render_fpodashboard,name='fpodashboard'),
	url(r'^forum/$',views.render_forum,name='forum'),
	url(r'^marketplace/$',views.render_marketplace,name='marketplace'),
]
