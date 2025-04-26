from django.shortcuts import render

def user_permission_management(request):
    return render(request, 'document_access_control/user_permission_management.html')
def role_based_access_control(request):
    return render(request, 'document_access_control/role_based_access_control.html')
def document_ownership_transfer(request):
    return render(request, 'document_access_control/document_ownership_transfer.html')

# user_permission_management

# role_based_access_control 

# document_ownership_transfer 