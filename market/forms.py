from django import forms

class SignupForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    info = forms.CharField(widget=forms.Textarea, required=False)
    bid = forms.IntegerField(required=False)