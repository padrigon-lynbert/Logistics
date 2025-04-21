from django.urls import path
from .views import vendor_activation
# from .views import vendor_activation, tracks, vendor_details
# from .templates.vendor_transaction.views import orders, invoices, cancel_transaction
# from .templates.vendor_performance.views import ratings, summary, request_meetup

urlpatterns = [
    # path('vendor/home/', home, name='home'),

    path('vendor/vendor_manager/vendor_activation/', vendor_activation, name='vendor_activation'),
    # path('vendor/vendor_manager/vendor_details/', vendor_details, name='vendor_details'),
    # path('vendor/vendor_manager/tracks/', tracks, name='tracks'),

    # path('vendor/vendor_transaction/orders/', orders, name='orders'),
    # path('vendor/vendor_transaction/invoices/', invoices, name='invoices'),
    # path('vendor/vendor_transaction/cancel_transaction/', cancel_transaction, name='cancel_transaction'),

    # path('vendor/vendor_performance/ratings/', ratings, name='ratings'),
    # path('vendor/vendor_performance/summary/', summary, name='summary'),
    # path('vendor/vendor_performance/request_meetup/', request_meetup, name='request_meetup'),
]