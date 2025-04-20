from django.shortcuts import render


# Create your views here.

# def vendor_portal(request):
#     logger.info("vendor_portal_home.html is being rendered")
#     return render(request, 'Sub1.html')

def booking_requests(request):
    return render(request, 'reservation_management/booking_requests.html')
def cancelation_and_modifications(request):
    return render(request, 'reservation_management/cancelation_and_modifications.html')
def reservation_approval(request):
    return render(request, 'reservation_management/reservation_approval.html')
