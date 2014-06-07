from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:    url(r'^$', 'literacy_network.views.edit_volunteer', name='home'),
    url(r'^$', RedirectView.as_view(url='volunteers', permanent=False), name='home'),
    url(r'^volunteers/$', 'literacy_network.views.edit_volunteer', name='home'),
    url(r'^volunteers/(?P<volunteer_id>\d{1,10})$', 'literacy_network.views.edit_volunteer', name='home'),
    # url(r'^literacy_network/', include('literacy_network.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
