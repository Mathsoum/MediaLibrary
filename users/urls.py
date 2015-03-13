from django.conf.urls import patterns, url

__author__ = 'Mathieu'

urlpatterns = patterns('users.views',
    url(r'^add$', 'add', name='add'),
    url(r'^connexion$', 'connexion_view', name='connexion_view'),
    url(r'^login$', 'connexion_navbar', name='connexion_navbar'),
    url(r'^logout$', 'logout_view', name='logout'),
)