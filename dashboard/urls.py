from django.urls import path
from .views import dashboard, microfinance

urlpatterns = [
    path('', microfinance, name='microfinance'),
    path('dashboard/', dashboard, name='dashboard'),
]
