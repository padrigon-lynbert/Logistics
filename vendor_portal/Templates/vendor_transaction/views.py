from django.shortcuts import render

def orders(request):

    
    return render(request, 'vendor_transaction/orders.html')


def invoices(request):
    return render(request, 'vendor_transaction/invoices.html')
def cancel_transaction(request):
    return render(request, 'vendor_transaction/cancel_transaction.html')