from django.shortcuts import render

def alerts_for_servicing_needs(request):
    return render(request, 'maintenance_management/alerts_for_servicing_needs.html')
def maintenance_history_logging(request):
    return render(request, 'maintenance_management/maintenance_history_logging.html')
def preventive_maintenance_scheduling(request):
    return render(request, 'maintenance_management/preventive_maintenance_scheduling.html')