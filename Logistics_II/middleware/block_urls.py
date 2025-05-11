from django.http import HttpResponseForbidden
from django.conf import settings
from urllib.parse import urlparse

class BlockAllDirectURLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Don't block direct access in development
        if settings.DEBUG:
            return self.get_response(request)

        # List of allowed paths/URLs (relative or full URLs)
        allowed_urls = [
            '/',  # Allow homepage (relative)
            '/login/',  # Allow login page (relative)
        ]

        referer = request.META.get('HTTP_REFERER', '')
        host = request.get_host()  # Get current host, to compare for full URLs

        # Check if referer is empty or if it's an external referer
        if referer:
            parsed_referer = urlparse(referer)
            referer_host = parsed_referer.netloc  # Get the host part of referer URL

            # Allow requests from the same host
            if referer_host == host:
                return self.get_response(request)

        # Allow requests from allowed URLs (relative paths)
        if request.path in allowed_urls:
            return self.get_response(request)

        # Block direct URL access
        return HttpResponseForbidden("Direct URL access is blocked.")
