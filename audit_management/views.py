from django.shortcuts import render

def audit_objective(request):
    return render(request, 'audit_planning_and_scheduling/audit_objective.html')
def scope_of_the_audit(request):
    return render(request, 'audit_planning_and_scheduling/scope_of_the_audit.html')
def communication_plan(request):
    return render(request, 'audit_planning_and_scheduling/communication_plan.html')

def policies(request):
    return render(request, 'compliance_management/policies.html')
def procedures(request):
    return render(request, 'compliance_management/procedures.html')
def audits(request):
    return render(request, 'compliance_management/audits.html')

def sales_performance(request):
    return render(request, 'reporting_analytics/sales_porformance.html')
def user_engagement(request):
    return render(request, 'reporting_analytics/user_engagement.html')
def social_media_activity(request):
    return render(request, 'reporting_analytics/social_media_activity.html')

