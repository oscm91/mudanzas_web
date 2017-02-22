from django import forms

from .models import TxtFile


class CargoForm(forms.ModelForm):
    class Meta:
        model = TxtFile
        fields = ('qqfile', 'qqtotalfilesize', 'qqfilename', 'qquserid', 'qquuid', )