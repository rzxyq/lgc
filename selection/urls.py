from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
	# The main page for category
    url(r'^$', login),
    # closed
    # url(r'^$', closed),
    url(r'^list/', selection),
)