"""lgc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    url(r'^about/', about, name='about'),
    url(r'^schedule/', schedule, name='schedule'),
    url(r'^faq/', faq, name='faq'),
    url(r'^contact/', contact, name='contact'),
    url(r'^thanks_selection/', thanks_selection, name='thanks'),
    url(r'^thanks_newstudent/', thanks_newstudent, name='thanks'),
    url(r'^thanks_upperclassman/', thanks_upperclassman, name='thanks'),
    url(r'^error_DNE/', error_DNE,),
    url(r'^error_login/', error_login,),
    url(r'^error_taken/', error_taken,),
    url(r'^error_selected/', error_selected,),
    url(r'^error_exists/', error_exists,),
    url(r'^error_chosen/', error_chosen,),
    
    # #New Students
    # url(r'^newstudent/', include('newstudent.urls', namespace="newstudents")),
    # url(r'^upperclassman/', include('upperclassman.urls', namespace="upperclassman")),
    # url(r'^selection/', include('selection.urls', namespace="selection")),
]
