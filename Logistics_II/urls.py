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
    path('', include('dashboard.urls')),
    # path('init/', include('app_init.urls')),
    path('vendor/', include('vendor_portal.urls')),
    path('audit/', include('audit_management.urls')),
    path('vehicle/', include('vehicle_reservation.urls')),
    path('fleet/', include('fleet_management.urls')),
    path('docs/', include('documents_tracking.urls')),
    path('docs/', include('market.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
