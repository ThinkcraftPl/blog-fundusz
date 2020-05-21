from django import forms


class WpisFormularz(forms.Form):
    start = forms.CharField(label="Wpisz tytuł postu", max_length=100)
    gram = forms.IntegerField(max_value=4,min_value=1,help_text="Jaki ngram użyć? (4>=n>=1)")
