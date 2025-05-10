from django.http import HttpResponseForbidden
from django.conf import settings

class BlockAllDirectURLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Allow in debug/dev environment
        if settings.DEBUG:
            return self.get_response(request)

        # Block requests without referer (direct URL access)
        if not request.META.get('HTTP_REFERER'):
            return HttpResponseForbidden("Direct URL access is banned.")

        return self.get_response(request)
