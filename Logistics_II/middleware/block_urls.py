import logging
from django.http import HttpResponseForbidden
from django.conf import settings

logger = logging.getLogger(__name__)

class BlockAllDirectURLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if settings.DEBUG:
            return self.get_response(request)

        logger.info("BlockAllDirectURLMiddleware triggered!")  # Log to check if it's being triggered

        return HttpResponseForbidden("Direct URL access is blocked.")
