from django.shortcuts import render

def vehicle_inspections(request):
    return render(request, 'safety_and_compliance/vehicle_inspections.html')
def regulatory_compliance_tracking(request):
    return render(request, 'safety_and_compliance/regulatory_compliance_tracking.html')
def accident_reporting(request):
    return render(request, 'safety_and_compliance/accident_reporting.html')

# vehicle_inspections
# regulatory_compliance_tracking
# accident_reporting