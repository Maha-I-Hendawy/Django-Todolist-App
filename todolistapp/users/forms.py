from django import forms  



class UserForm(forms.Form):
	username = forms.CharField(max_length=100, required=True)
	email = forms.CharField(max_length=100, required=True)
	password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput())
	confirm_password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput())





class LoginForm(forms.Form):
	username = forms.CharField(max_length=100, required=True)
	password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput())
