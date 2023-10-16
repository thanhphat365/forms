from django import forms

class LoginForm(forms.Form):
    user = forms.CharField(max_length=150),
    email = forms.EmailField(max_length=150),
    phone = forms.CharField(max_length=12)
    notes = forms.CharField(max_length=1000)
    addtress = forms.CharField()

