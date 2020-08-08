from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include,re_path
from . import views

urlpatterns = [


	url(r'^marketview/$',views.marketview,name='marketview'),
	url(r'^fpodashboard/$',views.fpodashboard,name='fpodashboard'),
	url(r'^forum/$',views.forum,name='forum'),
	#url(r'^about/$',views.about,name='about'),
	url(r'^knowledge/$',views.knowledge,name='knowledge'),
	url(r'^gallery/$',views.gallery,name='gallery'),
	url(r'^contact/$',views.contact,name='contact'),

	url(r'^input/$',views.forminput,name='forminput'),

	url(r'^$',views.about,name='about'),

]
