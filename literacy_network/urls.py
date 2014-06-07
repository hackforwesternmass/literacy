from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:    url(r'^$', 'literacy_network.views.edit_volunteer', name='home'),
    url(r'^$', RedirectView.as_view(url='volunteers/new', permanent=False), name='home'),
    url(r'^volunteers/$', 'literacy_network.views.volunteers', name='volunteers'),
    url(r'^volunteers/new$', 'literacy_network.views.edit_volunteer', name='new-volunteer'),
    url(r'^volunteers/(?P<volunteer_id>\d{1,10})$', 'literacy_network.views.edit_volunteer', name='home'),
    url(r'^volunteers/profile/(?P<volunteer_id>\d{1,10})$', 'literacy_network.views.edit_volunteer_profile'),
    url(r'^upload-industries$', 'literacy_network.views.upload_industries', name='industries'),

    # url(r'^literacy_network/', include('literacy_network.foo.urls')),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="auth_login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {"next_page" : "/"}, name="auth_logout"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/volunteers/+$', 'literacy_network.views.volunteers', name='volunteers'),
    url(r'^admin/', include(admin.site.urls)),
)
