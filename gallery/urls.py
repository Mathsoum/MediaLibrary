from django.conf.urls import patterns, url
from django.views.generic.list import ListView
from gallery.models import Image

urlpatterns = patterns('gallery.views',
    url(r'^$', 'album_list'),
    
    url(r'^image/$', 'image_list', name="List images"),
    url(r'^image/add/$', 'image_add', name='Add image'),
    url(r'^image/del/(?P<album_slug>.*)/(?P<image_id>.*)/$', 'image_del', name='Image del'),
    
    url(r'^album/$', 'album_list', name='List albums'),
    url(r'^album/add/$', 'album_add', name='Add album'),
    url(r'^album/(?P<slug>.*)/$', 'album_detail', name='Add album'),
)