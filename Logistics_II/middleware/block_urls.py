from django.http import HttpResponseForbidden
from django.conf import settings

class BlockAllDirectURLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if settings.DEBUG:
            return self.get_response(request)

        allowed_paths = ['/login/', '/']  # whitelist login/homepage if needed

        if request.path in allowed_paths:
            return self.get_response(request)

        referer = request.META.get('HTTP_REFERER', '')
        host = request.get_host()

        if not referer.startswith(f'https://{host}'):
            return HttpResponseForbidden("Direct URL access is not allowed.")

        return self.get_response(request)