from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'inscrits.views.Home'),
    url(r'^plan/$', 'inscrits.views.Plan'),
    url(r'^inscrits/$', 'inscrits.views.InscritsList'),
    url(r'^nouic/$', 'inscrits.views.Nouic'),
    url(r'^register/$', 'inscrits.views.NocesRegistration'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
