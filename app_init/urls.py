from django.urls import path
from .views import app_init

urlpatterns = [
    path('', app_init, name='dashboard')
]
