from django.shortcuts import render


# Create your views here.

# def vendor_portal(request):
#     logger.info("vendor_portal_home.html is being rendered")
#     return render(request, 'Sub1.html')

def vendor_activation(request):
    return render(request, 'vendor_manager/vendor_activation.html')
def vendor_details(request):
    return render(request, 'vendor_manager/vendor_details.html')
def tracks(request):
    return render(request, 'vendor_manager/tracks.html')



