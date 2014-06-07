from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:    url(r'^$', 'literacy_network.views.edit_volunteer', name='home'),
    url(r'^$', RedirectView.as_view(url='volunteers/new', permanent=False), name='home'),
    url(r'^volunteers/new$', 'literacy_network.views.edit_volunteer', name='home'),
    url(r'^volunteers/(?P<volunteer_id>\d{1,10})$', 'literacy_network.views.edit_volunteer', name='home'),

    url(r'^login$', 'django.contrib.auth.views.login', name="auth_login"),
    url(r'^logout$', 'django.contrib.auth.views.login', name="auth_loguot"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
