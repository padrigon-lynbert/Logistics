from django.shortcuts import render

# Create your views here.

def microfinance(request):
    return render(request, 'microfinance.html')
