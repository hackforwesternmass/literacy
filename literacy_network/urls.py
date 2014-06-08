from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # the home view will handle a redirection on the basis of user account type
    url(r'^$', 'literacy_network.views.home_redirect', name='home'),
    url(r'^volunteers/$', 'literacy_network.views.volunteers', name='volunteers'),
    url(r'^volunteers/new$', 'literacy_network.views.create_volunteer', name='new-volunteer'),
    url(r'^volunteers/edit/(?P<volunteer_id>\d{1,10})/$', 
        RedirectView.as_view(pattern_name='edit-volunteer-profile'), 
            name='edit-volunteer'),
    url(r'^volunteers/view/(?P<volunteer_id>\d{1,10})$', 
        'literacy_network.views.view_volunteer', name='view-volunteer'),
    url(r'^volunteers/profile/(?P<volunteer_id>\d{1,10})/(?P<hide_contact_form>True|False)?$', 
        'literacy_network.views.edit_volunteer_profile', name='edit-volunteer-profile'),
    url(r'^upload-industries$', 'literacy_network.views.upload_industries', name='industries'),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="auth_login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {"next_page" : "/logged-out"}, name="auth_logout"),
    url(r'^logged-out$', 'literacy_network.views.logged_out', name="logged_out"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/volunteers/+$', 'literacy_network.views.volunteers', name='volunteers'),
    url(r'^admin/', include(admin.site.urls)),
)
