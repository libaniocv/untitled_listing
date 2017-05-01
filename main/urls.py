from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'untitled_listing_tool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^$', views.index),
    url(r'^registrar/$', views.registrar),
)
