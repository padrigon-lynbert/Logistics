from django.shortcuts import render

def event_tracking (request):
    return render(request, 'activity_log/event_tracking.html')
def time_stamping(request):
    return render(request, 'activity_log/time_stamping.html')
def user_identification(request):
    return render(request, 'activity_log/user_identification.html')



# event_tracking 

# time_stamping 

# user_identification