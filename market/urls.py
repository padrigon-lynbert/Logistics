from django.urls import path
from .views import index_market, create, explore, author, vendor_signup
from .views import signup, signin

urlpatterns = [
    path('dashboard/index_market/', index_market, name='index_market'),
    path('dashboard/create/', create, name='create'),
    path('dashboard/explore/', explore, name='explore'),
    path('dashboard/author/', author, name='author'),
    path('dashboard/vendor_signup/', vendor_signup, name='vendor_signup'),
    path('dashboard/signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),

]