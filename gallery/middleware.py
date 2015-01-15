from django.shortcuts import redirect
from django.contrib import messages


class GalleryMiddleware(object):
    protected_pages = [
        '/',
        '/gallery',
        '/gallery/',
        '/gallery/user/add',
        '/gallery/login',
        '/gallery/logout',
        '/gallery/connexion',
    ]

    def process_request(self, request):
        if not request.user.is_authenticated():
            print('User not logged in! Path : %s' % request.path)
            if request.path not in self.protected_pages:
                messages.warning(request, 'You must be logged in to access this page!')
                return redirect('/')
