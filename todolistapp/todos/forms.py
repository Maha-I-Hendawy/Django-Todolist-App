from django import forms


class TodoForm(forms.Form):
    todo = forms.CharField(max_length=100)
    completed = forms.BooleanField(required=False)