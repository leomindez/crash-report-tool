#!/usr/bin/env python
#encoding: utf-8
from django.conf.urls import include, url
from views import dashboard, timeline, index

urlpatterns = [
	#url(r'^$', 'acra.views.dashboard', name='dashboard'),
	url(r'dashboard/', dashboard, name='dashboard'),
	url(r'timeline/', timeline, name='timeline'),
	url(r'_design/acra-storage/_update/report/', index, name='submit'),
	]
