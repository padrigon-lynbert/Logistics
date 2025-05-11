from django.http import HttpResponseForbidden
from django.conf import settings

class BlockAllDirectURLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if settings.DEBUG:
            return self.get_response(request)

        host = request.get_host()
        if host != 'logistics-production-d386.up.railway.app':
            return HttpResponseForbidden("Access denied.")

        return self.get_response(request)

