from django.http import HttpResponseForbidden
from django.conf import settings

class BlockAllDirectURLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Don't block direct access in development
        if settings.DEBUG:
            return self.get_response(request)

        referer = request.META.get('HTTP_REFERER')
        if not referer or not referer.startswith('https://yourdomain.com'):
            return HttpResponseForbidden("Direct URL access is banned.")

        return self.get_response(request)
