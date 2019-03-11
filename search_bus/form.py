from django import forms


class SearchForm(forms.Form):
    busno = forms.CharField()
    #booleans = forms.BooleanField()
