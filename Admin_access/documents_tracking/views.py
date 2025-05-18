from django.shortcuts import render

def event_tracking (request):
    return render(request, 'activity_log/event_tracking.html')
def time_stamping(request):
    return render(request, 'activity_log/time_stamping.html')
def user_identification(request):
    return render(request, 'activity_log/user_identification.html')

def user_permission_management(request):
    return render(request, 'document_access_control/user_permission_management.html')
def role_based_access_control(request):
    return render(request, 'document_access_control/role_based_access_control.html')
def document_ownership_transfer(request):
    return render(request, 'document_access_control/document_ownership_transfer.html')

def column_customization_and_sorting(request):
    return render(request, 'document_table/column_customization_and_sorting.html')
def inline_editing(request):
    return render(request, 'document_table/inline_editing.html')
def action_button(request):
    return render(request, 'document_table/action_button.html')


# event_tracking 

# time_stamping 

# user_identification