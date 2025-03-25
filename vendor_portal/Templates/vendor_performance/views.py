from django.shortcuts import render

def ratings(request):
    return render(request, 'vendor_performance/ratings.html')
def summary(request):
    return render(request, 'vendor_performance/summary.html')
def request_meetup(request):
    return render(request, 'vendor_performance/request_meetup.html')