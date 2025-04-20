from django.shortcuts import render

def sales_performance(request):
    return render(request, 'reporting_analytics/sales_porformance.html')
def user_engagement(request):
    return render(request, 'reporting_analytics/user_engagement.html')
def social_media_activity(request):
    return render(request, 'reporting_analytics/social_media_activity.html')