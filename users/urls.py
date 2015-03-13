from django.conf.urls import patterns, url

__author__ = 'Mathieu'

urlpatterns = patterns('users.views',
    url(r'^add$', 'user_add', name='user_add'),
    url(r'^connexion$', 'connexion_view', name='connexion_view'),
    url(r'^login$', 'connexion', name='connexion'),
    url(r'^logout$', 'logout_view', name='logout'),
)