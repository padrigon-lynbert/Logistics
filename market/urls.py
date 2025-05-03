from django.urls import path
from .views import index_market, create, explore, author, item_details, vendor_signup

urlpatterns = [
    path('dashboard/index_market/', index_market, name='index_market'),
    path('dashboard/create/', create, name='create'),
    path('dashboard/explore/', explore, name='explore'),
    path('dashboard/author/', author, name='author'),
    path('dashboard/item_details/', item_details, name='item_details'),
    path('vs/', vendor_signup, name='vendor_signup'),


]