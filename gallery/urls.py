from django.conf.urls import patterns, url

urlpatterns = patterns('gallery.views',

    url(r'^$', 'index', name='index'),

    url(r'^image/$', 'image_list', name='image_list'),
    url(r'^image/add/$', 'image_add', name='image_add'),
    url(r'^image/del/(?P<album_slug>.*)/(?P<image_id>.*)/$', 'image_del', name='image_del'),

    url(r'^album/$', 'album_list', name='album_list'),
    url(r'^album/add/$', 'album_add', name='album_add'),
    url(r'^album/del/(?P<slug>.*)/$', 'album_del', name='album_del'),
    url(r'^album/(?P<slug>.*)/$', 'album_detail', name='album_detail'),

    url(r'^user/add$', 'user_add', name='user_add'),
    url(r'^connexion$', 'connexion_view', name='connexion_view'),
    url(r'^login$', 'connexion', name='connexion'),
    url(r'^logout$', 'logout_view', name='logout'),
)