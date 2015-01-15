from django.shortcuts import redirect
from django.contrib import messages


class GalleryMiddleware(object):

    def process_request(self, request):
        if not request.user.is_authenticated():
            if request.path not in ["/", "/gallery"]:
                messages.warning(request, 'You must be logged in to access this page!')
                return redirect('/')
