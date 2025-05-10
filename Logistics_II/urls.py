"""
URL configuration for Logistics_II project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('temporary_microf.urls')),
    path('user_dash/', include('User_access.dashboard.urls')),
    path('vendor/', include('User_access.vendor_portal.urls')),
    path('audit/', include('User_access.audit_management.urls')),
    path('vehicle/', include('User_access.vehicle_reservation.urls')),
    path('fleet/', include('User_access.fleet_management.urls')),
    path('docs/', include('User_access.documents_tracking.urls')),
    path('docs/', include('Vendor_access.market.urls')),
    path('docs/', include('User_access.market_user.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
