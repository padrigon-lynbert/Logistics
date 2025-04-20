from django.shortcuts import render


# Create your views here.

# def vendor_portal(request):
#     logger.info("vendor_portal_home.html is being rendered")
#     return render(request, 'Sub1.html')

def license_and_certification_tracking(request):
    return render(request, 'driver_management/license_and_certification_tracking.html')
def driver_assignment(request):
    return render(request, 'driver_management/driver_assignment.html')
def driver_performance_monitoring(request):
    return render(request, 'driver_management/driver_performance_monitoring.html')
