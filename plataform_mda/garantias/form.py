from django import forms

class FormBaterias(forms.Form):
    baterias_7490 = forms.CharField(max_length=4)
    baterias_7480 = forms.CharField(max_length=4)
    baterias_E7470 = forms.CharField(max_length=4)

