from django.urls import path
from .views import vendor_activation, tracks, vendor_details
from .views import orders, invoices, cancel_transaction
from .views import ratings, summary, request_meetup
from .views import vendor_activation_view, dv


urlpatterns = [

    path('vendor_manager/vendor_activation/', vendor_activation, name='vendor_activation'),
    path('vendor_manager/vendor_details/', vendor_details, name='vendor_details'),
    path('vendor_manager/tracks/', tracks, name='tracks'),

    path('vendor_transaction/orders/', orders, name='orders'),
    path('vendor/vendor_transaction/invoices/', invoices, name='invoices'),
    path('vendor_transaction/cancel_transaction/', cancel_transaction, name='cancel_transaction'),
    # path('vendor_transaction/cancel_transaction/add_vendor_offer/', add_vendor_offer, name='add_vendor_offer'),

    path('vendor_performance/ratings/', ratings, name='ratings'),
    path('vendor_performance/summary/', summary, name='summary'),
    path('vendor_performance/request_meetup/', request_meetup, name='request_meetup'),

    path("vendors/vendor_manager/", vendor_activation_view, name="vendor_activation_view"),
    path("vendors/vendor_manager/dv", dv, name="dv"),

    # additional views

    

]