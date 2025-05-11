from django.http import HttpResponseForbidden
from django.conf import settings

class BlockAllDirectURLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Don't block direct access in development
        if settings.DEBUG:
            return self.get_response(request)

        # List of allowed paths/URLs
        allowed_urls = [
            '/',  # Allow homepage
            'https://logistics-production-d386.up.railway.app',  # Main site
        ]

        referer = request.META.get('HTTP_REFERER', '')

        # Allow request if referer matches any of the allowed URLs or paths
        for allowed_url in allowed_urls:
            if referer.startswith(allowed_url) or request.path.startswith(allowed_url):
                return self.get_response(request)

        # Block direct URL access
        return HttpResponseForbidden("Direct URL access is blocked.")
