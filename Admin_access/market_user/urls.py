from django.urls import path
from .views import index_market_user, create_user, explore_user, author_user, item_details_user, vendor_signup_user
from .views import signup_user, signin_user

urlpatterns = [
    path('dashboard/index_market_user/', index_market_user, name='index_market_user'),
    path('dashboard/create_user/', create_user, name='create_user'),
    path('dashboard/explore_user/', explore_user, name='explore_user'),
    path('dashboard/author_user/', author_user, name='author_user'),
    path('dashboard/item_details_user/', item_details_user, name='item_details_user'),
    path('dashboard/vendor_signup_user/', vendor_signup_user, name='vendor_signup_user'),
    path('dashboard/signup_user/', signup_user, name='signup_user'),
    path('dashboard/signin/', signin_user, name='signin_user'),

]