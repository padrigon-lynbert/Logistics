import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable to your project settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Logistics_II.settings')

# Set up Django
django.setup()

from market.models import Vendor




vendor = Vendor.objects.create(
    email="test@vendor.com",
    password="password123",
    service="Service1",
    about="About vendor",
    bid_amount=1000.00,
    company="Test Company",
    contact="Contact info"
)

print(vendor)
