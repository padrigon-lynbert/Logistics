from django.shortcuts import render

def inspection_scheduling(request):
    return render(request, 'compliance_and_maintenance_integration/inspection_scheduling.html')
def repair_and_maintenance_request(request):
    return render(request, 'compliance_and_maintenance_integration/repair_and_maintenance_request.html')
def usage_compliance(request):
    return render(request, 'compliance_and_maintenance_integration/usage_compliance.html')

def booking_requests(request):
    return render(request, 'reservation_management/booking_requests.html')
def cancelation_and_modifications(request):
    return render(request, 'reservation_management/cancelation_and_modifications.html')
def reservation_approval(request):
    return render(request, 'reservation_management/reservation_approval.html')

def fleet_assignment(request):
    return render(request, 'vehicle_allocation_and_tracking/fleet_assignment.html')
def usage_reports(request):
    return render(request, 'vehicle_allocation_and_tracking/usage_reports.html')
def vehicle_status_monitoring(request):
    return render(request, 'vehicle_allocation_and_tracking/vehicle_status_monitoring.html')

# new

def booking_history(request):
    return render(request, 'reservation_management/booking_history.html')

