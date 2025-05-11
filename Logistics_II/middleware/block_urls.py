from django.http import HttpResponseForbidden
from django.conf import settings

class BlockAllDirectURLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Don't block direct access in development
        if settings.DEBUG:
            return self.get_response(request)

        # List of allowed URLs
        allowed_urls = [
            'https://logistics-production-d386.up.railway.app',  # Your allowed URL
        ]

        # If the referer is one of the allowed URLs, bypass the blocking
        referer = request.META.get('HTTP_REFERER', '')
        if any(referer.startswith(url) for url in allowed_urls):
            return self.get_response(request)

        # If the referer is not allowed, block direct URL access
        return HttpResponseForbidden("Direct URL access is blocked.")
