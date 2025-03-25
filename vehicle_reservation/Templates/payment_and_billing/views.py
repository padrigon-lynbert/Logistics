from django.shortcuts import render


# Create your views here.

# def vendor_portal(request):
#     logger.info("vendor_portal_home.html is being rendered")
#     return render(request, 'Sub1.html')

def payment_processing(request):
    return render(request, 'payment_and_billing/payment_processing.html')
def payment_verification(request):
    return render(request, 'payment_and_billing/payment_verification.html')
def pricing_and_fare_calculation(request):
    return render(request, 'payment_and_billing/pricing_and_fare_calculation.html')



