from django.shortcuts import redirect
from django.contrib import messages


class MediaLibraryMiddleware(object):
    protected_pages = [
        '/',
        '/users/add',
        '/users/login',
        '/users/logout',
        '/users/connexion',
    ]

    def process_request(self, request):
        if not request.user.is_authenticated():
            if request.path not in self.protected_pages:
                messages.warning(request, 'You must be logged in to access this page!')
                return redirect('/')
