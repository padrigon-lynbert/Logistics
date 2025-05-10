from django.urls import path
from .views import microfinance

urlpatterns = [
    path('', microfinance, name='microfinance'),
]
