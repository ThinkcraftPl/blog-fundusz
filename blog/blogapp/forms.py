from django import forms


class WpisFormularz(forms.Form):
    start = forms.CharField(label="Wpisz frazę zaczynającą: ",label_suffix="", max_length=100)
    gram = forms.IntegerField(label="Rodzaj ngramu: ",label_suffix="",max_value=4,min_value=1)
