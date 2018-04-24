from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^hello/$', 'app.views.hello'),
                       url(r'^index/$', 'app.views.index'),
                       url(r'^home/$', 'app.views.home', name='home'),
                       url(r'^admin/', include(admin.site.urls)),
                       )
