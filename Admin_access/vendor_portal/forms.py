# from django import forms

# from .models import PRC_vendor_offers

# class VendorOffersForm(forms.ModelForm):
#     model = PRC_vendor_offers
#     fields = ['vendor_id', 'agreement_text','offer_price', 'status', 'prc_request_id']
#     widget = {'vendor_id': forms.NumberInput(attrs={'class': 'form-control'}),
#               'agreement_text': forms.CharField(),
#               'offer_price': forms.CharField(attrs={'class': 'form-control'}),
#               'status': forms.Select(attrs={'class': 'form-control'}),
#               'prc_request_id': forms.IntegerField(attrs={'class': 'form-control'}),
#     }