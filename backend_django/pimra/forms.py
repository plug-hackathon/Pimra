
from django import forms


# Form
class DumpForm(forms.Form):
    filename = forms.CharField()
