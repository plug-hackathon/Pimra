
from datetime import datetime

from django import forms


# Dump form
class DumpForm(forms.Form):
    filename = forms.CharField(initial=datetime.now().strftime("%y-%m-%d-%H:%M.dump"))

