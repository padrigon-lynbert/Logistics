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
from Admin_access.dashboard.views import dashboard



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard),
    path('user_dash/', include('Admin_access.dashboard.urls')),
    path('vendor/', include('Admin_access.vendor_portal.urls')),
    path('audit/', include('Admin_access.audit_management.urls')),
    path('vehicle/', include('Admin_access.vehicle_reservation.urls')),
    path('fleet/', include('Admin_access.fleet_management.urls')),
    path('docs/', include('Admin_access.documents_tracking.urls')),
    path('docs/', include('Admin_access.market_user.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)