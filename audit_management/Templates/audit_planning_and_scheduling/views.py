from django.shortcuts import render

def audit_objective(request):
    return render(request, 'audit_planning_and_scheduling/audit_objective.html')
def scope_of_the_audit(request):
    return render(request, 'audit_planning_and_scheduling/scope_of_the_audit.html')
def communication_plan(request):
    return render(request, 'audit_planning_and_scheduling/communication_plan.html')