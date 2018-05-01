from django import forms


class BinaryViewForm(forms.Form):
    binary = forms.FileField()
