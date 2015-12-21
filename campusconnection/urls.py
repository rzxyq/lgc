from django.conf.urls import patterns, include, url

from django.contrib import admin
from views import *
admin.autodiscover()

urlpatterns = patterns('',
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
    #New Students
    url(r'^newstudent/', include('newstudent.urls', namespace="newstudents")),
	url(r'^upperclassman/', include('upperclassman.urls', namespace="upperclassman")),
	url(r'^selection/', include('selection.urls', namespace="selection")),
    url(r'^admin/', include(admin.site.urls)),
)
