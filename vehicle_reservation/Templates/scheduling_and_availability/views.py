from django.shortcuts import render

def vehicle_availability_check(request):
    return render(request, 'scheduling_and_availability/vehicle_availability_check.html')
def recurring_reservations(request):
    return render(request, 'scheduling_and_availability/recurring_reservations.html')
def time_slot_management(request):
    return render(request, 'scheduling_and_availability/time_slot_management.html')