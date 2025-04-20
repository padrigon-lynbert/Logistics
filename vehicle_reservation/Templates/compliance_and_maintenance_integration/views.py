from django.shortcuts import render

def inspection_scheduling(request):
    return render(request, 'compliance_and_maintenance_integration/inspection_scheduling.html')
def repair_and_maintenance_request(request):
    return render(request, 'compliance_and_maintenance_integration/repair_and_maintenance_request.html')
def usage_compliance(request):
    return render(request, 'compliance_and_maintenance_integration/usage_compliance.html')
