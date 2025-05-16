from django.shortcuts import render


# Create your views here.

def license_and_certification_tracking(request):
    return render(request, 'driver_management/license_and_certification_tracking.html')
def driver_assignment(request):
    return render(request, 'driver_management/driver_assignment.html')
def driver_performance_monitoring(request):
    return render(request, 'driver_management/driver_performance_monitoring.html')

def alerts_for_servicing_needs(request):
    return render(request, 'maintenance_management/alerts_for_servicing_needs.html')
def maintenance_history_logging(request):
    return render(request, 'maintenance_management/maintenance_history_logging.html')
def preventive_maintenance_scheduling(request):
    return render(request, 'maintenance_management/preventive_maintenance_scheduling.html')

def vehicle_inspections(request):
    return render(request, 'safety_and_compliance/vehicle_inspections.html')
def regulatory_compliance_tracking(request):
    return render(request, 'safety_and_compliance/regulatory_compliance_tracking.html')
def accident_reporting(request):
    return render(request, 'safety_and_compliance/accident_reporting.html')

# 
def asset_management(request):
    return render(request, 'maintenance_management/asset_management.html')

def header(request):
    return render(request, 'nav_kl.html')
def driver_ass(request):
    return render(request, 'driver_management/driver_ass.html')
def vehicle_tracking(request):
    return render(request, 'driver_management/vehicle_tracking.html')
def coplianc_training(request):
    return render(request, 'safety_and_compliance/compliance_training.html')
