# -*- coding:utf-8 -*-
from django.conf.urls import patterns,include,url
from . import views

urlpatterns = patterns('',
		url(r'^$',views.post_list),
		#将r'^$'的url映射到视图views.post_list

)
