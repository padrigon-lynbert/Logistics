from django.urls import path
from .Templates.document_table.views import action_button, column_customization_and_sorting, inline_editing
from .Templates.activity_log.views import event_tracking, time_stamping, user_identification
from .Templates.document_access_control.views import document_ownership_transfer, role_based_access_control, user_permission_management

urlpatterns = [
    path('document/document_table/action_button/', action_button, name='action_button'),
    path('document/document_table/column_customization_and_sorting/', column_customization_and_sorting, name='column_customization_and_sorting'),
    path('document/document_table/inline_editing/', inline_editing, name='inline_editing'),

    path('document/activity_log/event_tracking/', event_tracking, name='event_tracking'),
    path('document/activity_log/time_stamping/', time_stamping, name='time_stamping'),
    path('document/activity_log/user_identification/', user_identification, name='user_identification'),

    path('document/activity_log/document_ownership_transfer/', document_ownership_transfer, name='document_ownership_transfer'),
    path('document/activity_log/role_based_access_control/', role_based_access_control, name='role_based_access_control'),
    path('document/activity_log/user_permission_management/', user_permission_management, name='user_permission_management'),

]
