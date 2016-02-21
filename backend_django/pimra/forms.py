
from datetime import datetime

from django import forms


# Dump form
class DumpForm(forms.Form):
    filename = forms.CharField()


class WriteForm(forms.Form):
    filename = forms.CharField()