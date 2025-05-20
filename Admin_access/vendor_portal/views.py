from django.shortcuts import render


# Create your views here.

def vendor_details(request):
    return render(request, 'vendor_manager/vendor_details.html')
def tracks(request):
    return render(request, 'vendor_manager/tracks.html')

def ratings(request):
    return render(request, 'vendor_performance/ratings.html')
def summary(request):
    return render(request, 'vendor_performance/summary.html')
def request_meetup(request):
    return render(request, 'vendor_performance/request_meetup.html')

def orders(request):
    return render(request, 'vendor_transaction/orders.html')
def invoices(request):
    return render(request, 'vendor_transaction/invoices.html')
def cancel_transaction(request):
    return render(request, 'vendor_transaction/cancel_transaction.html')

# db
from django.shortcuts import render
from .models import Vendor, Vendor_history

def vendor_activation(request):
    # Fetch all vendors
    vendors = Vendor.objects.all()
    vendor_history = Vendor_history.objects.all()

    # Pass vendors to the template
    return render(request, 'vendor_manager/vendor_activation.html', {
        'vendors': vendors,
        'prc_vendor_history': vendor_history,
        })

# ajax
from django.shortcuts import render, redirect
from .models import Vendor

def vendor_activation_view(request):
    if request.method == "POST":
        vendor_id = request.POST.get("vendor_id")
        new_status = request.POST.get("status")
        try:
            vendor = Vendor.objects.get(id=vendor_id)
            vendor.activation_status = new_status
            vendor.save()
        except Vendor.DoesNotExist:
            pass  # handle if needed
        return redirect("vendor_activation")  # name your url pattern this

    vendors = Vendor.objects.all()
    return render(request, "vendor_activation.html", {"vendors": vendors})



