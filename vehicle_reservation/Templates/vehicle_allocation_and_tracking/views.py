from django.shortcuts import render

def fleet_assignment(request):
    return render(request, 'vehicle_allocation_and_tracking/fleet_assignment.html')
def usage_reports(request):
    return render(request, 'vehicle_allocation_and_tracking/usage_reports.html')
def vehicle_status_monitoring(request):
    return render(request, 'vehicle_allocation_and_tracking/vehicle_status_monitoring.html')
