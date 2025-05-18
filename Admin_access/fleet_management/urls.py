from django.urls import path
from .views import alerts_for_servicing_needs, maintenance_history_logging, preventive_maintenance_scheduling
from .views import driver_assignment, license_and_certification_tracking, driver_performance_monitoring
from .views import accident_reporting, regulatory_compliance_tracking, vehicle_inspections
from .views import asset_management, header, driver_ass, vehicle_tracking, coplianc_training

urlpatterns = [
    path('fleet_mamagement/maintenance_management/alerts_for_servicing_needs/', alerts_for_servicing_needs, name='alerts_for_servicing_needs'),
    path('fleet_mamagement/maintenance_management/maintenance_history_logging/', maintenance_history_logging, name='maintenance_history_logging'),
    path('fleet_mamagement/maintenance_management/preventive_maintenance_scheduling/', preventive_maintenance_scheduling, name='preventive_maintenance_scheduling'),

    path('fleet_mamagement/maintenance_management/driver_assignment/', driver_assignment, name='driver_assignment'),
    path('fleet_mamagement/maintenance_management/license_and_certification_tracking/', license_and_certification_tracking, name='license_and_certification_tracking'),
    path('fleet_mamagement/maintenance_management/driver_performance_monitoring/', driver_performance_monitoring, name='driver_performance_monitoring'),

    path('fleet_mamagement/maintenance_management/accident_reporting/', accident_reporting, name='accident_reporting'),
    path('fleet_mamagement/maintenance_management/regulatory_compliance_tracking/', regulatory_compliance_tracking, name='regulatory_compliance_tracking'),
    path('fleet_mamagement/maintenance_management/vehicle_inspections/', vehicle_inspections, name='vehicle_inspections'),

    path('fleet_mamagement/asset_management/', asset_management, name='asset_management'),
    path('fleet_mamagement/header/', header, name='header'),
    path('fleet_mamagement/driver_ass/', driver_ass, name='driver_ass'),
    path('fleet_mamagement/vehicle_tracking/', vehicle_tracking, name='vehicle_tracking'),
    path('fleet_mamagement/coplianc_training/', coplianc_training, name='coplianc_training'),

]