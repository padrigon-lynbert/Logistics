from django.urls import path
from .views import index_market, create, explore, author, vendor_signup
from .views import signin
from .views import user_image

urlpatterns = [
    path('dashboard/index_market/', index_market, name='index_market'),
    path('dashboard/create/', create, name='create'),
    path('dashboard/explore/', explore, name='explore'),
    path('dashboard/author/', author, name='author'),
    path('dashboard/vendor_signup/', vendor_signup, name='vendor_signup'),
    path('signin/', signin, name='signin'),
    path('user-image/<int:user_id>/', user_image, name='user_image'),

]