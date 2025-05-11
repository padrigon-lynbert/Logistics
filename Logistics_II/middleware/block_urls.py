from django.http import HttpResponseForbidden
from django.conf import settings

class BlockAllDirectURLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if settings.DEBUG:
            return self.get_response(request)

        allowed_paths = ['/login/', '/']  # add more if needed

        if request.path in allowed_paths:
            request.session['visited'] = True
            return self.get_response(request)

        if not request.session.get('visited', False):
            return HttpResponseForbidden("Direct URL access is not allowed.")

        return self.get_response(request)
