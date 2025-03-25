from django.shortcuts import render


# Create your views here.

# def vendor_portal(request):
#     logger.info("vendor_portal_home.html is being rendered")
#     return render(request, 'Sub1.html')

def column_customization_and_sorting(request):
    return render(request, 'document_table/column_customization_and_sorting.html')
def inline_editing(request):
    return render(request, 'document_table/inline_editing.html')
def action_button(request):
    return render(request, 'document_table/action_button.html')

# column_customization_and_sorting
# inline_editing
# action_button



