from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$',          'inscrits.views.Home'),
    url(r'^plan/$',     'inscrits.views.Plan'),
    url(r'^inscrits/$', 'inscrits.views.InscritsList'),
    url(r'^nouic/$',    'inscrits.views.Nouic'),
    url(r'^register/$', 'inscrits.views.NocesRegistration'),
    url(r'^transport/$','inscrits.views.TransportListe'),
    url(r'^choixtransport/$', 'inscrits.views.ChoixTransport'),
    url(r'^asktransport/$',   'inscrits.views.AskTransport'),
    url(r'^cadeau/$',   'inscrits.views.Cadeau'),


    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# This is needed to serve static files like images and css
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()