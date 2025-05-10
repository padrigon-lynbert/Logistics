from django.http import HttpResponseForbidden

class BlockAllDirectURLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # If there's no referer, it's likely a direct URL access
        if not request.META.get('HTTP_REFERER'):
            # Block the request with a forbidden response
            return HttpResponseForbidden("Direct URL access is banned.")
        
        # Proceed with the usual response if it's not a direct access
        response = self.get_response(request)
        return response
