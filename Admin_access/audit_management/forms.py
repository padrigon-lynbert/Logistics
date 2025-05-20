from django import forms

from Admin_access.audit_management.models import Audit

class AuditForm(forms.ModelForm):
    class Meta:
        model = Audit
        fields = ['organization_id', 'title', 'audit_type', 'status', 'scheduled_date', 'created_by']
        widgets = {
            'organization_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'audit_type': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'scheduled_date': forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
            'created_by': forms.NumberInput(attrs={'class': 'form-control'})
        }