from django.contrib import admin
from django.urls import path,include,re_path
from . import views

urlpatterns = [
	path('\marketview',views.render_marketview,name='marketview'),
	path('\fpodashboard',views.render_fpodashboard,name='fpodashboard'),
	path('\forum',views.render_forum,name='forum'),
	path('\marketplace',views.render_marketplace,name='marketplace'),
]
