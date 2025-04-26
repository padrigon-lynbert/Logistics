from django.shortcuts import render

# Create your views here.
def dashboard(requrest):
    return render(requrest, 'dashboard.html')