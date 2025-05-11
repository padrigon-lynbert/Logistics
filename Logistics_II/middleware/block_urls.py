from django.http import HttpResponseForbidden
from django.conf import settings

class StrictRefererBlockMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if settings.DEBUG:
            return self.get_response(request)

        referer = request.META.get('HTTP_REFERER', '')
        host = request.get_host()

        # Block if no referer or external referer
        if not referer.startswith(f'https://{host}'):
            return HttpResponseForbidden("Direct URL access is blocked.")

        return self.get_response(request)