from django.shortcuts import render, get_object_or_404, redirect
from .models import PRC_vendor_offers
# from .forms import VendorOffersForm

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
    pvo = PRC_vendor_offers.objects.all()
    return render(request, 'vendor_transaction/cancel_transaction.html', {'prc_vendor_offers': pvo})

# db
from django.shortcuts import render
from .models import Vendor, Vendor_history, PRC_vendor_offers

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

from django.db import IntegrityError
def dv(request):
    offers = PRC_vendor_offers.objects.all().order_by('-id')
    try:
        if request.method == 'POST':
            PRC_vendor_offers.objects.create(
                vendor_id=request.POST.get('vendor_id'),
                agreement_text=request.POST.get('agreement_text'),
                offer_price=request.POST.get('offer_price'),
                status=request.POST.get('status'),
                prc_request_id=request.POST.get('prc_request_id')
            )
            return redirect('dv')  # redirect to avoid resubmit

        return render(request, 'vendor_transaction/cancel_transaction.html', {'prc_vendor_offers': offers})
    except IntegrityError:
        return render(request, 'vendor_transaction/cancel_transaction.html', {
            'prc_vendor_offers': offers,
            'integrity_error': "No vendor found with same ID"
            })





