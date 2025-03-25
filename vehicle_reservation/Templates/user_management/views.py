from django.shortcuts import render

def profile_management(request):
    return render(request, 'user_management/profile_management.html')
def user_roles_and_permissions(request):
    return render(request, 'user_management/user_roles_and_permissions.html')
def booking_history(request):
    return render(request, 'user_management/booking_history.html')