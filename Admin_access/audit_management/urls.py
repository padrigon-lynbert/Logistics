from django.urls import path
from .views import policies, procedures, audits, edit_audit
from .views import audit_findings, social_media_activity, user_engagement
from .views import audit_objective, communication_plan, scope_of_the_audit

urlpatterns = [
    path('audit/compliance_management/policies/', policies, name='policies'),
    path('audit/compliance_management/procedures/', procedures, name='procedures'),
    path('audit/compliance_management/audits/', audits, name='audits'),
    path('audit/compliance_management/edit_audit/<int:audit_id>/', edit_audit, name='edit_audit'),

    path('audit/reporting_analytics/audit_findings/', audit_findings, name='audit_findings'),
    path('audit/reporting_analytics/social_media_activity/', social_media_activity, name='social_media_activity'),
    path('audit/reporting_analytics/user_engagement/', user_engagement, name='user_engagement'),

    path('audit/audit_planning_and_scheduling/audit_objective/', audit_objective, name='audit_objective'),
    path('audit/audit_planning_and_scheduling/communication_plan/', communication_plan, name='communication_plan'),
    path('audit/audit_planning_and_scheduling/scope_of_the_audit/', scope_of_the_audit, name='scope_of_the_audit'),
]
