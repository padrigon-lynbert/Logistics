from django.shortcuts import render
from Admin_access.audit_management.models import Audit

def audit_objective(request):
    return render(request, 'audit_planning_and_scheduling/audit_objective.html')
def scope_of_the_audit(request):
    return render(request, 'audit_planning_and_scheduling/scope_of_the_audit.html')
def communication_plan(request):
    return render(request, 'audit_planning_and_scheduling/communication_plan.html')

def policies(request):
    audits = Audit.objects.order_by('audit_id')
    context = {'audits': audits}
    return render(request, 'compliance_management/policies.html', context)

def procedures(request):
    return render(request, 'compliance_management/procedures.html')
def audits(request):
    audits = Audit.objects.order_by('audit_id')
    context = {'audits': audits}
    return render(request, 'compliance_management/policies.html', context)

def audit_findings(request):
    return render(request, 'reporting_analytics/audit_findings.html')
def user_engagement(request):
    return render(request, 'reporting_analytics/user_engagement.html')
def social_media_activity(request):
    return render(request, 'reporting_analytics/social_media_activity.html')

