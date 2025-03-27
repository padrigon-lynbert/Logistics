from django.urls import path
from .Templates.reservation_management.views import booking_requests, cancelation_and_modifications, reservation_approval
from .Templates.vehicle_allocation_and_tracking.views import fleet_assignment, usage_reports, vehicle_status_monitoring
from .Templates.compliance_and_maintenance_integration.views import inspection_scheduling, repair_and_maintenance_request, usage_compliance

urlpatterns = [
    path('vehicle_reservation/user_management/booking_requests/', booking_requests, name='booking_requests'),
    path('vehicle_reservation/user_management/cancelation_and_modifications/', cancelation_and_modifications, name='cancelation_and_modifications'),
    path('vehicle_reservation/user_management/reservation_approval/', reservation_approval, name='reservation_approval'),

    path('vehicle_reservation/scheduling_and_availability/vehicle_status_monitoring/', vehicle_status_monitoring, name='vehicle_status_monitoring'),
    path('vehicle_reservation/scheduling_and_availability/fleet_assignment/', fleet_assignment, name='fleet_assignment'),
    path('vehicle_reservation/scheduling_and_availability/usage_reports/', usage_reports, name='usage_reports'),

    path('vehicle_reservation/payment_and_billing/inspection_scheduling/', inspection_scheduling, name='inspection_scheduling'),
    path('vehicle_reservation/payment_and_billing/repair_and_maintenance_request/', repair_and_maintenance_request, name='repair_and_maintenance_request'),
    path('vehicle_reservation/payment_and_billing/usage_compliance/', usage_compliance, name='usage_compliance'),


]
