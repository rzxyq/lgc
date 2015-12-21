from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
	# The main page for category
    # url(r'^$', upperclassman_closed),
    url(r'^$', upper),
)
