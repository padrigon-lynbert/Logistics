from django.shortcuts import render


# Create your views here.

# def vendor_portal(request):
#     logger.info("vendor_portal_home.html is being rendered")
#     return render(request, 'Sub1.html')

def policies(request):
    return render(request, 'compliance_management/policies.html')
def procedures(request):
    return render(request, 'compliance_management/procedures.html')
def audits(request):
    return render(request, 'compliance_management/audits.html')



