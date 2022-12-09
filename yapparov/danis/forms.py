from django import forms

class userreg(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"x","placeholder":"name"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"x","placeholder":"email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"x","placeholder":"password"}))