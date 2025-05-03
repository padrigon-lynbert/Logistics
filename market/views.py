from django.shortcuts import render

# Create your views here.
def index_market(request):
    return render(request, 'index.html')

def explore(request):
    return render(request, 'explore.html')

def item_details(request):
    return render(request, 'details.html')

def author (request):
    return render(request, 'author.html')

def create(request):
    return render(request, 'create.html')

def vendor_signup(request):
    return render(request, 'vendor_signup.html')