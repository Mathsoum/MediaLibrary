from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', 'MediaLibrary.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^users/', include('users.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
