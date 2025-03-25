from django.urls import path
from .Templates.user_management.views import booking_history, profile_management, user_roles_and_permissions
from .Templates.scheduling_and_availability.views import recurring_reservations, time_slot_management, vehicle_availability_check
from .Templates.payment_and_billing.views import payment_processing, payment_verification, pricing_and_fare_calculation

urlpatterns = [
    path('vehicle_reservation/user_management/booking_history/', booking_history, name='booking_history'),
    path('vehicle_reservation/user_management/profile_management/', profile_management, name='profile_management'),
    path('vehicle_reservation/user_management/user_roles_and_permissions/', user_roles_and_permissions, name='user_roles_and_permissions'),

    path('vehicle_reservation/scheduling_and_availability/recurring_reservations/', recurring_reservations, name='recurring_reservations'),
    path('vehicle_reservation/scheduling_and_availability/time_slot_management/', time_slot_management, name='time_slot_management'),
    path('vehicle_reservation/scheduling_and_availability/vehicle_availability_check/', vehicle_availability_check, name='vehicle_availability_check'),

    path('vehicle_reservation/payment_and_billing/payment_processing/', payment_processing, name='payment_processing'),
    path('vehicle_reservation/payment_and_billing/payment_verification/', payment_verification, name='payment_verification'),
    path('vehicle_reservation/payment_and_billing/pricing_and_fare_calculation/', pricing_and_fare_calculation, name='pricing_and_fare_calculation'),


]
